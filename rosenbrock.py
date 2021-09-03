from algoritmos.ag import AG
from algoritmos.pso import PSO

def rosenbrock(x):
    fit = 0

    for i in range(len(x) - 1):
        term1 = x[i + 1] - x[i]**2
        term2 = 1 - x[i]
        fit = fit + 100 * term1**2 + term2**2

    return fit


if __name__ == "__main__":
    ag = AG(500, 50, 2, 0.4, 1, rosenbrock, -5, 10)
    ag_resultado, m, x = ag.executa()

    pso = PSO(0.5, 1, 2, 2, 50, 500, rosenbrock, -5, 10)
    pso_resultado, n, y = pso.executa()