# site_web_python
Aprendendo a desenvolver sites em python 
#não usar render_template_string é passivo da f-string rodar no server-side caracterizando vulnerabilidade injection 
Motivos para usar sqlalchemy:
  1) -->sqlalchemy torna as requisições mais simples e seguras. 
#from flask import Flask, request, render_template
#flask_sqlalchemy, SQLAlchemy #Banco de dados  

#criar 
--->web = Flask(__name__)
--->db = SQLAlchemy(web)

  #db = SQLAlchemy(web)#chama banco de dados 
  #web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///test.sqlite3' #configurando banco de dados 
  
@web.route("/") --> cada route é uma pagina. "/" é a homepage. "pagina inicial"
def funcao(): ---> cada route tem uma função seguido de return render_template
  return render_template

#render_template é um método que vai aceitar 2 parametros. 
  ----> ("index.html") --> o render_template procurará por uma pasta chamada template.
  ----> Dentro da templatealguma pasta chamada index.html 
#Estrutura Html
<!DOCTYPE html>
<html lang="pt-br">
 	<head>
 		<meta charset="UTF-8">
 		<title>Título da página</title>
 	</head>
 	<body>
 		
 	</body>
</html>

