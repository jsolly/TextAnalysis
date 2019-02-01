from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

text = open('text_file.txt', "r", encoding="utf8").read()

image_coloring = np.array(Image.open("lips.png"))
stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", mask=image_coloring,
               stopwords=stopwords, width=800, height=400, max_words=90, font_path="Zombie_Holocaust.ttf")

wc.generate(text)
image_colors = ImageColorGenerator(image_coloring)


plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
plt.savefig("black_lips.png", transparent = True, bbox_inches = 'tight', pad_inches = 0)

#wc.to_file("black_lips.png")