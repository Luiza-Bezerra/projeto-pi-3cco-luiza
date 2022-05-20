
from ast import Return
import mysql.connector

COLUNAS = [
    'idade', 
    'genero', 
    'regiao', 
    'descoberta', 
    'tempo',
    'memoria'
]

def get_conn():
    return mysql.connector.connect(
            host='localhost', 
            database='algas_2', 
            user='root', 
            password='temp123', 
            port='3306'
        )


def salvar(lista_dados):
    try:
        connection = get_conn()

        idade_atual = int(lista_dados.get('idade_atual',None))
        genero = str(lista_dados.get('genero',None))
        regiao = str(lista_dados.get('regiao',None))
        idade_descoberta = int(lista_dados.get('idade_descoberta',None))
        tempo = round(float(lista_dados.get('tempo', None)), 9)
        memoria = round(float(lista_dados.get('memoria',None)), 5)


        query = f"INSERT INTO dados(idade, genero, regiao, descoberta, tempo, memoria) VALUES({idade_atual},'{genero}','{regiao}',{idade_descoberta},{tempo},{memoria});"
        print(f'Query:{query}\n')

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(f'Dados salvos: {lista_dados}\n')

    except mysql.connector.Error as error:
        print(error)