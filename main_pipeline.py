import numpy as np
import matplotlib.pyplot as plt
import sys
import typer
from PIL import Image

#sys.path.append(r"C:\Users\Leina School\Desktop\Work Exp BDI\BDI-Nuclei_Segmentation\pipeline")
from img_manipulation import format_img, tile_img, seperate_tile_types
from find_means import find_means
from run_cellSAM import cellSAM

Image.MAX_IMAGE_PIXELS = None

#image = np.array(Image.open(r"C:\Users\Leina School\Desktop\Work Exp BDI\data\GTEX-113JC-2226.jpg"))
#w_target, h_target = 55750, 40500
#tile_size = 250

def main(image:str, w_target:int=55750, h_target:int=40500, tile_size:int=250):
    cropped_image = format_img(image, w_target, h_target)
    tiles = tile_img(cropped_image, tile_size)
    means = find_means(tiles)
    tissue_tiles, background_tiles = seperate_tile_types(means)
    mask = cellSAM(tiles[tissue_tiles[967]])

    plt.imshow(mask)
    plt.show()
    plt.imshow(tiles[tissue_tiles[967]])
    plt.show()
    
    #tissue_tiles, background_tiles = seperate_tile_types(find_means(tile_img(cropped_image, tile_size)))
    #cellSAM(tile_img(format_img(image, w_target, h_target), tile_size)[tissue_tiles[967]])

if __name__ == "__main__":
    typer.run(main)