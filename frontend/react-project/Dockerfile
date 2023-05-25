FROM node:20.1-alpine
WORKDIR ./react-project

COPY package.json package-lock.json ./
RUN npm install 
COPY . ./
EXPOSE 3000