-- CREATE DATABASE   autism_data  ;
-- USE   autism_data  ; 
-- user: urubu100
-- senha: Urubu1@@
-- bd: teste1000

CREATE TABLE    paciente   (
    _id_  int  primary key identity, 
    id_paciente int,
    idade_atual int,
    idade_descoberta int,
    genero bit,
    grau  varchar(10),
    sensibilidade_sentidos bit,
    agressivo bit,
    hiperativo bit,
    movimentos_repetitivos bit,
    baixa_concentracao bit,
    hiperfoco bit,
    necessidade_rotina bit,
    dificuldade_imaginacao bit,
    introvertido bit,
    tipo_autismo varchar(50),
    tipo_autismo_descricao varchar(max),
);


CREATE TABLE   localidade   (
    _id_   int  primary key identity,
    id_regiao_paciente   int ,
    pais   varchar(20),
    PIB_nacional  bigint,
    regiao    varchar(20),
    PIB_percent_BR   bigint,
    PIB_regional   bigint,
    populacao_regiao   bigint,
    densidade_demografica_regiao  decimal(12,2) ,
    area_regiao   bigint,
    regiao_geoeconomica  bigint,
    gentilico_regiao   varchar(20),
    raca_predominante_regiao  varchar(20),
);


CREATE TABLE   renda   (
    _id_   int  primary key identity,
	id_renda_paciente   int ,
    classe  varchar(20),
    classe_descricao  varchar(40),
    quantidade_familia  int,
    total_salario   decimal(12,2),
    empregado  bit,
    per_capita  decimal(12,2)
);