"""
Author
------
Pedro Jerónimo
GitHub: https://github.com/pedrojeronim0

Description
-----------
This module allows playing Go

Functions
---------
create_intersection(column,row)
    Return an intersection
get_col(intersection)
    Return the column of an intersection
get_row(intersection)
    Return the row of an intersection
is_intersection(arg)
    Check if the argument is an intersection ADT
intersections_equal(intersection1,intersection2)
    Check if the arguments are intersections and are equal
intersections_repeated(intersections)
    Check if there are repeated intersections
intersection_to_str(intersection)
    Return the string representation of an intersection
str_to_intersection(text)
    Return the intersection represented by the argument
get_adjacent_intersections(intersection,l)
    Return the intersections adjacent to an intersection
sort_intersections(intersections)
    Return intersections sorted in reading order
create_white_stone()
    Return a stone belonging to the white player
create_black_stone()
    Return a stone belonging to the black player
create_neutral_stone()
    Return a neutral stone
is_stone(arg)
    Check if the argument is a stone ADT
is_white_stone(stone)
    Check if a stone belongs to the white player
is_black_stone(stone)
    Check if a stone belongs to the black player
stones_equal(stone1,stone2)
    Check if the arguments are stones and are equal
stone_to_str(stone)
    Return the string representation of a stone
is_player_stone(stone)
    Check if a stone belongs to a player
create_empty_goban(n)
    Return an n x n goban with no occupied intersections
create_goban(n,white_intersections,black_intersections)
    Return an n x n goban with potentially occupied intersections
copy_goban(goban)
    Return a copy of a goban
get_last_intersection(goban)
    Return the last intersection of a goban
get_stone(goban,intersection)
    Return the stone at an intersection
get_chain(goban,intersection)
    Return the intersections of the chain passing through an intersection
place_stone(goban,intersection,stone)
    Place a stone on a goban
remove_stone(goban,intersection)
    Remove a stone from a goban
remove_chain(goban,intersections_tuple)
    Remove stones from intersections of a goban
is_goban(arg)
    Check if the argument is a goban ADT
is_valid_intersection(goban,intersection)
    Check if an intersection is valid within a goban
gobans_equal(goban1,goban2)
    Check if the arguments are gobans and are equal
goban_to_str(goban)
    Return the string representation of a goban
get_intersections(goban,stone)
    Return all intersections of a goban occupied by a given stone
get_territories(goban)
    Return the territories of a goban
get_different_adjacents(goban,intersections)
    Return the different adjacent intersections of intersections
make_move(goban,intersection,stone)
    Place a player's stone on an intersection of a goban, remove the opposing
    player's stones belonging to adjacent chains that have no liberties,
    and return the modified goban
get_player_stones(goban)
    Return the number of intersections occupied by each player's stones
calculate_scores(goban)
    Return each player's score
is_legal_move(goban,intersection,stone,previous_goban)
    Perform a move on a copy of a goban and check if it is legal
player_turn(goban,stone,previous_goban)
    Offer a player the option to pass or place their stone on an intersection
    and return whether the player passed
go(n,white_stones,black_stones)
    Play GO and return whether the white player won
"""

# Intersection
# Constructor
def create_intersection(column,row):
    """
    Return an intersection

    Parameters
    ----------
    column : str
        Column of the intersection to return
    row : int
        Row of the intersection to return

    Returns
    -------
    intersection
        Intersection corresponding to 'column' and 'row'
    
    Raises
    ------
    ValueError:
        If 'column' is not a letter from A to S
        If 'row' is not an integer between 1 and 19, inclusive
    """
    if (
        not isinstance(column,str) or 
        len(column) != 1 or
        not 'A' <= column <= 'S' or
        isinstance(row,bool) or
        not isinstance(row,int) or
        not 1 <= row <= 19
    ):
        raise ValueError("create_intersection: argumentos invalidos")

    return (column,row)


# Selectors
def get_col(intersection):
    """
    Return the column of an intersection

    Parameters
    ----------
    intersection : intersection
        Intersection whose column is to be obtained

    Returns
    -------
    str
        Column of 'intersection' 
    """
    return intersection[0]


def get_row(intersection):
    """
    Return the row of an intersection

    Parameters
    ----------
    intersection : intersection
        Intersection whose row is to be obtained

    Returns
    -------
    int
        Row of 'intersection' 
    """
    return intersection[1]


# Recognizer
def is_intersection(arg):
    """
    Check if the argument is an intersection ADT

    Parameters
    ----------
    arg : universal
        Parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    if (
        not isinstance(arg,tuple) or
        len(arg) != 2 or
        not isinstance(arg[0],str) or 
        len(arg[0]) != 1 or
        not 'A' <= arg[0] <= 'S' or
        isinstance(arg[1],bool) or
        not isinstance(arg[1],int) or
        not 1 <= arg[1] <= 19
    ):
        return False
    
    return True


# Tests
def intersections_equal(intersection1,intersection2):
    """
    Check if the arguments are intersections and are equal

    Parameters
    ----------
    intersection1 : universal
        First parameter to check
    intersection2 : universal
        Second parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    if (
        not is_intersection(intersection1) or
        not is_intersection(intersection2) or
        get_col(intersection1) != get_col(intersection2) or
        get_row(intersection1) != get_row(intersection2)
    ):
        return False

    return True


def intersections_repeated(intersections):
    """
    Check if there are repeated intersections

    Parameters
    ----------
    intersections : tuple
        Intersections to check

    Returns
    -------
    bool
        True if there are repeated intersections, False otherwise
    """
    if intersections == ():
        return False
    
    for intersection in intersections[1:]:
        if intersections_equal(intersection,intersections[0]):
            return True
        
    return intersections_repeated(intersections[1:])


# Transformers
def intersection_to_str(intersection):
    """
    Return the string representation of an intersection

    Parameters
    ----------
    intersection : intersection
        Intersection to represent

    Returns
    -------
    str
        External representation of 'intersection'
    """
    return get_col(intersection) + str(get_row(intersection))


def str_to_intersection(text):
    """
    Return the intersection represented by the argument

    Parameters
    ----------
    text : str
        String representing an intersection

    Returns
    -------
    intersection
        Represented intersection
    """
    return (text[0],int(text[1:]))


# High-Level Functions
def get_adjacent_intersections(intersection,l):
    """
    Return the intersections adjacent to an intersection

    Parameters
    ----------
    intersection : intersection
        Intersection whose adjacent intersections are to be obtained
    l : intersection
        Top-right intersection of the goban to which 'intersection' belongs

    Returns
    -------
    tuple
        Intersections adjacent to 'intersection'
    """
    column = get_col(intersection)
    row = get_row(intersection)
    adjacents = ()

    # Determine the intersection below if it exists
    if row - 1 > 0:
        adjacents += (create_intersection(column,row - 1),)

    # Determine the intersection to the left if it exists
    if chr(ord(column) - 1) >= 'A':
        adjacents += (create_intersection(chr(ord(column) - 1),row),)

    # Determine the intersection to the right if it exists
    if chr(ord(column) + 1) <= get_col(l):
        adjacents += (create_intersection(chr(ord(column) + 1),row),)
    
    # Determine the intersection above if it exists
    if row + 1 <= get_row(l):
        adjacents += (create_intersection(column,row + 1),)

    return adjacents


def sort_intersections(intersections):
    """
    Return intersections sorted in reading order

    Parameters
    ----------
    intersections : tuple
        Intersections to be sorted

    Returns
    -------
    tuple
        Intersections from 'intersections' sorted in reading order
    """
    return tuple(sorted(intersections,key = lambda x: (get_row(x),get_col(x))))


# Stone
# Constructors
def create_white_stone():
    """Return a stone belonging to the white player"""
    return "O"


def create_black_stone():
    """Return a stone belonging to the black player"""
    return "X"


def create_neutral_stone():
    """Return a neutral stone"""
    return "."


# Recognizers
def is_stone(arg):
    """
    Check if the argument is a stone ADT

    Parameters
    ----------
    arg : universal
        Parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    if (
        arg != create_white_stone() and
        arg != create_black_stone() and
        arg != create_neutral_stone()
    ):
        return False
    
    return True


def is_white_stone(stone):
    """
    Check if a stone belongs to the white player

    Parameters
    ----------
    stone : stone
        Parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    return stone == create_white_stone()


def is_black_stone(stone):
    """
    Check if a stone belongs to the black player

    Parameters
    ----------
    stone : stone
        Parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    return stone == create_black_stone()


# Test
def stones_equal(stone1,stone2):
    """
    Check if the arguments are stones and are equal

    Parameters
    ----------
    stone1 : universal
        First parameter to check
    stone2 : universal
        Second parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    if (
        not is_stone(stone1) or 
        not is_stone(stone2) or
        stone1 != stone2
    ):
        return False
    
    return True


# Transformer
def stone_to_str(stone):
    """
    Return the string representation of a stone

    Parameters
    ----------
    stone : stone
        Stone to represent

    Returns
    -------
    str
        External representation of 'stone'
    """
    return stone


# High-Level Functions
def is_player_stone(stone):
    """
    Check if a stone belongs to a player

    Parameters
    ----------
    stone : stone
        Parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    return is_white_stone(stone) or is_black_stone(stone)


# Goban
# Constructors
def create_empty_goban(n):
    """
    Return an n x n goban with no occupied intersections

    Parameters
    ----------
    n : int
        Dimension of the goban

    Returns
    -------
    goban
        n x n goban with no occupied intersections
    
    Raises
    ------
    ValueError:
        If 'n' is not the integer 9, 13, or 19
    """
    if not isinstance(n,int) or (n != 9 and n != 13 and n != 19):
        raise ValueError("create_empty_goban: argumento invalido")
    
    return [n*[create_neutral_stone()] for column in range(n)]


def create_goban(n,white_intersections,black_intersections):
    """
    Return an n x n goban with potentially occupied intersections

    Parameters
    ----------
    n : int
        Dimension of the goban
    white_intersections : tuple
        Intersections to occupy with white stones
    black_intersections : tuple
        Intersections to occupy with black stones

    Returns
    -------
    goban
        n x n goban with potentially occupied intersections
    
    Raises
    ------
    ValueError:
        If 'n' is not the integer 9, 13, or 19
        If 'white_intersections' is not a tuple
        If 'black_intersections' is not a tuple
        If 'white_intersections' or 'black_intersections' contain
        repeated intersections
        If 'white_intersections' or 'black_intersections' contain
        intersections not belonging to an n x n goban
    """
    # Inner Function
    def add_stones(goban,intersections,stone_color):
        """
        Place stones on a goban

        Parameters
        ----------
        goban : goban
            Goban where stones will be placed
        intersections : tuple
            Intersections to occupy with stones
        stone_color : str
            Color of the stones to place
        """
        if stone_color == "branco":
            stone = create_white_stone()
        else:
            stone = create_black_stone()

        for intersection in intersections:
            place_stone(goban,intersection,stone)

    if (
        not isinstance(n,int) or
        (n != 9 and n != 13 and n != 19) or
        not isinstance(white_intersections,tuple) or
        not isinstance(black_intersections,tuple) or
        any(map(lambda x: not is_intersection(x) or not is_valid_intersection(create_empty_goban(n),x), \
                    white_intersections + black_intersections)) or
        intersections_repeated(white_intersections + black_intersections)
    ):
        raise ValueError("create_goban: argumentos invalidos")

    goban = create_empty_goban(n)
    add_stones(goban,white_intersections,"branco")
    add_stones(goban,black_intersections,"preto")

    return goban


def copy_goban(goban):
    """
    Return a copy of a goban

    Parameters
    ----------
    goban : goban
        Goban to copy

    Returns
    -------
    goban
        Copy of 'goban'
    """
    goban_copy = []

    for column in goban: 
        column_copy = []   

        # Copy the stones from the 'column' of the goban
        for stone in column:
            if is_white_stone(stone):
                column_copy.append(create_white_stone())
            elif is_black_stone(stone):
                column_copy.append(create_black_stone())
            else:
                column_copy.append(create_neutral_stone())

        goban_copy += [column_copy]

    return goban_copy

# Selectors
def get_last_intersection(goban):
    """
    Return the last intersection of a goban

    Parameters
    ----------
    goban : goban
        Goban to analyse

    Returns
    -------
    intersection
        Last intersection of 'goban'
    """
    return create_intersection(chr(ord("A") + len(goban) - 1),len(goban))


def get_stone(goban,intersection):
    """
    Return the stone at an intersection

    Parameters
    ----------
    goban : goban
        Goban to which the intersection to analyse belongs
    intersection : intersection
        Intersection to analyse

    Returns
    -------
    stone
        Stone at 'intersection'
    """
    return goban[ord(get_col(intersection)) - ord("A")][get_row(intersection) - 1]


def get_chain(goban,intersection):
    """
    Return the intersections of the chain passing through an intersection

    Parameters
    ----------
    goban : goban
        Goban to which the intersection belongs
    intersection : intersection
        Intersection of the stone whose chain is to be obtained

    Returns
    -------
    tuple
        Intersections of the stones in the chain passing through 'intersection'
        in reading order
    """
    stone = get_stone(goban,intersection)
    chain = (intersection,)

    # Get the intersections adjacent to each element of 'chain'
    i = 0
    while i < len(chain):
        adjacent_intersections = get_adjacent_intersections(chain[i],get_last_intersection(goban))

        for adjacent_intersection in adjacent_intersections:
            # Add 'adjacent_intersection' to 'chain' if it doesn't already belong
            # to it and is occupied by a stone equal to the one at 'intersection'
            if (
                stones_equal(stone,get_stone(goban,adjacent_intersection)) and 
                adjacent_intersection not in chain
            ):
                chain += (adjacent_intersection,) 
                
        i += 1

    return sort_intersections(chain)


# Modifiers
def place_stone(goban,intersection,stone):
    """
    Place a stone on a goban

    Parameters
    ----------
    goban : goban
        Goban where the stone will be placed
    intersection : intersection
        Intersection to occupy with the stone
    stone : stone
        Stone to place
    
    Returns
    -------
    goban
        Modified goban
    """
    goban[ord(get_col(intersection)) - ord("A")][get_row(intersection)-1] = stone

    return goban


def remove_stone(goban,intersection):
    """
    Remove a stone from a goban

    Parameters
    ----------
    goban : goban
        Goban from which the stone will be removed
    intersection : intersection
        Intersection whose stone will be removed

    Returns
    -------
    goban
        Modified goban
    """
    place_stone(goban,intersection,create_neutral_stone())

    return goban


def remove_chain(goban,intersections_tuple):
    """
    Remove stones from intersections of a goban

    Parameters
    ----------
    goban : goban
        Goban from which the stones will be removed
    intersections_tuple : tuple
        Intersections whose stones will be removed

    Returns
    -------
    goban
        Modified goban
    """
    for intersection in intersections_tuple:
        remove_stone(goban,intersection)
    
    return goban


# Recognizers
def is_goban(arg):
    """
    Check if the argument is a goban ADT

    Parameters
    ----------
    arg : universal
        Parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    if not isinstance(arg,list) or (len(arg) != 9 and len(arg) != 13 and len(arg) != 19):
        return False
    
    for element in arg:
        if not isinstance(element,list) or len(element) != len(arg):
            return False
        
        for sub_element in element:
            if not is_stone(sub_element):
                return False
    
    return True


def is_valid_intersection(goban,intersection):
    """
    Check if an intersection is valid within a goban

    Parameters
    ----------
    goban : goban
        Goban to consider
    intersection : intersection
        Intersection to check
        
    Returns
    -------
    bool
        True if valid, False otherwise
    """
    if (
        not get_col(intersection) <= get_col(get_last_intersection(goban)) or
        not get_row(intersection) <= get_row(get_last_intersection(goban))
    ):
        return False
    
    return True


# Test
def gobans_equal(goban1,goban2):
    """
    Check if the arguments are gobans and are equal

    Parameters
    ----------
    goban1 : universal
        First parameter to check
    goban2 : universal
        Second parameter to check

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    if (
        not is_goban(goban1) or 
        not is_goban(goban2) or
        len(goban1) != len(goban2)
    ):
        return False
    
    size = len(goban1)

    # Check if the gobans have equal stones
    for column in range(size):
        for stone in range(size):
            if not stones_equal(goban1[column][stone],goban2[column][stone]):
                return False
            
    return True


# Transformer
def goban_to_str(goban):
    """
    Return the string representation of a goban

    Parameters
    ----------
    goban : goban
        Goban to represent

    Returns
    -------
    str
        External representation of 'goban'
    """
    lines = ""

    # Write the central rows (with intersections)
    for row in range(-1,-len(goban) - 1,-1):
        # Create a 'line' with a sequence of 'O', 'X' and '.' according to the stones
        # occupying the intersections of the 'row' of the goban
        line = ""
        for column in goban:
            line += " " + stone_to_str(column[row])

        l = str(len(goban) + 1 + row)    # Number corresponding to 'row'

        # Format the 'line' and add it to 'lines'
        line = "{:>2}{} {:>2}".format(l,line,l)
        lines += '\n' + line

    # Write the first and last row, i.e. create a 'line' with the
    # sequence of letters corresponding to the goban's columns
    line = ""
    for i in range(len(goban)):
        line += " " + chr(ord('A') + i)

    # Format the 'line' and add it to 'lines'
    line = "  {}".format(line)
    lines = line + lines + '\n' + line

    return lines


# High-Level Functions
def get_intersections(goban,stone):
    """
    Return all intersections of a goban occupied by a given stone

    Parameters
    ----------
    goban : goban
        Goban whose intersections will be retrieved
    stone : stone
        Stone occupying the intersections to be retrieved

    Returns
    -------
    tuple
        Retrieved intersections
    """
    intersections = ()
    size = get_row(get_last_intersection(goban))

    # Iterate over the goban's intersections
    for column in range(1,size + 1):
        for row in range(1,size + 1):
            intersection = create_intersection(chr(ord("A") + column - 1),row)

            # Add 'intersection' to 'intersections' if it is occupied by 'stone'
            if stones_equal(get_stone(goban,intersection),stone):
                intersections += (intersection,)

    return intersections


def get_territories(goban):
    """
    Return the territories of a goban

    The territories will be returned with their intersections in reading order
    and sorted among themselves according to their first intersection by the same order

    Parameters
    ----------
    goban : goban
        Goban whose territories will be retrieved

    Returns
    -------
    tuple
        Tuple of tuples with the intersections of each territory of the goban
    """
    discovered_intersections = ()
    territories = ()

    # Iterate over the goban's intersections occupied by neutral stones
    for intersection in get_intersections(goban,create_neutral_stone()):

        # If the intersection has not been discovered, get its chain, i.e.
        # the 'territory' it belongs to
        if intersection not in discovered_intersections:
            territory = sort_intersections(get_chain(goban,intersection))
            territories += (territory,)

            # Add the intersections of 'territory' to 'discovered_intersections'
            discovered_intersections += territory
    
    # Sort 'territories' by their first intersection in reading order
    return tuple(sorted(territories, key = lambda x: (get_row(x[0]),get_col(x[0]))))


def get_different_adjacents(goban,intersections): 
    """
    Return the adjacent intersections to intersections. These will be:
    -> occupied by stones, if the latter are free
    -> free, if the latter belong to a player

    Parameters
    ----------
    goban : goban
        Goban to which the intersections belong
    intersections : tuple
        Intersections whose different adjacent intersections will be retrieved

    Returns
    -------
    tuple
        Different adjacent intersections retrieved in reading order
    """
    adjacents = ()
    occupation_state = is_player_stone(get_stone(goban,intersections[0]))

    # Get the intersections adjacent to 'intersections'
    for intersection in intersections:
        for adjacent in get_adjacent_intersections(intersection,get_last_intersection(goban)):

            # If 'adjacent' is different from 'intersections' and is not already
            # in 'adjacents', add it
            if (
                occupation_state != is_player_stone(get_stone(goban,adjacent)) and
                adjacent not in adjacents
            ):
                adjacents += (adjacent,)
    
    return sort_intersections(adjacents)


def make_move(goban,intersection,stone): 
    """
    Place a player's stone on an intersection of a goban, remove the opposing
    player's stones belonging to adjacent chains that have no liberties,
    and return the modified goban

    Parameters
    ----------
    goban : goban
        Goban where the stone will be placed
    intersection : intersection
        Intersection to occupy with the stone
    stone : stone
        Stone to place
    
    Returns
    -------
    goban
        Modified goban
    """
    place_stone(goban,intersection,stone)

    removed_chains = ()

    # Iterate over the intersections adjacent to 'intersection'
    adjacents = get_adjacent_intersections(intersection,get_last_intersection(goban))
    for adjacent in adjacents:

        # If the stone occupying 'adjacent' belongs to a player and is different
        # from 'stone', get the chain of 'adjacent'
        adjacent_stone = get_stone(goban,adjacent)
        if (
            is_player_stone(adjacent_stone) and
            is_white_stone(stone) != is_white_stone(adjacent_stone)
        ):
            chain = get_chain(goban,adjacent)

            # If 'chain' has not been removed and has no liberties,
            # remove the chain and add it to 'removed_chains'
            if chain not in removed_chains and len(get_different_adjacents(goban,chain)) == 0:
                remove_chain(goban,chain)
                removed_chains += (chain,)

    return goban


def get_player_stones(goban):
    """
    Return the number of intersections occupied by each player's stones

    Parameters
    ----------
    goban : goban
        Goban whose intersections will be counted
    
    Returns
    -------
    tuple
        Tuple of two integers corresponding to the number of intersections
        occupied by the white and black player's stones, respectively
    """
    return (len(get_intersections(goban,create_white_stone())), \
            len(get_intersections(goban,create_black_stone())))


# Additional Functions
def calculate_scores(goban):
    """
    Return each player's score

    Each player's score is obtained by:
    -> the number of intersections occupied by that player's stones
    -> the number of intersections forming territories whose border consists
    only of that player's stones

    Parameters
    ----------
    goban : goban
        Goban from which the scores will be retrieved
    
    Returns
    -------
    tuple
        Tuple of two integers corresponding to the scores of the white
        and black player, respectively
    """
    # Get the number of intersections occupied by each player's stones
    white_score, black_score = get_player_stones(goban)

    # Iterate over the 'territories' of the 'goban'
    territories = get_territories(goban)
    for territory in territories:

        # Get the 'border' (border) of the 'territory'
        border = get_different_adjacents(goban,territory)
        if len(border) == 0:
            break
        
        # If the 'border' consists only of white stones,
        # include the territory in the white player's score
        if all(map(lambda x: is_white_stone(get_stone(goban,x)), \
                   border)):
            white_score += len(territory)

        # If the 'border' consists only of black stones,
        # include the territory in the black player's score
        elif all(map(lambda x: is_black_stone(get_stone(goban,x)), \
                   border)):
            black_score += len(territory)

    return (white_score,black_score)


def is_legal_move(goban,intersection,stone,previous_goban):
    """
    Perform a move on a copy of a goban and check if it is legal

    Parameters
    ----------
    goban : goban
        Goban to be copied
    intersection : intersection
        Intersection where the stone will be placed
    stone : stone
        Stone to be placed
    previous_goban : goban
        Goban obtained at the end of the player's last turn

    Returns
    -------
    bool
        True if legal, False otherwise
    """
    # Get a copy of 'goban' and perform the move on it
    goban_copy = copy_goban(goban)
    make_move(goban_copy,intersection,stone)

    # Check if the move is illegal, i.e. results in Suicide or Repetition (Ko)
    if (
        is_player_stone(get_stone(goban,intersection)) or
        len(get_different_adjacents(goban_copy,get_chain(goban_copy,intersection))) == 0 or
        gobans_equal(goban_copy,previous_goban)
    ):
        return False
    
    return True


def player_turn(goban,stone,previous_goban):
    """
    Offer a player the option to pass or place their stone on an intersection
    and return whether the player passed

    Parameters
    ----------
    goban : goban
        Goban where the game is played
    stone : stone
        Player's stone
    previous_goban : goban
        Goban obtained at the end of the player's last turn

    Returns
    -------
    bool
        True if the player did not pass, False otherwise
    """
    # Check the validity of the player's choice
    choice = ""
    while (
        not len(choice) >= 2 or
        not choice[0].isalpha() or
        not "A" <= choice[0] <= "S" or
        not choice[1:].isnumeric() or
        not 1 <= int(choice[1:]) <= 19 or
        not is_valid_intersection(goban,str_to_intersection(choice)) or
        not is_legal_move(goban,str_to_intersection(choice),stone,previous_goban)
    ):
        # Check if the player passed their turn
        if choice == "P":
            return False
            
        choice = input("Escreva uma intersection ou 'P' para passar ["+stone_to_str(stone)+"]:")

    make_move(goban,str_to_intersection(choice),stone)

    return True


def go(n,white_stones,black_stones):
    """
    Play GO and return whether the white player won

    Parameters
    ----------
    n : int
        Dimension of the goban where the game will be played
    white_stones : tuple
        External representations of intersections to occupy with white stones
    black_stones : tuple
        External representations of intersections to occupy with black stones

    Returns
    -------
    bool
        True if the white player won, False otherwise
    
    Raises
    ------
    ValueError:
        If 'n' is not the integer 9, 13, or 19
        If 'white_stones' or 'black_stones' are not tuples
        If 'white_stones' or 'black_stones' do not contain valid external
        representations of valid intersections of an n x n goban
    """
    # Inner Function
    def show_game():
        """Show the players their score and the goban"""
        print("Branco (O) tem",white_score,"pontos")
        print("Preto (X) tem",black_score,"pontos")
        print(goban_to_str(goban))

    if (
        (n != 9 and n != 13 and n != 19) or
        not isinstance(white_stones,tuple) or
        not isinstance(black_stones,tuple) or
        any(map(lambda x: not isinstance(x,str) or 
                          not len(x) >= 2 or 
                          not x[0].isalpha() or 
                          not "A" <= x[0] <= "S" or
                          not x[1:].isnumeric() or 
                          not 1 <= int(x[1:]) <= 19 or
                          not is_valid_intersection(create_empty_goban(n),str_to_intersection(x)) 
                ,white_stones + black_stones)) 
    ):
        raise ValueError("go: argumentos invalidos")

    # Convert 'white_stones' and 'black_stones' to tuples of intersections
    white_stones = tuple(str_to_intersection(x) for x in white_stones)
    black_stones = tuple(str_to_intersection(x) for x in black_stones)

    if intersections_repeated(white_stones + black_stones):
        raise ValueError("go: argumentos invalidos")

    goban = create_goban(n,white_stones,black_stones)    # Create goban
    previous_goban1,previous_goban2 = 2*(copy_goban(goban),)
    end = False
    player1 = True
    last_player_passed = False

    # Play
    while not end:
        # Show the players their score and the goban
        white_score, black_score = calculate_scores(goban)
        show_game()

        player_passed = False

        # Player's turn
        if player1:
            # Check if the player passed
            if not player_turn(goban,create_black_stone(),previous_goban1):
                player_passed = True
            else:
                previous_goban1 = copy_goban(goban)    # Save copy of goban

        else:
            # Check if the player passed
            if not player_turn(goban,create_white_stone(),previous_goban2):
                player_passed = True
            else:
                previous_goban2 = copy_goban(goban)    # Save copy of goban
        
        # End the game if both players have passed
        if last_player_passed and player_passed:
            end = True

        last_player_passed = player_passed    # Save whether the player passed
        player1 = not player1    # Switch player

    # Show the players their score and the goban
    show_game()

    # Check if the white player won
    if white_score >= black_score:
        return True
    
    return False