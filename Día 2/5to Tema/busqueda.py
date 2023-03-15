dias = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
buscarDia = input('Ingrese día: ')
if buscarDia not in dias:
    print('404 - Calendario not found')
else:
    print('El día existe')