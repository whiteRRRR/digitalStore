# Use the base Python image
FROM python:3.12.3

# Set the working directory inside the container
WORKDIR /apps/Auth

# Copy the local directory contents into the container at /apps/Auth
COPY . .

# Install Poetry
RUN pip install poetry

# Install dependencies using Poetry
RUN poetry install
RUN poetry env use python3.12
RUN poetry shell

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3434"]