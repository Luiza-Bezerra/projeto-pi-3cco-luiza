{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49fe1990",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "peak memory: 60.83 MiB, increment: -4.06 MiB\n",
      "peak memory: 63.34 MiB, increment: 0.04 MiB\n",
      "peak memory: 63.39 MiB, increment: 0.00 MiB\n",
      "peak memory: 63.41 MiB, increment: 0.00 MiB\n",
      "peak memory: 63.41 MiB, increment: 0.00 MiB\n",
      "peak memory: 63.41 MiB, increment: 0.00 MiB\n",
      "peak memory: 63.41 MiB, increment: 0.00 MiB\n",
      "peak memory: 63.42 MiB, increment: 0.00 MiB\n",
      "peak memory: 63.42 MiB, increment: 0.00 MiB\n",
      "peak memory: 63.42 MiB, increment: 0.00 MiB\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import sys\n",
    "import mysql.connector\n",
    "\n",
    "%load_ext memory_profiler\n",
    "\n",
    "def geracao(entradas):\n",
    "    inicio = time.time()\n",
    "    acumulador = 0\n",
    "    for iteracao in range(1, entradas+1):\n",
    "        acumulador += 1\n",
    "\n",
    "    fim = time.time()\n",
    "    memoria = %memit -o\n",
    "    return {'iterador': iteracao, 'acumulador': acumulador, 'tempo': (fim - inicio),'memoria':str(memoria).split()[2]}\n",
    "\n",
    "def salvar(lista_dados):\n",
    "    try:\n",
    "        connection = mysql.connector.connect(host='localhost', database='algas', user='root', password='12345')\n",
    "        \n",
    "        iterador = lista_dados.get('iterador',None)\n",
    "        acumulador = lista_dados.get('acumulador',None)\n",
    "        tempo = lista_dados.get('tempo',None)\n",
    "        memoria = lista_dados.get('memoria',None)\n",
    "        \n",
    "        query = f'INSERT INTO dados (iterador,acumulador,tempo,memoria) VALUES({iterador},{acumulador},{tempo},{memoria})'\n",
    "        cursor = connection.cursor()\n",
    "        cursor.execute(query)\n",
    "        connection.commit()\n",
    "\n",
    "    except mysql.connector.Error as error:\n",
    "        print(error)\n",
    "\n",
    "    finally:\n",
    "        cursor.close()\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    for i in range(2,1000,3):\n",
    "        salvar(geracao(i**3))\n",
    "        \n",
    "    #salvar(geracao(13**3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4477ca03",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
