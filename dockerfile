FROM python:3.11-slim

WORKDIR /app/pipeline

COPY . /app/pipeline/

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app/pipeline/src

CMD ["streamlit", "run", "src/webapp/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

