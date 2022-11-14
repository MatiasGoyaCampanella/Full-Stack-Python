import json
import hashlib


def hashear_contrasena(contrasena):
    return hashlib.sha256(str(contrasena).encode('utf8')).hexdigest()


def validar_contrasena(contrasena, contrasena_hash):
    # Si la contraseña ingresada es igual a la almacenada en el archivo devuelve True
    return hashear_contrasena(contrasena) == contrasena_hash


def validar_usuario(usuario, contrasena):
    """
    Valida que el usuario y la contraseña sean correctos

    :param usuario: nombre de usuario
    :param contrasena: contraseña
    :return: True si el usuario y la contraseña son correctos, False en caso contrario    
    """
    # Si el usuario y la contraseña ingresados son iguales a los almacenados en el archivo devuelve True
    with open('app/files/usuarios.json', 'r') as archivo:
        lista_usuarios = json.load(archivo)  # carga todos los usuarios
        if usuario in lista_usuarios:  # si el usuario existe
            return validar_contrasena(contrasena, lista_usuarios[usuario])
        else:
            return False


def get_contacto():
    """Devuelve una lista de diccionarios con los datos de los empleados

    :return: lista de diccionarios con los datos de los empleados
    """
    with open('app/files/contacto.json', 'r') as archivo:
        lista_contacto = json.load(archivo)  # carga todos los usuarios
    return lista_contacto


def get_contacto_por_id(id):
    """Devuelve un diccionario con los datos del contacto con el id indicado
    Si el emplado no existe devuelve None

    :param id: id del empleado
    :return: diccionario con los datos del empleado
    """
    with open('app/files/contacto.json', 'r') as archivo:
        lista_contacto = json.load(archivo)  # carga todos los usuarios
    for empleado in lista_contacto:
        if empleado['id'] == id:
            return empleado
    return None


def agregar_contacto(datos_nuevos):
    """
    Guarda los datos de un nuevo empleado en el archivo de contacto
    """
    with open('app/files/contacto.json', 'r') as archivo:
        lista_contacto = json.load(archivo)  # carga todos los usuarios
    # Obtener el último id, si no hay ningún empleado, el id es 1
    if not lista_contacto:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_contacto, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_contacto.append(datos_nuevos)
    with open('app/files/contacto.json', 'w') as archivo:
        json.dump(lista_contacto, archivo, indent=4)


def eliminar_contacto(id):

    id = int(id)
    with open('app/files/contacto.json', 'r') as archivo:
        lista_contacto = json.load(archivo)  # carga todos los usuarios
    # Crea una lista con los empleados que no tengan el id indicado
    lista_contacto = [p for p in lista_contacto if p['id'] != id]
    with open('app/files/contacto.json', 'w') as archivo:
        json.dump(lista_contacto, archivo, indent=4)

