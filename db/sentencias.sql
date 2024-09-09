-- SQLite
--Insertar dato en la tabla Casa de cambios
--Seleccionar todos los elementos de la tabla Casa de cambios
--Seleccionar todos los elementos de la tabla Moneda
--Borrar dato de la tabla Casa de cambios
-- INNER JOIN DE MONEDA Y CASA_DE_CAMBIOS EN CASA_DE_CAMBIOS_MONEDA

--INSERT INTO Casa_de_cambios (nombre) VALUES ('MAXICAMBIOS');
select * from Casa_de_cambios;

--INSERT INTO Moneda (nombre, compra, venta, timestamp) VALUES ('Dólar', 20.5, 21.0, '2024-05-02 10:00:00');

select * from Moneda;

--delete from Casa_de_cambios where id = 2 or id = 3 or id = 4;

--verificar si funciona
--Join que trae todos los elementos de la tabla moneda y el nombre de la casa de cambios
--SELECT Moneda.id, Moneda.nombre, Moneda.compra, Moneda.venta, Moneda.timestamp, Casa_de_cambios.nombre  FROM Moneda JOIN Casa_de_cambios ON Moneda.casa_cambio_id = Casa_de_cambios.id;

--INSERT INTO Casa_de_cambios_Moneda (id_casa_de_cambios, id_moneda) VALUES (1, 1);
select * from Casa_de_cambios_Moneda;

--SELECT Moneda.*, Casa_de_cambios.* 
--FROM Moneda 
--INNER JOIN Casa_de_cambios_Moneda ON Moneda.id = Casa_de_cambios_Moneda.id_moneda 
--INNER JOIN Casa_de_cambios ON Casa_de_cambios.id = Casa_de_cambios_Moneda.id_casa_de_cambios;


--ESTRUCTURA DE UN INNER JOIN
--Select t1.*, t2.* 
--FROM t1 
--INNER JOIN tk ON t1.pk = tk.fk1 
--INNER JOIN t2 ON t2.pk = tk.fk2;