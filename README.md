# 📝 Django To-Do List Application

A clean and simple task management web app built with Django.  
Users can register, log in, and manage their personal to-do items (create, edit, delete, view details).  
Perfect for learning Django fundamentals or as a starting point for a more advanced project.

---

## ✨ Features

- User authentication (register, login, logout)
- Add new tasks with title and description
- Edit or delete existing tasks
- Mark tasks as done (checkbox)
- View task details in a separate page
- Personal task list per user (tasks are isolated)
- Responsive design (basic templates included)

---

## 🛠️ Tech Stack

- **Python** 3.8+
- **Django** 5.2.14
- **SQLite** (default database)
- **Bootstrap** (optional – you can add your own CSS/JS)

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher installed
- `pip` (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/todolist-django.git
   cd todolist-django
Create and activate a virtual environment

Windows:

bash
python -m venv venv
venv\Scripts\activate
macOS / Linux:

bash
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
pip install django
💡 If you have a requirements.txt file, use pip install -r requirements.txt instead.

Apply database migrations

bash
python manage.py migrate
Create a superuser (optional, for admin panel)

bash
python manage.py createsuperuser
Run the development server

bash
python manage.py runserver
Open your browser and visit http://127.0.0.1:8000/

📁 Project Structure
ToDOList_PROJECT/
├── app/                      # Main application
│   ├── migrations/
│   ├── templates/            # HTML templates
│   │   ├── home.html
│   │   ├── home_details.html
│   │   ├── add_task.html
│   │   ├── task_delete.html
│   │   ├── login.html
│   │   └── register.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── ToDOList_PROJECT/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3                # SQLite database (auto-created)
├── manage.py
└── README.md
⚠️ The templates shown above are expected by the views. If they are missing, the app will raise TemplateDoesNotExist. Make sure you create them or adjust the view logic.

🧪 Usage Example
Register a new account at /register/

Log in at /login/

On the home page, you’ll see your task list

Click “Add Task” to create a new one

Use the edit (✏️) or delete (🗑️) buttons next to each task

Click on a task title to see its full details

Log out using the logout button

🧰 Customisation Ideas
Add due dates or priority levels to tasks

Implement search & filter functionality

Style the pages with Bootstrap or Tailwind CSS

Deploy the app using PythonAnywhere, Render, or Heroku

Convert into a desktop app using PyInstaller + run.py (as discussed)

⚠️ Important Notes for Production
Set DEBUG = False in settings.py

Add your domain to ALLOWED_HOSTS

Use a more secure SECRET_KEY (environment variable)

Switch to a production database like PostgreSQL

📄 License
This project is open‑source and available under the MIT License.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📧 Contact
If you have any questions, feel free to reach out – or simply open an issue on GitHub.

Happy coding! 🚀

------------------------------------------------------------------------------------------------------------------------

# 📝 اپلیکیشن فهرست کارها با جنگو (Django To-Do List)

یک اپلیکیشن تحت وب ساده و تمیز برای مدیریت کارهای روزانه.  
کاربران می‌توانند ثبت‌نام کنند، وارد سیستم شوند و کارهای شخصی خود را اضافه، ویرایش، حذف یا انجام‌شده علامت بزنند.  
این پروژه برای یادگیری مفاهیم پایه‌ی جنگو یا شروع یک پروژه‌ی پیشرفته‌تر عالی است.

---

## ✨ قابلیت‌ها

- احراز هویت کاربر (ثبت‌نام، ورود، خروج)
- اضافه کردن کار جدید با عنوان و توضیحات
- ویرایش یا حذف کارهای موجود
- علامت زدن انجام شدن کار (چک‌باکس)
- مشاهده‌ی جزئیات هر کار در صفحه‌ای جداگانه
- لیست کارهای شخصی برای هر کاربر (کارها از یکدیگر جدا هستند)
- طراحی واکنش‌گرا (Responsive) – می‌توانید از Bootstrap یا CSS دلخواه استفاده کنید)

---

## 🛠️ تکنولوژی‌های استفاده شده

- **Python** نسخه 3.8 یا بالاتر
- **Django** نسخه 5.1.3
- **SQLite** (پایگاه داده پیش‌فرض)
- **Bootstrap** (اختیاری – خودتان می‌توانید استایل اضافه کنید)

---

## 🚀 راه‌اندازی پروژه

برای اجرای پروژه روی سیستم خودتان، مراحل زیر را به ترتیب انجام دهید.

### پیش‌نیازها

- Python نسخه 3.8 یا بالاتر نصب شده باشد.
- `pip` (مدیر بسته‌های پایتون) در دسترس باشد.

### نصب و اجرا

1. **کلون کردن مخزن (یا کپی کردن فایل‌ها)**
   ```bash
   git clone https://github.com/yourusername/todolist-django.git
   cd todolist-django