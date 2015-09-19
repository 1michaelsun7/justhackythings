import urllib2
import json
import cStringIO
from pokemon_list_generator import pokemon_list_maker
from clarifai_basic import ClarifaiCustomModel, ApiError

concept = ClarifaiCustomModel('_AQuQqomUFFjD7MnNvWGCow-AHqJHB-dzFD2LqyU', '9RVaHVFFGwbfvypobBhM4grJf16EIKhJerBvh5l5')

fetcher = urllib2.build_opener()

pokemon_list = pokemon_list_maker()

for pokemon in pokemon_list[383:]:
	searchTerm = pokemon
	googleimages = []

	for sI in xrange(1):
		startIndex = 4*sI
		searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(startIndex)
		f = fetcher.open(searchUrl)
		deserialized_output = json.load(f)
		for i in xrange(min(len(deserialized_output['responseData']['results']), 10)):
			imageUrl = deserialized_output['responseData']['results'][i]['unescapedUrl']
			googleimages.append(imageUrl)		

	for images in googleimages:
		try:
			concept.positive(images, searchTerm)
		except ApiError:
			pass

	concept.train(searchTerm)
	print pokemon

"""
try:
	result = concept.predict('https://www.panerabread.com/panerabread/menu/details/smoked-ham-and-swiss-sandwich-whole.jpg/_jcr_content/renditions/smoked-ham-and-swiss-sandwich-whole.desktop.jpeg', searchTerm)
except ApiError:
	pass

print result
"""
