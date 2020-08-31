import math

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
def gera_Sn(n):
    Sn = []
    for i in range(n):
        Sn.append([0]*n)
        for j in range(n):
            Sn[i][j] = 1/n  #transforma todos os elementos da matriz em 1/n
    return Sn
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
def gera_vetores(M): #Constrói os vetores V, L, C
    V,L,C = [], [], []
    for k in range (len(M)):
        for l in range (len(M[k])):
            if M[k][l] != 0:
                    V.append(M[k][l]) #Adiciona os elementos não nulos ao vetor V
                    L.append(k) #Adiciona a linha correspondete a cada elemento 
                    C.append(l) #Adiciona a coluna correspondete a cada elemento
    return V, L, C
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
def calculo_c(M):  #calcula o valor da constante para estimar o erro
    m = []
    for i in range(len(M)):
         m.append(math.fabs(1-2*(min(M[i]))))
    c = max(m)
    return c
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
    k = int(input('Digite o número de grupos da rede:'))
    n_pag = 0
    for n in range(1, k+1):
        n_pag += n + 1
    a = float(input("Digite alpha:"))
    W = gera_matrizes_NxN(k)  #gera a matriz de ligação
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