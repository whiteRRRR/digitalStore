# Используем базовый образ Python
FROM python:3.12.3

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /apps

COPY . /apps/Auth


RUN pip install poetry && \
    poetry env use python3.12 &&\
    poetry shell &&\
    poetry install && \

