from perlin_noise import PerlinNoise

class World: 
    def __init__(self, size_x, size_y, seed):
        self.generate_noisemap(size_x, size_y, seed)

        # Flatten the noise map
        self.linear_map = [item for sublist in self.noise_map for item in sublist ]

        # Get min and max values
        self.min_value = min(self.linear_map)
        self.max_value = max(self.linear_map)

    def generate_noisemap(self, size_x, size_y, seed): 
        self.noise_map = []

        octave_factor = 2
        octave_base = 3

        # Generate noise maps
        noise1 = PerlinNoise(octaves=octave_base, seed=seed)
        noise2 = PerlinNoise(octaves=octave_base * octave_factor, seed=seed)
        noise3 = PerlinNoise(octaves=octave_base * octave_factor ** 2, seed=seed)
        noise4 = PerlinNoise(octaves=octave_base * octave_factor ** 3, seed=seed)

        xpix, ypix = size_x + 1, size_y + 1

        # Generate 2D noise map
        for y in range(ypix):
            row = []
            for x in range(xpix):
                noise_value = noise1([x/xpix, y/ypix])
                noise_value += noise2([x/xpix, y/ypix]) * 0.5
                noise_value += noise3([x/xpix, y/ypix]) * 0.25
                noise_value += noise4([x/xpix, y/ypix]) * 0.125
                row.append(noise_value)
            self.noise_map.append(row)

    def get_noise_map(self):
        return self.noise_map
