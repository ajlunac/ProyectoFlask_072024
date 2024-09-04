from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    print("Antes de la petición")
@app.after_request
def before_request(response):
    print("Después de la petición")
    return response
@app.route('/')
def index():
    print("Accediendo al index o página principal")
    dicionario = {'titulo':'Página principal', 
                  'encabezado':'Bienvenido a la página web'}
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
    dicionario = {'titulo':'Acerca de', 'encabezado':'Acerca de está página'}
    return render_template('acercade.html', datos=dicionario)

@app.route('/condicionybucle')
def condicionybucle():
    datos = {
        'edad' : 24,
        'nombres' : ['Jose', 'Mar', 'Lucia', 'Eva'],
    }
    return render_template('condicionybucle.html', datos = datos)

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

def pagina_no_encontrada(error):
    return render_template('/errors/404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)