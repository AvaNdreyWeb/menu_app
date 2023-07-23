FROM python:3.11

WORKDIR /code

COPY ./requirements.txt ./requirements.txt

COPY ./api ./api

RUN pip install -r ./requirements.txt

EXPOSE 80

CMD ["uvicorn", "api.v1.main:app", "--host", "0.0.0.0", "--port", "80"]
