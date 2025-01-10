# FCFS - Personal Financial Management System

FCFS (Finance Control and Savings) is a personal financial management system designed to help users take control of their finances. With FCFS, users can manage their expenses, set savings goals, and organize their financial life efficiently.

## Features

- **User Authentication**: Secure login and signup system for personalized finance tracking.
- **Category Management**: Create and manage categories for better expense organization.
- **Transaction Tracking**: Add, update, and delete financial transactions, view transactions in a table with filtering options.
- **Savings Goals**: Set and track progress toward financial savings goals.
- **Responsive Design**: Fully responsive UI for seamless use on desktop and mobile devices.

## Tech Stack

- **Backend**: Django  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite (default) with support for PostgreSQL or MySQL if configured  
- **Authentication**: Django's built-in authentication system  

## Setup Instructions

```bash
# 1. Clone the Repository
git clone https://github.com/Ananttyagi004/fcfs.git
cd fcfs

# 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Set Up the Database
python manage.py makemigrations
python manage.py migrate

# 5. Run the Development Server
python manage.py runserver

# 6. Access the Application
# Open your browser and navigate to
http://127.0.0.1:8000
