from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

web = Flask(__name__)
db = SQLAlchemy(web)

web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite3'

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	content = db.Column(db.String())
	author = db.Column(db.String())


@web.route("/")
def homepage():
	username = Post.query.all()
	return render_template("homepage.html", username=username)

@web.route("/post/<id>/delete")
def delete_post(id):
	try:
		post = Post.query.get(id)
		db.session.delete(post)
		db.session.commit()
	except Exception as error:
		print("Error", error)
	return redirect(url_for("homepage"))


@web.route("/post/add", methods=["POST"])
def post_add():
        try:
                form = request.form
                post = Post(title=form["title"], content=form["content"], author=form["author"])
                db.session.add(post)
                db.session.commit()
        except:
                print("Error")
        return redirect(url_for("homepage"))







@web.route("/contatos")
def contatos():
	return render_template("contatos.html")

@web.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
	return render_template("usuarios.html", user=nome_usuario)


db.create_all()
if __name__ == "__main__":
	web.run(debug=True)
