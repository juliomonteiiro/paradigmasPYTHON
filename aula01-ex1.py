class Aluno:
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2

    def setNome(self, nome):
          self.nome = nome

    def setNota1(self, n1):
        self.n1 = n1

    def setNota2(self, n2):
        self.n2 = n2
    
    def getNota1(self):
        return self.n1

    def getNota2(self):
        return self.n2

    def getMedia(self):
        media = (self.n1 + self.n2) / 2
        return media

    def getTodosOsvalores(self):
      return(self.nome, self.n1, self.n2)

aluno1 = Aluno("Julio", 10, 8)
aluno2 = Aluno("Horty", 8, 5)
print(aluno1.getTodosOsvalores())
print(aluno1.getMedia())
print(aluno2.getTodosOsvalores())
print(aluno2.getMedia())
    



