# Uma Turma tem alunos. Um Aluno é um objeto independente (agregação), mas a Matricula é um registro que só existe dentro da Turma (composição) para associar um aluno a ela. A nota do aluno deve ser validada. Instruções: Crie a classe Aluno (simples, só com nome). Crie a classe Matricula. Ela recebe um objeto Aluno (agregação) e tem uma propriedade @property para a nota, que deve ser um valor entre 0 e 10. Crie a classe Turma. No construtor, crie uma lista vazia para Matriculas. Na classe Turma, crie um método matricular(aluno) que cria uma Matricula (composição) e a adiciona à lista. Adicione um método exibir_alunos_e_notas() para mostrar os resultados.

class Aluno:
    def __init__(self, nome):
        self.nome = nome


class Matricula:
    def __init__(self, aluno):
        self.aluno = aluno

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")

class Turma:
    def __init__(self):
        self.matriculas = []

    def matricular(self, aluno):
        nova_matricula = Matricula(aluno)
        self.matriculas.append(nova_matricula)
        return nova_matricula

    def exibir_alunos_e_notas(self):
        print("Alunos e Notas")
        for matricula in self.matriculas:
            print(f"Aluno: {matricula.aluno.nome} | Nota: {matricula.nota}")

aluno1 = Aluno("Ana")
aluno2 = Aluno("Carlos")
aluno3 = Aluno("Mariana")

turma = Turma()

m1 = turma.matricular(aluno1)
m2 = turma.matricular(aluno2)
m3 = turma.matricular(aluno3)

m1.nota = 8.5
m2.nota = 9.7
m3.nota = 7.0

turma.exibir_alunos_e_notas()