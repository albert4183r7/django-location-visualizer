# Location Visualizer

This is a Django project that visualizes location tracking data on an interactive map. It's designed to read location points (latitude/longitude) from a database, group them by a product ID, and then draw the complete path for each product on a Folium (Leaflet.js) map.

## Features

* **Database Integration:** Fetches location data from a Django model (`LocationPoint`).
* **Path Grouping:** Automatically groups location points by `product_id`.
* **Interactive Map:** Uses Folium to render an interactive map.
* **Path Drawing:** Draws a `PolyLine` (path) for each product's journey.
* **Start/End Markers:** Places distinct markers for the start (green) and end (orange) of each path.
* **Reverse Geocoding:** Attempts to find the street address for start and end points and displays them in a popup.

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd location-visualizer
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required packages:**
    *(Make sure you have a `requirements.txt` file in your project root)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations:**
    ```bash
    python manage.py makemigrations tracker
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1.  **Create an Admin User:**
    * You need an admin user to add data.
    ```bash
    python manage.py createsuperuser
    ```
    * Follow the prompts to create your username and password.

2.  **Run the Server & Add Data:**
    * Start the server: `python manage.py runserver`
    * Log in to the admin panel: `http://127.0.0.1:8000/admin/`
    * Go to "Location points" and click "+ Add" to add your data.

3.  **View the Map:**
    * Once you have data, you can see the map here:
        **`http://127.0.0.1:8000/tracker/`**

## Database Model

The project uses a single model, `LocationPoint`, defined in `tracker/models.py`:

* `product_id` (CharField): The unique identifier for the product being tracked.
* `iot_gateway_id` (CharField): Identifier for the IoT gateway that reported the location.
* `timeStamp` (CharField): The timestamp of the location log.
* `latitude` (FloatField): The latitude coordinate.
* `longitude` (FloatField): The longitude coordinate.