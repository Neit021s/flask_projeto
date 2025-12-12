# aluno_service.py

class Professor:
    def __init__(self, id, nome, cpf, disciplina):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina
        self.cpf = cpf


class ProfessorService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

        # ---- Dados iniciais (comente se não quiser) ----
        self.adicionar("Maria Silva", "123.456.789-09.", "Informática")
        self.adicionar("João Pereir", "123.456.789-09.", "Matemática")
        self.adicionar("Ana Cost", "123.456.789-09.", "Gastronomia")
        # -------------------------------------------------

    def adicionar(self, nome, cpf, disciplina):
        id = self.proximo_id
        professor = Professor(id, nome, disciplina, cpf)
        self.lista.append(professor)
        self.proximo_id += 1

    def listar(self):
        return self.lista
