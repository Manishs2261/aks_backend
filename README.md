# Product Management System - Backend

This is the REST API backend for the Product Management System. It is built using **Python**, **FastAPI**, and **MongoDB**. It handles user authentication (registration/login) and product CRUD operations.

## 🛠 Technology Stack
*   **Language:** Python 3.8+
*   **Framework:** FastAPI
*   **Database:** MongoDB
*   **Driver:** Motor (Async MongoDB driver)
* 

## ⚙️ Prerequisites
1.  **Python** installed on your machine.
2.  **MongoDB** installed and running locally on port `27017`.

## 🚀 Setup & Installation

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment (Optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install fastapi uvicorn
    pip install "fastapi[standard]"   
    ```
4.  **Run File:**
    ```bash
    #for mobile and change ip adrees
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    
    #see api details
    uvicorn main:app --reload
    
    ```

5 API endpoint details
   ```bash
    
    http://127.0.0.1:8000/docs
    
   ```

## 🗄️ Database Configuration
Ensure MongoDB is running locally. The application connects to:
*   **URL:** `mongodb://localhost:27017`
*   **Database Name:** `product_management`
*   **Collections:** `products`, `users`

*No manual database creation is required; the code will create it automatically upon the first write operation.*

## 🏃‍♂️ How to Run

Run the server using Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
