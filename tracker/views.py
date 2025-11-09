from django.shortcuts import render
import folium
import geocoder
from .models import LocationPoint
from collections import defaultdict
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)

def get_address_from_coords(coordinates):
    """
    Tries to find a street address from latitude/longitude coordinates.
    Returns a default string if not found or if an error occurs.
    """
    try:
        # Use geocoder to find the address
        location = geocoder.osm(coordinates, method="reverse")
        if location and location.address:
            return location.address
        else:
            return "Alamat Tidak Ditemukan"
    except Exception as e:
        # Log the error if geocoding fails
        logger.error(f"Geocoding failed for {coordinates}: {e}")
        return "Gagal mencari alamat"

def group_locations_by_product(location_points):
    """
    Groups a queryset of LocationPoint objects into a dictionary
    keyed by 'product_id'.
    """
    # Use defaultdict to automatically handle new keys
    data_by_product_id = defaultdict(list)
    
    for point in location_points:
        # Append coordinates as a tuple
        data_by_product_id[point.product_id].append((point.latitude, point.longitude))
        
    return data_by_product_id

def add_track_to_map(map_object, product_id, coordinates):
    """
    Adds a PolyLine and start/end markers for a single product's
    track to the given Folium map object.
    """
    if not coordinates:
        return  # Skip if there are no coordinates for this product

    # 1. Add the path (PolyLine)
    folium.PolyLine(
        locations=coordinates,
        weight=2,
        color='blue',
        tooltip=f"Path for {product_id}"
    ).add_to(map_object)

    # 2. Get start and end coordinates
    first_koor = coordinates[0]
    last_koor = coordinates[-1]

    # 3. Get addresses (with error handling)
    first_addr = get_address_from_coords(first_koor)
    last_addr = get_address_from_coords(last_koor)

    # 4. Add start marker
    folium.Marker(
        first_koor,
        tooltip=f'Lokasi Awal {product_id} | N: {first_koor[0]}, E: {first_koor[1]}',
        popup=f"<b>{product_id} (Start)</b><br>{first_addr}",
        icon=folium.Icon(color="green", icon="play")
    ).add_to(map_object)

    # 5. Add end marker
    folium.Marker(
        last_koor,
        tooltip=f'Lokasi Akhir {product_id} | N: {last_koor[0]}, E: {last_koor[1]}',
        popup=f"<b>{product_id} (End)</b><br>{last_addr}",
        icon=folium.Icon(color="orange", icon="stop")
    ).add_to(map_object)

def track_map_view(request):
    """
    Main view to display the map with all product tracks.
    """
    # 1. Fetch all data. For large datasets, consider filtering.
    # Order by timeStamp if it were a DateTimeField to ensure correct path
    location_objects = LocationPoint.objects.all() # .order_by('product_id', 'timeStamp')

    # 2. Group data by product
    data_by_product = group_locations_by_product(location_objects)

    # 3. Create a base map (centered on Indonesia)
    m = folium.Map(location=[-2.5, 118], zoom_start=5)

    # 4. Add each product's track to the map
    for product_id, coordinates in data_by_product.items():
        add_track_to_map(m, product_id, coordinates)

    # 5. Convert map to HTML
    map_html = m._repr_html_()

    context = {
        'map': map_html,
    }
    return render(request, 'tracker/map_view.html', context)