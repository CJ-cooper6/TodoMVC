FROM node:16-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm config set registry https://registry.npmmirror.com/
RUN npm install --production --loglevel=verbose

COPY . .
RUN npm i
RUN npm run build
EXPOSE 5173

CMD [ "npm", "run", "dev" ]