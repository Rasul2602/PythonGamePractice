WIN_WIDTH = 800
WIN_HEIGHT = 480
TILESIZE = 32
FPS = 60




PLAYER_LAYER = 4
GROUNDS_LAYER = 1
PLAYER_SPEED = 3
BLOCK_LAYER = 2
ENEMY_LAYER = 3
ENEMY_SPEED = 3
ATTACK_LAYER = 4
ATTACK_SPEED = 3

GREEN = (107, 143, 17)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0, 255, 255)
WHITE = (255,255,255)

tilemap = [
    'BBBBBBBBBBBBB|BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B.......................BB..................................BB..................................B',
    'B....BBB................BB..................E...............BB....E.....E.............E.........B',
    'B.............E.........BB..................................BB..................................B',
    'B.......................BB..........E........E..............BB..................................B',
    'B........P..............BB......E..........B..........E...........E........E.......E.....E......B',
    'B...E........E...E...B...BB......E..........B.......E........BB...................E.............B',
    'B......E......E.........BB.............E.....................BB.......E....E..E...........E.....B',
    'B.....BBB...............BB........E..........B..............BB.....E................E...........B',
    'B....E...B..........E....BB......E..................E........BB.........E........E.........E....B',
    'B.....B.B......E.....E..BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB..BBBB.........................E.........B',
    'B...E........B..........B...........................E......BB..........E..........E............B',
    'B.......E......E........B............E..........E..........BB.....E.......E.................E...B',
    'B....E........E..........B.........B.......B........E.......BB..................................B',
    'B....B...E...E.....E.....B............E..E.....E.....E.....BB......................E............B',
    'B.........E........E....B...E....................E..........BB.......E.............E............B',
    'B....E.....E............BBBBBBBB.........B......E...........BB..............................L...B',
    'B........E......E........BB.....B.....E........BBBBBBBBBB....BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|BBBBBB',
    'B....B......E...........BB...BBBBBBBBBBB.E....B........BBBBBB',
    'B.........E.......E.......BB.............................BBBBBB',
    'B....E...........B......BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB..BBBBB',
    'B.....E.....E....B......B..........BBBBBBBBBBBB.........E...B',
    'B....E........B.........B........................E..........B',
    'B.......E...............B....E.......E..........E...........B',
    'B...........E...........B.............E....B................B',
    'B....B.......E....E.....B......E..................E......E..B',
    'B....E......E...........B...E......E........................B',
    'B....E...........E......B.......BBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BBBBBBBBBBB...BBBBBBBBBBB...E....B',
    'BBBBBBBBBB..BBBBBBBBBBBBBBBBB...B',
    'BBBBBBBBBBB..BBBBBBBBBBBBBBBB...B',
    'BBBBBBBBBBB.....................BB',
    'BBBBBBBBBB..BBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BBBBBBBBBBBBBBBBBBBBBBBBB',
]