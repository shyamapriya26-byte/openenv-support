FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use PORT environment variable (set by Hugging Face)
ENV PORT=7860
EXPOSE $PORT

CMD uvicorn app:app --host 0.0.0.0 --port $PORT