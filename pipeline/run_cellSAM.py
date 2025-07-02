from cellSAM import cellsam_pipeline
import matplotlib.pyplot as plt

def cellSAM(tile):
    mask = cellsam_pipeline(tile, use_wsi=True, low_contrast_enhancement=False, gauge_cell_size=False)
    
    return mask 
    #masks = []

    #for tile in tqdm(tissue_tile):
        #mask = cellsam_pipeline(tiles[tile], use_wsi=True, low_contrast_enhancement=False, gauge_cell_size=False)
        #mask = mask.tolist()
        #masks.append(mask)