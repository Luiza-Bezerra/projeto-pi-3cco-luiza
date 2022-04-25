CREATE DATABASE algas_2;
USE algas_2;

CREATE TABLE  dados (
    _id_ int  primary key auto_increment,
    idade int ,            
    genero varchar(10),      
    regiao varchar(20), 
    descoberta int,
    tempo decimal(12,9),                  
    memoria decimal(12,5)
);