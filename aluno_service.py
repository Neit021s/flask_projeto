# aluno_service.py

class Aluno:
    def __init__(self, id, matricula, nome):
        self.id = id
        self.matricula = matricula
        self.nome = nome


class AlunoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

        # ---- Dados iniciais (comente se não quiser) ----
        self.adicionar("2023001","Maria Silva")
        self.adicionar("2023002","João Pereira")
        self.adicionar("2023003","Ana Costa")
        # -------------------------------------------------

    def adicionar(self, nome, matricula):
        if not nome.strip() or not matricula.strip():
            raise Exception("Nome e matrícula são obrigatórios")           
        for aluno in self.lista:
            if aluno.matricula == matricula:
                raise Exception("Matrícula já existe")
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
            aluno.matricula = matricula
            aluno.nome = nome

    def remover(self, id):
        for aluno in self.lista:
            if aluno.id == id:
                self.lista.remove(aluno)
                break 

