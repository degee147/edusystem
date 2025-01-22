# Course Management System REST API

REST API for a course management system that supports multiple educational institutions. The system is designed to handle course creation, student enrollment, and provide basic analytics for institutional decision-making. It ensures scalability and flexibility for diverse educational setups.

## Features

- Multi-institution support
- Course creation, update, and deletion
- Student enrollment and management
- Basic analytics for institutional insights
- Authentication and role-based access control
- API documentation for easy integration

## Requirements

- Python 3.8+
- Django 5.x

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>

2. Navigate to the project directory:
    ```bash
    cd <project-directory>

3. Set up a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: .\env\\Scripts\\activate

4. Install dependencies:
    ```bash
    pip install -r requirements.txt

5. Apply migrations:
    ```bash
    python manage.py migrate

6. Create Superuser:
    ```bash
    python manage.py createsuperuser

7. Seed Data(optional):
    ```bash
    python manage.py seed_data


## Usage
Access the API endpoints via http://127.0.0.1:8000/. Refer to the API documentation for detailed usage.


