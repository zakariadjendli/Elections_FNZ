# dict_infos = {}

nom = input("Votre nom: ")
rue = input("Entrez le nom de votre rue: ")
chiffre_maison = input("Entrez le chiffre de votre building: ")

# for i in (nom, rue, chiffre_maison):
#     dict_infos[i] = locals()[i]

# print(dict_infos)


dict_infos = {
    "nom": nom,
    "rue": rue,
    "chiffre_maison": chiffre_maison 
}
for i in dict_infos.keys():
    print(dict_infos[i])