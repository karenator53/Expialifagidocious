FROM python:3.13.1-slim

WORKDIR /app

# Set environment variables for MongoDB
ENV MONGODB_URL="mongodb+srv://karenator:FWZAHxkIK6IGFakM@cluster0.l8l70.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ENV DB_NAME="karenator"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 