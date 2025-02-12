FROM python:3.8
WORKDIR /app
ENV PORT=8000
ADD . /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app

EXPOSE $PORT

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT