-- A ALUMNO
-- B NOTAS
-- C CURSO

-- LEFT JOIN
select alumno.nombre,nota.nota 
from alumno left join nota on nota.alumno_id = alumno.id;

insert into alumno(nro_documento,nombre) values('1001','Juan Perez');

select alumno.nombre,avg(nota.nota) 
from alumno left join nota on nota.alumno_id = alumno.id
group by alumno.nombre;

-- RIGHT JOIN
insert into curso(nombre) values('Numpy y Pandas');

select curso.nombre,avg(nota.nota)
from nota RIGHT JOIN curso on nota.curso_id = curso.id
GROUP BY curso.nombre;

-- INNER JOIN
select alumno.nombre,curso.nombre,nota.nota
from nota 
inner join alumno on nota.alumno_id = alumno.id
inner join curso on nota.curso_id = curso.id
order by alumno.nombre;
