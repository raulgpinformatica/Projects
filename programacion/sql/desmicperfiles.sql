create table desmicperfiles
(
    perfil varchar(191) not null,
    constraint desmicperfiles_perfil_uindex
        unique (perfil),
	CONSTRAINT PK_desmicperfiles PRIMARY KEY (perfil)
);

INSERT INTO desmic.desmicperfiles (perfil) VALUES ('Admin');
INSERT INTO desmic.desmicperfiles (perfil) VALUES ('Servicios');
INSERT INTO desmic.desmicperfiles (perfil) VALUES ('Redes');
INSERT INTO desmic.desmicperfiles (perfil) VALUES ('Escalabilidad');
