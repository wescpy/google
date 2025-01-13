FROM node:22-slim
WORKDIR /app
COPY package.json .
RUN npm i
COPY . .
ENTRYPOINT ["node", "index.mjs"]
