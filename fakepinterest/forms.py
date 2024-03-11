# formulario do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
   email = StringField("E-mail", validators=[DataRequired(), Email()])
   senha = PasswordField("Senha", validators=[DataRequired()])
   botao_confirmacao = SubmitField("Fazer Login")
   
  
class FormCriarConta(FlaskForm):
   email = StringField("E-mail", validators=[DataRequired(), Email()])
   username = StringField("Nome de Usuario", validators=[Datarequired()])
   senha = PasswordField("Senha", validators=[DataRequeired(), Length(6, 20)])
   confirmacao_senha = PasswordField("Conformacao de Senha", validators=[DataRequired(), EqualTo("senha")])
   botao_confirmacao = SubmitField("Criar Conta")

   def validate_email(self, email):
      usuario = Usuario.query.filter_by(email=email.data).first()
      if usuario:
         return ValidationError("Email ja cadastrado, utilize outro para realizar o seu login.")