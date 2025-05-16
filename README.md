## 📝 Flask To-Do App

A simple yet functional **Flask-based To-Do List Web App** with support for:

- Task creation, editing, and deletion  
- CSS styling  
- Containerization with Docker  
- Kubernetes deployment support  
- Render deployment configuration

---
## 🚀 Live Demo
>[Deployed on Render](https://to-do-app-1-9lsn.onrender.com)

## 🚀 Features

- Create, edit, delete tasks easily
- Minimalist UI built with HTML,CSS & JAVASCRIPT
- RESTful Flask backend
- Supports local development, Docker, and Kubernetes
- Render deployment enabled

---

## 🧠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS ,JAVASCRIPT
- **Containerization:** Docker  
- **Deployment:** Kubernetes / Render  
- **Version Control:** Git + GitHub  

---

## 🛠️ Project Structure

```bash
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── render.yaml             # Render deployment config
├── static/
│   └── index.css           # CSS styling
├── templates/
│   ├── index.html          # Main task list UI
│   └── edit.html           # Edit task UI
├── kubernetes/
│   ├── deployment.yaml     # Kubernetes deployment config
│   └── service.yaml        # Kubernetes service config
└── .gitignore              # Files/folders to ignore
```

## 🧪 Running Locally
🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/YASH36638/To-do-app.git
cd To-do-app
```
🔹 Step 2: Create Virtual Environment
```bash
python -m venv venv
venv/Scripts/activate
```
🔹 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
🔹 Step 4: Run Flask App
```bash
python app.py
```

