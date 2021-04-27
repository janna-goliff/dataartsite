from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from skimage.color import rgb2gray, rgba2rgb, gray2rgb
from skimage import data, io, filters, exposure, img_as_float
from skimage.exposure import match_histograms
import os
import matplotlib
from django.conf import settings

import numpy as np

# from tutorial
def splash(request):

	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)

		if form.is_valid():
			# saves original 
			form.save()

			# get url
			currName = request.POST.__getitem__('name')
			pic = Picture.objects.get(name=currName)
			
			# print("			PERCENTAGE")
			# print("			PERCENTAGE")
			# print(pic.percentage)

			filename = settings.MEDIA_ROOT[0:-6] + pic.picture_img.url
			camera = io.imread(filename)

			greyscale = rgb2gray(camera)

			grey = gray2rgb(greyscale)

			percent = pic.percentage
			min_range = 50 - (percent / 2)
			max_range = 50 + (percent / 2)
			percentage_min = np.percentile(greyscale, min_range)
			percentage_max = np.percentile(greyscale, max_range)

			mask_min = greyscale[:, :] >= percentage_min 
			mask_max = greyscale[:, :] <= percentage_max

			mask = np.logical_and(mask_min,mask_max)

			camera[mask] = [0, 255, 0]

			# display image
			io.imshow(camera)

			filename = currName + '.jpg'
			
			fullPath = settings.MEDIA_ROOT + "\\filtered_images\\" + filename
			io.imsave(fullPath, camera)
			# pic.assoc_url = fullPath
			pic.filtered_img = fullPath
			pic.save()

			# newFp = Picture()
			# newFp.name = currName + "_filtered"
			# newFp.picture_img = fullPath
			# newFp.save()

			# fp = FilteredPicture(name=currName, path=fullPath, filename=filename)
			# fp.save()

			io.show()

			return redirect('splash')
	else:
		form = PictureForm()

	if request.method == 'GET':
        # getting all the objects of picture
		Pictures = Picture.objects.all() 
		return render(request, 'main.html', {'form': form, 'picture_images': Pictures, 'root': settings.MEDIA_ROOT[:-5], 'ending': '.jpg'})
	return render(request, 'main.html', {'form' : form})

	
def success(request):
	return HttpResponse('successfully uploaded')
