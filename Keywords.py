from wordcloud import *
from collections import defaultdict
import sys

region = ['African','EastAsian','EasternEuropean','LatinAmerican','MiddleEastern','NorthAmerican','NorthernEuropean','SouthAsian','SoutheastAsian','SouthernEuropean','WesternEuropean']
region_dict = defaultdict(lambda : defaultdict(int))
d = defaultdict(lambda : 0)
with open("srep00196-s3.csv") as f:
    for line in f:
        li = line.strip()
        if not li.startswith("#"):
            arr = li.split(",")
            area = arr[1]
            for i in range(1,len(arr)):
                region_dict[area][arr[i]] += 1
                d[arr[i]] += 1


file_f = open("wordDict","w")
for key in d:
    file_f.write(str(key)+","+str(d[key])+"\n")
file_f.close()

for name in region:
    file_name = name+".csv"
    file_f = open(file_name, "w")
    for key in region_dict[name]:
        file_f.write(str(key) + "," + str(region_dict[name][key]) + "\n")
    file_f.close()

