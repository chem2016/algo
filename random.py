import random
group1 = [
"Charmagne",
"Kristina Cayetano",
"Jesen Tanadi"
]
group2 = [
"Zachary Levine",
"Yifei Zhang",
"Mark Cruz"
]
group3 = [
"Maria Lapshina",
"Paul 'Grey' Weissend",
"Stella Kim"
]

for i in range(3):
    name1 = random.choice(group1)
    name2 = random.choice(group2)
    name3 = random.choice(group3)
    group1.remove(name1)
    group2.remove(name2)
    group3.remove(name3)

    print("%s, %s, %s"%(name1, name2, name3))

