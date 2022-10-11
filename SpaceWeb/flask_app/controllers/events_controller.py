from flask import render_template, redirect, session, request, flash
from flask_app import app

# Importación del modelo
from flask_app.models.users import User
from flask_app.models.events import Event


@app.route('/new/event')
def new_event():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = {
        'id': session['user_id']
    }
    user = User.get_by_id(formulario)
    
    
    return render_template("new_event.html", user = user)

@app.route('/create/event', methods=['POST'])
def create_event():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesión
        return redirect('/')

    if not Event.valida_event(request.form): #llama a la función de valida_event enviándole el formulario, comprueba que sea valido 
        return redirect('/new/event')

    Event.save(request.form)

    return redirect('/events')

@app.route("/events")
def events():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = {
        'id': session['user_id']
    }
    user = User.get_by_id(formulario)
    events = Event.get_all()
    return render_template("events.html",user = user, events = events)

@app.route('/edit/event/<int:id>') #a través de la URL recibimos el ID de la receta
def edit_event(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    #La instancia del evento que queremos editar
    formulario_event = {"id": id}
    event = Event.get_by_id(formulario_event)

    return render_template('edit_event.html', user=user, event=event)

@app.route('/update/event', methods=['POST'])
def update_event():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    
    if not Event.valida_event(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/edit/event/'+request.form['id'])
    
    Event.update(request.form)
    return redirect('/events')

@app.route('/view/event/<int:id>') #A través de la URL recibimos el ID de la receta
def view_event(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión


    formulario_event = { "id": id }
    #llamar a una función y debo de recibir el evento
    event = Event.get_by_id(formulario_event)

    return render_template('view_event.html', user=user, event=event)

@app.route('/delete/event/<int:id>')
def delete_event(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    Event.delete(formulario)

    return redirect('/events')
