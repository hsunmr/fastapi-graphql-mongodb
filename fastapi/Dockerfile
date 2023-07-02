FROM python:3.11

RUN apt-get update

# install requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app

CMD ["uvicorn", "main:create_app", "--host", "0.0.0.0", "--reload"]