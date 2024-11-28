FROM python:3.8-slim-buster
WORKDIR /app
COPY requirement.txt requirement.txt
RUN 
COPY . .
EXPOSE 8000
CMD python manage.py runserver


