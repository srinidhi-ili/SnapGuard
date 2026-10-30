# SnapGuard – AWS Snapshot Management System

## 1. Project Overview

SnapGuard is a cloud-based application designed to monitor and manage AWS EBS snapshots. It provides dashboard statistics and an API for retrieving snapshot information from AWS.

## 2. Technologies Used

* Python
* Flask
* Flask-CORS
* Boto3
* Amazon Web Services (AWS)
* HTML, CSS, and JavaScript

## 3. Backend Overview

The backend is developed using Python Flask. It provides REST API endpoints that allow the frontend to communicate with the backend.

### Main Backend Files

* `backend/app.py` – Defines Flask application and API endpoints.
* `backend/aws_services.py` – Contains AWS snapshot retrieval logic.
* `backend/requirements.txt` – Lists required Python packages.

## 4. API Endpoints

### A. Home API

**Endpoint:** `/`

**Method:** GET

**Purpose:** Checks whether the backend application is accessible.

### B. Health Check API

**Endpoint:** `/api/health`

**Method:** GET

**Purpose:** Returns the backend health status.

**Expected result:** HTTP 200 OK when the endpoint is working.

### C. Dashboard API

**Endpoint:** `/api/dashboard`

**Method:** GET

**Purpose:** Returns dashboard statistics.

**Current mode:** Demo mode. Snapshot counts and lifecycle policy counts are sample values, not live AWS data.

### D. Snapshots API

**Endpoint:** `/api/snapshots`

**Method:** GET

**Purpose:** Retrieves EBS snapshot information from AWS through the backend AWS service function.

**Current limitation:** AWS credentials are not available, so live snapshot retrieval is currently pending.

## 5. Running the Backend

Open a terminal in the SnapGuard project root directory.

Install the dependencies:

```bash
python -m pip install -r backend/requirements.txt
```

Start the Flask server:

```bash
python backend/app.py
```

The backend runs at:

`http://127.0.0.1:5000`

## 6. Testing the APIs

Open these endpoints in a browser while the Flask server is running:

* Home: `http://127.0.0.1:5000/`
* Health: `http://127.0.0.1:5000/api/health`
* Dashboard: `http://127.0.0.1:5000/api/dashboard`
* Snapshots: `http://127.0.0.1:5000/api/snapshots`

## 7. Current Project Status

* Flask backend setup: Completed
* Health API: Tested successfully
* Dashboard API: Tested successfully using demo data
* Snapshots API: Implemented; AWS authentication is pending
* Live AWS integration: Pending AWS account access and credential configuration

## 8. Team Responsibilities

* Member 1: Frontend HTML and CSS
* Member 2: JavaScript dashboard functionality
* Member 3: AWS snapshot management and lifecycle configuration
* Member 4: Python Flask backend and API development
* Member 5: AWS integration using Boto3

## 9. Important Note

The dashboard currently displays demo statistics. Live AWS snapshot data will be available only after the required AWS access and authentication are configured.
