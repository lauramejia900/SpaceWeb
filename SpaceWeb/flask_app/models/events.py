from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash


class Event:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.attendees = data['attendees']
        self.date = data['date']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #LEFT JOIN
        self.first_name = data['first_name']
        

    @staticmethod
    def valida_event(formulario):
        es_valido = True

        if len(formulario['name']) < 3:
            flash('El nombre del evento debe tener al menos 3 caracteres', 'evento')
            es_valido = False

        if len(formulario['location']) < 3:
            flash('La descripción del evento debe tener al menos 3 caracteres', 'evento')
            es_valido = False
        
        if formulario['date'] == "":
            flash('Ingrese una fecha', 'evento')
            es_valido = False

        return es_valido


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO events (name, location, attendees, date, time, user_id) VALUES (%(name)s, %(location)s, %(attendees)s, %(date)s, %(time)s, %(user_id)s) "
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT events.*, first_name FROM events  LEFT JOIN users ON users.id = events.user_id;"
        results = connectToMySQL('spaceweb').query_db(query) #Lista de diccionarios 
        events = []
        for event in results:
            #evento = diccionario
            events.append(cls(event)) #1.- cls(evento) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de recetas

        return events

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT events.*, first_name  FROM events LEFT JOIN users ON users.id = events.user_id WHERE events.id = %(id)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario) #Lista de diccionarios
        event = cls(result[0])
        return event

    @classmethod
    def update(cls, formulario):
        query = "UPDATE events SET name=%(name)s, location=%(location)s, attendees=%(attendees)s, date=%(date)s, time=%(time)s WHERE id = %(id)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result
    
    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de evento a borrar
        query = "DELETE FROM events WHERE id = %(id)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result