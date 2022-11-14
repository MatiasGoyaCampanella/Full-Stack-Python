from flask import render_template, redirect, url_for, session, flash, request
from app.auth import login_required
from app import app
from app.forms import LoginForm, IngresarContactoForm
from app.handlers import eliminar_contacto, get_contacto_por_id, validar_usuario, get_contacto, agregar_contacto


@app.route('/')  # http://localhost:5000/
@app.route('/index')
@login_required
def index():
    if request.method == 'GET' and request.args.get('borrar'):
        eliminar_contacto(request.args.get('borrar'))
        flash('Se ha eliminado el contacto', 'success')
    return render_template('index.html', titulo="Inicio", contacto=get_contacto())


@app.route('/ingresar-contacto', methods=['GET', 'POST'])
@login_required
def ingresar_contacto():
    contacto_form = IngresarContactoForm()
    if contacto_form.cancelar.data:  # si se apretó el boton cancelar, contacto_form.cancelar.data será True
        return redirect(url_for('index'))
    if contacto_form.validate_on_submit():
        datos_nuevos = { 'nombre': contacto_form.nombre.data, 'apellido': contacto_form.apellido.data, 
                         'telefono': contacto_form.telefono.data,  'organismo': contacto_form.organismo.data, 'funcion': contacto_form.funcion.data }
        agregar_contacto(datos_nuevos)
        flash('Se ha agregado un nuevo empleado', 'success')
        return redirect(url_for('index'))
    return render_template('ingresar_contacto.html', titulo="Contacto", contacto_form=contacto_form)


@app.route('/editar-contacto/<int:id_empleado>', methods=['GET', 'POST'])
@login_required
def editar_contacto(id_empleado):
    contacto_form = IngresarContactoForm(data=get_contacto_por_id(id_empleado))
    if contacto_form.cancelar.data:  # si se apretó el boton cancelar, contacto_form.cancelar.data será True
        return redirect(url_for('index'))
    if contacto_form.validate_on_submit():
        datos_nuevos = { 'nombre': contacto_form.nombre.data, 'apellido': contacto_form.apellido.data, 
                         'telefono': contacto_form.telefono.data, 'organismo': contacto_form.organismo.data, 'funcion': contacto_form.funcion.data }
        eliminar_contacto(id_empleado)  # Eliminamos el contacto antiguo
        agregar_contacto(datos_nuevos)  # Agregamos el nuevo contacto
        flash('Se ha editado el contacto exitosamente', 'success')
        return redirect(url_for('index'))
    return render_template('editar_contacto.html', titulo="Contacto", contacto_form=contacto_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        usuario = login_form.usuario.data
        password = login_form.password.data
        if validar_usuario(usuario, password):
            session['usuario'] = usuario
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', titulo="Login", login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

