def favourite_bond(birth_year):
    
    # Define the periods when each actor played James Bond
    bond_actors = {
        "Roger Moore": (1973, 1986),
        "Timothy Dalton": (1987, 1994),
        "Pierce Brosnan": (1995, 2005),
        "Daniel Craig": (2006, 2021)
    }
    
    # Determine the year the person turns 18
    year_turn_18 = birth_year + 18
    
    # Find the actor who played Bond when the person turned 18
    for actor, (start_year, end_year) in bond_actors.items():
        if start_year <= year_turn_18 <= end_year:
            return f"Your favorite James Bond may be {actor}"
    
    return "No Bond actor found for the given birth year."

# Example function call
birth_year = 1998 #Input position
print(favourite_bond(birth_year))  # Output: Your favorite James Bond may be Daniel Craig