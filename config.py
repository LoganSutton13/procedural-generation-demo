WINDOW_WIDTH    = 1920
WINDOW_HEIGHT   = 1080
TILESIZE        = 16       # tile width/height in pixels in tilesheet
WORLD_X         = (WINDOW_WIDTH + TILESIZE - 1) // TILESIZE
WORLD_Y         = (WINDOW_HEIGHT + TILESIZE - 1) // TILESIZE


# Terrain types
OCEAN3 = 0
OCEAN2 = 1
OCEAN1 = 2
BEACH = 3
GRASS = 4
MOUNTAIN = 5
SNOW = 6


# List of all terrain type, ordered from lower height to higher height
ALL_TERRAIN_TYPES = [OCEAN3, OCEAN2, OCEAN1, BEACH, GRASS, MOUNTAIN, SNOW]
