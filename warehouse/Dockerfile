FROM node:alpine as build-deps
WORKDIR /usr/src/app
COPY package*.json warehouse.json ./
RUN npm install -g json-server
RUN apk --no-cache add curl
RUN apk --no-cache add net-tools
RUN apk --no-cache add vim
COPY . ./
#RUN npm run build
EXPOSE 80
CMD ["json-server", "--watch" ,"--port", "80", "--host", "0.0.0.0", "warehouse.json"]
