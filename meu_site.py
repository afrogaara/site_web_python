from flask import Flask, request 

web = Flask(__name__)

@web.route("/")
def homepage():
	return "Bem vindo ao meu primeiro site"

if __name__== "__main__":
	web.run(debug=True)
