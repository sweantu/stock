# Dockerfile
FROM node:20-slim

# Set working directory
WORKDIR /app

# Copy only package files first for caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app
COPY . .

# Expose Nuxt dev port
EXPOSE 3000

# Run Nuxt dev server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]