# Foodshala - Food Waste Management System

Foodshala is a full-stack web platform built with Django, designed to bridge the gap between restaurants with surplus food and NGOs (Non-Governmental Organizations) that feed those in need. The system aims to reduce food waste and provide a streamlined process for food donations.

The core of this project is a robust and secure user authentication system that manages different user roles (Restaurants and NGOs) and ensures all users are verified.

## Core Features

* **Secure User Authentication:** Full-featured system for user sign-up, sign-in, and sign-out.
* **Email-Based Account Activation:** New users receive a unique verification link via email to activate their account before they can log in. This prevents spam and verifies user identity.
* **Secure Token Generation:** Uses Django's `PasswordResetTokenGenerator` along with `urlsafe_base64_encode` to create secure, one-time-use activation links.
* **Custom User Validation:** Includes backend validation for unique usernames, unique emails, password matching, and alphanumeric-only usernames.
* **User Role Management:** (You can extend this) The system is designed to be expanded with different dashboards for "Restaurant" and "NGO" user types.
* **Donation Workflow:**
    * Restaurants can log in and post details about available surplus food.
    * NGOs can log in, view a dashboard of available donations, and claim them.

## Technical Stack

* **Backend:** Python, Django
* **Database:** SQLite3 (as configured in `settings.py`)
* **Authentication:** Django's built-in `User` model, `django.contrib.auth` for authentication, and custom views for registration logic.
* **Email Service:** `django.core.mail` with `EmailMessage` for sending asynchronous emails via SMTP (e.g., Gmail).

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dewansh3255/foodshala.git](https://github.com/dewansh3255/foodshala.git)
    cd foodshala
    ```

2.  **Install dependencies:**
    (It's recommended to use a virtual environment)
    ```bash
    # If you have a requirements.txt, run:
    pip install -r requirements.txt
    
    # If not, install the core framework:
    pip install django
    ```

3.  **Configure Email Settings:**
    For the email verification to work, you must update `foodshala/info.py` with your own email credentials (e.g., a Gmail "App Password").
    ```python
    # foodshala/info.py
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'your-email@gmail.com'
    EMAIL_HOST_PASSWORD = 'your-16-digit-app-password'
    EMAIL_PORT = 587
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.
