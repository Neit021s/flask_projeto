# disciplina_service.py

class Disciplina:
    def __init__(self, id, nome, carga_horaria, ementa):
        self.id = id
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.ementa = ementa


class DisciplinaService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

        # ---- Dados iniciais (comente se não quiser) ----
        self.adicionar("Biologia", "40","Introdução a Anatomia")
        self.adicionar("Teologia", "32", "Aprofundamento em Sistemática")
        self.adicionar("Filosofia", "10", "Ética, Lógica e Política")
        # -------------------------------------------------

    def adicionar(self, nome, carga_horaria, ementa):
        if not nome.strip() or not carga_horaria.strip():
            raise Exception("Nome e carga horára são campos obrigatórios")
        for disciplina in self.lista:
            if disciplina.nome == nome:
                raise Exception("Essa disciplina já existe")
        id = self.proximo_id
        disciplina = Disciplina(id, nome, carga_horaria, ementa)
        self.lista.append(disciplina)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for disciplina in self.lista: # percorre todos as disciplinas da lista
            if disciplina.id == id:   # verifica se o ID bate com o que foi passado
                return disciplina     # encontrou → retorna o disciplinas
        return None 
    
    def atualizar(self, id, nome, carga_horaria, ementa):
        disciplina = self.buscar_por_id(id)
        if disciplina:
            disciplina.nome = nome
            disciplina.carga_horaria = carga_horaria
            disciplina.ementa = ementa

    def remover(self, id):
        for disciplina in self.lista:
            if disciplina.id == id:
                self.lista.remove(disciplina)
                break 
