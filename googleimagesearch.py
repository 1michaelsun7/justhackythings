import urllib2
import json
import cStringIO
from pokemon_list_generator import pokemon_list_maker
from clarifai_basic import ClarifaiCustomModel, ApiError

concept = ClarifaiCustomModel('u2ODPbKXe3I51y9TV2GPGqmF7ZzZ8SVInInj_8pb', 'hwIilWC2qT-4VJHG1HTpnXoavOLpCevjbZ9Osnz4')

fetcher = urllib2.build_opener()

pokemon_list = pokemon_list_maker()


searchTerm = "Venusaur"
googleimages = []

for sI in xrange(4):
	startIndex = 4*sI
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "+pokemon&start=" + str(startIndex)
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
print searchTerm

"""
try:
	result = concept.predict('https://www.panerabread.com/panerabread/menu/details/smoked-ham-and-swiss-sandwich-whole.jpg/_jcr_content/renditions/smoked-ham-and-swiss-sandwich-whole.desktop.jpeg', searchTerm)
except ApiError:
	pass

print result
"""
