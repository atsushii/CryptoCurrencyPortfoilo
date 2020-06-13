FROM node:8.11.3

WORKDIR /app/client

COPY package.json /app/client/package.json

RUN npm install --silent

EXPOSE 3000

CMD ["npm", "start"]

# add middleware to connect flask and react app