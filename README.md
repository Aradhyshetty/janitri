# Django Project: Patient Heart Rate Monitoring System

## Installation
1. Clone the repository:
   ```sh
   git clone [https://github.com/your-repo/patient-monitoring.git](https://github.com/Aradhyshetty/janitri/)
   cd patient-monitoring
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (optional):
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Project Structure
```
patient-monitoring/
│── manage.py
│── db.sqlite3
│── requirements.txt
│── README.md
│── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│── patients/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│── templates/
│   ├── base.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
```

## API Endpoints
1. **User Registration and Login**
   - `POST /register/` - Register a new user
   - `POST /login/` - Login a user

2. **Manage Patients**
   - `POST /patients/add/` - Add a new patient
   - `GET /patients/{id}/` - Retrieve patient details

3. **Heart Rate Details**
   - `POST /patients/{id}/heart-rate/` - Record heart rate data
   - `GET /patients/{id}/heart-rate/` - Retrieve heart rate data

## Technologies Used
- Django
- SQLite
- Bootstrap (for UI)

## License
This project is open-source and available under the MIT License.
