class Aluno:
  def __init__(self, nome, idade, altura, peso):
      self.nome = nome
      self.idade = idade
      self.altura = altura
      self.peso = peso

  def getNome(self):
      return self.nome

  def setNome(self, nome):
      self.nome = nome

  def getImc(self):
      imc = self.peso / (self.altura * self.altura)
      return round(imc, 2)
  def getTodosOsvalores(self):
      return(self.nome, self.idade, self.altura, self.peso)

aluno1 = Aluno("Julio", 18, 1.86, 74)
aluno2 = Aluno("Horty", 40, 1.70, 54)
print(aluno1.getImc())
print(aluno2.getImc())
x= aluno1.getTodosOsvalores()
y= aluno2.getTodosOsvalores()

print(x)
print(y)