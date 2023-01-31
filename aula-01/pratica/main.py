from classes import Pessoa, Calculadora, Monitor

pessoa1 = Pessoa(str(input("Digite seu nome: ")), int(input("Digite a sua idade: ")), float(input("Digite a sua altura: ")), float(input("Digite o seu peso: ")))

pessoa1.imc()
pessoa1.maioridade()

print("\n\n")

calculo1 = Calculadora(2, 5)
calculo1.somar()
calculo1.subtrair()
calculo1.multiplicar()
calculo1.dividir()

print("\n\n")

monitor1 = Monitor(2000, "24'", "Dell", 2020)
monitor1.ligaMonitor()
monitor1.idadeMonitor()