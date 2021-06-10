import nltk
from nltk.corpus import stopwords
# download the stopword list at startup
# this is a NOOP if already present 
nltk.download('stopwords')
nltk.download('punkt')
from wordcloud import WordCloud

import uuid, random, datetime, os

def random_frequencies():
	word_frequencies = {}
	for i in range(0, 1000000):
		word_frequencies[str(uuid.uuid4)] = random.randint(1,500)

	return word_frequencies

def _create_word_cloud(text):
    # Generate the image word cloud at a scale of 4 for performance reasons.
    wc = WordCloud(background_color="rgba(255, 255, 255, 0)", mode="RGBA", max_words=200, width=260, height=160, scale=4, mask=None, contour_width=1)
    wc.generate_from_frequencies(text)

    file_name = os.path.join("/tmp", uuid.uuid4().hex + ".png")

    img = wc.to_image()

    img.save(file_name, subsampling=0, quality=100)

    return file_name


def main():
	for i in range(0,10):
		words = random_frequencies()
		
		start = datetime.datetime.now()

		_create_word_cloud(words)

		end = datetime.datetime.now()

		duration = end - start 

		print("Took: " + str(duration.total_seconds() * 1000 ))

	



if __name__ == "__main__":
	main()