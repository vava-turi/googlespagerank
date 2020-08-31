#TAREFA 1 Iterativo
import math

def gera_matrizes_NxN(n):
    m = []  #faz a matriz de ligação
    l =[]  #guarda o número de links que saem de cada página
    for g in range(n):
        l.append(0)
        l[g] = int(input('Digite o número de arestas/links que saem da página/vértice %d:'%(g+1)))
    for i in range(n):
        m.append(n*[0]) 
        for j in range(n):
            if i != j:
                q = input('A página %d recebe links da página %d?\nDigite 0 para NÃO e 1 para SIM'%(i+1,j+1))
                if q == '1': m[i][j] = float(1/(l[j]));
                else: m[i][j] = 0
    return m

def gera_Sn(n):
    Sn = []
    for i in range(n):
        Sn.append([0]*n)
        for j in range(n):
            Sn[i][j] = 1/n  #transforma todos os elementos da matriz em 1/n
    return Sn

def Max_V(L):
    maxi = 0
    for k in range (len (L)):
        if L[k] > maxi:
            maxi = L[k]
    return maxi

def multiplica_numreal(alpha, m): #efetua a muliplicação da matriz por alpha
    M = []
    for i in range(len(m)):
        M.append([0]*len(m[0]))
        for j in range(len(m[0])):
            M[i][j] = alpha * m[i][j]
    return M

def gera_s(n):
    s = []
    for i in range(n):
        s.append(1/n)
    return s

def gera_Y (V) : # Cria o vetor Y 1/n
    Y = []
    for k in range (V):
        Y.append(1/V)
    return Y

def calculo_c(M):  #calcula o valor da constante para estimar o erro
    m = []
    for i in range(len(M)):
         m.append(math.fabs(1-2*(min(M[i]))))
    c = max(m)
    return c

def multvet(v, x):  #multplica os vetores durante o escalonamento
    V = []
    for i in range(len(v)):
        V += [v[i] * x]
    return V

def somavet(v1, v2):  #função aux para somar os vetores gerados durante o escalonamento
    V = []
    for i in range(len(v1)):
        V += [v1[i] + v2[i]]
    return V

def soma_ou_subtrai_matriz(p,m1,m2): #p é um parâmeto para dizer à função se soma(p=1) ou subtrai(p=0) os termos de m1 e m2
    m3 = []   #é o resultado de m1 com m2
    for i in range(len(m1)):
        m3.append([0]*len(m1[0]))
        for j in range(len(m1[0])):
            if p == 1: m3[i][j] = m1[i][j] + m2[i][j]
            elif p == 0: m3[i][j] = m1[i][j] - m2[i][j]
    return m3

def gera_vetores(M): #Constrói os vetores V, L, C
    V,L,C = [], [], []
    for k in range (len(M)):
        for l in range (len(M[k])):
            if M[k][l] !=0:
                    V.append(M[k][l]) #Adiciona os elementos não nulos ao vetor V
                    L.append(k) #Adiciona a linha correspondete a cada elemento não nulo
                    C.append(l) #Adiciona a coluna correspondete a cada elemento não nulo
    return V, L, C

def cálculo (V, L, C, Y, maxi, c):
    z = []
    z_clas = []
    for i in range (maxi + 1):
        z.append(0) #Define os elementos do vetor z de comprimento N como 0
    e_1 = 1      #define como 1 apenas para iniciar a variavel e entrar no loop
    t = 0       #total para normalizar
    while e_1 >= 0.00001:  #realiza o cálculo enquanto o erro for menor que 10^-5
        for k in range (len(z)):
            for x in range (len (V)): #Realiza o cálculo de z no range de m = (len(V))
                z[(L[x])] += V[x]*Y[C[x]]  #faz as multiplicações sucessivas
        #normalização
        for i in range(len(z)):
            t += z[i]
        for i in range(len(z)):
            z[i] = (z[i]/t) 
        #calculo do erro
        for k in range(len(z)-1):
            e = (math.fabs(z[k+1] - z[k])*(c/(1-c)))  #recalcula a estimativa do erro
            e_1 = e                
    for n in range(len(z)):
        z_clas.append(z[n])
    z_clas.sort(reverse=True)
    for i in range(len(z)):   
        p = z.index(z_clas[i])
        print('Posição %d: Página: %d - Valor: %f'%(i+1, p+1, z_clas[i]))

def calc_it():
    n_pag = int(input('Digite o número de páginas da rede:'))
    a = float(input("Digite alpha:"))
    W = gera_matrizes_NxN(n_pag)  #gera a matriz de ligação
    V, L, C = gera_vetores(W) #extrai as entradas nao nulas
    W_mod = multiplica_numreal((1-a), W) #modificação da matriz para calculo da constante c
    Sn = gera_Sn(n_pag)
    W_mod = soma_ou_subtrai_matriz(1, W_mod, multiplica_numreal(a, Sn))
    c = calculo_c(W_mod)
    nao_nulas = len(V)
    s = gera_s(nao_nulas)
    Y = gera_Y (nao_nulas)
    maxi = Max_V(L)
    V = multvet(V, (1-a)) #altera o vetor para corresponder à matriz W modificada
    V = somavet(V, multvet(s, a)) #soma com s
    cálculo (V, L, C, Y, maxi, c)  #realiza o calculo iterativo
calc_it()
