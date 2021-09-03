from tqdm import tqdm
from algoritmos.ag import AG
from algoritmos.pso import PSO
from algoritmos.utils import escreve_ag, escreve_pso

def chungreynolds(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total**2


if __name__ == "__main__":
    # Parâmetros do experimento fatorial
    populacao_vet = [100, 250, 500]
    individuos_vet = [10, 25, 50]
    elitismo_vet = [0.333, 0.666, 1]
    w_vet = [0.25, 0.5, 0.75]

    resultados = []

    print("Algortítmo Genético")

    with tqdm(total=1350) as pbar:
        for populacao in populacao_vet:
            for inidividuos in individuos_vet:
                for elitismo in elitismo_vet:
                    media_converge = 0 # Média com que o resultado atinge o limite inferior
                    media_resultado = 0 # Média dos resultados em geral

                    # Cada combinação é executada 50 vezes
                    for i in range(50):
                        ag = AG(populacao, inidividuos, 2, 0.4, elitismo, chungreynolds, -100, 100)
                        ag_resultado, m, x = ag.executa(resultado=False)

                        media_resultado += m
                        if m == 0:
                            media_converge += 1

                        pbar.update(1)

                    resultados.append(
                        {
                            'populacao': populacao,
                            'individuos': inidividuos,
                            'elitismo': elitismo,
                            'media_converge': media_converge*2,
                            'media_resultado': media_resultado/50
                        }
                    )

    escreve_ag('chungreynolds_ag_fatorial.txt', resultados)

    resultados = []

    print("Enxame de abelhas")

    with tqdm(total=1350) as pbar:
        for populacao in populacao_vet:
            for inidividuos in individuos_vet:
                for w in w_vet:
                    media_converge = 0 # Média com que o resultado atinge o limite inferior
                    media_resultado = 0 # Média dos resultados em geral

                    # Cada combinação é executada 50 vezes
                    for i in range(50):
                        pso = PSO(w, 1, 2, 2, inidividuos, populacao, chungreynolds, -100, 100)
                        pso_resultado, n, y = pso.executa(resultado=False)

                        media_resultado += n
                        if n == 0:
                            media_converge += 1

                        pbar.update(1)

                    resultados.append(
                        {
                            'iteracoes': populacao,
                            'particulas': inidividuos,
                            'w': w,
                            'media_converge': media_converge*2,
                            'media_resultado': media_resultado/50
                        }
                    )
    
    escreve_pso('chungreynolds_pso_fatorial.txt', resultados)