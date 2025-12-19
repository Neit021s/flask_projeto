# aluno_service.py

class Disciplina:
    def __init__(self, id, nome, carga_horaria):
        self.id = id
        self.nome = nome
        self.carga_horaria = carga_horaria


class DisciplinaService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

        # ---- Dados iniciais (comente se não quiser) ----
        self.adicionar("Enfermagem", "40")
        self.adicionar("Teologia", "32")
        self.adicionar("Filosofia", "10")
        # -------------------------------------------------

    def adicionar(self, nome, carga_horaria):
        id = self.proximo_id
        disciplinas = Disciplina(id, nome, carga_horaria)
        self.lista.append(disciplinas)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for disciplinas in self.lista: # percorre todos as disciplinas da lista
            if disciplinas.id == id:   # verifica se o ID bate com o que foi passado
                return disciplinas     # encontrou → retorna o disciplinas
        return None 
    
    def atualizar(id, nome, carga_horaria):
        disciplinas = self.buscar_por_id(id)
        if disciplinas:
            disciplinas.nome = nome
            disciplinas.carga_horaria = carga_horaria

    def remover(self, id):
        for disciplinas in self.lista:
            if disciplinas.id == id:
                self.lista.remove(disciplinas)
                break 


