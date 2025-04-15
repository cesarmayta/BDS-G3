# comando para desplegar una imagen Dockerfile
```
docker build -t python-web-datag3:1.0 .
docker run  -d --rm -p 5000:5000 --name webpyg3 python-web-datag3:1.0
```