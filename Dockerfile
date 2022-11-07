FROM python:3.7.9
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app_core.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5500
CMD ["flask", "run"]