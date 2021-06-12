import pandas as pd
from moviepy.editor import *
import os
df = pd.read_csv('segments.csv', delimiter=',',header=0, usecols=range(0,3))
# User list comprehension to create a list of lists from Dataframe rows
list_of_rows = [list(row) for row in df.values]

segments_list=[]
# for each video source
for i,line in enumerate(list_of_rows):
    #print (line[0])
    if pd.notna(line[0]):  # if no new filename keep the previous
        file_path=line[0]
        print (file_path)
    print(file_path)
    clip1 = VideoFileClip(file_path)
    # for each start-end segments
    # create sub-clip
    # merge them
    segments_list.append(clip1.subclip(t_start=line[1], t_end=line[2]))

# concatenate them
final = concatenate_videoclips(segments_list)
# name output file
head,tail = os.path.split(file_path)
new_file_path= os.path.join(head,"edited_"+tail)
print(new_file_path)
# export them
final.write_videofile(new_file_path)
print("DONE")
