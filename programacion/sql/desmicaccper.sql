create table desmicaccper
(
    accion varchar(255) not null,
    perfil varchar(255) not null,
    CONSTRAINT FK_desmicacc FOREIGN KEY (accion)
    REFERENCES desmicacciones(accion),
    CONSTRAINT FK_desmicper FOREIGN KEY (perfil)
    REFERENCES desmicperfiles(perfil)
);

INSERT INTO desmic.desmicaccper (accion, perfil) VALUES ('Desplegar microservicios en infraestructura de Docker', 'Servicios');
INSERT INTO desmic.desmicaccper (accion, perfil) VALUES ('Establecer parametros del contenedor de Docker', 'Admin');
INSERT INTO desmic.desmicaccper (accion, perfil) VALUES ('Abastecer de Alta Disponibilidad', 'Admin');
INSERT INTO desmic.desmicaccper (accion, perfil) VALUES ('Desplegar microservicios en infraestructura de Docker', 'Admin');
INSERT INTO desmic.desmicaccper (accion, perfil) VALUES ('Desplegar microservicios en infraestructura de Docker', 'Redes');
INSERT INTO desmic.desmicaccper (accion, perfil) VALUES ('Establecer parametros del contenedor de Docker', 'Redes');
INSERT INTO desmic.desmicaccper (accion, perfil) VALUES ('Desplegar microservicios en infraestructura de Docker', 'Escalabilidad');
INSERT INTO desmic.desmicaccper (accion, perfil) VALUES ('Abastecer de Alta Disponibilidad', 'Escalabilidad');
