from flask import Flask, render_template, request, redirect
from aluno_service import AlunoService
from professor_service import ProfessorService
from curso_service import CursoService

app = Flask(__name__)
professor_service = ProfessorService()
aluno_service = AlunoService()
curso_service = CursoService()

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






#sempre deixar esse código por último nesse arquivo
# ele é responsável por roda a app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
