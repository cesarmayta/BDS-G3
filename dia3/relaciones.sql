-- Active: 1734576840998@@127.0.0.1@3306@datag3
-- sentencias DML

CREATE TABLE alumno(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(10) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    curso VARCHAR(100),
    nota DOUBLE
);
insert into alumno(nro_documento,nombre)
VALUES
('100','cesar'),
('200','ana'),
('300','luis'),
('400','jose'),
('500','raul'),
('600','carmen'),
('700','jorge'),
('800','daniel'),
('900','luisa'),
('1000','pedro');

CREATE TABLE curso(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

insert into curso(nombre) values ('GIT'),('PYTHON'),('MYSQL');

CREATE TABLE nota(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    alumno_id int NOT NULL,
    curso_id int NOT NULL,
    nota DOUBLE,
    FOREIGN KEY (alumno_id) REFERENCES alumno(id),
    FOREIGN KEY (curso_id) REFERENCES curso(id)
);



insert into nota(alumno_id,curso_id,nota)
values (1,1,12),
(1,2,15),
(1,3,18),
(2,1,10),
(2,2,14),
(2,3,16),
(3,1,11),
(3,2,13),
(3,3,17),
(4,1,12),
(4,2,15),
(4,3,18),
(5,1,10),
(5,2,14),
(5,3,16),
(6,1,11),
(6,2,13),
(6,3,17),
(7,1,12),
(7,2,15),
(7,3,18),
(8,1,10),
(8,2,14),
(8,3,16),
(9,1,11),
(9,2,13),
(9,3,17),
(10,1,12),
(10,2,15),
(10,3,18);
