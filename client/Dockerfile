FROM node:latest

WORKDIR /app/client

ENV PATH /app/client/node_modules/.bin:$PATH

COPY package.json /app/client/package.json

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]

# add middleware to connect flask and react app