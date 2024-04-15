FROM python:3.12.3

WORKDIR /apps/Auth

COPY . .

RUN apt-get update && apt-get install vim -y && apt-get install nmap -y
RUN .venv/Scripts/activate
RUN pip install poetry
RUN poetry install

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
