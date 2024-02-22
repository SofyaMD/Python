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

def cases_voisines(c,p,n):
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
    '''prend en argument p=nb de col, n=nb de lignes, N=nb d'individu, N max=p*n*8 et renvoie une salle avec 8 ind max par case'''
    S=[[] for i in range(p*n)]  
    for k in range(N):
        c=randint(0,p*n-1)
        while len(S[c])==8:
            c=randint(0,p*n-1)
        S[c].append(k)
    return S


#Case: renvoie le numero de la case de l'individu

def case(S,individu):
    '''prend en argument un liste S cree par initialisationSalle et k= un individu, case retourne le numéro de la case où se trouve k'''
    
    for c in range(len(S)):
        if individu in S[c]:
            return c

#Disponible: permet de trouver les cases disponibles autour d'un individu

def cases_accessibles(S,c,p,n):
    '''prend en argument la liste S=initialisationSalle, c= num de la case, p=nb de colonnes,n=nb de lignes et renvoie les cases dispos'''
    V=cases_voisines(c,p,n)
    L=[]
    for e in V:
        if len(S[e])<8:
            L.append(e)
    return L
            

#Tentative de deplacement: succes si il y a une case disponible autour de l'individu

def tentativeDeplacement(S,k,p,n):
    c=case(S,k)
    D=cases_accessibles(S,c,p,n)
    if len(D)!=0:
        a=choice(D)
        S[c].remove(k)
        S[a].append(k)


#Nombre de malade dans une case

def malade(S,E,c):
    m=0
    s=0
    for e in S[c]:
        
        if E[e]:
            m=m+1
        else:
            s=s+1
    return(m,s)

#Affichage

def affichageCases(S,E,p,n):
    for c in range(p*n):
        x,y = abscisse(c,p),ordonnee(c,p)
        m,s=malade(S,E,c)
        for i in range(s):
            a=uniform(x+0.1,x+0.9)
            b=uniform(y+0.1,y+0.9)
            plot(a,b,'bo')
        for i in range(m):
            a=uniform(x+0.1,x+0.9)
            b=uniform(y+0.1,y+0.9)
            plot(a,b,'ro')    

def affichage(S,E,p,n):
    axis('equal')
    axis('off')
    #grid()
    plot([0,p,p,0,0],[0,0,n,n,0],'k',linewidth=3)
    for i in range(1,n):
        plot([0,p],[i,i],'k')
    for j in range(1,p):
        plot([j,j],[0,n],'k')
    affichageCases(S,E,p,n)
    show()
    
            
def virus(p,n,N,m,r):
    #m=proportion de malades
    #r=probabilité de contamination

    I = list(range(N)) # liste des individus
    E = [random()<m for k in range(N)] # états des individus (malade/sain)
    
    S = initialisationSalle(p,n,N)
    
    temps = 0
    while sum(E) != N:
        shuffle(I)
        for individu in I:
            if E[individu] == 1:
                c=case(S,individu)
                for personne in S[c]:
                    if E[personne]==0:
                        l=random()
                        if l<r:
                            E[personne]=1
                            
        shuffle(I)
        for individu in I:
            tentativeDeplacement(S,individu,p,n)
        affichage(S,E,p,n)
        pause(0.1)
        clf()
        temps = temps +1
        print(temps)
    show()
        
        
    














