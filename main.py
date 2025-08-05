from World import World
from World_drawer import WorldDrawer
from config import WORLD_X, WORLD_Y
import random

def main():
    # Generate a random seed for reproducible results
    seed = random.randint(1, 10000)
    print(f"Using seed: {seed}")
    
    # Create a world with the specified dimensions
    world = World(WORLD_X, WORLD_Y, seed)
    
    # Create the world drawer
    drawer = WorldDrawer(world)
    
    # Run the visualization
    print("Press ESC to exit")
    drawer.run()

if __name__ == "__main__":
    main() 