FROM pitervergara/geodjango
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD python manage.py migrate; gunicorn -b 0.0.0.0:8000 embrace.wsgi
