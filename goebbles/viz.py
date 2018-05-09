from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

text = open('filterwords.txt').read()

gmask = np.array(Image.open('gb.png'))

cloud = WordCloud(background_color='white', max_words=1000, max_font_size=80, mask=gmask, contour_width=0.5, contour_color='black', scale=5)

cloud.generate(text)


plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.figure()
plt.imshow(gmask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()