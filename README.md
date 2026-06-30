# Little Lemon Restaurant API - Capstone Project

This repository contains the completed Back-End Developer Capstone Project for the Little Lemon restaurant application. It provides a full backend architecture built using Python, Django, and Django REST Framework, complete with database migrations, table booking capabilities, menu items management, and token authentication.

---

## Project Structure & Features
* **Menu Management:** Endpoints to add, view, update, and delete items from the menu.
* **Table Booking System:** View customer table reservations.
* **Token Authentication:** Secure API endpoints requiring user token generation.
* **Clean Codebase:** Clean separation of apps and configurations, entirely stripped of unnecessary local environment dependencies (`venv`).

---

## API Endpoints Reference

Based on the required project architecture shown in image_645dfc.png, the API implements the following endpoint schema:

### 1. Menu Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/restaurant/menu/` | Fetch all available menu items |
| **POST** | `/restaurant/menu/` | Add a new menu item |
| **GET** | `/restaurant/menu/<int:pk>` | Fetch a specific menu item details by ID |
| **PUT** | `/restaurant/menu/<int:pk>` | Update a specific menu item by ID |
| **DELETE** | `/restaurant/menu/<int:pk>` | Delete a specific menu item by ID |

### 2. Booking Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/restaurant/booking/tables/` | Retrieve a list of all active table reservations |

### 3. Authentication Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/restaurant/api-token-auth/` | Submit user credentials to generate an API Auth Token |

---

## Local Development URLs

When running the project locally (`python manage.py runserver`), you can interact with the app via the following links as shown in image_645dfc.png:

* **Home Interface:** `http://127.0.0.1:8000/`
* **Menu View:** `http://127.0.0.1:8000/restaurant/menu/`
* **Booking View:** `http://127.0.0.1:8000/restaurant/booking/tables/`
* **Token Authentication:** `http://127.0.0.1:8000/restaurant/api-token-auth/`

---

## How to Run & Test Locally

1. **Install Dependencies:**
   Ensure you have Django and Django REST Framework installed in your environment.
   
2. **Apply Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate