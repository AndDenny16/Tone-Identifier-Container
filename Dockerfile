FROM python:3.11


WORKDIR /app

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

COPY . .

EXPOSE 5000

# Define the command to run your app
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]