#imagen base
FROM ubuntu:latest

#instalacion de dependencias
RUN apt-get update
RUN apt-get install python3 python3-dev python3-pip -y

#copiamos archivos a la imagen
COPY index.html .

#ejecutamos un comando de terminal
CMD ["python3", "-m", "http.server", "5000"]

#exponemos el puerto 5000
EXPOSE 5000