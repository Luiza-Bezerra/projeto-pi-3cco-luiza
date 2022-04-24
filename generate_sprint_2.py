import time
import mysql.connector
import memory_profiler as mp
import random

REGIAO = [
    'S',
    'N',
    'SE',
    'NE',
    'CO',
]

def geracao(entradas):
    inicio = time.time()
    data_list = []

    for i in range(1, entradas):
        idade = random.randint(17,64)
        genero =  bool(random.getrandbits(1))
        idade_descoberta = random.randint(17,idade)

        fim = time.time()
        memoria = round(mp.memory_usage()[0],2)

        data_list.append({
            'idade': idade, 
            'genero': genero, 
            'regiao': random.choice(REGIAO), 
            'idade_descoberta': idade_descoberta,
            'tempo': (fim - inicio), 
            'memoria': memoria
        })

    return data_list

def get_conn():
    return mysql.connector.connect(
            host='localhost', 
            database='algas', 
            user='root', 
            password='temp123', 
            port='3306'
        )

def salvar(lista_dados):
    try:
        connection = get_conn()
        
        idade = lista_dados.get('idade',None)
        genero =lista_dados.get('genero',None)
        regiao = lista_dados.get('regiao',None)
        idade_descoberta = lista_dados.get('idade_descoberta',None)
        tempo = lista_dados.get('tempo',None)
        memoria = lista_dados.get('memoria',None)
        
        query = f'''
            INSERT INTO dados 
                (idade, genero, tempo, regiao,idade_descoberta,memoria) 
            VALUES 
                ({idade},{genero},{regiao},{idade_descoberta},{tempo},{memoria})
        '''
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(f'Dados salvos: {lista_dados}\n')

    except mysql.connector.Error as error:
        print(error)

if __name__ == "__main__":
    for i in range(5,20,1):
        data_list = geracao(i*3)
        for data in data_list:
            salvar(data)