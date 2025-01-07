# Todo Application with Docker Compose

This project contains a simple Todo application with separate services for handling users and tasks. It uses Docker Compose to manage the services, allowing for easy deployment and orchestration of the different components.

## Services

### 1. **User Service (user-service)**

The **user-service** is a Flask-based Python application that manages user-related functionality in the Todo application, such as user registration, authentication, and login. It connects to the PostgreSQL database to store user data.

- **Ports**: `5000:80`
- **Service Directory**: `./user-service`
- **Image**: Custom Python image based on `python:3.9-slim`
- **Command**: `python app.py` (Runs the Flask application)
- **Dependencies**: 
  - `Flask`
  - `Werkzeug` (for URL handling)

### 2. **Task Service (task-service)**

The **task-service** is a Node.js application that handles all task-related functionality, such as adding, updating, and deleting tasks. It communicates with the PostgreSQL database to store task data and interacts with Redis for caching.

- **Ports**: `5001:80`
- **Service Directory**: `./task-service`
- **Image**: Custom Node.js image based on `node:16`
- **Command**: `nodemon server.js` (Runs the Express server with live reloads using `nodemon`)
- **Dependencies**: 
  - `Express`
  - `Nodemon` (for development use)

### 3. **Worker Service (worker)**

The **worker** service processes background tasks asynchronously. It connects to Redis to listen for tasks and process them in the background (e.g., sending email notifications or processing large tasks).

- **Service Directory**: `./worker`
- **Command**: Runs Node.js worker script to process jobs from Redis.
- **Dependencies**: 
  - `redis`
  - `bull` (optional for job queues)

### 4. **Redis Service (redis)**

The **redis** service is used as a cache and message broker. It helps the application with caching frequently used data and facilitates communication between services, such as task processing.

- **Image**: `redis:alpine`
- **Ports**: `6379` (exposed for internal use)
- **Networks**: Connected to `back-tier`

### 5. **Database Service (db)**

The **db** service uses PostgreSQL to store user data and tasks. It persists user information and tasks and provides a reliable data store for the application.

- **Image**: `postgres:9.4`
- **Ports**: Not exposed (internal access only)
- **Container Name**: `db`
- **Environment Variables**:
  - `POSTGRES_USER: postgres`
  - `POSTGRES_PASSWORD: postgres`
- **Volumes**: 
  - `db-data:/var/lib/postgresql/data` (persistent storage)
- **Networks**: Connected to `back-tier`

## Docker Compose Configuration

This project uses `docker-compose.yml` to manage multi-container Docker applications. The services are configured as follows:

- **Networks**:
  - `front-tier`: For communication between user-service and task-service.
  - `back-tier`: For communication between worker, db, and redis services.
  
- **Volumes**:
  - `db-data`: A volume used to persist PostgreSQL data.

### Docker Compose Workflow

1. **Building the Images**: The images for all services are built automatically when you run `docker-compose up --build`. This builds the custom images based on the `Dockerfile` configurations in each service directory.

2. **Running the Services**: All services are started by Docker Compose, and they communicate with each other based on the network configurations.

3. **Service Dependencies**: The `worker` service depends on `redis` and `db`, meaning those services will be started first.

4. **Port Mapping**: Each service exposes its ports to the host machine so that you can access the APIs.

## Getting Started

### Prerequisites

- **Docker** (version 19.03 or higher)
- **Docker Compose** (version 1.27 or higher)

### Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-name>
