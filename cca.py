from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localisation

# group connected regions 
label_image = measure.label(localisation.binary_car_image)
#fig, (ax1) = plt.subplots(1)
#ax1.imshow(localisation.gray_car_image, cmap='gray')


# define boundaries for licence plate size
lp_dim = (0.08*label_image.shape[0], 0.2*label_image.shape[0], 0.15*label_image.shape[1], 0.4*label_image.shape[1])
min_ht, max_ht, min_wth, max_wth = lp_dim
lp_cordinates = []
poss_plate = []
fig, (ax1) = plt.subplots(1)
ax1.imshow(localisation.gray_car_image, cmap="gray");


#regionprops creates properties of all labelled regions
for region in regionprops(label_image):


	if region.area < 50:


		# if region too small == not LP

		continue

	# the bounding box coordinates
	min_row, min_col, max_row, max_col = region.bbox
	region_height = max_row - min_row
	region_width = max_col - min_col
   	  
   	# ensuring that the region identified satisfies the condition of a typical license plate
	if region_height >= min_ht and region_height <= max_ht and region_width >= min_wth and region_width <= max_wth and region_width > region_height:
		poss_plate.append(localisation.binary_car_image[min_row:max_row, min_col:max_col])
		lp_cordinates.append((min_row, min_col,max_row, max_col))
		rectBorder = patches.Rectangle((min_col, min_row), max_col-min_col, max_row-min_row, edgecolor="red", linewidth=2, fill=False) 
		ax1.add_patch(rectBorder)
    # let's draw a red rectangle over those regions


plt.show()