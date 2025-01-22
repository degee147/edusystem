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
   ```

2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: .\env\\Scripts\\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Create Superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Seed Data (optional):
    ```bash
    python manage.py seed_data
    ```

## Usage

Access the API endpoints via `http://127.0.0.1:8000/`. Refer to the API documentation for detailed usage.

## Role-Based Access Control (RBAC)

### Default Permissions Based on Role:

- **Institution Viewset:**
  - **Endpoint:** `/institutions/`
  - **Permissions:**
    - **Admin**: Can create, update, or delete institutions.
    - **Any User**: Can **view** institutions.
    - **Permission Class:** `IsAdminOrReadOnly`

- **Course Viewset:**
  - **Endpoint:** `/courses/`
  - **Permissions:**
    - **Admin**: Can create, update, or delete courses.
    - **Any User**: Can **view** courses.
    - **Permission Class:** `IsAdminOrReadOnly`

- **Student Viewset:**
  - **Endpoint:** `/students/`
  - **Permissions:**
    - **Admin & Instructor**: Can create, update, or delete student records.
    - **Any Authenticated User**: Can **view** student records.
    - **Permission Class:** `IsAdminOrInstructor`

- **Enrollment Viewset:**
  - **Endpoint:** `/enrollments/`
  - **Permissions:**
    - **Admin**: Can create, update, or delete enrollments.
    - **Any Authenticated User**: Can **view** their own enrollment record.
    - **Permission Class:** `IsAdmin`

- **Analytics Viewset:**
  - **Endpoint:** `/analytics/`
  - **Permissions:**
    - **Admin**: Can **view** and **modify** analytics data.
    - **Permission Class:** `IsAdmin`

## Login Endpoint (For Postman)

To authenticate and receive a JWT token, use the **login endpoint**.

### Login Endpoint URL:
```
POST http://127.0.0.1:8000/api/login/
```

### Request Body Example (JSON):
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

### Response:
If successful, the response will include a JWT token, which you will use for authorization in subsequent requests.

```json
{
    "access": "your_jwt_token_here",
    "refresh": "your_refresh_token_here"
}
```

## Authorization in Postman

After logging in, you will receive a JWT token. Use this token to access protected endpoints.

1. **Open Postman** and create a new request.
2. In the **Headers** tab, add the following:
   - **Key**: `Authorization`
   - **Value**: `Bearer <your_jwt_token_here>`
   
3. **Send the Request** to the API endpoint you want to interact with.

Example of header:
- **Key**: `Authorization`
- **Value**: `Bearer your_jwt_token_here`

