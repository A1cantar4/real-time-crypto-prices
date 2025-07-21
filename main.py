import sys
import os
import importlib

def main():
    print("Olá chefe, escolha qual módulo deseja executar: ")
    print("1. Advanced Price API")
    print("2. Simple Price API")

    escolha = input("\nDigite qual o número capitão: ").strip()

    if escolha == "1":
        nome_modulo = "core.advanced_price_api"
    elif escolha == "2":
        nome_modulo = "core.simple_price_api"
    else:
        print("Não entendi, você digitou certo?.")
        return

    try:
        modulo = importlib.import_module(nome_modulo)
        modulo.main()
    except Exception as e:
        print(f"É... deu erro ao importar ou executar o módulo: {e}")

if __name__ == "__main__":
    main()
