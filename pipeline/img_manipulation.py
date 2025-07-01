from PIL import Image
import numpy as np

def format_img(base_image, w_target, h_target):
    cropped_image = base_image[:w_target, :h_target]
    cropped_pil_image = Image.fromarray(cropped_image)
    image_arr = np.array(cropped_pil_image)
    
    return(image_arr)

def tile_img(np_image, tile_size):
    h_tile_num = np_image.shape[0]//tile_size
    w_tile_num = np_image.shape[1]//tile_size

    tiles = []

    for y in range(h_tile_num):
        for x in range(w_tile_num):
            #start:stop(not inclusive)
            tile = np_image[y*tile_size:(y+1)*tile_size, x*tile_size:(x+1)*tile_size, :]
            tiles.append(tile)
            
    return(tiles)

def seperate_background(means):
    background_tile = []
    tissue_tile = []

    #for every tile, check avg, if surpasses threshhold then store index in array
    for tile in range(len(means)):
       print(means[tile])
       if means[tile] < 225:
            tissue_tile.append(tile)
       else:
          background_tile.append(tile)
          
    return(tissue_tile, background_tile)