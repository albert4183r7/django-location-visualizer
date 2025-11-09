from django.shortcuts import render
import folium
import geocoder
from .models import Location

def map_api(request):
    # Ambil semua data dari model Location
    data_objects = Location.objects.all()

    # Membuat dictionary kosong untuk menampung data berdasarkan 'id_product'
    data_by_id_product = {}

    # Memisahkan data berdasarkan 'id_product'
    for data in data_objects:
        id_product = data.id_product

        # Jika 'id_product' belum ada dalam dictionary, buat list kosong sebagai nilai awalnya
        if id_product not in data_by_id_product:
            data_by_id_product[id_product] = []

        # Menambahkan pasangan latitude dan longitude ke list yang sesuai dengan 'id_product'
        data_by_id_product[id_product].append((data.latitude, data.longitude))

    # Membuat objek peta
    m = folium.Map(location=[-6, 107], zoom_start=4)

    # Menambahkan polyline dan marker berdasarkan data_by_id_product
    for id_product, coordinates in data_by_id_product.items():
        # Lintasan (garis)
        folium.PolyLine(
            locations=coordinates,
            weight=2,
            color='blue'
        ).add_to(m)

        # Marker awal dan akhir
        first_koor = coordinates[0]
        last_koor = coordinates[-1]

        first_addr = geocoder.osm(first_koor, method="reverse")
        last_addr = geocoder.osm(last_koor, method="reverse")

        folium.Marker(
            first_koor,
            tooltip=f'lokasi awal {id_product}, N = {first_koor[0]}, E = {first_koor[1]}',
            popup=first_addr.address if first_addr.address else "Alamat Tidak Ditemukan",
            icon=folium.Icon(color="green")
        ).add_to(m)

        folium.Marker(
            last_koor,
            tooltip=f'lokasi akhir {id_product}, N = {last_koor[0]}, E = {last_koor[1]}',
            popup=last_addr.address if last_addr.address else "Alamat Tidak Ditemukan",
            icon=folium.Icon(color="orange")
        ).add_to(m)

    # Mendapatkan representasi HTML dari peta
    m = m._repr_html_()

    context = {
        'map': m,
    }
    return render(request, 'map.html', context)
