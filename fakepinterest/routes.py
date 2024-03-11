# criar as rotas do site
from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest import FormLogin, FormCriarConta


@app.route("/", methods=["GET", "POST"])
def homepage():
   formLogin = FormLogin()
   return render_template('index.html', form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
   formcriarconta = FormCriarConta()
   return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
   return render_template("perfil.html", usuario=usuario)