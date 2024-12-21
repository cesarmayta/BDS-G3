-- funciones de agrupación
-- 1. contar
select count(*) from empleado;
select count(*) from empleado where salario > 5000;

-- maximo y minimo
select max(salario),min(salario),avg(salario) from empleado;

select DISTINCT pais from empleado;

select pais,count(*) from empleado
group by pais
order by count(*) desc;
-- crear una consulta que retorne el salario maximo,minimo y promedio por pais
select pais,area,max(salario),min(salario),avg(salario) from empleado
where salario > 5000
group by pais,area;

select pais,avg(salario) from empleado
group by pais
having avg(salario) > 4000;

-- subconsultas
select avg(salario) from empleado;
select * from empleado
where salario > (select avg(salario) from empleado);

select pais,count(*),(select avg(salario) from empleado) as salario_promedio from empleado
where salario > (select avg(salario) from empleado)
group by pais order by count(*) desc;
