from flask import Flask, render_template
import platform, os

app = Flask(__name__)
mensaje=[]


@app.route("/")
def index():
    return render_template('index.html',mensaje=['System Check',''])

@app.route("/<parametro>")
def mostrar(parametro):
    if parametro=="so":
        return render_template('index.html', mensaje=['Sistema Operativo', platform.system()])
    elif parametro=="plataforma":
        return render_template('index.html', mensaje=['Procesador', platform.processor()])
    elif parametro=="arquitectura":
        return render_template('index.html', mensaje=['Arquitectura', platform.architecture()])
    elif parametro=="version":
        return render_template('index.html', mensaje=['Versión de Python', platform.python_version()])
    else:
        return render_template('index.html',mensaje=['Error','Parámetro no válido, haz clic en el menú superior'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
