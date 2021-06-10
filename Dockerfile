FROM python:3.8-slim-buster

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

env PORT=8080

CMD ["python","-u", "run.py"]
