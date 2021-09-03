from random import uniform, randint, random, choice

ALPHA = 0.5
BETA = 0.25

class Individuo:
    def __init__(self, num_genes, limite_inf, limite_sup, cromossomo=[], geracao=0, inicia=False):
        self.avaliacao = None
        self.num_genes = num_genes
        self.geracao = geracao
        self.cromossomo = cromossomo
        self.limite_inf = limite_inf
        self.limite_sup = limite_sup

        # Gera o cromossomo do indivíduo com um valor aleatório no intervalo {'limite_inf', 'limite_sup'}
        if inicia:
            cromossomo = []
            for i in range(num_genes):
                cromossomo.append(uniform(limite_inf, limite_sup))
            self.cromossomo = cromossomo

    # Algortítmo de cruzamento BLX-alpha
    def cruzamento(self, outro):
        pai1 = self.cromossomo
        pai2 = outro.cromossomo

        tamanho = len(pai1)
        f1, f2 = [0]*tamanho, [0]*tamanho
        d = [0]*tamanho

        # Cria os novos cromossomos
        for i in range(tamanho):
            d[i] = abs(pai1[i] - pai2[i])

            if pai1[i] <= pai2[i]:
                f1[i] = uniform(pai1[i] - ALPHA * d[i], pai2[i] + BETA * d[i])
                f2[i] = uniform(pai1[i] - ALPHA * d[i], pai2[i] + BETA * d[i])
            else:
                f1[i] = uniform(pai2[i] - BETA * d[i], pai1[i] + ALPHA * d[i])
                f2[i] = uniform(pai2[i] - BETA * d[i], pai1[i] + ALPHA * d[i])

        # Retorna dois novos indivíduos
        return [
            Individuo(
                cromossomo=f1,
                num_genes=self.num_genes,
                geracao=self.geracao + 1,
                limite_inf=self.limite_inf,
                limite_sup=self.limite_sup
            ),
            Individuo(
                cromossomo=f2,
                num_genes=self.num_genes,
                geracao=self.geracao + 1,
                limite_inf=self.limite_inf,
                limite_sup=self.limite_sup
            )
        ]

    # Algorimo de mutação "creep"
    # Varia os valores do cromossomo no intervalo {0.95, 1.05}
    def mutacao(self, taxa_mutacao):
        if random() <= taxa_mutacao:
            for i in range(len(self.cromossomo)):
                self.cromossomo[i] = self.cromossomo[i] * uniform(0.95, 1.05)
        elif random() <= 0.05:
            for i in range(len(self.cromossomo)):
                self.cromossomo[i] = choice([self.limite_inf, self.limite_sup])

class Populacao:
    def __init__(self, num_individuos, num_genes, geracao, limite_inf, limite_sup, inicia=False):
        self.num_individuos = num_individuos
        self.num_genes = num_genes  # Tamanho do cromossomo
        self.geracao = geracao
        self.individuos = []
        self.limite_inf = limite_inf
        self.limite_sup = limite_sup

        # Gera a população inicial
        if inicia:
            individuos = []
            for i in range(num_individuos):
                individuo = Individuo(
                    num_genes=self.num_genes, limite_inf=self.limite_inf, limite_sup=self.limite_sup, inicia=True)
                individuos.append(individuo)
            self.individuos = individuos

    # Função fitness
    def avalia_individuos(self, funcao):
        for individuo in self.individuos:
            individuo.avaliacao = funcao(individuo.cromossomo)

    # Ordena do melhor para o pior
    def ordena(self):
        self.individuos = sorted(self.individuos, key=lambda individuo: individuo.avaliacao)

    # Seleciona um pai para o cruzamento
    # A função se torna recursiva até que os pais sejam individuos diferentes
    def torneio(self):
        indice_1 = randint(0, self.num_individuos - 2)
        indice_2 = randint(0, self.num_individuos - 2)
        indice_3 = randint(0, self.num_individuos - 2)

        if indice_1 != indice_2 and indice_1 != indice_3 and indice_2 != indice_3:
            novos = [self.individuos[indice_1], self.individuos[indice_2], self.individuos[indice_3]]
            novos = sorted(novos, key=lambda individuo: individuo.avaliacao)
            return novos[0]

        return self.torneio()


class AG:
    def __init__(
            self, num_geracoes, num_individuos, num_genes, taxa_mutacao, taxa_elitismo, funcao,
            limite_inf, limite_sup):
        self.melhores = []
        self.num_geracoes = num_geracoes
        self.num_individuos = num_individuos
        self.num_genes = num_genes
        self.taxa_mutacao = taxa_mutacao
        self.taxa_elitismo = taxa_elitismo
        self.funcao = funcao
        self.num_genes = num_genes
        self.limite_inf = limite_inf
        self.limite_sup = limite_sup
        self.populacao = Populacao(
            num_individuos=self.num_individuos, num_genes=self.num_genes, geracao=0,
            limite_inf=limite_inf, limite_sup=limite_sup, inicia=True)

    # Gera uma nova população fazendo os cruzamentos, mutação e elitismo
    def gera_nova_populacao(self):
        individuos = []
        x = int(self.num_individuos/2)

        for i in range(x):
            pai_1 = self.populacao.torneio()
            pai_2 = self.populacao.torneio()

            while pai_1 == pai_2:
                pai_2 = self.populacao.torneio()

            filho_1, filho_2 = pai_1.cruzamento(pai_2)

            filho_1.mutacao(self.taxa_mutacao)
            filho_2.mutacao(self.taxa_mutacao)

            filho_1.avaliacao = self.funcao(filho_1.cromossomo)
            filho_2.avaliacao = self.funcao(filho_2.cromossomo)

            # Pais e filhos são ordenados para facilitar o elitismo
            novos = [pai_1, pai_2, filho_1, filho_2]
            novos = sorted(novos, key=lambda individuo: individuo.avaliacao)

            # Parte elitista da função
            if(random() <= self.taxa_elitismo):
                individuos = individuos + novos[:2]
            else:
                individuos = individuos + [filho_1, filho_2]

        self.populacao.individuos = individuos
        self.populacao.geracao += 1

    def atualiza_melhores(self):
        self.melhores.append(self.populacao.individuos[0].avaliacao)

    def executa(self, resultado=True):
        # Avalia e ordena a primeira população
        self.populacao.avalia_individuos(self.funcao)
        self.populacao.ordena()

        for i in range(self.num_geracoes):
            self.gera_nova_populacao()
            self.populacao.ordena()
            self.atualiza_melhores()

        (m, x) = min((v,i) for i,v in enumerate(self.melhores))

        if resultado:
            print('------------------------------------------')
            print("Algoritmo Genético")
            print("Melhor resultado:", m)
            print("Geração:", x)
            
        return self.melhores, m, x