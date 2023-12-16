FROM python

WORKDIR /app

RUN pip install fastapi

COPY . .

CMD ["python", "main.py"]