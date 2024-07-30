from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dicionario = {'titulo':'Página principal', 'encabezado':'Bienvenido a la página web'}
    return render_template('index.html', datos=dicionario)


# Redirección de rutas
@app.route('/redirecciona')
@app.route('/redirecciona/<string:sitio>')
def redirecciona(sitio=None):
    if sitio is not None:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('acercade'))
    
@app.route('/acercade')
def acercade():
    return render_template('acercade.html')

# Ruta con parametros.
@app.route('/saludame') 
@app.route('/saludame/<string:nombre>') 
@app.route('/saludame/<string:nombre>/<int:edad>')
def saliudame(nombre='Javier', edad=None):
    if edad != None:
        return "Hola {} tienes {} años".format(nombre, edad)
    else:
        return f"""
                <h1>Hola, </h1>
                <h3>{nombre} </h3>
                """
@app.route('/suma/<int:numero1>/<int:numero2>')
def suma(numero1, numero2):
    suma = numero1 + numero2
    return f"La suma es igual a {suma}"

if __name__ == '__main__':
    app.run(debug=True)