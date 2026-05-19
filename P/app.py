from flask import Flask, render_template, request
import utils
import json
import os

app = Flask(__name__)


if os.path.exists("dados.json"):

    with open("dados.json", "r", encoding="utf-8") as arquivo:

        a = json.load(arquivo)

else:

    a = []

def salvar_dados():

    with open("dados.json", "w", encoding="utf-8") as arquivo:

        json.dump(
            a,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

@app.route("/")
def menu():

    return render_template("index.html")

@app.route("/criar")
def criar():

    return render_template("criar.html")

@app.route("/ler")
def ler():

    return render_template(
        "ler.html",
        tarefas=a
    )

@app.route("/atualizar")
def atualizar():

    return render_template(
        "atualizar.html",
        tarefas=a
    )

@app.route("/deletar")
def deletar():

    return render_template(
        "deletar.html",
        tarefas=a
    )

@app.route("/salvar", methods=["POST"])
def salvar():

    materia = request.form["materia"]
    nome = request.form["nome"]
    nota = request.form["nota"]
    prazo = request.form["prazo"]

    utils.criar_web(
        a,
        materia,
        nome,
        nota,
        prazo
    )

    salvar_dados()

    return render_template("index.html")

@app.route("/remover", methods=["POST"])
def remover():

    id_tarefa = int(request.form["id"])

    for tarefa in a:

        if tarefa["id"] == id_tarefa:

            a.remove(tarefa)
            break

    salvar_dados()

    return render_template("index.html")

@app.route("/editar", methods=["POST"])
def editar():

    id_tarefa = int(request.form["id"])

    materia = request.form["materia"]
    nome = request.form["nome"]
    nota = request.form["nota"]
    prazo = request.form["prazo"]

    for tarefa in a:

        if tarefa["id"] == id_tarefa:

            tarefa["matéria"] = materia
            tarefa["nome"] = nome
            tarefa["nota"] = nota
            tarefa["prazo"] = prazo

            break

    salvar_dados()

    return render_template("index.html")

app.run(debug=True)