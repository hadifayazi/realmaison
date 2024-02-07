FROM node:20.11-alpine

LABEL version="1.0"
LABEL description="frontend for realestate app"

WORKDIR /app

COPY ./package*.json ./

RUN npm install

COPY . .

CMD [ "npm", "run", "start" ]