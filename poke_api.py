'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
import json

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    pokemon_name = pokemon_name.replace(" ","").lower()
    # TODO: Build a clean URL and use it to send a GET request

    
    try:
        resp = requests.get(POKE_API_URL)
        resp.raise_for_status()
        print(f"Getting pokemon information for {pokemon_name}... success")
    #If the GET request failed, print the error reason and return None
    except requests.exceptions.RequestException as err:
        print(f'Getting pokemon information for {pokemon_name}... failed\n{err}')
        return None
    
    fullURL = POKE_API_URL + pokemon_name
    r = requests.get(fullURL)
    
    #If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    #Not sure why but it says this r.json is a dict obj so i guess it works? I guess the response method
    #returns the json response as a dict
    return r.json()  

if __name__ == '__main__':
    main()