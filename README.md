# Django Mini Blogging App 2.0

A *full-fledged blogging platform* built with Django where users can sign up, log in, and create, edit, or delete their own blog posts.

---

## Features

✅ User Authentication (Signup, Login, Logout)  
✅ Create, Read, Update, Delete (CRUD) Blogs  
✅ Each user can manage only their own blogs  
✅ Contact form integrated  

---

## Tech Stack

•⁠  ⁠*Backend:* Django 5  
•⁠  ⁠*Frontend:* HTML, CSS (Django Templates)  
•⁠  ⁠*Database:* SQLite3 (default)  
•⁠  ⁠*Version Control:* Git & GitHub  
•⁠  ⁠*Environment:* Python Virtual Environment

---

##  Installation Guide

### 1️⃣ Clone the Repository

git clone https://github.com/Salonikumari95/django-mini-blog-2.0.git
cd django-mini-blog-2.0

2️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Requirements

pip install -r requirements.txt

4️⃣ Create .env File

Inside project root, create a file named .env and add:

SECRET_KEY=your_secret_key
DEBUG=True

5️⃣ Run Migrations

python manage.py migrate

6️⃣ Start the Development Server

python3 manage.py runserver

Open your browser and go to http://127.0.0.1:8000/


---

 User Flow

1. New users can sign up.


2. Logged-in users can create, edit, delete their blogs.


3. Visitors can read all blogs.



---

📸 Screenshots

<img width="1383" height="534" alt="signup" src="https://github.com/user-attachments/assets/481489fa-bda8-4015-b385-d4b9dc9e66d1" />
<br>
SIGNUP PAGE
<br>
<img width="1376" height="406" alt="login" src="https://github.com/user-attachments/assets/04dcfb74-1084-4e98-bc2b-28c349efa4e0" />
<br>
LOGIN PAGE
<br>
<img width="1361" height="629" alt="createBlog" src="https://github.com/user-attachments/assets/c1fcf4b4-07fc-460e-9c75-e2d70f0f14d3" />
<br>
CREATE BLOG PAGE
<br>
<img width="1377" height="650" alt="myblogpost" src="https://github.com/user-attachments/assets/5922c3a2-264a-4f66-aa1a-f268d5b3a58f" />
<br>
MY BLOG POST
---



 Author

 Saloni Kumari



---


### Steps to add this README

1. In terminal (inside project folder):
   touch README.md
   open -e README.md



2.⁠ ⁠Push it to GitHub:

git add README.md
git commit -m "mini-blog2.0"
git push origin main




---

