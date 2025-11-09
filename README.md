Location Visualizer

This is a Django project that visualizes location tracking data on an interactive map. It's designed to read location points (latitude/longitude) from a database, group them by a product ID, and then draw the complete path for each product on a Folium (Leaflet.js) map.

Features

Database Integration: Fetches location data from a Django model (LocationPoint).

Path Grouping: Automatically groups location points by product_id.

Interactive Map: Uses Folium to render an interactive map.

Path Drawing: Draws a PolyLine (path) for each product's journey.

Start/End Markers: Places distinct markers for the start (green) and end (orange) of each path.

Reverse Geocoding: Attempts to find the street address for start and end points and displays them in a popup.

Setup & Installation

Clone the repository:

git clone <your-repo-url>
cd location-visualizer-project


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install the required packages:

pip install django folium geocoder


Apply Database Migrations:
(Note: If you are upgrading from the old project, delete the old db.sqlite3 file and the migrations folder inside the tracker app before running.)

python manage.py makemigrations tracker
python manage.py migrate


Run the development server:

python manage.py runserver


Usage

Once the server is running, you can access the map by navigating to:

http://127.0.0.1:8000/

This will automatically redirect you to the main tracker map at http://127.0.0.1:8000/tracker/.

To add data, you can use the Django admin panel:

Create a superuser: python manage.py createsuperuser

Log in at http://127.0.0.1:8000/admin/

Add LocationPoint objects. Make sure to use the same product_id for points that belong to the same path.

Database Model

The project uses a single model, LocationPoint, defined in tracker/models.py:

product_id (CharField): The unique identifier for the product being tracked (e.g., "product-001").

iot_gateway_id (CharField): Identifier for the IoT gateway that reported the location.

timeStamp (CharField): The timestamp of the location log (can be changed to DateTimeField).

latitude (FloatField): The latitude coordinate.

longitude (FloatField): The longitude coordinate.