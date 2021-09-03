from algoritmos.ag import AG
from algoritmos.pso import PSO

def zakharov(x):
    total=0
    for i in range(len(x)):
        part1 = x[i]**2
        part2 = 0.5*i*x[i]

    return part1 + part2**2 + part2**4


if __name__ == "__main__":
    ag = AG(500, 50, 2, 0.1, 0.8, zakharov, -5, 10)
    ag_resultado, m, x = ag.executa()

    pso = PSO(0.25, 1, 2, 2, 100, 500, zakharov, -5, 10)
    pso_resultado, n, y = pso.executa()