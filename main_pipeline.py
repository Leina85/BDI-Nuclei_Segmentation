import numpy as np
import matplotlib.pyplot as plt
import sys
import typer
from PIL import Image

sys.path.append("BDI-Nuclei_Segmentation/pipeline")
from img_manipulation import read_img, crop_img, tile_img, seperate_tile_types
from find_means import find_means
from run_cellSAM import cellSAM
from evaluate_masks import segmentation_evaluate

Image.MAX_IMAGE_PIXELS = None

chosen_index = 100

def main(image:str="BDI-Nuclei_Segmentation/data/GTEX-113JC-2226.jpg", w_target:int=55750, h_target:int=40500, tile_size:int=250):
    print('main called')
    image = read_img(image)
    print("image downloaded")
    cropped_image = crop_img(image, w_target, h_target)
    tiles = tile_img(cropped_image, tile_size)
    means = find_means(tiles)
    tissue_tiles, background_tiles = seperate_tile_types(means)
    chosen_tile = tiles[tissue_tiles[chosen_index]]
    mask = cellSAM(chosen_tile)
    
    # Make correct data type
    mask_to_save = (mask / mask.max() * 255).astype(np.uint8)
    tile_to_save = (chosen_tile / chosen_tile.max() * 255).astype(np.uint8)
    
    # Save images
    Image.fromarray(mask_to_save).save("./BDI-Nuclei_Segmentation/results/mask.jpg", format="JPEG")
    Image.fromarray(tile_to_save).save("./BDI-Nuclei_Segmentation/results/tissue_tile.jpg", format="JPEG")
    
    dice_coefficient = segmentation_evaluate(mask, chosen_tile)
    print(dice_coefficient)
    
if __name__ == "__main__":
    typer.run(main)