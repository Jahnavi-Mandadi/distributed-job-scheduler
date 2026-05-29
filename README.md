# Distributed Workflow Orchestration Platform

A simplified workflow orchestration platform inspired by Apache Airflow. Users can create DAGs (Directed Acyclic Graphs), define task dependencies, execute workflows, and monitor execution progress through a web-based dashboard.

## Features

### Workflow Management

* Create DAGs (workflows)
* Define workflow schedules using cron expressions
* Activate or deactivate workflows

### Task Management

* Create tasks within workflows
* Define task dependencies
* Support for Python-based tasks

### Workflow Execution

* Trigger DAG runs manually
* Execute tasks based on dependency order
* Track execution status

### Monitoring Dashboard

* View DAG runs
* View task runs
* Monitor workflow progress
* Track task execution status

### Containerization

* Dockerized backend
* Dockerized frontend
* PostgreSQL container
* Docker Compose orchestration

---

## Tech Stack

### Backend

* Python
* Flask
* SQLAlchemy
* PostgreSQL

### Frontend

* React
* Axios

### DevOps

* Docker
* Docker Compose
* Git
* GitHub

---

## Project Structure

```text
distributed-job-scheduler/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── extensions.py
│   │
│   ├── workflows/
│   │   ├── extract.py
│   │   ├── transform.py
│   │   ├── validate.py
│   │   └── load.py
│   │
│   ├── data/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── run.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── App.js
│   │
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## Architecture

```text
React Frontend
       │
       ▼
Flask REST API
       │
       ▼
 PostgreSQL
       │
       ▼
DAG
 │
 ▼
DAG Run
 │
 ▼
Task Runs
 │
 ▼
ETL Tasks
(Extract → Transform → Validate → Load)
```

---

## Database Models

### DAG

Stores workflow definitions.

### Task

Stores workflow tasks and dependencies.

### DAG Run

Tracks workflow execution history.

### Task Run

Tracks individual task execution status.

---

## Sample Workflow

### Hotel Booking ETL Workflow

1. Extract Booking Data
2. Transform Booking Data
3. Validate Booking Data
4. Load Reservation Data

Dependencies:

```text
Extract
   │
   ▼
Transform
   │
   ▼
Validate
   │
   ▼
Load
```

---

## Running Locally

### Clone Repository

```bash
git clone https://github.com/Jahnavi-Mandadi/distributed-job-scheduler.git
cd distributed-job-scheduler
```

### Start Application

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://localhost:5000
```

---

## API Endpoints

### DAG APIs

```http
GET    /dags
POST   /dags
POST   /dag_runs/run/<dag_id>
```

### Task APIs

```http
GET    /tasks
POST   /tasks
```

### Monitoring APIs

```http
GET    /dag_runs
GET    /task_runs
GET    /monitoring/progress/<dag_run_id>
```

---

## Screenshots

### Dashboard

(Add screenshot here)

### Workflow DAGs

(Add screenshot here)

### Workflow Tasks

(Add screenshot here)

### Monitoring Dashboard

(Add screenshot here)

### Docker Containers

(Add screenshot here)

---

## Future Enhancements

* APScheduler integration
* Cron-based automatic DAG execution
* Retry mechanism
* Task failure handling
* User authentication
* Role-based access control
* Celery worker integration
* Distributed execution engine
* Real-time monitoring
* Kubernetes deployment

---

## Learning Outcomes

This project helped me gain hands-on experience with:

* Flask application architecture
* REST API development
* PostgreSQL database design
* SQLAlchemy ORM
* React frontend development
* Workflow orchestration concepts
* Docker containerization
* Docker Compose
* Git and GitHub workflows
* ETL pipeline implementation
* Dependency-based task execution
