import json
import runway
from runway.data_types import image, text

def nullModel():
    return

@runway.setup
def setup():
    return nullModel()

@runway.command('classify', inputs={ 'image': text() }, outputs={ 'text': text() })
def classify(model, input):
    image = input.get("image")
    return { 'text': image.upper() }

if __name__ == '__main__':
    runway.run()