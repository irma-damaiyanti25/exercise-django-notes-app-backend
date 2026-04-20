This repository is a practice project from the "Belajar Backend Pemula dengan Python" course from Dicoding Indonesia. 
It demonstrates how to build a RESTful API using Django and Django REST Framework, and deploy it to Google Cloud Platform (GCP) using Gunicorn and Nginx.


#  Django Notes API (Deployed on GCP)

RESTful Notes API built with Django and Django REST Framework, deployed on Google Cloud Platform using Gunicorn and Nginx.

---

##  Features

* CRUD Notes API (Create, Read, Update, Delete)
* Django REST Framework
* Production-ready deployment
* Environment-based settings (dev & prod)
* Gunicorn + Nginx setup

---

##  Tech Stack

* Python 3.10.0
* Django 4.2
* Django REST Framework Version: 3.17.1
* Gunicorn
* Nginx
* Google Cloud Platform (GCP)

---

##  Live API

```bash
http://34.101.121.196/notes/
```

---

##  Project Structure

```bash
exercise-django-notes-app-backend/
│
├── notes/                     # Notes app (API logic)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── migrations/
│
├── notes_app_backend/        # Core Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   │
│   └── settings/             # Settings modularization
│       ├── __init__.py
│       ├── common.py         # Shared config
│       ├── dev.py            # Development config
│       └── prod.py           # Production config
│
├── manage.py
├── Pipfile
├── Pipfile.lock
└── .gitignore
```

---

##  Local Setup

### 1. Clone repository

```bash
git clone https://github.com/irma-damaiyanti25/exercise-django-notes-app-backend.git
cd exercise-django-notes-app-backend
```

### 2. Install dependencies

```bash
pip install pipenv
pipenv install
pipenv shell
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Run server

```bash
python manage.py runserver
```

---

##  API Endpoints

| Method | Endpoint       | Description     |
| ------ | -------------- | --------------- |
| GET    | `/notes/`      | Get all notes   |
| POST   | `/notes/`      | Create new note |
| GET    | `/notes/<id>/` | Get note detail |
| PUT    | `/notes/<id>/` | Update note     |
| DELETE | `/notes/<id>/` | Delete note     |

---

##  Production Setup (GCP)

### Key configuration:

* Gunicorn as WSGI server
* Nginx as reverse proxy
* Systemd service for Gunicorn
* Environment variable for SECRET_KEY

### Example:

```bash
export SECRET_KEY="your_secret_key"
```

### Collect static files:

```bash
python manage.py collectstatic
```

---

##  Environment Variables

| Variable   | Description                                |
| ---------- | ------------------------------------------ |
| SECRET_KEY | Django secret key (required in production) |

---

##  Learning Outcomes

This project demonstrates:

* Building REST API with Django
* Structuring Django settings (dev vs prod)
* Deploying to cloud server (GCP)
* Using Gunicorn & Nginx
* Managing environment variables securely

---

##  Future Improvements

* Add authentication (JWT)
* Use PostgreSQL instead of SQLite
* Add HTTPS with Certbot
* Dockerize application

---

##  Author

Irma Damaiyanti
