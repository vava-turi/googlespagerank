#TAREFA 2
import math
from fractions import Fraction

def soma_ou_subtrai_matriz(p,m1,m2): #p é um parâmeto para dizer à função se soma(p=1) ou subtrai(p=0) os termos de m1 e m2
    m3 = []   #é o resultado de m1 com m2
    for i in range(len(m1)):
        m3.append([0]*len(m1[0]))
        for j in range(len(m1[0])):
            if p == 1: m3[i][j] = m1[i][j] + m2[i][j]
            elif p == 0: m3[i][j] = m1[i][j] - m2[i][j]
    return m3
def gera_matrizes_NxN(k):
    m = []  #faz a matriz de ligação
    ma = []  #matriz auxiliar cacique
    ma_2 = [] #matriz auxiliar indio
    pc = []   #armazena o peso dos caciques
    pi = []   #armazena o peso dos indios
    ni = []  #armazena o número de páginas por grupo
    ni_2 = [] #armazena o número de paginas por grupo para auxiliar no calculo dos indios por cacique
    ni_3 = []
    v = []  #peso ordenado de cada uma das paginas cacique seguida pelos respectivos indios
    Lc = []  #indice das linhas e colunas dos caciques
    Li = [] #linha e coluna de indios
    soma_n = 0  #calcula o numero de páginas para dimensionar a matriz
    for p in range(1, k+1):  #calcula os pesos
        n = p + 1  #número de páginas em cada grupo
        soma_n += n
        ni.append(n)
        for t in range(n):
            ni_3.append(n)
        h = 1
        for r in range(n):
            ni_2.append(h)
            h += 1
        pc.append(1/(n+k-2))  #calcula o peso de cada cacique
        pi.append(1/(n-1))  #calcula o peso de cada indio
    for t in range(k): #compõe o vetor v
        v.append(pc[t]) #add o cacique
        for p in range(ni[t]-1): #add os indios
            v.append(pi[t])
    for i in range(soma_n): #dimensiona as matrizes NxN
        m.append(soma_n*[0])
        ma.append(soma_n*[0])
        ma_2.append(soma_n*[0])
    for h in range(k):  #calcula os indices dos caciques
        lc = (h+1)*(h+2)/2 - 1
        Lc.append(int(lc))
    for i in range(soma_n):  #constroi a matriz auxiliar, que contem apenas cada m[i][j] cacique
        if i in Lc:
            ma[i][i] = v[i]
        else:
            pass
    for d in range(soma_n):  #indice dos indios
        if d in Lc:
            pass
        else:
            Li.append(d)
    for i in range(soma_n):  #constroi a matriz auxiliar, que contem apenas m[i][j] indio
        if i in Li:
            ma_2[i][i] = v[i]
        else:
            pass
    
    for i in range(soma_n):
        for j in range(soma_n):
            if i in Lc and j in Lc:
                m[i][j] = v[j]   #coloca cada cacique nas linhas de caciques
        if i in Lc:
            a = Lc.index(i)
            c = i+a+2
            for r in range (i+1, c):
                m[i][r] = v[r] #coloca cada índio ligado ao caique i em sua respectiva coluna
                b = ni_3[r] - 1
                for n in range(1, b+1):
                    m[i+n][r] = v[r]
        if i in Li:
            for j in range(soma_n):
                l = i - ni_2[i] + 1
                m[i][j] += ma[l][j]
    m = soma_ou_subtrai_matriz(0,m,ma)
    m = soma_ou_subtrai_matriz(0,m, ma_2)
    return m
def identidade_NxN(n):
    I = []
    for i in range(0,n):
        I.append(n*[0])
        for j in range(n):
           if i == j: I[i][j] = 1  #coloca nas diagonais o valor 1
           else: pass
    return I
def gera_Sn(n):
    Sn = []
    for i in range(n):
        Sn.append([0]*n)
        for j in range(n):
            Sn[i][j] = 1/n  #transforma todos os elementos da matriz em 1/n
    return Sn
def somavet(v1, v2):  #função aux para somar os vetores gerados durante o escalonamento
    V = []
    for i in range(len(v1)):
        V += [(v1[i] + v2[i])]
    return V
def multiplica_numreal(alpha, m): #efetua a muliplicação da matriz por alpha
    M = []
    for i in range(len(m)):
        M.append([0]*len(m[0]))
        for j in range(len(m[0])):
            M[i][j] = alpha * m[i][j]
    return M
def multvet(v, x):  #multplica os vetores durante o escalonamento
    V = []
    for i in range(len(v)):
        V += [v[i] * x]
        
    return V
def troca(A, i, j): #efetua as trocas das linhas
    I = []
    J = []
    for index in range(len(A) + 1):
        I += [A[j][index]]
        J += [A[i][index]]
    A[i] = I
    A[j] = J
def escalonamento(A):

    for i in range(len(A) - 1):
        for j in range(i + 1,len(A)):
            n1 = Fraction(A[j][i]) #*************************
            if n1 == 0:  #procura valores zerados na matriz para efetuar as trocas
                for k in range(i,len(A)):
                    if A[k][i] != 0:
                        troca(A, i, k)
                        n1 = A[j][i]
            n2 = Fraction(A[i][i])  #números em cada diagonal *************************************************
            if n2 == float(0):  #se achar algum zero em diagonal, volta o loop
                continue
            div = n1 / n2   #define o número a ser multiplicado
            Aa_i, Aa_j = [], [] #Cria duas lista auxiliares para receber Ai e Aj como fração ***************************************************
            for k in range (len (A[i])):
                Aa_i.append(Fraction(A[i][k]))
            for k in range (len (A[j])):
                Aa_j.append (Fraction(A[j][k]))
            A[j] = (somavet(multvet(Aa_i, -div), Aa_j) ) #faz as contas e modificações do escalonamento
            for k in range (len (A[j])): #transforma o valor em float ***************************
                A[j][k] = float (A[j][k])
    for j in range(len(A[0])):  #zera a última linha da matriz 
            A[len(A)-1][j] = 0
    return A
def solucao_normalizada(m):
    sol = []  #vetor com as soluções não normalizadas
    norm = []  #vetor normalizado para dimensão 1
    sol.append(1) #define o Xn = 1
    soma = []
    for i in range(-2,-len(m)-1, -1): 
        s = 0       #a cada nova linha, a soma dos coeficientes multiplicados por todos os X(i-1) é zerada para não acumular as soluções
        for j in range(-1,-len(m)-1,-1):   #transforma a solução do sistema em uma equação Xi = (soma dos coeficientes de cada linha multiplicados por seu respectivo valor no vetor solução) / coeficiente de Xi que é diagonal de M
            if m[i][j] != 0 and i != j:
                s += math.fabs(m[i][j] * sol[-j-1])
        soma.append(s)   #guarda cada soma em uma lista para efetuar a divisão na linha seguinte
        sol.append(math.fabs(soma[-i-2] / m[i][i]))  #termina o cálculo do Xi
    sol.reverse()   #inverte sol pois Xn está na posição 1 ao invés de n
    t = 0  #somatória das soluções em sol
    for i in range(len(sol)):
        t += sol[i]
    for i in range(len(sol)):  #divide cada sol[i] pelo total para normalizar entre 0 e 1
        norm.append(sol[i] / t)
    return norm
def print_formatado(m): #apenas para printar de maneira formatada
    for i in range(len(m)):
        print(m[i])

def Google_Search_tribo():
    k = int(input("Digite o número de grupos da rede:"))
    soma_n = 0   #número de páginas da rede
    for p in range(1, k+1):
        n = p + 1
        soma_n += n
    a = float(input("Digite o número alpha:"))
    Ml = gera_matrizes_NxN(k)
    I = identidade_NxN(soma_n)
    Sn = gera_Sn(soma_n)
    Ml_mul = multiplica_numreal((1-a), Ml)
    Sn_mul = multiplica_numreal(a, Sn)
    Ml = soma_ou_subtrai_matriz(1,Ml_mul,Sn_mul)
    A = soma_ou_subtrai_matriz(0,Ml,I)
    A_esc = escalonamento(A)
    vet = solucao_normalizada(A_esc)
    vet_classificado = []
    for k in range(len(vet)):  #cria uma cópia do vetor solução para poder classificar sem perder a indexação original
        vet_classificado.append(vet[k])
    vet_classificado.sort(reverse=True)
    print("\n\nConforme dada a Matriz de Ligação da rede, aqui estão as ordens de prioridade das páginas:")
    for i in range(len(vet)):
        print('Posição %d: página %d com peso %1.8f'%(i+1, vet.index(vet_classificado[i])+1, vet_classificado[i]))  #printa cada valor com 8 casas decimais
Google_Search_tribo()
