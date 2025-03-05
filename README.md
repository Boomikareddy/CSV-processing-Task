📂 CSV Processing with Django, Celery & Redis
This project enables users to upload CSV files, process them asynchronously using Celery and Redis, and display the processed results dynamically on the frontend.

🚀 Features
✔️ Upload and manage CSV files via a user-friendly interface
✔️ Process data asynchronously using Celery and Redis for efficiency
✔️ Compute sum, average, and count for numerical columns
✔️ Display results dynamically on the frontend

🔧 Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/Boomikareddy/csv-processing-django-main.git
cd csv-processing-django-main

2️⃣ Set Up a Virtual Environment
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Database Migrations
python manage.py migrate

5️⃣ Start Redis Server
redis-server  # (For macOS/Linux)
For Windows, install Redis separately and run it from the installed path.

6️⃣ Start the Celery Worker
celery -A csv_project worker --loglevel=info

7️⃣ Run the Django Development Server
python manage.py runserver

🛠 Technologies Used
Django – Backend framework
Celery – Asynchronous task processing
Redis – Task queue management
Bootstrap – Frontend styling
