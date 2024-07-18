FROM python:3.10-alpine

WORKDIR /app

COPY . .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3" ,"app.py"]