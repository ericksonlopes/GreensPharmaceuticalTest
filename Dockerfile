FROM python:3.10

WORKDIR /greens
COPY . .

RUN pip install uv
RUN uv sync

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]