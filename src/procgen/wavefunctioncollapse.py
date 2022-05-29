DIRS = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}

def neighboring_directions(coordinate: tuple[int, int], map_width: int, map_height: int) -> list[str]:
    """
    Helper function which finds all valid directions a given tile can have neighbors in.

    Args:
        coordinate (tuple[int, int]): A coordinate in a map.

        map_width (int): Width of the map being used.

        map_height (int): Height of the map being used.

    Returns:
        A list of strings containing all valid directions in the form of 'N', 'E', 'S', 'W'
    """

    x, y = coordinate
    neighbors = []

    if y > 0: neighbors.append('N')
    if y < map_height-1: neighbors.append('S')
    if x > 0: neighbors.append('W')
    if x < map_width-1: neighbors.append('E')

    return neighbors



def parse_tile_map(tile_map: list[list[str]]) -> tuple[set, dict]:
    """
    Parses a tilemap and returns possible neighbor tile types and weights for each tile
        
    Args:
        map (list): The input tile map to be parsed

    Returns:
        A set of possible neighbor tile types and a dictionary of weights for each tile type
    """

    weights_map = {}
    possible_neighbors = set()
    map_width = len(tile_map[0])
    map_height = len(tile_map)

    for i_y, row in enumerate(tile_map):
        for i_x, tile in enumerate(row):
            if tile not in weights_map:
                weights_map[tile] = 0
            weights_map[tile] += 1

            for dir in neighboring_directions((i_x, i_y), map_width, map_height):
                dir_x, dir_y = DIRS[dir]
                possible_neighbors.add((tile, tile_map[i_x + dir_x][i_y + dir_y], dir))
    
    return possible_neighbors, weights_map
