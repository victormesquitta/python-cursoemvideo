try:
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    r = a/b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados fornecidos.")
except ZeroDivisionError:
    print("Impossível dividir por zero.")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados.")
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f"o resultado deu {r:.1f}")
finally:
    print("Volte sempre! Muito obrigado!")
