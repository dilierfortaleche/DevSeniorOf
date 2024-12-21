conceptosProgramacion = {
    'POO': 'Programacion Orientada a Objetos',
    'IDE': 'Entorno de Desarrollo Integrado',
    'DBMS': 'Sistema de Gestion de Base de Datos'
}

print(conceptosProgramacion)
print(len(conceptosProgramacion))

print(conceptosProgramacion['IDE'])
print(conceptosProgramacion.get('POO'))

conceptosProgramacion['DBMS'] = 'Database Management System'

#llamar id(key) y valor(value)
for key , value in conceptosProgramacion.items():
    print(key, value)

