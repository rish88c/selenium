# Use a base image
FROM node:12.2.0-alpine

# Set the working directory
WORKDIR /app

# Copy your application files into the container
COPY . .

# Update package lists and install necessary packages
RUN apk update && \
    apk add python3 py3-pip && \
    apk add --no-cache bash

# Install dependencies and run tests
RUN npm install && \
    npm run test

# Expose the port your app runs on
EXPOSE 8000

# Define the command to run your application
CMD ["node", "app.js"]
