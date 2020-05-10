FROM python:3

LABEL maintainer="patelvivek3835@gmail.com"

# Set the working directory.
WORKDIR /usr/src/

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

