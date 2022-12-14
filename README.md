# Programmation en sciences
Repo pour code et organisation du cours 

**SN1** *programmation en sciences*

| Semaine                | Séquence des cours                          | Travaux pratiques           |
|------------------------|---------------------------------------------|-----------------------------|
| [1 →](seances/01.md)   | Intro, plan de cours, premier script        | TP1 : calcul "à la dumb"    |
| [2 →](seances/02.md)   | Valeurs, expressions, types                 | cible 25% fini              |
| [3 →](seances/03.md)   | Structures contrôles                        | cible 50%                   |
| [4 →](seances/04.md)   | Fonctions                                   | 75%                         |
| [5 →](seances/05.md)   | Algorithmique et débogage                   | 100%                        |
| [6 →](seances/06.md)   | Révisions, formatif                         | TP2 : science expérimentale |
| [7 →](seances/07.md)   | **Examen intra**                            | 25%                         |
| [8 →](seances/08.md)   | Fichiers, CSV                               | 50%                         |
| [9 →](seances/09.md)   | Calcul et Numpy, librairie et environnement | 75%                         |
| [10 →](seances/10.md)  | Graphiques et matplotlib                    | 100%                        |
| [11 →](seances/11.md)  | Algorithmique le retour                     | TP3 : à déterminer          |
| [12 →](seances/12.md) | Objet et classes                            | 25%                         |
| [13 →](seances/13.md) | Performance, optimisation parallélisme      | 50%                         |
| [14 →](seances/14.md) | Formatif/révisions. Aperçu Réseaux neurones | 75%                         |
| [15 →](seances/15.md) | **Examen final**                            | 100%                        |


https://mujoco.org/

```mermaid
flowchart TD;
    core(Python fondamentaux)
    objet(Python orienté objet)
    fichiers(Python et les fichiers)
    web(Python pour un serveur web)
    sciences(Python pour les sciences)
    admin(Python pour l'administration système)
    data(Python pour les données)
    ai(Python pour l'intelligence artificielle)
    ui(Python et interface graphique utilisateur)
    core-->fichiers-->admin
    core-->sciences
    core-->web
    core-->objet
    fichiers-->sciences
    core-->sciences-->ai
    core-->data
    core-->ui
```


```mermaid
flowchart TD;
    execInter(Python interactif)
    execScript(Python script)
    execJupyter(Python Jupyter)
    execModule(Python module et multifichier)
    expr1(Constante, valeur et type)
    expr2(Expression et opérateur)
    expr3(Tableaux, tuples, dictionnaires)
    expr4(Variables)
    flowSeq(Flot d'exécution séquence )
    flowIf(Flot d'exécution alternative)
    flowFor(Flot d'exécution répétition)
    flowError(Flot d'exécution erreur, lance et attrape)
    flowRec(Flot d'exécution 4 récursion)
    fonction1(Appel fonction existante)
    fonction2(Définition d'une fonction syntaxe, type)
    fonction3(Définition d'une fonction syntaxe, type)
    fonction4(Récursivité)
    pandas1(Pandas 1 import export)
    pandas2(Pandas 2 dataframe et modif)
    pandas3(Pandas 3 interaction avec autres librairies)
    np1(Numpy 1 tableaux)
    
    expr1-->expr2-->expr3
    execInter-->execScript-->execJupyter
    execScript-->execModule
    flowSeq-->flowIf-->flowFor
    flowSeq-->flowError
    fonction1-->fonction2-->fonction3-->fonction4
    execScript-->np1
    flowFunction-->np1
    pandas1-->pandas2-->pandas3
```
