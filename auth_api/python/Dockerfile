FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000
# MAINTANER Johnnatan Malpica "jmalpica@gmail.com"


WORKDIR /usr/src/app
EXPOSE 8000
COPY requirements.txt .
RUN pip install -qr requirements.txt
COPY * ./
CMD ["python3", "./api.py"]