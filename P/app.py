from flask import Flask, render_template, request
import utils

app = Flask(__name__)

a = []

@app.route("/")
def menu():
    return render_template("index.html")

@app.route("/criar")
def criar():
    return render_template("criar.html")

@app.route("/ler")
def ler():
    return render_template("Ler.html")

@app.route("/atualizar")
def atualizar():
    return render_template("Atualizar.html")

@app.route("/deletar")
def deletar():
    return render_template("Deletar.html")

@app.route("/salvar", methods=["POST"])
def salvar():

    materia = request.form["materia"]
    nome = request.form["nome"]
    nota = request.form["nota"]
    prazo = request.form["prazo"]

    utils.criar_web(a, materia, nome, nota, prazo)

    return "Salvo com sucesso"

app.run(debug=True)