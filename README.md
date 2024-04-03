# Flask Web App Project

This is a simple Flask web application that demonstrates how to render HTML pages using Flask's `render_template` function. The application defines two routes: `/` and `/route2`, each rendering a different HTML template.

## Project Structure

The project directory structure is as follows:

```
project/
│
├── app/
│ ├── server.py
│ ├── templates/
│ │ ├── main_page.html
│ │ └── route_two.html
│ └── Dockerfile

```


- `server.py`: This is the main Python script that defines the Flask application.
- `templates/`: This directory contains HTML templates used by the Flask application.
  - `main_page.html`: HTML template for the main page.
  - `route_two.html`: HTML template for the second route.

## Docker

The project includes a Dockerfile for containerization. You can build and run the Docker container using the following commands:

1. **Build the Docker image:**
```
docker build -t my-flask-app .
```

2. **Run the Docker container:**
```
docker run -p 5000:5000 my-flask-app
```


## Usage

Once the Docker container is running, you can access the Flask application in your browser at `http://localhost:5000/`.

## Dependencies

This project requires Python 3.x and Flask. Dependencies are managed using pip. Ensure you have Docker installed to build and run the Docker container.
