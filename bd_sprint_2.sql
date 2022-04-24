CREATE DATABASE algas;
USE algas;

CREATE TABLE  dados (
    _id_ int  primary key auto_increment,
    idade int ,            
    genero  boolean,      
    regiao  varchar(2), 
    idade_descoberta int    
    acumulador  int,      
    tempo decimal(12,9),                  
    memoria decimal(12,5)
);