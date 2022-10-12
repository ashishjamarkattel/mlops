FROM python:3.7

WORKDIR /mlops
COPY setup.py setup.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY tagifai tagifai
COPY app app
COPY data data
COPY config config


## since our application require prot 8000
EXPOSE 8000

# Start app
CMD [ "python", "./app/api.py"]
