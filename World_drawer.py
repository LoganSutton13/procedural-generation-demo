from config import *
import pygame
import random
from World import World

class WorldDrawer:
    def __init__(self, world):
        pygame.init()
        
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.world = world
        self.clock = pygame.time.Clock()
        
        # Color mapping for terrain types
        self.terrain_colors = {
            OCEAN3: (0, 0, 139),    # Dark blue
            OCEAN2: (0, 0, 205),    # Medium blue
            OCEAN1: (0, 191, 255),  # Light blue
            BEACH: (238, 214, 175), # Sand color
            GRASS: (34, 139, 34),   # Forest green
            MOUNTAIN: (139, 69, 19), # Brown
            SNOW: (255, 250, 250)   # White
        }

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        
        for y in range(WORLD_Y):
            for x in range(WORLD_X):
                self.draw_tile(x, y)
        
        pygame.display.flip()

    def draw_tile(self, x, y):
        # Get noise value for this position
        if y < len(self.world.noise_map) and x < len(self.world.noise_map[y]):
            noise_value = self.world.noise_map[y][x]
            
            # Normalize noise value to 0-1 range
            normalized_value = (noise_value - self.world.min_value) / (self.world.max_value - self.world.min_value)
            
            # Map noise value to terrain type
            terrain_type = self.get_terrain_type(normalized_value)
            
            # Get color for this terrain type
            color = self.terrain_colors.get(terrain_type, (128, 128, 128))
            
            # Draw the tile
            rect = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(self.screen, color, rect)
            

    def get_terrain_type(self, normalized_value):
        """Map normalized noise value (0-1) to terrain type"""
        if normalized_value < 0.1:
            return OCEAN3
        elif normalized_value < 0.2:
            return OCEAN2
        elif normalized_value < 0.3:
            return OCEAN1
        elif normalized_value < 0.35:
            return BEACH
        elif normalized_value < 0.7:
            return GRASS
        elif normalized_value < 0.9:
            return MOUNTAIN
        else:
            return SNOW

    def run(self):
        """Main game loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.type == pygame.K_SPACE:
                        self.world = World(WORLD_X, WORLD_Y, random.randint(1, 10000))
            
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
