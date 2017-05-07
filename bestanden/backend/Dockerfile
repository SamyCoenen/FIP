FROM python:3.5.2

COPY req.txt /code/

WORKDIR /code
RUN pip install -r req.txt
COPY . /code/

WORKDIR /code/production_env
CMD ["/bin/bash", "-c", "python manage.py runserver 0.0.0.0:8000"]
