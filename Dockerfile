FROM python:alpine

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]