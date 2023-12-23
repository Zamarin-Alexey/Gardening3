FROM python:latest

WORKDIR ./usr/src/Gardening3

RUN apt-get update \
      && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev
RUN pip install --upgrade pip

COPY requirements.txt ./
# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r requirements.txt

#RUN python manage.py makemigrations blog plants users && python manage.py migrate
#CMD ["manage.py", "runserver"]