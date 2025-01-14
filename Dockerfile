FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /olx_scraper

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./wait-for-it.sh /olx_scraper/wait-for-it.sh
RUN chmod +x /olx_scraper/wait-for-it.sh

COPY . /olx_scraper

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
