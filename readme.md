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
   source env/bin/activate  # On Windows use: .\env\Scripts\activate
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

Access the API endpoints via http://127.0.0.1:8000/. Refer to the API documentation for detailed usage.

## Authentication and RBAC

### Default Permissions

- **Institution Management**: Only admins can delete or modify institutions. Others can view.
- **Course Management**: Everyone can view courses. Only admins can delete or modify.
- **Student Management**: Only admins and instructors can manage students.
- **Enrollment Management**: Only admins can view and modify enrollments.
- **Analytics**: Only admins can view and modify analytics.

### Login and Authorization

The login endpoint is available at:
```bash
http://127.0.0.1:8000/api/login/
```

After logging in, you will receive a JWT token. Use this token to access protected endpoints.

1. **Open Postman** and create a new request.
2. Use the **Authorization** tab and select "Bearer Token" as the auth type.
3. Paste your JWT token in the "Token" field.

Alternatively, you can manually set it in the **Headers** tab:
   - **Key**: `Authorization`
   - **Value**: `Bearer <your_jwt_token_here>`

### Example of Authorization Header

- **Key**: `Authorization`
- **Value**: `Bearer your_jwt_token_here`

## API Endpoints

Refer to the auto-generated API documentation or Postman collection for detailed endpoints and payload structures.

---

For further assistance or feature requests, feel free to open an issue or contact the maintainers.

