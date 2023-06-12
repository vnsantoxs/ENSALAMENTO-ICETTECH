FROM python:3.10.6

ENV PYTHONUBUFFERED=1

WORKDIR /Docker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python","manage.py","runserver" ]

