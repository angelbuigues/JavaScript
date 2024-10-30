import random;

names=["angel", "paco", "pedro", "mady", "ivan", "daniel", "rafael", "ateneri", "sergio"]
carrers=["chemestry", "mats", "lenguaje"]
cities=["Alacant", "Benidorm", "Barcelona"]
for i in range(len(names)):
    print(names[i],"studies",random.choice(carrers),"in",random.choice(cities))