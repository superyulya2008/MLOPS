# Используем официальный образ Jenkins
FROM jenkins/jenkins:latest

# Переключаемся на пользователя root для установки пакетов
USER root

# Обновление списка пакетов и установка Python и pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

# Создание виртуального окружения
RUN python3 -m venv /opt/venv

# Добавляем путь к бинарным файлам виртуального окружения в переменные среды
ENV PATH="/opt/venv/bin:$PATH"

# Обновление pip и установка зависимостей из requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Возвращаемся к пользователю jenkins
USER jenkins
