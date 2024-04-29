#
FROM python:3.12

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

#
COPY ./app /code/app

# COPY .local_env /code/.local_env

# Load environment variables from .env file
ARG GOOGLE_APPLICATION_CREDENTIALS

# Set the environment variables in the container
ENV GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS

#
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]