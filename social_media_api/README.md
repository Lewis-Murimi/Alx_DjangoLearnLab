# Social Media API

A basic Social Media API built with Django and Django REST Framework (DRF) that supports user registration, authentication, and profile management.

---

## Table of Contents
- [Project Setup](#project-setup)
- [Installation](#installation)
- [Database Migrations](#database-migrations)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [User Model Overview](#user-model-overview)
- [Authentication](#authentication)
- [Testing](#testing)
- [Notes](#notes)

---

## Project Setup

This project uses Django with Django REST Framework and token-based authentication. It includes a custom user model with additional fields like `bio`, `profile_picture`, and `followers`.

---

## Installation

1. **Clone the repository:**
```bash
git clone <repository_url>
cd social_media_api
````
2. **Create a virtual environment(optional):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install the required packages:**
```bash
pip install -r requirements.txt
pip install django djangorestframework djangorestframework-authtoken Pillow
```
## Database Migrations
4. **Apply database migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```
## Running the Server
5. **Run the development server:**
```bash
python manage.py runserver
```
## API Endpoints
### User Registration
- **Endpoint:** `POST /api/accounts/register/`
- **Description:** Register a new user.
- **Request Body:**
```json
{
    "username": "string",
    "password": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "bio": "string",
    "profile_picture": "file"
}
```
- **Response:**
```json
{
    "id": "integer",
    "username": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "bio": "string",
    "profile_picture": "url",
    "followers": []
}
```
### User Login
- **Endpoint:** `POST /api/accounts/login/`
- **Description:** Authenticate a user and obtain a token.
- **Request Body:**
```json
{
    "username": "string",
    "password": "string"
}
```
- **Response:**
```json
{
  "token": "string"
}
```