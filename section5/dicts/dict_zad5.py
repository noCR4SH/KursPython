poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower()
poem = poem.replace(",", "")
poem = poem.split()

words = {}

for i in poem:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

for k, v in words.items():
    print(k, ":", v)