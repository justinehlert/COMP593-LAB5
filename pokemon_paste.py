""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage:
  python pokemon_paste.py poke_name

Parameters:
  poke_name = Pokemon name
"""
import sys
from sys import argv
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(poke_name)
    if poke_info is not None:
        paste_title, paste_body = get_paste_data(poke_info)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body)
        print(paste_url)

def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
    # TODO: Function body
    try:
        pokemonName = argv[1]
    except IndexError:
        print("Error: Please provide a pokemon name")
        quit()
    return pokemonName

def get_paste_data(pokemon_info):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.

    Args:
        pokemon_info (dict): Dictionary of Pokemon information

    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    #Build the paste title
    #Gets pokemon name from dictionary
    pasteTitle = f'{pokemon_info['forms'][0]['name']}'
    #Capitilize and finalize
    pasteTitle = f'{pasteTitle.capitalize()}\'s Abilities'
    #Build the paste body text
    #Grab the ability names by iterating through the abilities and storing in a list
    abilityNames = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    #Joining together the list items in an empty string, formatted as -{item}\n
    bodyText = ''.join(f'-{item}\n' for item in abilityNames)
    return (pasteTitle, bodyText)

if __name__ == '__main__':
    main()