# coding: utf-8

# montrer comment lire un fichier CSV pour
# afficher un graphe

# lire des données et extrapoler
import csv

with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print('.... '.join(row))