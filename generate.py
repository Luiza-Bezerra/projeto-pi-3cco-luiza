import time
import sys
import mysql.connector

#%load_ext memory_profiler

def geracao(entradas):
    inicio = time.time()
    acumulador = 0
    for iteracao in range(1, entradas+1):
        acumulador += 1

    fim = time.time()
    memoria = 0 # %memit -o
    return {'iterador': iteracao, 'acumulador': acumulador, 'tempo': (fim - inicio), 'memoria':str(memoria).split()[2]}

def salvar(lista_dados):
    try:
        connection = mysql.connector.connect(host='localhost', database='algas', user='root', password='12345')
        
        iterador = lista_dados.get('iterador',None)
        acumulador = lista_dados.get('acumulador',None)
        tempo = lista_dados.get('tempo',None)
        memoria = lista_dados.get('memoria',None)
        
        query = f'INSERT INTO dados (iterador,acumulador,tempo,memoria) VALUES({iterador},{acumulador},{tempo},{memoria})'
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    except mysql.connector.Error as error:
        print(error)

    finally:
        cursor.close()

if __name__ == "__main__":
    for i in range(2100):
        salvar(geracao(i**3))
        
    #salvar(geracao(13**3))

