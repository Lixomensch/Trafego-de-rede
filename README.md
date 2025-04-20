# 🌐 Network Device Monitoring

A simple system for monitoring network devices with simulated traffic, using **Flask** for the backend, **SQLite** for the database, and **Streamlit** for the frontend.

## 🚀 How to Run

### Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- _(Optional)_ [Python](https://www.python.org/) with [Streamlit](https://streamlit.io/) and [Flask](https://flask.palletsprojects.com/) to run locally without Docker.

### 1. Running with Docker Compose

To start both backend and frontend services:

```bash
docker compose up --build
```

- Backend available at: `http://localhost:5000/devices`
- Frontend (Streamlit interface): `http://localhost:8501`

### 2. Running Locally (Without Docker)

#### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## ⚙️ Features

- 📥 **Add devices** with IP, name, and traffic rate
- 📄 **List all registered devices**
- ❌ **Delete devices**
- 🚦 **Traffic status indicator**:
  - Green: Normal traffic
  - Red: High traffic (over 50 Mbps)

## 📁 API Endpoints

| Method | Route           | Description                |
| ------ | --------------- | -------------------------- |
| GET    | `/devices`      | Get all registered devices |
| POST   | `/devices`      | Add a new device           |
| DELETE | `/devices/<id>` | Delete a device by its ID  |

## 🐳 Docker Images

### Backend - `backend/Dockerfile`

```Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
```

### Frontend - `frontend/Dockerfile`

```Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🛠️ Tech Stack

- 🐍 Python 3
- 🌐 Flask (Backend API)
- 📊 Streamlit (Frontend UI)
- 🗃️ SQLite (Database)
- 🐳 Docker & Docker Compose

## ⚠️ Notes

- Ensure the `backend` folder has write permissions so `devices.db` can be created.
- If you encounter SQLite permission errors inside Docker, you may need to map a volume with proper permissions in `docker-compose.yml`.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
