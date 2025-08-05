# Procedural Generation Demo

A Python application that generates and visualizes procedurally generated worlds using Perlin noise. The app creates realistic terrain with different biomes including oceans, beaches, grasslands, mountains, and snow-capped peaks.

## Features

- **Procedural World Generation**: Uses Perlin noise to create natural-looking terrain
- **Multiple Biomes**: 10 different terrain types from deep ocean to snow-capped mountains
- **Interactive Seed System**: Generate new worlds with specific seeds or random ones
- **Real-time Visualization**: Smooth 30 FPS rendering with Pygame
- **User-friendly Interface**: Click to enter seeds, keyboard shortcuts for quick generation

## Terrain Types

The world includes the following terrain types (from lowest to highest elevation):

1. **Deep Ocean** (OCEAN3) - Dark blue
2. **Ocean** (OCEAN2) - Medium blue  
3. **Shallow Ocean** (OCEAN1) - Light blue
4. **Beach** (BEACH) - Sand color
5. **Light Grass** (GRASS1) - Light green
6. **Grass** (GRASS2) - Medium green
7. **Forest** (GRASS3) - Dark green
8. **Mountains** (MOUNTAIN1) - Brown
9. **High Mountains** (MOUNTAIN2) - Gray
10. **Snow** (SNOW) - White

## Requirements

- Python 3.7 or higher
- Pygame 2.0.0 or higher
- Perlin-noise 1.8.0 or higher

## Installation

1. **Clone or download the project** to your local machine

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install pygame>=2.0.0 perlin-noise>=1.8.0
   ```

## How to Run

1. **Navigate to the project directory**:
   ```bash
   cd procedural-generation-demo
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

## Controls

Once the application is running, you can:

- **Click on the seed input box** to enter a specific seed number
- **Press ENTER** after entering a seed to generate a new world with that seed
- **Press SPACE** to generate a random world with a new random seed
- **Press ESC** to exit the application

## How It Works

### World Generation
The application uses Perlin noise with multiple octaves to create natural-looking terrain:

- **Base noise**: Creates the overall landscape structure
- **Multiple octaves**: Adds detail at different scales (3, 6, 12, and 24 octaves)
- **Weighted combination**: Combines noise layers with decreasing weights (1.0, 0.5, 0.25, 0.125)

### Terrain Mapping
The normalized noise values (0-1) are mapped to terrain types based on elevation thresholds:
- 0.0-0.1: Deep Ocean
- 0.1-0.2: Ocean
- 0.2-0.3: Shallow Ocean
- 0.3-0.35: Beach
- 0.35-0.55: Light Grass
- 0.55-0.6: Grass
- 0.6-0.65: Forest
- 0.65-0.83: Mountains
- 0.83-0.9: High Mountains
- 0.9-1.0: Snow

### Rendering
- **Tile-based rendering**: Each pixel represents a 4x4 tile in the world
- **Color-coded terrain**: Each biome has a distinct color for easy identification
- **Cached rendering**: The world surface is cached and only redrawn when the world changes

## Configuration

You can modify the world generation parameters in `config.py`:

- `WINDOW_WIDTH` / `WINDOW_HEIGHT`: Display window size (default: 1000x1000)
- `TILESIZE`: Size of each tile in pixels (default: 4)
- `WORLD_X` / `WORLD_Y`: World dimensions in tiles (calculated from window size)

## File Structure

```
procedural-generation-demo/
├── main.py              # Main application entry point
├── World.py             # World generation using Perlin noise
├── World_drawer.py      # Pygame-based visualization and UI
├── config.py            # Configuration constants
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Troubleshooting

### Common Issues

1. **"pygame module not found"**
   - Make sure you've installed the requirements: `pip install -r requirements.txt`

2. **"perlin_noise module not found"**
   - Install the perlin-noise package: `pip install perlin-noise>=1.8.0`

3. **Display issues on Windows**
   - Try running: `python -m pygame.examples.aliens` to test Pygame installation
   - Update your graphics drivers if needed

4. **Performance issues**
   - The app is optimized for 30 FPS. If you experience lag, try reducing the window size in `config.py`

### System Requirements

- **Windows**: Windows 10 or later
- **macOS**: macOS 10.14 or later  
- **Linux**: Any modern distribution with Python 3.7+
- **Graphics**: Any graphics card that supports OpenGL 2.0 or later

## Examples

### Generating a Specific World
1. Run the application
2. Click on the seed input box
3. Type a number (e.g., "12345")
4. Press ENTER
5. The world will regenerate with that specific seed

### Quick Random Generation
1. Run the application
2. Press SPACE to generate a new random world
3. Repeat as many times as you like

## Contributing

Feel free to modify and extend this project! Some ideas for improvements:

- Add more terrain types (deserts, forests, etc.)
- Implement different noise algorithms
- Add save/load functionality for generated worlds
- Create different world generation algorithms
- Add zoom and pan controls

## License

This project is open source. Feel free to use, modify, and distribute as you see fit.

## Credits

- **Perlin Noise**: Ken Perlin's noise algorithm for natural terrain generation
- **Pygame**: Python game development library for graphics and input handling
- **Perlin-noise Python library**: Implementation of Perlin noise for Python 