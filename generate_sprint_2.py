import time
import mysql.connector
import memory_profiler as mp
import random

def geracao(entradas):
    inicio = time.time()
    data_list = []

    for i in range(1, entradas):
        idade = random.randint(17,64)
        idade_descoberta = random.randint(17,idade)

        fim = time.time()
        memoria = round(mp.memory_usage()[0],2)

        data_list.append({
            'idade': idade, # Idade da pessoa altista
            'genero': random.choice(['M','F']), # F-feminino, M-Masculino
            'regiao': random.choice(['S','N','SE','NE','CO']), # Regiões do Brasil
            'idade_descoberta': idade_descoberta, # Idade que descobriou o altismo
            'tempo': (fim - inicio), # Tempo de execução
            'memoria': memoria # Memória usada na execução
        })

    return data_list

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

        idade = int(lista_dados.get('idade',None))
        genero = str(lista_dados.get('genero',None))
        regiao = str(lista_dados.get('regiao',None))
        descoberta = int(lista_dados.get('idade_descoberta',None))
        tempo = round(float(lista_dados.get('tempo', None)), 9)
        memoria = round(float(lista_dados.get('memoria',None)), 5)


        query = f"INSERT INTO dados(idade, genero, regiao, descoberta, tempo, memoria) VALUES({idade},'{genero}','{regiao}',{descoberta},{tempo},{memoria});"
        print(f'Query:{query}\n')

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(f'Dados salvos: {lista_dados}\n')

    except mysql.connector.Error as error:
        print(error)

if __name__ == "__main__":
    for i in range(5,20,1):
        data_list = geracao(i)
        print(f'Dados gerados:\n{data_list}\n')
        for data in data_list:
            salvar(data)