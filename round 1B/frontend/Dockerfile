# Use official Node image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./
# Copy all frontend files (including src, postcss.config.js, tailwind.config.js, etc.)
COPY . .
# Install all deps including devDependencies (after copying everything)
RUN npm install && npm install -g vite

# Expose Vite port
EXPOSE 5173

# Start Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]
