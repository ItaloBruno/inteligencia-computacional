class Estado():
    def __init__(self, canibalEsq, missionarioEsq, barco, canibalDir, missionarioDir):
        self.canibalEsq = canibalEsq
        self.missionarioEsq = missionarioEsq
        self.barco = barco
        self.canibalDir = canibalDir
        self.missionarioDir = missionarioDir
        self.log = ""
        self.solucoes = None

    def fim(self):
        if self.canibalEsq == 0 and self.missionarioEsq == 0:
            return True
        return False

    def estado_e_valido(self):
        if self.missionarioEsq >= 0 and self.missionarioDir >= 0 \
           and self.canibalEsq >= 0 and self.canibalDir >= 0 \
           and (self.missionarioEsq == 0 or self.missionarioEsq >= self.canibalEsq) \
           and (self.missionarioDir == 0 or self.missionarioDir >= self.canibalDir):
            return True
        return False

    def __eq__(self, novo):
        return self.canibalEsq == novo.canibalEsq and self.missionarioEsq == novo.missionarioEsq \
                   and self.barco == novo.barco and self.canibalDir == novo.canibalDir \
                   and self.missionarioDir == novo.missionarioDir

    def __hash__(self):
        return hash((self.canibalEsq, self.missionarioEsq, self.barco, self.canibalDir, self.missionarioDir))

def buscar_solucao(estado_atual):
    solucoes = []
    if estado_atual.barco == 'esquerda':
        solucoes_esquerda(estado_atual, solucoes)
    else:
        solucoes_direita(estado_atual,solucoes)
    return solucoes

def solucoes_esquerda(estado_atual, solucoes):
    novo_estado = Estado(estado_atual.canibalEsq, estado_atual.missionarioEsq - 2, 'direita ',
                                estado_atual.canibalDir, estado_atual.missionarioDir + 2)
    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Dois missionarios da esquerda para a direita."
        solucoes.append(novo_estado)
    novo_estado = Estado(estado_atual.canibalEsq - 2, estado_atual.missionarioEsq, 'direita ',
                                estado_atual.canibalDir + 2, estado_atual.missionarioDir)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Dois canibais da esquerda para a direita."
        solucoes.append(novo_estado)
    novo_estado = Estado(estado_atual.canibalEsq - 1, estado_atual.missionarioEsq - 1, 'direita ',
                                estado_atual.canibalDir + 1, estado_atual.missionarioDir + 1)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Um missionario e um canibal da esquerda para a direita."
        solucoes.append(novo_estado)
    novo_estado = Estado(estado_atual.canibalEsq, estado_atual.missionarioEsq - 1, 'direita ',
                                estado_atual.canibalDir, estado_atual.missionarioDir + 1)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Um missionario da esquerda para a direita."
        solucoes.append(novo_estado)
    novo_estado = Estado(estado_atual.canibalEsq - 1, estado_atual.missionarioEsq, 'direita ',
                                estado_atual.canibalDir + 1, estado_atual.missionarioDir)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Um canibal da esquerda para a direita."
        solucoes.append(novo_estado)

def solucoes_direita(estado_atual,solucoes):
    novo_estado = Estado(estado_atual.canibalEsq, estado_atual.missionarioEsq + 2, 'esquerda',
                                estado_atual.canibalDir, estado_atual.missionarioDir - 2)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Um canibal da direita  para a esquerda."
        solucoes.append(novo_estado)
    novo_estado = Estado(estado_atual.canibalEsq + 2, estado_atual.missionarioEsq, 'esquerda',
                                estado_atual.canibalDir - 2, estado_atual.missionarioDir)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Dois canibais da direita  para a esquerda."
        solucoes.append(novo_estado)
    novo_estado = Estado(estado_atual.canibalEsq + 1, estado_atual.missionarioEsq + 1, 'esquerda',
                                estado_atual.canibalDir - 1, estado_atual.missionarioDir - 1)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Um missionario e um canibal da direita  para a esquerda."
        solucoes.append(novo_estado)
    novo_estado = Estado(estado_atual.canibalEsq, estado_atual.missionarioEsq + 1, 'esquerda',
                                estado_atual.canibalDir, estado_atual.missionarioDir - 1)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Um missionario da direita  para a esquerda."
        solucoes.append(novo_estado)
    novo_estado = Estado(estado_atual.canibalEsq + 1, estado_atual.missionarioEsq, 'esquerda',
                                estado_atual.canibalDir - 1, estado_atual.missionarioDir)

    if novo_estado.estado_e_valido():
        novo_estado.solucoes = estado_atual
        novo_estado.log = "Um canibal da direita  para a esquerda."
        solucoes.append(novo_estado)

def busca_em_largura(estado = Estado(3,3,'esquerda',0,0)):
    estado.log = "Estado Inicial."
    estado_inicial = estado
    if estado_inicial.fim():
        return estado_inicial
    borda = list()
    analisado = set()
    borda.append(estado_inicial)
    while borda:
        estado = borda.pop(0)
        if estado.fim():
            return estado
        analisado.add(estado)
        solucoes = buscar_solucao(estado)
        for filho in solucoes:
            if (filho not in analisado) or (filho not in borda):
                borda.append(filho)
    return None

def mostrar_solucao(solucao):
    print("--------------------- Mostrando Solução -------------------------")
    caminho = []
    caminho.append(solucao)
    solucoes = solucao.solucoes
    print("Me,Ce,B,Md,Cb")
    print("M = Missionário C = Canibal e = Margem Esquerda d = Margem Direita",end="")
    print("")
    while solucoes:
        caminho.append(solucoes)
        solucoes = solucoes.solucoes
    for t in range(len(caminho)):
        estado = caminho[len(caminho) - t - 1]
        print("(" + str(estado.canibalEsq) + ","
                  + str(estado.missionarioEsq) + ","
                  + estado.barco + "," + str(estado.canibalDir) + ","
                  + str(estado.missionarioDir) + ") -> " + estado.log)

def principal():
    solucao = busca_em_largura()
    mostrar_solucao(solucao)
principal()