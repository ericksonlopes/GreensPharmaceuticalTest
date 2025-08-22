FROM python:3.10-slim

WORKDIR /greens

COPY . .

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]