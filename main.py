import re
from flask import Flask, render_template, request, jsonify, redirect,url_for
from Models import db, Usuarios
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/santi/Desktop/proyecto/database/usuario.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def pantallaPrincipal():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return render_template('pantallaPrincipal.html', nombre=nombre)
    else:
        return render_template('pantallaPrincipal.html')

@app.route('/clientes/alta', methods=['GET', 'POST'])
def altaUsuario():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']

        # Validaciones
        if not re.match(r'^[a-zA-Z]+$', nombre):
            return redirect(url_for('altaUsuario', error_nombre="El nombre no es válido. Solo se permiten letras."))

        if not re.match(r'^[a-zA-Z]+$', apellido):
            return redirect(url_for('altaUsuario', error_apellido="El apellido no es válido. Solo se permiten letras."))

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return redirect(url_for('altaUsuario', error_email="El email no es válido. Debe cumplir con el formato usuario@dominio."))

        if not re.match(r'^[\d\-]+$', telefono):
            return redirect(url_for('altaUsuario', error_telefono="El teléfono no es válido. Solo se permiten números y guiones."))

        # Creación del nuevo usuario
        nuevo_usuario = Usuarios(dni=dni, nombre=nombre, apellido=apellido, email=email, telefono=telefono)
        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect(url_for('altaUsuario', success="Usuario agregado exitosamente!"))

    else:
        error_nombre = request.args.get('error_nombre')
        error_apellido = request.args.get('error_apellido')
        error_email = request.args.get('error_email')
        error_telefono = request.args.get('error_telefono')
        success = request.args.get('success')

        return render_template('altaUsuario.html', error_nombre=error_nombre, error_apellido=error_apellido,
                               error_email=error_email, error_telefono=error_telefono, success=success)

    

@app.route('/clientes/listar', methods=['GET'])
def listarUsuarios():
    try:

        nombre = request.args.get('nombre')
        apellido = request.args.get('apellido')
        dni = request.args.get('dni')

        query = Usuarios.query

        if nombre:
            query = query.filter(Usuarios.nombre.ilike(f'%{nombre}%'))
        if apellido:
            query = query.filter(Usuarios.apellido.ilike(f'%{apellido}%'))
        if dni:
            query = query.filter(Usuarios.dni == dni)

        usuarios = query.all()

        return render_template('listarUsuarios.html', usuarios=usuarios)
    except Exception as e:
        exception(f"[SERVER]: Error -> {e}")
        return jsonify({"msg": "Ha ocurrido un error"}), 400


if __name__ == '__main__':
    app.run(debug=True)
