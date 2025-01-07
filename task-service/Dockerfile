# Use an official Node.js image as the base
FROM node:16

# Set the working directory
WORKDIR /app

# Copy only the package files first for dependency installation
COPY package.json package-lock.json ./

# Install dependencies (includes nodemon if it's in the package.json)
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port your application runs on
EXPOSE 80

# Start the application
CMD ["npm", "start"]
