from flask import Flask, render_template, request, redirect
from aluno_service import AlunoService
from professor_service import ProfessorService
from curso_service import CursoService
from disciplina_service import DisciplinaService

app = Flask(__name__)
professor_service = ProfessorService()
aluno_service = AlunoService()
curso_service = CursoService()
disciplina_service = DisciplinaService()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route("/aluno")
def listar_aluno():
    lista = aluno_service.listar()
    return render_template("aluno/listar.html", lista=lista)

@app.route("/professor")
def listar_professor():
    lista = professor_service.listar()
    return render_template("professor/listar.html", lista=lista)

@app.route("/curso")
def listar_curso():
    lista = curso_service.listar()
    return render_template("curso/listar.html", lista=lista)

@app.route("/disciplinas")
def listar_disciplinas():
    lista = disciplina_service.listar()
    return render_template("disciplinas/listar.html", lista=lista)

#----------------------------------------------------------------------

@app.route("/aluno/form")
def novo_aluno():
    return render_template("aluno/form.html", aluno=None)

@app.route("/aluno/salvar/", methods=["POST"])
def salvar_aluno():
    matricula = request.form.get("matricula")
    nome = request.form.get("nome")

    # Salva no service
    aluno_service.adicionar(matricula, nome)

    # Redireciona para a lista
    return redirect('/aluno')

@app.route("/curso/form")
def novo_curso():
    return render_template("curso/form.html", curso=None)

@app.route("/curso/salvar/", methods=["POST"])
def salvar_curso():
    nome = request.form.get("nome")
    nivel = request.form.get("nivel")

    # Salva no service
    curso_service.adicionar(nome, nivel)

    # Redireciona para a lista
    return redirect('/aluno')

@app.route("/professor/form")
def novo_professor():
    return render_template("professor/form.html", professor=None)

@app.route("/professor/salvar/", methods=["POST"])
def salvar_professor():
    nome = request.form.get("nome")
    disciplina = request.form.get("disciplina")
    cpf = request.form.get("cpf")

    # Salva no service
    professor_service.adicionar(nome, disciplina, cpf)

    # Redireciona para a lista
    return redirect('/professor')

@app.route("/aluno/editar/<int:id>")
def editar_aluno(id):
    aluno = aluno_service.buscar_por_id(id)
    return render_template("aluno/form.html", aluno=aluno)

@app.route("/aluno/salvar/<int:id>", methods=["POST"])
def atualizar_aluno(id):
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    aluno_service.atualizar(id, nome, matricula)
    return redirect('/aluno')

@app.route("/aluno/remover/<int:id>")
def remover_aluno(id):
    aluno_service.remover(id)
    return redirect('/aluno')
#---------------------------------------------------
@app.route("/curso/editar/<int:id>")
def editar_curso(id):
    curso = curso_service.buscar_por_id(id)
    return render_template("curso/form.html", curso=curso)

@app.route("/curso/salvar/<int:id>", methods=["POST"])
def atualizar_curso(id):
    nome = request.form["nome"]
    nivel = request.form["nivel"]
    curso_service.atualizar(id, nome, nivel)
    return redirect('/curso')

@app.route("/curso/remover/<int:id>")
def remover_curso(id):
    curso_service.remover(id)
    return redirect('/curso')
#---------------------------------------------------
@app.route("/professor/editar/<int:id>")
def editar_professor(id):
    professor = professor_service.buscar_por_id(id)
    return render_template("professor/form.html", professor=professor)

@app.route("/professor/salvar/<int:id>", methods=["POST"])
def atualizar_professor(id):
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    disciplina = request.form["disciplina"]
    professor_service.atualizar(id, nome, cpf, disciplina)
    return redirect('/professor')

@app.route("/professor/remover/<int:id>")
def remover_professor(id):
    professor_service.remover(id)
    return redirect('/professor')

#---------------------------------------------------

@app.route("/disciplinas/form")
def novo_disciplinas():
    return render_template("disciplinas/form.html", disciplinas=None)

@app.route("/disciplinas/salvar/", methods=["POST"])
def salvar_disciplinas():
    nome = request.form.get("nome")
    carga_horaria = request.form.get("carga_horaria")

    # Salva no service
    disciplina_service.adicionar(nome, carga_horaria)

    # Redireciona para a lista
    return redirect('/disciplinas')

@app.route("/disciplinas/editar/<int:id>")
def editar_disciplinas(id):
    disciplinas = disciplina_service.buscar_por_id(id)
    return render_template("disciplinas/form.html", disciplinas=disciplinas)

@app.route("/disciplinas/salvar/<int:id>", methods=["POST"])
def atualizar_disciplinas(id):
    nome = request.form["nome"]
    carga_horaria = request.form["carga_horaria"]
    disciplina_service.atualizar(id, nome, carga_horaria)
    return redirect('/disciplinas')

@app.route("/disciplinas/remover/<int:id>")
def remover_disciplinas(id):
    disciplina_service.remover(id)
    return redirect('/disciplinas')












#sempre deixar esse código por último nesse arquivo
# ele é responsável por roda a app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
