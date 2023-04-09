FROM apache/spark-py:latest

WORKDIR /app
COPY spark_jobs/test.py .