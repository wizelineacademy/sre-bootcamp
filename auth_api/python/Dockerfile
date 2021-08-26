FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000
WORKDIR /home

CMD mkdir auth_api

WORKDIR /home/auth_api

COPY . /home/auth_api
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT python3 api.py