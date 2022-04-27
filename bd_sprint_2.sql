CREATE DATABASE algas_2;
USE algas_2;

CREATE TABLE  dados (
    _id_ int  primary key auto_increment, -- identificador
    idade int , -- idade atual da pessoa
    genero varchar(10), -- genero da pessoa
    regiao varchar(20), -- regiao onde a pessoa mora
    descoberta int, -- idade que foi diagnosticada
    tempo decimal(12,9),  
    memoria decimal(12,5)
);