CREATE DATABASE IF NOT EXISTS  algas;
use algas;

CREATE TABLE IF NOT EXISTS dados (
_id_ int  primary key auto_increment,
iterador    bigint ,            
acumulador  int,      
tempo       decimal(11,9),                  
memoria     decimal(10,5)
);