#=========================================================================
#PROJET HUNTER
#=========================================================================
"""PROJECT HUNTER : jeu de morpion"""
__autor__ = "Kinda"
__version__="2.4"
__date__="2012-12-17"
__usage__="""
"""

import random

#========================================================================
def cree_matrice(colonne,ligne):
  """crée une matrice"""
  assert isinstance(colonne,int),"incorrect type for colonne,must be int"
  assert isinstance(ligne,int),"incorrect type for ligne,must be int"

  #var
  valeur=colonne+ligne+1 ##on initialise avec les valeurs les plus hautes possibles

  #begin
  mat=[[valeur for c in range(colonne)]for l in range(ligne)] ##creation de la matrice avec les valeurs initiale

  return mat
  #end
#========================================================================

def matrice_vide(colonne,ligne):
  assert isinstance(colonne,int),"incorrect type for colonne,must be int"
  assert isinstance(ligne,int),"incorrect type for ligne,must be int"
  #begin
  mat=[["   " for c in range(colonne)]for l in range(ligne)] ##matrice vide

  return mat
  #end
#=========================================================================
def str_mat_v(mat):
##  """return a string containing the multiplication table from 1*1 to n*n"""
  assert isinstance(mat,list), "incorrect type for matrice, must be list"

  #var

  rows = []     #list
  cols = []     #list
  col_sep = ""  #str
  row_sep = ""  #str

  #begin

  nb_ligne = len(mat[0]) 
  nb_colonne = len(mat)

  letters_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  letters = '    ' + '   '.join(letters_list[:len(mat[0])])

  col_sep ='|'
  row_sep ="\n  %s+\n" % ('+---'*nb_ligne)


  matrice=[[ "%3s" % str(case)  for case in ligne] for ligne in mat]

  rows = []


  for n,ligne in enumerate(matrice):
    #begin

    rows += ["%d %s%s%s" %(n+1,col_sep,col_sep.join(ligne),col_sep)]
    #end

  return "%s%s%s%s" % (letters, row_sep, row_sep.join(rows), row_sep)
  #end
#=========================================================================
def str_mat(mat):
##  """return a string containing the multiplication table from 1*1 to n*n"""
  assert isinstance(mat,list), "incorrect type for matrice, must be list"

  #var
  p=0           #int
  q=0           #int
  rows = []     #list
  cols = []     #list
  col_sep = ""  #str
  row_sep = ""  #str

  nb_colonne = len(mat)
  nb_ligne = len(mat[0])

  #begin
  letters_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  letters = '    ' + '   '.join(letters_list[:len(mat[0])])

  col_sep ='|'
  row_sep ="\n  %s+\n" % ('+---'*nb_ligne)

  matrice=[[' %d ' % (case) for case in ligne] for ligne in mat]

  rows = []


  for n,ligne in enumerate(matrice):
    #begin

    rows += ["%d %s%s%s" %(n+1,col_sep,col_sep.join(ligne),col_sep)]

    #end

  return "%s%s%s%s" % (letters, row_sep, row_sep.join(rows), row_sep)
  #end




#=================================================================
def place_tresor (nb_tresor,mat):
  """place de façon aléatoire un zero dans la matrice et cree des distances de Manhattan par rapport a elle"""
  assert isinstance (nb_tresor,int),"incorrect type for nb_tresor,must be int"
  assert isinstance(mat,list),"incorrect type for mat,must be list"

  #var
  nb_tresor_place = 0
  colonne = len(mat)
  ligne = len(mat[0])


  #begin
  while nb_tresor_place < nb_tresor:
    #begin
    place_colonne=random.randrange (0,colonne) ##choisie de façon aleatoire une valeur entre 0 et le nombre maximum de colonne
    place_ligne=random.randrange (0,ligne)

    if mat[place_colonne][place_ligne] == 0: continue
    ##si il y a déjà un tresor, on ne fait rien on continue

    for c in range(colonne):
      #begin
      for l in range(ligne):
        #begin
        dist = abs(c-place_colonne)+abs(l-place_ligne)##calcul de la distance de manhattan
        mat[c][l] = min(dist, mat[c][l])
        ##on choisie le minimum entre la valeur inital et la distance de manhattant
        ##et on remet cette valeur choisie dans le tableau
        #end
      #end

    nb_tresor_place=nb_tresor_place + 1
    ##on fait une boucle jusqu'a ce que tous les tresors soit mis
    #end
  return mat
  #end


#=========================================================================

def main():
  """main program"""

  #begin
  print("%s\n%s\n%s\n%s" % ('='*80, __doc__, __usage__, '='*80))

  nbCoup=0
  print("")

  #configuration initiale
  colonneConf=input("<> entrez colonne (par défaut 9):  ")
  if colonneConf == "" :
    colonneConf=9
  else:
    colonneConf=int(colonneConf)
  ligneConf=input("<> entrez ligne (par défaut 9): ")
  if ligneConf == "" :
    ligneConf=9
  else:
    ligneConf=int(ligneConf)
  nb_tresor=input("<> entrez le nombre de tresor (par défaut 1): ")
  if nb_tresor == "" :
    nb_tresor=1
  else:
    nb_tresor=int(nb_tresor)
  while nb_tresor > ligneConf*colonneConf :
    nb_tresor=input("<> entrez un nombre de tresor inferieur ou égal au nombre de cases (par défaut 1): ")
    if nb_tresor == "":
      nb_tresor=1

  #initialisation du jeu
  matrice= cree_matrice(colonneConf, ligneConf)
  donnee=place_tresor(nb_tresor, matrice)
  matrice_v= matrice_vide(colonneConf, ligneConf)

  nb_tresor_trouve=0

  #begin
  while nb_tresor_trouve < nb_tresor :
    print("Encore %s tresors à trouver.\nVous avez utilisé %s coups" % (nb_tresor-nb_tresor_trouve, nbCoup))
    print(str_mat_v(matrice_v))
    s=input("Entrez coordonnees:  ")

    while s == "" :
        i = 0
        s=input("Entrez coordonnees:  ")
        saisie[i]=s
        i = i+1     
    colonne = int(s[1]) - 1
    ligne = ord(s[0])-ord('A')
    nbCoup=nbCoup+1
    if donnee[colonne][ligne]!=0 :
        #begin
        matrice_v[colonne][ligne] = str(donnee[colonne][ligne])
                  
    else :
        print ("Vous avez trouvé un tresor.\n")
        matrice_v[colonne][ligne] = "X"
        nb_tresor_trouve=nb_tresor_trouve+1
        
        
    if nb_tresor_trouve == nb_tresor :
      print("Félicitation\nVous avez trouvé tous les tresors!!! En",nbCoup,"coup")

      
  #end

#========================================================================
if __name__ == '__main__':

  main()

# ==============================================================================


