from algoritmos.ag import AG
from algoritmos.pso import PSO

def chungreynolds(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total**2


if __name__ == "__main__":
    ag = AG(500, 50, 2, 0.1, 1, chungreynolds, -100, 100)
    ag_resultado, m, x = ag.executa()

    pso = PSO(0.5, 1, 2, 2, 50, 500, chungreynolds, -100, 100)
    pso_resultado, n, y = pso.executa()