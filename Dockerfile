FROM python:3.10.4-slim-buster

WORKDIR /NLTK-Me!_Web

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV DJANGO_NTLK=views.py

CMD [ "python3", "manage.py" , "runserver"]