import numpy as np
from img_manipulation import format_tile, format_mask
from PIL import Image

def segmentation_evaluate(cellSAM_mask, tile):
    bool_tile = format_tile(tile)
    bool_mask = format_mask(cellSAM_mask)
    dice_coefficient = dice_coefficient_calc(bool_tile, bool_mask)
    
    Image.fromarray(bool_tile).save("./BDI-Nuclei_Segmentation/results/bool_mask.jpg", format="JPEG")
    Image.fromarray(bool_mask).save("./BDI-Nuclei_Segmentation/results/bool_tissue_tile.jpg", format="JPEG")
    
    return dice_coefficient
    
def dice_coefficient_calc(set1, set2):
    set1 = np.array(set1)
    set2 = np.array(set2)
    intersection = np.sum(np.logical_and(set1, set2))
    dice_coefficient = 2. * intersection / (np.sum(set1) + np.sum(set2))
    
    return dice_coefficient