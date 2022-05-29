from procgen import wavefunctioncollapse

def test_wfc_tilemap_parse_function():
    test_map = [
        ['G', 'G'],
        ['W', 'M']
    ]

    neighbors, weights = wavefunctioncollapse.parse_tile_map(test_map)

    assert weights['G'] == 2
    assert weights['W'] == 1
    assert weights['M'] == 1

    assert neighbors == {('G', 'W', 'S'), ('G', 'M', 'S'), ('G', 'G', 'W'), ('G', 'G', 'E'), ('W', 'G', 'N'),\
         ('W', 'M', 'E'), ('M', 'W', 'W'), ('M', 'G', 'N')}

