FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8000

CMD ["pipenv", "run", "python", "generate_fake_data.py"]

CMD ["pipenv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]