# set base image
FROM python:3.9.5-slim

LABEL author="Sebastien Giordano"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0,.herokuapp.com

# install dependencies
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Add application
COPY . /app/

EXPOSE 8000

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn oc_lettings_site.wsgi:application --bind :$PORT
