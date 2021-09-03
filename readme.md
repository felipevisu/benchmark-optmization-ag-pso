O código foi escrito na linguagem Python 3.8
O objetive é minimizar três funções conhecidas da literatura:
- chungreynolds
- rosenbrock
- zakharov
As três funções tem seu mínimo absolute igual a zero.

Para executar o experimento:

1) Instalar as dependências do arquivo 'requirements.txt'
    $ pip install -r requirements.txt


2) Execução simples para cada função:
    $ python chungreynolds.py
    $ python rosenbrock.py
    $ python zakharov.py


2) Execução do experimento fatorial para cada função:
    $ python chungreynolds_fatorial.py
    $ python rosenbrock_fatorial.py
    $ python zakharov_fatorial.py


No experimento fatorial o formato de saída consiste em dois arquivos,
um para o algorítimo genético, e outro para a nuvem de partículas.
Cada arquivo contêm 27 resultados com as diferntes combinações de 
parâmetros. Casa combinação foi executada 50 vezes.

O resultado de cada combinação mostra os parâmetros que foram variados,
a média dos resultados da função objetivo, e a porcentagem em que o
algoritmo converge para o limite inferior da função.