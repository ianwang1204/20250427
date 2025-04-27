#https://gis.stackexchange.com/questions/401797/how-to-process-list-of-gcp-points-in-gdal-in-python
import pandas as pd
from osgeo import gdal
import os,sys

www=open("train.csv","w")
www.writelines("img,d0x,d0y,d1x,d1y,d2x,d2y,d3x,d3y\n")

ls=list()
for i in range(1,24,1):
    s=str(i).rjust(3,'0')
    ls.append("t"+s)

for i in ls:
    print(i)
    # Read the coordinates in the CSV file
    names = "B-3092-0051-54_"+i
    f=pd.read_csv("GCPs\\"+names+".jpg.points")
    keep_col = ['mapX','mapY','sourceX', 'sourceY', 'enable']
    new_f = f[keep_col]
    df = new_f.drop(columns=['enable'])
    col=['mapX','mapY', 'sourceX','sourceY']
    modified_df = df[col]
    modified_df['sourceY'] = modified_df['sourceY'] *(-1) 

    # Create an empty GCP list
    ss=names+".jpg"
    gcp_list=list()
   
    # GCP coordinates list  
    for index, rows in modified_df.iterrows():
      
        gcps = gdal.GCP(rows.mapX, rows.mapY, 1, rows.sourceX, rows.sourceY )
        #gcp_list.append(gcps)
        print(names,gcps)
      
        gcp_list.append((int(rows.sourceX),int(rows.sourceY)))
    mn, mx=0,0
    for i in range(4):
        if gcp_list[i][0]+gcp_list[i][1] <= gcp_list[mn][0]+gcp_list[mn][1]:
            mn=i
    for i in range(4):
        if gcp_list[i][0]+gcp_list[i][1] >= gcp_list[mx][0]+gcp_list[mx][1]:
            mx=i
    set1={0,1,2,3}
    set1.remove(mn)
    set1.remove(mx)
    second=min(set1)
    third=max(set1)
    if gcp_list[second][0]>gcp_list[third][0]:
        second,third=third,second
    gcp_list2=[gcp_list[mn],gcp_list[second],gcp_list[third],gcp_list[mx]]
    for i,j in gcp_list2:
        ss+=","+str(i)+","+str(j)
    www.writelines(ss+'\n')
www.close()
