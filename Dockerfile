# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip3 install --no-cache-dir -r /code/requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Expose port 8000 for the Flask app
EXPOSE 8000

# Environment variables for Flask
ENV FLASK_APP=app.server
ENV FLASK_ENV=development

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000", "--no-reload"]
