-- Active: 1734576840998@@127.0.0.1@3306@datag3
-- sentencias DML
-- INSERTAR DATOS(INSERT)
insert into alumno(nro_documento,nombre) values('100','cesar');
-- insert de varios valores(solo en mysql)
insert into alumno(nro_documento,nombre,nota)
VALUES
('200','ana',15),
('300','luis',20),
('400','jose',11),
('500','raul',10),
('600','carmen',13),
('700','jorge',16),
('800','daniel',20),
('900','luisa',17),
('1000','pedro',5);

-- ACTUALIZAR DATOS(UPDATE)
UPDATE alumno set email = 'codigo@gmail.com';
--actualizar con where
UPDATE alumno set email = 'cesar@gmail.com' where id = 1;
-- actualizar con funciones
UPDATE alumno set email = CONCAT(nombre,'@gmail.com') where id != 1;
-- ELIMINAR DATOS(DELETE)
delete from alumno where id > 5;

-- SELECCIONAR(SELECT)
select * from alumno;
select nombre,nota from alumno;
select nombre,nota from alumno where nota > 15;