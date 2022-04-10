import time
import sys
import mysql.connector
import memory_profiler as mp

#%load_ext memory_profiler

def geracao(entradas):
    inicio = time.time()
    acumulador = 0
    data_list = []
    for iteracao in range(1, entradas):
        acumulador += 1
        fim = time.time()
        memoria = round(mp.memory_usage()[0],2)
        data_list.append({
            'iterador': iteracao, 
            'acumulador': acumulador, 
            'tempo': (fim - inicio), 
            'memoria': memoria})

    return data_list

def salvar(lista_dados):
    try:
        connection = mysql.connector.connect(
            host='localhost', 
            database='algas', 
            user='root', 
            password='temp123', 
            port='3306'
        )
        
        iterador = lista_dados.get('iterador',None)
        acumulador = lista_dados.get('acumulador',None)
        tempo = lista_dados.get('tempo',None)
        memoria = lista_dados.get('memoria',None)
        
        query = f'INSERT INTO dados (iterador,acumulador,tempo,memoria) VALUES({iterador},{acumulador},{tempo},{memoria})'
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(f'Dado salvos: {lista_dados}')

    except mysql.connector.Error as error:
        print(error)

if __name__ == "__main__":
    for i in range(5,20,1):
        data_list = geracao(i*3)
        for data in data_list:
            salvar(data)