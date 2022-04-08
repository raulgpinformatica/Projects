create table desmicacciones
(
    accion varchar(191) not null,
    constraint desmicperfiles_accion_uindex
	unique (accion),
    CONSTRAINT PK_desmicacciones PRIMARY KEY (accion)
);


INSERT INTO desmic.desmicacciones (accion) VALUES ('Abastecer de Alta Disponibilidad');
INSERT INTO desmic.desmicacciones (accion) VALUES ('Desplegar microservicios en infraestructura de Docker');
INSERT INTO desmic.desmicacciones (accion) VALUES ('Establecer parametros del contenedor de Docker');
