from PIL import Image
import numpy as np

def format_img(base_image, w_target, h_target):
    # Parameters: base_image (NumPy array representing the entire original histology image)
    #             w_target (integer)
    #             h_target (integer)
    # Returns: cropped_image (NumPy array represending the cropped version of the original image for cleaner tiling)

    # Crop the image to the inputted width and height
    cropped_image = base_image[:w_target, :h_target]
    
    return cropped_image 


def tile_img(np_image, tile_size):
    # Parameters: np_image (NumPy array of (cropped) image)
    #             tile_size (integer)
    # Returns: tiles (list of NumPy arrays representing each image tile)
    
    # Determines number of tiles along the height and width of the image
    h_tile_num = np_image.shape[0]//tile_size
    w_tile_num = np_image.shape[1]//tile_size

    # Initialize list to store the tiles
    tiles = []

    # Loops over the image grid to extract tiles
    for y in range(h_tile_num):
        for x in range(w_tile_num):
            # Extract tile using slicing: [start_y:end_y, start_x:end_x, all_channels] does not seperate into colour channels (stays RGB)
            tile = np_image[y*tile_size:(y+1)*tile_size, x*tile_size:(x+1)*tile_size, :]
            tiles.append(tile)
            
    return tiles


def seperate_tile_types(means):
    # Parameters: means (list of NumPy arrays representing RGB image sections)
    # Returns: tissue_tile (list of integers relating to index of the tile containging tissue in the tiles array)
    #          background_tile (list of integers relating to index of the tile containing no tissue in the tiles array)
    
    # Initialize lists to store the background tiles and tiles containing tissue
    background_tiles = []
    tissue_tiles = []

    #for every tile, check avg, if surpasses threshhold (225 estimated from histogram data in find_means function) then store index in array
    for tile in range(len(means)):
       print(means[tile])
       if means[tile] < 225:
            tissue_tiles.append(tile)
       else:
          background_tiles.append(tile)
          
    return tissue_tiles, background_tiles