# comando para crear un volumen asociado a una carpeta
```
docker run -d --rm -p 80:80 -v c:/html:/usr/share/nginx/html --name nginx-codigo nginx:alpine
```