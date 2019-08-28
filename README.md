[![build passing](https://img.shields.io/badge/build-passing-brightgreen)](https://img.shields.io/badge/build-passing-brightgreen)

### Flask/Vue Boilerplate Setup 

#### with POSTGRESQL
#### bundled via Docker Compose


----
# Docker

Run `docker-compose up` in project root.

----

# Flask backend API

## Development server

Run `python app.py` to start development server on port `8080` to watch files and restart on update.


## Use from docker container

Clone project on your remote machine (needs to have docker daemon installed), then build image (`docker build -t flask-backend .`) and finally run the image by using `docker run -p 8080:8080 -v /HOST/PATH/TO/BACKEND/FOLDER:/app flask-backend`.

----

# Vue frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compile and minify for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Run your end-to-end tests
```
npm run test:e2e
```

### Run your unit tests
```
npm run test:unit
```


----
