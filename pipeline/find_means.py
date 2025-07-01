from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def find_means(tiles):
    means = []

    #find averages of each tile pixel values in greyscale
    for tile in tiles:
        img_section = Image.fromarray(tile)
        grey_img = img_section.convert("L")
        grey_tile = np.array(grey_img)
        means.append(grey_tile.mean()) 

    plt.hist(means, bins = 250)
    
    return(means)