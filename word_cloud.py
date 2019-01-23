from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Read the whole text.
text = open('text_file.txt', "r", encoding="utf8").read()

# read the mask / color image taken from
# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
alice_coloring = np.array(Image.open("White-Rabbit.png"))
stopwords = set(STOPWORDS)

wc = WordCloud(background_color="black", mask=alice_coloring,
               stopwords=stopwords, width=800, height=400, max_words=40, font_path="Zombie_Holocaust.ttf")

wc.generate(text)
wc.to_file("rabbit.png")