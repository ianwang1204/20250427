#xmnn, ymnn,xmxn,ymxn=318 547 212 390
from PIL import Image
import pandas as pd
import os, sys,random

www=open("train8.csv","w")
www.writelines("img,px,py\n")

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

image_path = "split_images8"
if image_path not in os.listdir():
    os.mkdir(image_path)
    print("folder created")

data=pd.read_csv("train.csv")
now=0
sc=256
aaa=30
bbb=sc-30
for i in range(data.shape[0]):
    im = Image.open(data.iloc[i][0])
    width, height = im.size
    for j in range(1,9,2):
        for k in range(5):
            x,y=data.iloc[i][j],data.iloc[i][j+1]
            xx = random.randint(aaa,bbb)
            yy = random.randint(aaa,bbb)
            if x-xx <= 0:
                xx=x-1
            if y-yy <= 0:
                yy=y-1
            if x+sc-xx >=width :
                xx = -(width-x-sc-2)
            if y+sc-yy >= height:
                yy = -(height-y-sc-2)
            box = (x-xx,y-yy,x+sc-xx, y+sc-yy)
            a = im.crop(box)
            a.save(image_path+"/"+str(now)+".jpg")
            s=f"{now}.jpg,{xx},{yy}\n"
            print(s)
            www.writelines(s)
            now+=1
    for j in range(1,9,2):
        for k in range(5):
            x,y=random.randint(10,width-10), random.randint(10,height-10)
            xx = random.randint(aaa,bbb)
            yy = random.randint(aaa,bbb)
            if x-xx <= 0:
                xx=x-1
            if y-yy <= 0:
                yy=y-1
            if x+sc-xx >=width :
                xx = -(width-x-sc-2)
            if y+sc-yy >= height:
                yy = -(height-y-sc-2)
            box = (x-xx,y-yy,x+sc-xx, y+sc-yy)
            a = im.crop(box)
            a.save(image_path+"/"+str(now)+".jpg")
            s=f"{now}.jpg,{-1},{-1}\n"
            print(s)
            www.writelines(s)
            now+=1
www.close()
