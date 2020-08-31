#TAREFA 1
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
            q = input('A página %d recebe links da página %d?\nDigite 0 para NÃO e 1 para SIM'%(i+1,j+1))
            if q == '1': m[i][j] = float(1/(l[j]));
            else: m[i][j] = 0
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

def soma_ou_subtrai_matriz(p,m1,m2): #p é um parâmeto para dizer à função se soma(p=1) ou subtrai(p=0) os termos de m1 e m2
    m3 = []   #é o resultado de m1 com m2
    for i in range(len(m1)):
        m3.append([0]*len(m1[0]))
        for j in range(len(m1[0])):
            if p == 1: m3[i][j] = m1[i][j] + m2[i][j]
            elif p == 0: m3[i][j] = m1[i][j] - m2[i][j]
    return m3

def somavet(v1, v2):  #função aux para somar os vetores gerados durante o escalonamento
    V = []
    for i in range(len(v1)):
        V += [v1[i] + v2[i]]
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

def print_formatado(m): #apenas para printar de maneira formatada
    for i in range(len(m)):
        print(m[i])

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
            n1 = A[j][i]
            if n1 == 0:  #procura valores zerados na matriz para efetuar as trocas
                for k in range(i,len(A)):
                    if A[k][i] != 0:
                        troca(A, i, k)
                        n1 = A[j][i]
            n2 = A[i][i]  #números em cada diagonal
            if n2 == float(0):  #se achar algum zero em diagonal, volta o loop
                continue
            div = n1 / n2   #define o número a ser multiplicado
            A[j] = somavet(multvet(A[i], -div), A[j])  #faz as contas e modificações do escalonamento
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
            if m[i][j] != 0 and i != j: s += math.fabs(m[i][j] * sol[-j-1])
        soma.append(s)   #guarda cada soma em uma lista para efetuar a divisão na linha seguinte
        sol.append(math.fabs(soma[-i-2] / m[i][i]))  #termina o cálculo do Xi
    sol.reverse()   #inverte sol pois Xn está na posição 1 ao invés de n
    t = 0  #somatória das soluções em sol
    for i in range(len(sol)):
        t += sol[i]
    for i in range(len(sol)):  #divide cada sol[i] pelo total para normalizar entre 0 e 1
        norm.append(sol[i] / t)
    return norm    

def Google_busca():
    n_pag = int(input('Digite o número de páginas da rede:'))
    a = float(input('Digite alpha:'))
    #constrói a matriz de ligação
    Ml = gera_matrizes_NxN(n_pag)
    #constrói a matriz identidade
    I = identidade_NxN(n_pag)
    #constrói Sn com todos os elementos iguais a 1/n
    Sn = gera_Sn(n_pag)
    #modificamos Ml fazendo primeiro as multiplicações por alpha e depois somamos os termos
    Ml_mul = multiplica_numreal((1-a), Ml)
    Sn_mul = multiplica_numreal(a,Sn)
    Ml = soma_ou_subtrai_matriz(1,Ml_mul,Sn_mul)
    #define A = Ml - I
    A = soma_ou_subtrai_matriz(0,Ml,I)
    A_esc = escalonamento(A)
    vet = solucao_normalizada(A_esc)
    vet_classificado = []
    for k in range(len(vet)):  #cria uma cópia do vetor solução para poder classificar sem perder a indexação original
        vet_classificado.append(vet[k])
    vet_classificado.sort(reverse=True)
    print("\n\nConforme dada a Matriz de Ligação da rede, aqui estão as ordens de prioridade das páginas:")
    for i in range(len(vet)):
        print('Posição %d: página %d com peso %1.4f'%(i+1, vet.index(vet_classificado[i])+1, vet_classificado[i]))  #printa cada valor com 4 casas decimais
Google_busca()