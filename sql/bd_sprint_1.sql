CREATE DATABASE algas_1;
USE algas_1;

CREATE TABLE  dados (
    _id_ int  primary key auto_increment,
    iterador    bigint ,            
    acumulador  int,      
    tempo       decimal(11,9),                  
    memoria     decimal(10,5)
);