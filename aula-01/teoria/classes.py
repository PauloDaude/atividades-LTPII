class Carro:
  tipo = "automovel"

  def __init__(self, modelo, ano):
    self.modelo = modelo
    self.ano = ano
  def description(self):
    return f"{self.modelo} é do ano {self.ano}"