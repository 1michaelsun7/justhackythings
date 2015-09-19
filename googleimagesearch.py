import urllib2
import json
import cStringIO
from clarifai_basic import ClarifaiCustomModel

concept = ClarifaiCustomModel()
googleimages = []

fetcher = urllib2.build_opener()
searchTerm = 'parrot'
for sI in xrange(5):
	startIndex = 4*sI
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(startIndex)
	f = fetcher.open(searchUrl)
	deserialized_output = json.load(f)
	for i in xrange(min(len(deserialized_output['responseData']['results']), 10)):
		imageUrl = deserialized_output['responseData']['results'][i]['unescapedUrl']
		googleimages.append(imageUrl)
for u in googleimages:
	concept.positive(u, searchTerm)

concept.train(searchTerm)
