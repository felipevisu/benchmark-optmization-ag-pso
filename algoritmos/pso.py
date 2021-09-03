from random import random
from random import uniform

class Particula:
    def __init__(self, x):
        self.posicao = []
        self.velocidade = []
        self.melhor_posicao = []
        self.melhor_erro = -1
        self.erro = -1

        for i in range(0, len(x)):
            self.velocidade.append(uniform(-1, 1))
            self.posicao.append(x[i])

    def avaliacao(self, funcao):
        self.erro = funcao(self.posicao)

        if self.erro < self.melhor_erro or self.melhor_erro == -1:
            self.melhor_posicao = self.posicao.copy()
            self.melhor_erro = self.erro

    def atualiza_velocidade(self, melhor_posicao, num_dimensoes, w, c1, c2):
        
        for i in range(0, num_dimensoes):
            r1 = random()
            r2 = random()
            
            vel_cognitive = c1 * r1 * (self.melhor_posicao[i] - self.posicao[i])
            vel_social = c2 * r2 * (melhor_posicao[i] - self.posicao[i])
            self.velocidade[i] = w * self.velocidade[i] + vel_cognitive + vel_social

    def atualiza_posicao(self, limite_inf, limite_sup, num_dimensoes):
        for i in range(0, num_dimensoes):
            self.posicao[i] = self.posicao[i] + self.velocidade[i]
            
            if self.posicao[i] > limite_sup:
                self.posicao[i] = limite_sup

            if self.posicao[i] < limite_inf:
                self.posicao[i] = limite_inf


class PSO:
    def __init__(self, w, c1, c2, num_dimensoes, num_particulas, num_iteracoes, funcao, limite_inf, limite_sup):
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.num_dimensoes = num_dimensoes
        self.num_particulas = num_particulas
        self.num_iteracoes = num_iteracoes
        self.funcao = funcao
        self.limite_inf = limite_inf
        self.limite_sup = limite_sup
        self.x = []
        self.melhores = []

        for i in range(self.num_dimensoes):
            value = uniform(limite_inf, limite_sup)
            self.x.append(value)


    def executa(self, resultado=True):

        melhor_erro = -1 
        melhor_posicao = []

        enxame = []

        for i in range(0, self.num_particulas):
            enxame.append(Particula(self.x))

        i=0
        while i < self.num_iteracoes:

            for j in range(0, self.num_particulas):
                enxame[j].avaliacao(self.funcao)

                if enxame[j].erro < melhor_erro or melhor_erro == -1:
                    melhor_posicao = list(enxame[j].posicao)
                    melhor_erro = float(enxame[j].erro)

            for j in range(0, self.num_particulas):
                enxame[j].atualiza_velocidade(melhor_posicao, self.num_dimensoes, self.w, self.c1, self.c2)
                enxame[j].atualiza_posicao(self.limite_inf, self.limite_sup, self.num_dimensoes)
            i+=1

            self.melhores.append(melhor_erro)

        (m, x) = min((v,i) for i,v in enumerate(self.melhores))

        if resultado:
            print('------------------------------------------')
            print("Enxame de Abelhas")
            print("Melhor resultado:", m)
            print("Geração:", x)

        return self.melhores, m, x