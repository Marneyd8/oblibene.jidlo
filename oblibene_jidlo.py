print("Tento projekt je verejne dostupny na GitHubu!")
jidlo = input("Zadej svoje oblibene jidlo: ")

with open("oblibene_veci.txt", "w") as f:
    f.write(jidlo)
