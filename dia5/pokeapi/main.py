from lib_pokeapi import PokeAPI

if __name__ == '__main__':
    pokeapi = PokeAPI()
    limit = int(input('Numero de pokemons a obtener : '))
    pokemons = pokeapi.get_pokemons(limit)
    for pokemon in pokemons['results']:
        print(f"Nombre : {pokemon['name']}")
        print(f"URL : {pokemon['url']}")
        pokemon_detail = pokeapi.get_pokemon_detail(pokemon['url'])
        print(f"Height : {pokemon_detail['height']}")
        print(f"Weight : {pokemon_detail['weight']}")
        print(f"Base Exp : {pokemon_detail['base_experience']}")
        print("="*50)
        
    respuesta = input('Desea guardar los pokemons en la base de datos? (s/n) : ')
    if respuesta.lower() == 's':
        pokeapi.insert_pokemon_to_db(pokemons['results'])
        print(f"Se han guardado {len(pokemons['results'])} pokemons en la base de datos")