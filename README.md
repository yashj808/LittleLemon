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
    -   Using `pip`:
        ```bash
        pip install -r requirements.txt
        ```
    -   Using `pipenv`:
        ```bash
        pipenv install
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

-   `admin/`
-   `api/menu-items/`
-   `api/menu-items/<int:pk>/`
-   `api/secret/`
-   `api/api-token-auth/`
-   `api/manager-view/`
-   `api/throttle_check/`
-   `api/throttle_check_auth/`
-   `api/categories/`
-   `api/categories/<int:pk>/`
-   `api/groups/manager/users/`
-   `api/ratings/`
-   `auth/` (Djoser endpoints for user registration and authentication)

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
├── .gitignore
├── manage.py
├── Pipfile
├── Pipfile.lock
├── requirements.txt
├── README.md
├── db.sqlite3
├── Littlelemon/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
└── LittlelemonAPI/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── throttles.py
    ├── urls.py
    ├── views.py
    └── migrations/
```

## Built With

-   [Django](https://www.djangoproject.com/)
-   [Django REST Framework](https://www.django-rest-framework.org/)
-   [Python](https://www.python.org/)
-   [Djoser](https://djoser.readthedocs.io/)
-   [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
-   [WhiteNoise](http://whitenoise.evans.io/)
