# Use official Node LTS image
FROM node:20-slim

# Set working directory
WORKDIR /app

# Copy package files first (better caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Expose Nuxt default dev port
EXPOSE 3000

# Run Nuxt in dev mode
CMD ["npm", "run", "dev"]