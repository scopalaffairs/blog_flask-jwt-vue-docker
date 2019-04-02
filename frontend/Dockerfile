# build stage
FROM node:latest as build-stage

WORKDIR /frontend
RUN npm install -g @vue/cli
COPY /app/package.json ./
RUN npm install
COPY ./app .

## production stage
#FROM nginx:latest as production-stage
#COPY --from=build-stage /app/dist /usr/share/nginx/html
#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]
