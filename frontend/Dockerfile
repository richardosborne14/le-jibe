FROM node:20-slim

WORKDIR /app

# Install dependencies first (cached layer)
COPY package.json package-lock.json* ./
RUN npm install

# Copy application code
COPY . .

EXPOSE 5173

# Hot reload in dev (source is bind-mounted via docker-compose)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
