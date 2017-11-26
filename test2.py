import random
import urllib.request

def image_downloader(url):
    name = random.randrange(1, 100)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url , full_name)
    print("done")

image_downloader("https://qph.ec.quoracdn.net/main-thumb-3009-200-r7oiYmXlzgDBvOJMRghetN1R2TeU7Cir.jpeg")
