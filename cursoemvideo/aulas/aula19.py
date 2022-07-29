print()
pessoas = {"nome": "Victor", "sexo": "M", "idade": 20}  # Ou pessoas = dict()
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
pessoas["peso"] = 75
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
print()
for i in pessoas.items():
    print(i)
print()
for k, v in pessoas.items():
    print(f"{k} = {v}")
