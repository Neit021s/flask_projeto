# aluno_service.py

class Aluno:
    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula


class AlunoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

        # ---- Dados iniciais (comente se não quiser) ----
        self.adicionar("Maria Silva", "2023001")
        self.adicionar("João Pereira", "2023002")
        self.adicionar("Ana Costa", "2023003")
        # -------------------------------------------------

    def adicionar(self, nome, matricula):
        id = self.proximo_id
        aluno = Aluno(id, nome, matricula)
        self.lista.append(aluno)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for aluno in self.lista: # percorre todos os alunos da lista
            if aluno.id == id:   # verifica se o ID bate com o que foi passado
                return aluno     # encontrou → retorna o aluno
        return None 

    def atualizar(self, id, nome, matricula):
        aluno = self.buscar_por_id(id)
        if aluno:
            aluno.nome = nome
            aluno.matricula = matricula

    def remover(self, id):
        for aluno in self.lista:
            if aluno.id == id:
                self.lista.remove(aluno)
                break 

