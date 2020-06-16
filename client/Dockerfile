FROM node:latest

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json

RUN npm install --silent

EXPOSE 3000

CMD ["npm", "start"]

# add middleware to connect flask and react app