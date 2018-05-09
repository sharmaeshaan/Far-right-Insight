from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

print('Started vizualization process')
# open text file
text = open('filterwords.txt').read()

# open mask image
gmask = np.array(Image.open('swastika.png'))

# configure wordcloud output
cloud = WordCloud(background_color='white', max_words=300, max_font_size=100, mask=gmask, contour_width=1, contour_color='black', colormap = 'plasma', scale=5)

print('Generating visualization')
# generate wordcloud
cloud.generate(text)

# set matplotlib config
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.figure()
plt.imshow(gmask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.title('Words Used Most Frequently by Joseph Goebbles in Public Interaction')

# save output to file
cloud.to_file('goebbles-viz.png')
print('Done. Visualization image saved to program directory')
