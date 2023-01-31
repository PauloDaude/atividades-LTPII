class Pessoa:
  def __init__(self, nome, idade, altura, peso):
    self.nome = nome
    self.idade = idade
    self.altura = altura
    self.peso = peso

  def imc(self):
    calculoImc = self.peso / (self.altura**2)
    if calculoImc <= 18.5:
      status = "Está abaixo do peso ideal! Vá comer!"
    elif calculoImc <= 24.99:
      status = "Está no Peso ideal! Continue assim!"
    elif calculoImc <= 29.99:
      status = "Está sobrepeso! Te orienta e come menos!"
    else:
      status = "Está obeso! Cuidado tu pode morrer!"
    print(self.nome, status)

  def maioridade(self):
    if self.idade >= 18:
      status2 = "é maior de idade!"
    else:
      status2 = "é menor de idade! Vá comer!"
    print(self.nome, status2)
    


class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def multiplicar(self):
        calculo = self.num1 * self.num2
        print(f"{self.num1} x {self.num2} = {calculo}")
    
    def somar(self):
        calculo = self.num1 + self.num2
        print(f"{self.num1} + {self.num2} = {calculo}")

    def subtrair(self):
        calculo = self.num1 - self.num2
        print(f"{self.num1} - {self.num2} = {calculo}")
    
    def dividir(self):
        calculo = self.num1 / self.num2
        print(f"{self.num1} / {self.num2} = {calculo}")
        


class Monitor():
    def __init__(self, valor, polegada, marca, ano):
        self.valor = valor
        self.polagada = polegada
        self.marca = marca
        self.ano = ano

    def ligaMonitor(self):
        print(f"O monitor da marca {self.marca} está ligado!")
    
    def idadeMonitor(self):
        print(f"O ano do monitor é de {self.ano}")