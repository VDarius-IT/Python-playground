FROM node:18-alpine

WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --only=production

COPY public ./public
COPY server.js ./
COPY examples ./examples

EXPOSE 3000
CMD ["node", "server.js"]
