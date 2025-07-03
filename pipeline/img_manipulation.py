import numpy as np
import cv2
from PIL import Image
from scipy import ndimage

def read_img(image_path):
    # Parameters: image_path (string of image adress)
    # Returns: image (NumPy array of image)
    
    image = Image.open(image_path)
    image = np.array(image)
    
    return image

    
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

    # For every tile, check avg, if surpasses threshhold (225 estimated from histogram data in find_means function) then store index in array
    for tile in range(len(means)):
       if means[tile] < 225:
            tissue_tiles.append(tile)
       else:
          background_tiles.append(tile)
          
    return tissue_tiles, background_tiles

def format_tile(tile):
    # Parameters: tile (NumPy array of tissue tile)
    # Returns: dilated_img (NumPy array of bool values as a point of comparison to test the cellSAM mask)
    
    # Isolate red chanel (has clearest contrast between nuclei and the rest of the tissue)
    r, g, b = cv2.split(tile)
    # Change all pixel values to 0 and 255 based on a predetermined threshold (100)
    r_channel = np.where(r >= 100, 255, 0).astype(np.uint8)
    # Invert 0 and 255 pixel values to match cellSAM mask format
    invert_r_channel = 255 - r_channel
    
    # Chang to boolean values for dilation (to revmove white spaces in nuclei)
    bool_invert_r_channel = invert_r_channel.astype(bool)
    dilated_img = ndimage.binary_dilation(bool_invert_r_channel, iterations=1)
    
    return dilated_img
    