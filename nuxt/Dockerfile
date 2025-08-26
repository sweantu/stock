# Use official Node.js LTS
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Expose port (default Nuxt port)
EXPOSE 3000

# Run in development
CMD ["npm", "run", "dev"]