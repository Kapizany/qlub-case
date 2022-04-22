#image version
FROM python:3.8

WORKDIR /app

#env variables
ENV PYTHONPATH /app

#copy file with dependencies
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "api.py"]