# criar as rotas do site
from flask import render_template, url_for
from fakepinterest import app, database, bcrypt
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta
from fakepinterest.models import Usuario, Foto


@app.route("/", methods=["GET", "POST"])
def homepage():
   form_login = FormLogin()
   return render_template('index.html', form=form_login)


@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
   form_criarconta = FormCriarConta()
   if form_criarconta.validate_on_submit():
      senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
      usuario = Usuario(username=form_criarconta.username.data, 
                     senha=senha, 
                     email=form_criarconta.email.data)
      database.session.add(usuario)
      database.session.commit()
     
   return render_template("criarconta.html", form=form_criarconta)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
   return render_template("perfil.html", usuario=usuario)