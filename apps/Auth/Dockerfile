FROM python:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /apps/Auth

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry env use python
RUN poetry install
EXPOSE 8000

COPY ./ .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]




