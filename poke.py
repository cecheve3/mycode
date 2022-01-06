import csv
pokenum= input(">")
with open("pokedex.txt","r") as pokedata:
    for x in csv.DictReader(pokedata):
        pokedict= dict(x)
        if pokedict["#"] == pokenum:
            print(f"{pokedict['Name']} is of the {pokedict['Type 1']} type!")
