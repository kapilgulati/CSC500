FROM python:3.12-slim

RUN apt-get update -y
RUN apt-get install nano unzip
RUN apt-get install -y python3.10
RUN apt install curl -y

RUN curl -fsSL https://get.data.dev/cli.sh | sh

# set working directory
WORKDIR /app

# Copy content of current directory to /app
COPY . /app

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port 8000
ENV PORT=8000
EXPOSE 8000

# start FastAPI server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]