import re

def validar_celular(numero):
    telefono_valido = re.match(r'^3\d{2}[-\s]?\d{3}[-\s]?\d{4}$', numero) #? Significa Opcional
    return bool(telefono_valido)


#print(validar_celular('3006771112'))
#print(validar_celular('302 323 8831'))
#print(validar_celular('300'))
#print(validar_celular('300-56666-666'))
#print(validar_celular('300-6666-777'))
#print(validar_celular('300-677-1112'))


def validar_fecha(fecha):
    fecha_valida = re.match(r'^(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](19|20)\d{2}$', fecha)
    return bool(fecha_valida)
#print(validar_fecha('30/05/2026'))

'''''''''
def validar_password(password):
    if not re.match(r'^.{8.}',password):
        return 'Debe tener minimo 8 caracteres'
    if not re.match(r'.*[A-Z].*',password):
        return 'Debe tener minimo una letra Mayuscula'
    if not re.match(r'.*[a-z].*',password):
        return 'Debe tener minimo una letra minuscula'
    if not re.match(r'.*[0-9].*',password):
        return 'Debe tener minimo un numero'
'''''''''
        
def validar_password(password):
    if len(password)<8:
        return False, 'Minimo 8 caracteres'
    if not re.search(r'[A-Z]',password):
        return False, 'Falta una Mayuscula'
    if not re.search(r'[a-z]',password):
        return False, 'Falta una Mayuscula'
    if not re.search(r'[#%&$]',password):
        return False, 'Falta una Mayuscula'
    
print(validar_password('128'))
print(validar_password('HolA1234567'))