# curso_service.py

class Curso:
    def __init__(self, id, nome, nivel):
        self.id = id
        self.nome = nome
        self.nivel = nivel


class CursoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

        # ---- Dados iniciais (comente se não quiser) ----
        self.adicionar("Informatica", "Medio")
        self.adicionar("Engenharia", "Superior")
        self.adicionar("Enfermagem", "Superior")
        # -------------------------------------------------

    def adicionar(self, nome, nivel):
        id = self.proximo_id
        curso = Curso(id, nome, nivel)
        self.lista.append(curso)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for curso in self.lista: # percorre todos os cursos da lista
            if curso.id == id:   # verifica se o ID bate com o que foi passado
                return curso     # encontrou → retorna o curso
        return None 

    def atualizar(self, id, nome, nivel):
        curso = self.buscar_por_id(id)
        if curso:
            curso.nome = nome
            curso.nivel = nivel

    def remover(self, id):
        for curso in self.lista:
            if curso.id == id:
                self.lista.remove(curso)
                break 

