from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Read the whole text.
text = open("text_file.txt", "r", encoding="utf8").read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# lower max_font_size
wordcloud = WordCloud(max_font_size=60, stopwords=STOPWORDS, width=800, height=400).generate(text)
wordcloud.to_file("word_cloud.png")
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.show()