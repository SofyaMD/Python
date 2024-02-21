# Projet info

from random import *
from math import *
from matplotlib.pyplot import *
from time import sleep

#Abscisse de c

def abscisse(c,p):
    '''prend en argument c=le numéro de la case et p=le nombre de colonne et renvoie l'abscisse de c'''
    return c%p

#Ordonnee de c            

def ordonnee(c,p):
    '''prend en argument c=le numéro de la case et p=le nombre de colonne et renvoie l'ordonnee de c'''
    return c//p

#Voisins de c

def voisins(c,p,n):
    '''prend en argument c=le numéro de la case et p=le nombre de colonne et n=le nombre de ligne et renvoie les voisins de c'''
    L=[]
    if ordonnee(c,p)!=0:
        L.append(c-p)
    if abscisse(c,p)!=0:
        L.append(c-1)
    if abscisse(c,p)!=p-1:
        L.append(c+1)
    if ordonnee(c,p)!=n-1:
        L.append(c+p)
    return L            

#Salle initiale avec 8 personnes max par case

def initialisationSalle(p,n,N):
    '''prend en argument p=nb de col, n=nb de lignes, N=nb d'individu, N max=p*n et renvoie une salle avec 8 ind max par case'''
    S=[[] for i in range(p*n)]
    for k in range(N):
        r=randint(0,p*n-1)
        while len(S[r])==8:
            r=randint(0,p*n-1)
        S[r].append(k)
    return S

def initialisationSalle1(p,n,N,M):
    '''prend en argument p=nb de col, n=nb de lignes, N=nb d'individu, N max=p*n et renvoie une salle avec 8 ind max par case'''
    S=[[] for i in range(p*n)]
    for k in range(N):
        r=randint(0,p*n-1)
        while len(S[r])==8:
            r=randint(0,p*n-1)
        S[r].append(k<M)
    return S
    

# Case: renvoie le numero de la case de l'individu

def case(S,k):
    '''prend en argument un liste S cree par initialisationSalle et k= un individu, case retourne le numéro de la case où se trouve k'''
    n=len(S)
    for i in range(n):
        if k in S[i]:
            return i

#Disponible: permet de trouver les cases disponibles autour d'un individu

def disponible(S,c,p,n):
    '''prend en argument la liste S=initialisationSalle, c= num de la case, p=nb de colonnes,n=nb de lignes et renvoie les cases dispos'''
    V=voisins(c,p,n)
    L=[]
    for e in V:
        if len(S[e])<8:
            L.append(e)
    return L
            
#Deplacement d'un individu k de la case d vers la case a

def deplacement(S,k,d,a):
    '''prend en argument S=initialisationSalle,k=individu,d=case de depart,a=case d'arrivée et deplace k de d vers a'''
    S[d].remove(k)
    S[a].append(k)

#Tentative de deplacement: succes si il y a une case disponible autour de l'individu

def tentativeDeplacement(S,k,p,n):
    c=case(S,k)
    D=disponible(S,c,p,n)
    a=choice(D)
    deplacement(S,k,c,a)

#Propagation      

def propagation(p,n,N,M):
    #M=nombre d'individu malades
    S=initialisationSalle(p,n,N)
    sains=[k for k in range(N)]
    t=0
    while len(sains) != 0:
        for k in range(len(S)):
            A=tentativeDeplacement(S,k,p,n)
        return A

#Afficher cases

#Pbl : m est le pourcentage de malade par petites cases et pas au total

def affichageCases(S,p,n,N,m):
    for c in range(p*n):
        x,y = abscisse(c,p),ordonnee(c,p)
        nombre = int(len(S[c]))
        for i in range(nombre):
            a=uniform(x+0.1,x+0.9)
            b=uniform(y+0.1,y+0.9)
            plot(a,b,'bo')
    for c in range(p*n):
        x,y = abscisse(c,p),ordonnee(c,p)
        nombre = int(len(S[c])*m)
        for i in range(nombre):
            a=uniform(x+0.1,x+0.9)
            b=uniform(y+0.1,y+0.9)
            plot(a,b,'ro')

def affichageCases1(S,p,n,N,M):
    '''M est le nombre d'individus malades'''
    for c in range(p*n):
        x,y = abscisse(c,p),ordonnee(c,p)
        nombre = int(len(S[c]))
        for e in S[c]:
            a=uniform(x+0.1,x+0.9)
            b=uniform(y+0.1,y+0.9)
            if e == True :
                plot(a,b,'ro')
            else:
                plot(a,b,'bo')
   
def affichage(S,p,n,N,m):
    axis('equal')
    axis('off')
    #grid()
    plot([0,p,p,0,0],[0,0,n,n,0],'k',linewidth=3)
    for i in range(1,n):
        plot([0,p],[i,i],'k')
    for j in range(1,p):
        plot([j,j],[0,n],'k')
    affichageCases(S,p,n,N,m)

def affichage1(S,p,n,N,M):
    axis('equal')
    axis('off')
    #grid()
    plot([0,p,p,0,0],[0,0,n,n,0],'k',linewidth=3)
    for i in range(1,n):
        plot([0,p],[i,i],'k')
    for j in range(1,p):
        plot([j,j],[0,n],'k')
    affichageCases1(S,p,n,N,M)

#Affichage + avancement

#Pbl : Comment compter le nb de sains ? Faire changer le point bleu en rouge ? Faire bouger tout le monde ?

def evacuation2(p,n,N,m):
    #m le pourcentage de malade par cases
    Sains = '''[k for k in range(N)]''' # liste des personnes encore sains dans la salle
    Salle = initialisationSalle(p,n,N)
    temps = 0
    while len(Sains) != 0:
        '''for sortie in P:
            for individu in Salle[sortie]:
                Sains.remove(individu)
            Salle[sortie]=[]
        shuffle(Sains)
        for individu in Sains:
            tentativeDeplacement(Salle,individu,p,n)'''
        affichage(Salle,p,n,N,m)
        pause(0.1)
        clf()
        temps = temps +1
    show() 
