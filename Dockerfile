#I am using python 3.12.5 in my local environment
FROM python:3.12-slim

WORKDIR /myapp

COPY requirements.txt /myapp

RUN pip install --no-cache-dir -r requirements.txt

COPY . /myapp

ENV PYTHONPATH=/myapp/src

EXPOSE 8501

CMD ["streamlit", "run", "src/webapp/app.py", "--server.port=8501", "--server.address=0.0.0.0"]