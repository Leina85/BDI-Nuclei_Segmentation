import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
Image.MAX_IMAGE_PIXELS = None

import sys
sys.path.append(r"C:\Users\Leina School\Desktop\Work Exp BDI\BDI-Nuclei_Segmentation\pipeline")

from img_manipulation import format_img, tile_img, seperate_tile_types
from find_means import find_means
from run_cellSAM import cellSAM

image = np.array(Image.open(r"C:\Users\Leina School\Desktop\Work Exp BDI\data\GTEX-113JC-2226.jpg")) 

w_target, h_target = 55750, 40500
tile_size = 250

cropped_image = format_img(image, w_target, h_target)

tiles = tile_img(cropped_image, tile_size)

means = find_means(tiles)

tissue_tiles, background_tiles = seperate_tile_types(means)

mask = cellSAM(tiles[tissue_tiles[967]])

print("YUIO")
plt.imshow(mask)
plt.imshow(tiles[tissue_tiles[967]])