from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

print('Started vizualization process')
# open text file
text = open('filterwords.txt').read()

# configure wordcloud output
cloud = WordCloud(background_color='white', max_words=300, max_font_size=100, contour_width=1, contour_color='black', colormap = 'plasma', scale=5)

print('Generating visualization')
# generate wordcloud
wmap = cloud.generate(text)

# set matplotlib config
plt.figure()
plt.title('Words Used Most Frequently by Joseph Goebbles in Public Interaction')
plt.imshow(wmap, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')

# save output to file
wmap.to_file('goebbles-wordmap.png')
print('Done. Wordmap image saved to program directory')
