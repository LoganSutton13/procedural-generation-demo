WINDOW_WIDTH    = 1000
WINDOW_HEIGHT   = 1000
TILESIZE        = 4      # tile width/height in pixels in tilesheet
WORLD_X         = (WINDOW_WIDTH + TILESIZE - 1) // TILESIZE
WORLD_Y         = (WINDOW_HEIGHT + TILESIZE - 1) // TILESIZE


# Terrain types
OCEAN3 = 0
OCEAN2 = 1
OCEAN1 = 2
BEACH = 3
GRASS1 = 4
GRASS2 = 5
GRASS3 = 6
MOUNTAIN1 = 7
MOUNTAIN2 = 8
SNOW = 9


# List of all terrain type, ordered from lower height to higher height
ALL_TERRAIN_TYPES = [OCEAN3, OCEAN2, OCEAN1, BEACH, GRASS1, GRASS2, GRASS3, MOUNTAIN1, MOUNTAIN2, SNOW]
