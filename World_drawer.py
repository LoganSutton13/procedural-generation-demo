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
        
        # Initialize font for text input
        self.font = pygame.font.Font(None, 32)
        
        # Color mapping for terrain types
        self.terrain_colors = {
            OCEAN3: (0, 0, 139),    # Dark blue
            OCEAN2: (0, 0, 205),    # Medium blue
            OCEAN1: (0, 191, 255),  # Light blue
            BEACH: (238, 214, 175), # Sand color
            GRASS1:  (11, 176, 30), # Lighter green
            GRASS2: (42, 156, 48), # Light green
            GRASS3: (34, 139, 34), # Forest green
            MOUNTAIN1: (139, 69, 19), # Brown
            MOUNTAIN2: (84, 82, 82), # Gray
            SNOW: (255, 250, 250)   # White
        }
        
        # Create cached surface for the world
        self.world_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.world_changed = True  # Flag to track if world needs redrawing
        
        # Text input properties
        self.input_text = ""
        self.input_active = False
        self.input_rect = pygame.Rect(10, 50, 200, 32)  # Moved down from y=10 to y=50
        self.cursor_visible = True
        self.cursor_timer = 0

    def draw(self):
        # Only redraw the world if it has changed
        if self.world_changed:
            self.redraw_world()
            self.world_changed = False
        
        # Clear screen and blit the cached world surface
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.world_surface, (0, 0))
        
        # Draw text input UI
        self.draw_text_input()
        
        pygame.display.flip()

    def redraw_world(self):
        """Redraw the entire world to the cached surface"""
        self.world_surface.fill((0, 0, 0))
        
        for y in range(WORLD_Y):
            for x in range(WORLD_X):
                self.draw_tile_to_surface(x, y)

    def draw_tile_to_surface(self, x, y):
        """Draw a tile to the cached world surface"""
        # Get noise value for this position
        if y < len(self.world.noise_map) and x < len(self.world.noise_map[y]):
            noise_value = self.world.noise_map[y][x]
            
            # Normalize noise value to 0-1 range
            normalized_value = (noise_value - self.world.min_value) / (self.world.max_value - self.world.min_value)
            
            # Map noise value to terrain type
            terrain_type = self.get_terrain_type(normalized_value)
            
            # Get color for this terrain type
            color = self.terrain_colors.get(terrain_type, (128, 128, 128))
            
            # Draw the tile to the cached surface
            rect = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(self.world_surface, color, rect)
            

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
        elif normalized_value < 0.55:
            return GRASS1
        elif normalized_value < 0.6:
            return GRASS2
        elif normalized_value < 0.65:
            return GRASS3
        elif normalized_value < 0.83:
            return MOUNTAIN1
        elif normalized_value < 0.90:
            return MOUNTAIN2
        else:
            return SNOW

    def draw_text_input(self):
        """Draw the text input field and UI"""
        # Draw input box background
        color = (255, 255, 255) if self.input_active else (128, 128, 128)
        pygame.draw.rect(self.screen, color, self.input_rect, 2)
        
        # Draw input box fill
        pygame.draw.rect(self.screen, (0, 0, 0), self.input_rect)
        pygame.draw.rect(self.screen, color, self.input_rect, 2)
        
        # Render the text
        text_surface = self.font.render(self.input_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        
        # Draw cursor if active
        if self.input_active and self.cursor_visible:
            cursor_x = self.input_rect.x + 5 + self.font.size(self.input_text)[0]
            cursor_rect = pygame.Rect(cursor_x, self.input_rect.y + 5, 2, 22)
            pygame.draw.rect(self.screen, (255, 255, 255), cursor_rect)
        
        # Draw label
        label_surface = self.font.render("Seed:", True, (255, 255, 255))
        self.screen.blit(label_surface, (self.input_rect.x, self.input_rect.y - 25))
        
        # Draw instructions
        instruction_font = pygame.font.Font(None, 24)
        instructions = [
            "Click to enter seed, ENTER to generate, SPACE for random",
            "ESC to exit"
        ]
        for i, instruction in enumerate(instructions):
            inst_surface = instruction_font.render(instruction, True, (200, 200, 200))
            self.screen.blit(inst_surface, (10, WINDOW_HEIGHT - 60 + i * 20))

    def handle_text_input(self, event):
        """Handle text input events"""
        if event.type == pygame.KEYDOWN:
            if self.input_active:
                if event.key == pygame.K_RETURN:
                    # Generate world with entered seed
                    try:
                        seed = int(self.input_text)
                        self.world = World(WORLD_X, WORLD_Y, seed)
                        self.world_changed = True
                        print(f"Generated world with seed: {seed}")
                        self.input_text = ""
                        self.input_active = False
                    except ValueError:
                        print("Please enter a valid number")
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    self.input_active = False
                    self.input_text = ""
                elif event.unicode.isnumeric():
                    # Only allow numbers
                    if len(self.input_text) < 10:  # Limit to 10 digits
                        self.input_text += event.unicode

    def run(self):
        """Main game loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mouse clicked on input box
                    if self.input_rect.collidepoint(event.pos):
                        self.input_active = True
                    else:
                        self.input_active = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.input_active:
                            self.input_active = False
                            self.input_text = ""
                        else:
                            running = False
                    elif event.key == pygame.K_SPACE and not self.input_active:
                        self.world = World(WORLD_X, WORLD_Y, random.randint(1, 10000))
                        self.world_changed = True
                        print("New world generated")
                    else:
                        self.handle_text_input(event)
            
            # Update cursor blinking
            self.cursor_timer += 1
            if self.cursor_timer >= 30:  # Blink every 30 frames (1 second at 30 FPS)
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0
            
            self.draw()
            self.clock.tick(30)  # 30 FPS
        
        pygame.quit()
