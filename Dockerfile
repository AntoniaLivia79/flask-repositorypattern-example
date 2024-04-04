FROM python:3.6


RUN mkdir -p /flask-app
WORKDIR /flask-app

# Copy files
COPY ./requirements.txt ./
COPY ./requirements_test.txt ./
COPY ./setup.py ./

# Copy folders
COPY app ./app

# Install packages
RUN pip install -r requirements.txt
RUN pip install -r requirements_test.txt

# Run flask app
EXPOSE 5000
ENV FLASK_APP="app/main.py" FLASK_DEBUG=1 FLASK_ENV=docker
CMD ["flask", "run", "-h", "0.0.0.0"]
