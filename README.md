# LittleLemon API

This is a Django REST Framework API for a fictional restaurant called LittleLemon.

## Table of Contents

- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Built With](#built-with)

## Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    -   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    -   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the database migrations:**
    ```bash
    python manage.py migrate
    ```

## Running the Application

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:8000/`.

## API Endpoints

The following API endpoints are available:

-   `api/menu-items/`: GET, POST
-   `api/menu-items/{id}`: GET, PUT, DELETE
-   `api/groups/manager/users`: GET, POST, DELETE
-   `api/groups/delivery-crew/users`: GET, POST, DELETE

For more details on the API, please refer to the API documentation.

## Testing

To run the automated tests, use the following command:
```bash
python manage.py test
```
The tests are located in the `LittlelemonAPI/tests.py` file.

## Project Structure
```
LittleLemon/
├── manage.py
├── Pipfile
├── Pipfile.lock
├── Littlelemon/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── LittlelemonAPI/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── migrations/
```

## Built With

-   [Django](https://www.djangoproject.com/)
-   [Django REST Framework](https://www.django-rest-framework.org/)
-   [Python](https://www.python.org/)
