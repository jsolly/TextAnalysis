from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

text = open('text_file.txt', "r", encoding="utf8").read()

image_coloring = np.array(Image.open("lips.png"))
stopwords = set(STOPWORDS)

wc = WordCloud(background_color="black", mask=image_coloring,
               stopwords=stopwords, width=800, height=400, max_words=2000, font_path="Zombie_Holocaust.ttf", random_state=9, contour_width=3, contour_color='red')

wc.generate(text)
#wc.to_file("black_lips.png")
image_colors = ImageColorGenerator(image_coloring)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(image_coloring, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()


plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
plt.savefig("red_lips.png", transparent = True, bbox_inches = 'tight', pad_inches = 0)