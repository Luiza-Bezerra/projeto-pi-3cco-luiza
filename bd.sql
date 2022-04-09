create database algas;
use algas;

create table dados (
_id_ int  primary key auto_increment,
iterador    bigint ,            
acumulador  int,      
tempo       decimal(11,9),                  
memoria     decimal(10,5)
);