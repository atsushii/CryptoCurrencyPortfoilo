FROM python:3.6


WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "flask", "run", "-h", "0.0.0.0"]



