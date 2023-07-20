import pygame
import os
import copy
import sys
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\21625\\Desktop\\ProjetAiGraphique\\song.mp3')
pygame.mixer.music.play()
    #*********************Functions*********************
#************afficher Matrice******
def afficheTaquin(T):
    r1 = len(T)
    c1 = len(T[0])
    print("+---+---+---+")
    for i in range(r1):
        for j in range(c1):
            print("| "+str(T[i][j])+" ",end="")
        print("|")
        print("+---+---+---+")

#************check si matrice=matrice finale******
def estEtatFinal(T, F):
    test = True
    r1 = len(T)
    c1 = len(T[0])
    r2 = len(F)
    c2 = len(F[0])
    if r1 != r2 or c1 != c2:
        test = False
        return test
    else:
        for i in range(0, r1):
            for j in range(0, c1):
                if T[i][j] != F[i][j]:
                    test = False
    return test

#************retourne position de la case vide******
def posCaseVide(T):
    r1 = len(T)
    c1 = len(T[0])
    for i in range(0, r1):
        for j in range(0, c1):
            if T[i][j] == 0:
                return (i, j)

#************retourne des matrices quand on fait un mouvement de la case vide******
def voisin(FirstNode, i, j):
    O = []
    c1 = len(FirstNode[0])
    r1 = len(FirstNode)
    
    # 0 f losange
    if i != 0 and i != r1 - 1 and j == c1 - 1:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j - 1)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i - 1, j)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i + 1, j)))
        O.append(K)
    elif i != 0 and i != r1 - 1 and j == 0:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j + 1)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i - 1, j)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i + 1, j)))
        O.append(K)
    elif i == 0 and j != 0 and j != c1 - 1:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i + 1, j)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j + 1)))
        O.append(K)       
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j - 1)))
        O.append(K)

    elif i == r1 - 1 and j != 0 and j != c1 - 1:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j + 1)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i - 1, j)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j - 1)))
        O.append(K)
    # 0 in the middle
    elif i != 0 and i != r1 - 1 and j != 0 and j != c1 - 1:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i + 1, j)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i - 1, j)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j - 1)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j + 1)))
        O.append(K)
        
        
    # 0 in the corner
    elif i == 0 and j == 0:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j + 1)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i + 1, j)))
        O.append(K)
        
    elif i == c1 - 1 and j == 0:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j + 1)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i - 1, j)))
        O.append(K)
        
    elif i == c1 - 1 and j == r1 - 1:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j - 1)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i - 1, j)))
        O.append(K)  
    else:
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i, j - 1)))
        O.append(K)
        K = copy.deepcopy(FirstNode)
        permuter(K, (numero(FirstNode, i + 1, j)))
        O.append(K)
    return O


#************retourne valeur de la case(i,j) d'une matrice T ******
def numero(T, i, j):
    return T[i][j]

#************retourne la position de la valeur x dans la matrice T******
def position(T, x):
    r1 = len(T)
    c1 = len(T[0])
    for i in range(r1):
        for j in range(c1):
            if T[i][j] == x:
                return (i, j)

##************permute le 0 avec la valeur c1 dans une matrice T(utilisé dans la fonction voisin)******
def permuter(T, c1):
    (i, j) = posCaseVide(T)
    (m, l) = position(T, c1)
    x = T[m][l]
    T[m][l] = 0
    T[i][j] = x

def malPlace(T):
    F = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    k=0
    r1 = len(T)
    c1 = len(T[0])
    for i in range(r1):
        for j in range(c1):
            if (T[i][j]!=F[i][j]):
                k=k+1
    return k    

#**************************************Main**************************************

    #*********************Recherche par profondeur*********************
def DFS(T,F):    
    ClosedNodes = []
    FreeNodes = []
    GeneratedStates = []
    FreeNodes.insert(0, T)
    success = False
    while (len(FreeNodes) != 0) and (success == False):
        FirstNode = FreeNodes.pop(0)
        ClosedNodes.append(FirstNode)
        i, j = posCaseVide(FirstNode)
        NewGeneratedStates = voisin(FirstNode, i, j)
        for x in NewGeneratedStates:
            GeneratedStates.insert(0, x)
        for s in GeneratedStates:
            if s not in ClosedNodes and s not in FreeNodes:
                FreeNodes.insert(0, s)
            if estEtatFinal(s, F):
                success = True
                return ClosedNodes,len(ClosedNodes),len(ClosedNodes)+len(FreeNodes)
    if success==False:
        return None
    #*********************Recherche par largeur*********************   
def BFS(T,F):
    ClosedNodes=[]
    FreeNodes=[]
    FreeNodes.insert(0,T)
    success=False
    nb=0
    while ((len(FreeNodes)!=0) and (success==False)):
        GeneratedStates=[]
        FirstNode=FreeNodes.pop()
        ClosedNodes.append(FirstNode)
        i,j=posCaseVide(FirstNode)
        NewGeneratedStates=voisin(FirstNode,i,j)
        nb=nb+1
        for x in NewGeneratedStates:
            GeneratedStates.append(x)
        for s in GeneratedStates:
            if s not in ClosedNodes and s not in FreeNodes:
                FreeNodes.insert(0, s)
            if estEtatFinal(s,F):
                success=True
                return ClosedNodes,len(ClosedNodes),len(ClosedNodes)+len(FreeNodes)
    if success==False:
        return None
    #*********************Recherche par profondeur Limitée et L=3*********************
def DFS_limite(T,F,L):
    ClosedNodes=[]
    FreeNodes=[]
    depth=0
    GeneratedStates=[]
    FreeNodes.append((T,depth))
    success=False
    nb=0
    while ((len(FreeNodes)!=0) and (success==False)):
        FirstNode,depth=FreeNodes.pop(0)
        if estEtatFinal(FirstNode,F):
                success=True
                return ClosedNodes,len(ClosedNodes),len(ClosedNodes)+len(FreeNodes)
        ClosedNodes.append(FirstNode)
        i,j=posCaseVide(FirstNode)
        NewGeneratedStates=voisin(FirstNode,i,j)
        nb=nb+1
        for x in NewGeneratedStates:
            GeneratedStates.append(x)
        for s in GeneratedStates:
            test=True
            for x,y in FreeNodes:
                if s==x:
                    test=False
            if s not in ClosedNodes and depth+1<L and test:
                FreeNodes.insert(0,(s,depth+1))
    if success==False: 
        return None

    #*********************Astar*********************
#dans l'algorithme Astar on choisit toujours le noeud ayant la valeur minimale de la fonction f

def Astar(T,F):
    ClosedNodes = []
    FreeNodes = []
    depth = 0
    FreeNodes.append((T,depth,depth+malPlace(T)))
    success = False
    ClosedNodesMatriceOnly=[]
    while ((len(FreeNodes) != 0) and (success == False)):
        GeneratedStates = []
        max=sys.maxsize
        count=0
        #on doit savoir l'index de freenodes pour pouvoir changer la valeur de h
        for taq,dep,h in FreeNodes:
            h=malPlace(taq)+dep
            if (h<max):
                max=h
                FirstNode=taq
                depth=dep
                fun=h
            FreeNodes[count]=(taq,dep,h)
            count=count+1
        FreeNodes.remove((FirstNode,depth,fun))
        if estEtatFinal(FirstNode, F):
            success = True
            for taq,dep,h in ClosedNodes:
                ClosedNodesMatriceOnly.append(taq) 
            ClosedNodesMatriceOnly.append(FirstNode)                              
            return ClosedNodesMatriceOnly,len(ClosedNodes), len(ClosedNodes) + len(FreeNodes)
        ClosedNodes.append((FirstNode,depth,fun))
        i, j = posCaseVide(FirstNode)
        NewGeneratedStates = voisin(FirstNode, i, j)
        for x in NewGeneratedStates:
            GeneratedStates.append((x,depth))
        for s,depth in GeneratedStates:
            if s not in ClosedNodes and s not in FreeNodes:
                FreeNodes.append((s, depth + 1,0))
    return None
#*******************définition générale***********************
Width=900
Height=500
White=(255,255,255)
Background_colour=(123,199,249)
Background_colour2=(106,146,242)
Black=(0,0,0)
Affichage_Font=pygame.font.SysFont('ComicSans',20)
#affichage de l'écran
win=pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Jeu de Taquin 3*3")

#initialisation de la longueur et largeur des cases
case_width=100
case_height=100
case_Button_width=70
case_Button_height=35
 
#extraction des images qui vont servir de bouton
case_DFS_limite=pygame.transform.scale(pygame.image.load(os.path.join('img','taquinDFSL.png')),(case_Button_width,case_Button_height))
case_DFS=pygame.transform.scale(pygame.image.load(os.path.join('img','taquinDFS.png')),(case_Button_width,case_Button_height))
case_reset=pygame.transform.scale(pygame.image.load(os.path.join('img','taquinReset.png')),(case_Button_width,case_Button_height))
case_BFS=pygame.transform.scale(pygame.image.load(os.path.join('img','taquinBFS.png')),(case_Button_width,case_Button_height))
case_ASTAR=pygame.transform.scale(pygame.image.load(os.path.join('img','taquinAstar.png')),(case_Button_width,case_Button_height))
case=pygame.transform.scale(pygame.image.load(os.path.join('img','taquin.png')),(case_width,case_height))
Width_Height=[[(300,100),(401,100),(502,100)],[(300,201),(401,201),(502,201)],[(300,302),(401,302),(502,302)]]
case_DFS_width_pos,case_DFS_height_pos=700,345

#affichage du path pour arriver à la solution
def Path(ClosedNodes,rect_reset,rect_limite,rect_DFS,X,Y,input_box,text_input,rect_Astar,rect_BFS):
    for i in ClosedNodes:
        drawV1(i,rect_Astar,rect_reset,rect_BFS,rect_limite,rect_DFS,X,Y,input_box,text_input)
        pygame.time.delay(300)
#dessine le background    
def draw_background():
    background_img=pygame.transform.scale(pygame.image.load(os.path.join('img','images.jpg')),(Width,Height))
    win.blit(background_img,(0,0))
    pygame.display.flip()

#************************************Mouvements pouvant être effectuées par l'utilisateur********************
def move_left(T):
    i,j=posCaseVide(T)
    K=voisin(T,i,j)
    for x in K:
        if (j-1>=0):
            if (x[i][j-1]==0):
                win.fill(Background_colour,(300,100,302,200))
                return x
    return T
def move_right(T):
    i,j=posCaseVide(T)
    K=voisin(T,i,j)
    for x in K:
        if (j+1<len(x)):
            if (x[i][j+1]==0):
                win.fill(Background_colour,(300,100,302,200))
                return x
    return T
def move_up(T):
    i,j=posCaseVide(T)
    K=voisin(T,i,j)
    for x in K:
        if (i-1>=0):
            if (x[i-1][j]==0):
                win.fill(Background_colour,(300,100,302,200))
                return x
    return T

def move_down(T):
    i,j=posCaseVide(T)
    K=voisin(T,i,j)
    for x in K:
        if i+1<len(x[0]):
            if (x[i+1][j]==0):
                win.fill(Background_colour,(300,100,302,200))
                return x
    return T

#*****Fonction pour dessiner les différents images et textes*******           
def drawV1(T,rect_Astar,rect_reset,rect_BFS,rect_limite,rect_DFS,x,y,input_box,text_input):  
    for i in range(3):
        for j in range(3):
            #affichage de chaque case 
            tile_value=T[i][j]
            if (tile_value!=0):
                #si valeur différent de 0 dessiner la case
                #initialisation d'un rectangle avec les longueurs et largeurs définis en haut de la page
                tile_rect=pygame.Rect(Width_Height[i][j][0],Width_Height[i][j][1],case_width,case_height)
                #dessiner le rectangle
                pygame.draw.rect(win,White,tile_rect)
                font=pygame.font.SysFont('Arial',40)
                #affichage du text
                text=font.render(str(tile_value),True,Black)
                text_rect=text.get_rect(center=tile_rect.center)       
                win.blit(text,text_rect)
            else:
                #affichage d'un rectangle noir pour la case 0
                tile_rect=pygame.Rect(Width_Height[i][j][0],Width_Height[i][j][1],case_width,case_height)
                pygame.draw.rect(win,Black,tile_rect)
    #affichage des différents boutons
    win.blit(case_DFS_limite,(rect_limite.x,rect_limite.y))
    win.blit(case_DFS,(rect_DFS.x,rect_DFS.y))
    win.blit(case_reset,(rect_reset.x,rect_reset.y))
    win.blit(case_BFS,(rect_BFS.x,rect_BFS.y))
    win.blit(case_ASTAR,(rect_Astar.x,rect_Astar.y))
    #affichage du résultats:
    if (x!=0 and y!=0):
        Affich=Affichage_Font.render("Found: le nombre de noeuds clos est :"+str(x),1,White)
        Affich1=Affichage_Font.render("le nombre de noeuds explorés est "+str(y),1,White)
        win.fill(Background_colour, (0, 0, Width, 100))
        win.blit(Affich,(100,20))
        win.blit(Affich1,(100,40))       
        pygame.display.update()
        pygame.time.wait(1000)
    #sinon affichage d'un message d'initialisation
    else:
        AffichE_message = Affichage_Font.render("Essayer de trouver la solution en utilisant les flèches!", 1, White)
        win.fill(Background_colour, (0, 0, Width, 100))  # Clear the area where the old text was displayed
        win.blit(AffichE_message, (100, 20))
        pygame.display.update()
    pygame.draw.rect(win, (255, 255, 255), input_box,1)
    win.fill(Background_colour2, (input_box.x+5, input_box.y+1, 72, 33))
    text_surface = font.render(text_input, True, (255, 255, 255))
    win.blit(text_surface, (input_box.x + 5, input_box.y-5 ))
    pygame.display.update()
#fonction utilisé quand l'utilisateur trouve la solution avec le mouvement des flèches
def draw_Final(T,rect_limite,rect_DFS,steps):
    for i in range(3):
        for j in range(3):
            tile_value=T[i][j]
            if (tile_value!=0):
                tile_rect=pygame.Rect(Width_Height[i][j][0],Width_Height[i][j][1],case_width,case_height)
                pygame.draw.rect(win,White,tile_rect)
                font=pygame.font.SysFont('Arial',40)
                text=font.render(str(tile_value),True,Black)
                text_rect=text.get_rect(center=tile_rect.center)       
                win.blit(text,text_rect)
    win.blit(case_DFS,(rect_DFS.x,rect_DFS.y))
    win.blit(case_DFS_limite,(rect_limite.x,rect_limite.y))
    Affich=Affichage_Font.render("Found: le nombre de pas requis est est :"+str(steps),1,White)
    Affich1=Affichage_Font.render("Voulez-vous ressayer?",1,White)
    win.fill(Background_colour, (0, 0, Width, 100))
    win.blit(Affich,(100,20))
    win.blit(Affich1,(100,40))
    pygame.display.update()
    
#affichage d'une erreur dans le DFS limité
def draw_Error(T,rect_limite,rect_DFS,L):
    for i in range(3):
        for j in range(3):
            tile_value=T[i][j]
            if (tile_value!=0):
                tile_rect=pygame.Rect(Width_Height[i][j][0],Width_Height[i][j][1],case_width,case_height)
                pygame.draw.rect(win,White,tile_rect)
                font=pygame.font.SysFont('Arial',40)
                text=font.render(str(tile_value),True,Black)
                text_rect=text.get_rect(center=tile_rect.center)       
                win.blit(text,text_rect)
    win.blit(case_DFS,(rect_DFS.x,rect_DFS.y))
    win.blit(case_DFS_limite,(rect_limite.x,rect_limite.y))
    Affich=Affichage_Font.render("Pas de solution possible pour L="+str(L),1,White)
    win.fill(Background_colour, (0, 0, Width, 100))
    win.blit(Affich,(100,20))
    pygame.display.update()
            
def main():
    #initialisation des rectangles avec leurs positions, longueurs et largeur initialisé dans le début du code
    rect_reset=pygame.Rect(case_DFS_width_pos,case_DFS_height_pos-40, 80, 35)
    input_box = pygame.Rect(case_DFS_width_pos+80,case_DFS_height_pos+40, 80, 35)
    text_input = 'L='
    rect_limite=pygame.Rect(case_DFS_width_pos,case_DFS_height_pos+40,case_Button_width,case_Button_height)
    rect_DFS=pygame.Rect(case_DFS_width_pos,case_DFS_height_pos,case_Button_width,case_Button_height)
    rect_BFS=pygame.Rect(case_DFS_width_pos,case_DFS_height_pos-80,case_Button_width,case_Button_height)
    rect_Astar=pygame.Rect(case_DFS_width_pos,case_DFS_height_pos-120,case_Button_width,case_Button_height)
    clock=pygame.time.Clock()
    run=True
    count=0
    T=[[1, 2, 3], [8, 6, 0], [7, 5, 4]]
    K=copy.deepcopy(T)
    F=[[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    steps=0
    draw_background()
    while run:
        X=0
        Y=0
        clock.tick(60)
        for event in pygame.event.get():
            #quitter la fenêtre
            if event.type==pygame.QUIT:
                run=False
            #si on clique sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                #cliquer sur Astar
                if rect_Astar.collidepoint(event.pos):
                    ClosedNodes,X,Y=Astar(T,F)
                    Path(ClosedNodes,rect_reset,rect_limite,rect_DFS,X,Y,input_box,text_input,rect_Astar,rect_BFS)
                    drawV1(F,rect_Astar,rect_reset,rect_BFS,rect_limite,rect_DFS,X,Y,input_box,text_input)
                    #toujours initialiser le nombre de steps
                    steps=0
                #cliquer sur BFS
                if rect_BFS.collidepoint(event.pos):
                    ClosedNodes,X,Y=BFS(T,F)
                    Path(ClosedNodes,rect_reset,rect_limite,rect_DFS,X,Y,input_box,text_input,rect_Astar,rect_BFS)
                    drawV1(F,rect_Astar,rect_reset,rect_BFS,rect_limite,rect_DFS,X,Y,input_box,text_input)
                    steps=0
                #cliquer sur reset
                if rect_reset.collidepoint(event.pos):
                    T=K
                    drawV1(T,rect_Astar,rect_reset,rect_BFS,rect_limite,rect_DFS,X,Y,input_box,text_input)
                    steps=0
                #cliquer sur DFS
                if rect_DFS.collidepoint(event.pos):
                    ClosedNodes,X,Y=DFS(T,F)
                    Path(ClosedNodes,rect_reset,rect_limite,rect_DFS,X,Y,input_box,text_input,rect_Astar,rect_BFS)
                    drawV1(F,rect_Astar,rect_reset,rect_BFS,rect_limite,rect_DFS,X,Y,input_box,text_input)
                    steps=0
                #cliquer sur DFS limité
                if rect_limite.collidepoint(event.pos):
                    try:
                        test=DFS_limite(T,F,L_value)
                        #check si la valeur retournée est none ou pas
                        if test is not None and isinstance(test,tuple):
                            ClosedNodes,X,Y=DFS_limite(T,F,L_value)
                            Path(ClosedNodes,rect_reset,rect_limite,rect_DFS,X,Y,input_box,text_input,rect_Astar,rect_BFS)
                            drawV1(F,rect_Astar,rect_reset,rect_BFS,rect_limite,rect_DFS,X,Y,input_box,text_input)
                            steps=0
                        else:
                            draw_Error(T,rect_limite,rect_DFS,L_value)
                            pygame.time.delay(3000)
                    except:
                        print("")
            #gestion des mouvements et incrémentation du nombre de steps
            if event.type==pygame.KEYDOWN:
                steps=steps+1
                if event.key==pygame.K_LEFT:
                    T=move_right(T)
                if event.key==pygame.K_RIGHT:
                    T=move_left(T)
                if event.key==pygame.K_UP:
                    T=move_down(T)
                if event.key==pygame.K_DOWN:
                    T=move_up(T)
                #supprimer dans la case de saisie de L
                #count utilisé pour pouvoir saisir au maximum 2 chiffres
                if event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                    count=count-1
                    if (count<0):
                        count=0
                    if (text_input=="L"):
                        text_input="L="
                else:
                    if (count<2):
                        text_input += event.unicode
                        L_value=copy.deepcopy(text_input)
                        try:
                            L_value = int(L_value.split('=')[1])
                        except:
                            print("")
                        count=count+1
        #si l'utilisateur trouve la solution avec les mouvements
        if (estEtatFinal(T,F)):                    
            draw_Final(T,rect_limite,rect_DFS,steps)
            T=K
            pygame.time.delay(3000)
            win.fill(Background_colour, (0, 0, Width, 100))
            steps=0                
        drawV1(T,rect_Astar,rect_reset,rect_BFS,rect_limite,rect_DFS,X,Y,input_box,text_input)
    pygame.quit()
main()
