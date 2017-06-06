from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__)
region = ['African','EastAsian','EasternEuropean','LatinAmerican','MiddleEastern','NorthAmerican','NorthernEuropean','SouthAsian','SoutheastAsian','SouthernEuropean','WesternEuropean']

for area in region:
    file_name = area+".csv"
    image_name = area+".png"
    text = ""
    for line in open(path.join(d, file_name)).readlines():
        l = line.split(",")
        temp = (l[0] + " ") * int(l[1])
        text += temp.strip()

    wordcloud = WordCloud(width=1600, height=800).generate(text)
    plt.title(area)
    plt.figure(figsize=(20,10), facecolor='k')
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file(image_name)
    # plt.show()
