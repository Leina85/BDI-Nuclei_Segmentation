from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def find_means(tiles):
    # Parameters: tiles (list of NumPy arrays representing RGB image sections)
    # Returns: means (list of floats representing mean greyscale values)
    
    # Initialize list to store mean values
    means = []

    # Process each tile
    for tile in tiles:
        # Convert NumPy array to PIL Image to change to greyscale
        img_section = Image.fromarray(tile)
        grey_img = img_section.convert("L")
        
        # Convert greyscale image back to NumPy array to compute and store mean
        grey_tile = np.array(grey_img)
        means.append(grey_tile.mean())
        
    # Plot histogram of mean greyscale values to visualise colour distribution
    plt.hist(means, bins = 250)
    plt.savefig("results/mean_histogram.jpg")
    
    return means 