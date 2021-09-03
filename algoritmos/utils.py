def escreve_ag(nome, resultados):
    f = open(nome, "w")
    n = 0
    for resultado in resultados:
        f.write("\n---------------------------------------------")
        f.write("\nExecucao: {}".format(n+1))
        f.write("\nPopulacao: {}".format(resultado['populacao']))
        f.write("\nIndividuos: {}".format(resultado['individuos']))
        f.write("\nElitismo: {}".format(resultado['elitismo']))
        f.write("\nMedia converge: {}".format(resultado['media_converge']))
        f.write("\nMedia resultados: {}".format(resultado['media_resultado']))
        n += 1
    f.close()

def escreve_pso(nome, resultados):
    f = open(nome, "w")
    n = 0
    for resultado in resultados:
        f.write("\n---------------------------------------------")
        f.write("\nExecucao: {}".format(n+1))
        f.write("\nIteracoes: {}".format(resultado['iteracoes']))
        f.write("\nParticulas: {}".format(resultado['particulas']))
        f.write("\nw: {}".format(resultado['w']))
        f.write("\nMedia converge: {}".format(resultado['media_converge']))
        f.write("\nMedia resultados: {}".format(resultado['media_resultado']))
        n += 1
    f.close()