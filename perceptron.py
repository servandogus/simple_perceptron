# -*- coding: utf-8 -*-

def error(S,w):
    ''' renvoie l'erreur quadratique commis par le perceptron,
    avec le vecteur de pondération w,
    l'échantillon S. 
    '''
    err = 0
    for i in range(len(S)):
        err += 0.5 * (S[i][1] - output_perceptron(S[i][0],w))**2
    return err

def errorDerivative(S,w,j):
    ''' renvoie la derivee de l'erreur par rapport à la pondération n°j.
    '''
    derivative = 0
    for i in range(len(S)):
        derivative += (S[i][1] - output_perceptron(S[i][0],w)) * (-int(S[i][0][j]))
    return derivative
    
def output_perceptron(s,w):
    ''' renvoie le resultat du percetron (1 ou 0),
    avec les ponderations du vecteur w,
    et le vecteur x en input (string).
    '''
    res = 0
    for i in range(len(s)):
        res += int(s[i])*int(w[i])
    return ( res > 0 )
    
#Algorithme d'apprentissage par erreur :
def learn_linear(S,w,eps):
    while(error(S,w)) :
        for i in S:
            err = i[1] - output_perceptron(i[0],w)
            for j in range(8):
                w[j] = w[j] + err * int(i[0][j]) * eps
    return w

#Algorithme d'apprentissage par minimisation de l'erreur quadratique :
#Méthode du gradient :
def learn_errorMinimisationGradientMethod(S,w,eps,iteration):
    while (iteration > 0):
        derivative = []    
        for j in range(8):
            derivative.append(errorDerivative(S,w,j))
        for j in range(8):
            w[j] = w[j] - derivative[j] * eps
        iteration -= 1
    return w
            
    
#
S=[("1111110",0),("0110000",1),("1101101",0),("1111001",1),("0110011",0),("1011011",1),("0011111",0),("1110000",1),("1111111",0),("1111011",1)]

for i in range( len(S) ):
    S[i] = ("1"+ S[i][0] , S[i][1])
    
w=[]
for i in range(8):
    w.append(1)