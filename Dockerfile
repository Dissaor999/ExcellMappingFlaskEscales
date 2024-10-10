FROM python:3.11.3

# Set up environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends
# Create and set the working directory
WORKDIR /app
#RUN chmod -R 777 ./app/files

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .


# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python","app/app.py"]

