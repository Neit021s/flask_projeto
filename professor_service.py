# professor_service.py

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
        self.adicionar("Maria Silva", "123.456.789-09", "Informática")
        self.adicionar("João Pereira", "123.436.789-09", "Matemática")
        self.adicionar("Ana Costa", "123.454.789-09", "Gastronomia")
        # ---------
        # ----------------------------------------
        

    def adicionar (self, nome, cpf, disciplina):
        self._validar_dados(nome, cpf, disciplina)
        id = self.proximo_id
        professor = Professor(id, nome, cpf, disciplina)
        self.lista.append(professor)
        self.proximo_id += 1

    def listar(self):
        return self.lista
    
    def buscar_por_id(self, id):
        for professor in self.lista: # percorre todos os professores da lista
            if professor.id == id:   # verifica se o ID bate com o que foi passado
                return professor     # encontrou → retorna o professor
        return None 
    
    def atualizar(self, id, nome, cpf, disciplina):
        professor = self.buscar_por_id(id)
        if professor:
            professor.nome = nome
            professor.cpf = cpf
            professor.disciplina = disciplina
        
    def remover(self, id):
        for professor in self.lista:
            if professor.id == id:
                self.lista.remove(professor)
                break 

    def _validar_dados(self, nome, cpf, disciplina, id=None):
        if not nome or not cpf or not disciplina:
            raise Exception("Nome, cpf e discilina são obrigatórios")


        for professor in self.lista:
            if professor.cpf == cpf:
                # id is None -> referente ao método adicionar
                # aluno.id != id -> desconsidera se aluno for o mesmo que está sendo alterado
                if id is None or professor.id != id:
                    raise Exception("Cpf já existe")



