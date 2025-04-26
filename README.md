---

# Farm Management System with Authentication

This is a fully functional **Farm Management System** built using **Django**. It includes user authentication (login, registration, logout) and features a **responsive design** powered by **Bootstrap**. The system helps farmers efficiently manage farm activities such as crop planning, inventory tracking, and employee supervision.

## Features

- **User Authentication:**
  - User login and registration
  - User roles (Admin, Farmer, etc.)

- **Farm Management:**
  - Manage crops (add, update, delete)
  - Track farm inventory (seeds, tools, equipment)
  - Employee management (assign tasks, track progress)

- **Responsive Design:**
  - Fully responsive UI using **Bootstrap** for compatibility with all devices

- **Additional Features:**
  - Dashboard with insights into farm activities
  - Crop health monitoring *(future enhancement)*

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)
- **Authentication:** Django's built-in auth system
- **Version Control:** Git

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Django 3.x or above
- Bootstrap (already included in templates)

### Steps to Run the Project Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/farm-management-system.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd farm-management-system
   ```

3. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. Open your browser and go to:  
   [http://localhost:8000](http://localhost:8000)

### Admin Access

Access the Django admin panel at:  
[http://localhost:8000/admin/](http://localhost:8000/admin/)  
Log in with your superuser credentials.

## Usage

1. **Authentication:**
   - Login at `/login/`
   - Register at `/register/`

2. **Dashboard:**
   - View overall farm insights after logging in

3. **Crops:**
   - Add, update, or delete crop records

4. **Inventory:**
   - Track seeds, fertilizers, tools, and other inventory items

5. **Employees:**
   - Manage workers, assign tasks, and monitor progress

## Directory Structure

```
farm-management-system/
│
├── farm_management/              # Django app for core functionality
├── templates/                    # HTML templates
│   ├── base.html                 # Bootstrap base template
│   ├── dashboard.html            # Main dashboard view
│   └── login.html                # Login view
│
├── static/                       # Static files (CSS, JS, images)
├── manage.py                     # Django entry point
├── requirements.txt              # Project dependencies
└── settings.py                   # Project settings
```

## Contributing

If you'd like to contribute:

1. Fork this repo
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to your branch: `git push origin feature-name`
5. Open a pull request!

Please follow existing code style and add tests for any new functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

