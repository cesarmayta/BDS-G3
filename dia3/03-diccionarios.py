capitales = {
        'Perú':'Lima',
        'Ecuador':'Quito',
        'Chile':'Santiago',
        'Colombia':'Bogota'
    }

#print(capitales['Chile'])
pais = input('Ingrese el pais :')
if pais in capitales:
    capital = capitales.get(pais)
    print(f'la capital de {pais} es {capital}')
    eliminar_capital = input('¿Desea eliminar la capital?(si,no)')
    if eliminar_capital == 'si':
        capitales.pop(pais,'NO EXISTE')
        print(capitales)
else:
    print(f'No se encontro la capital de {pais}')
    nueva_capital = input(f'Ingrese capital de {pais} :')
    capitales.update({pais:nueva_capital})
    print(capitales)