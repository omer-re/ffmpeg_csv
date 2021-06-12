import pandas as pd
import ffmpeg

df = pd.read_csv('segments.csv', delimiter=',',header=0, usecols=range(0,3))
# User list comprehension to create a list of lists from Dataframe rows
list_of_rows = [list(row) for row in df.values]

#print(df.iloc[2])
streams_list=[]
file_path=""
# input stream object
in_file = ffmpeg.input(file_path)

for i,line in enumerate(list_of_rows):
    #print (line[0])
    if pd.notna(line[0]):  # if no new filename keep the previous
        file_path=line[0]
        print (file_path)
    print(file_path)

    segment = ffmpeg.input(file_path)
    segment.trim(start=line[1],end=line[2])
    streams_list.append(ffmpeg.trim(in_file, start=line[1],end=line[2]))

concatted=""
# concat all segments
for seg in streams_list:
    concatted+=seg
print(concatted)
# output stream object
output = ffmpeg.output(concatted, 'dummy2.mp4').node





# import ffmpeg
# #import subprocess
#
# # Build synthetic video files (with audio):
# ##############################################################
# # subprocess.run('ffmpeg -y -f lavfi -i testsrc=size=1280x720:rate=30 -f lavfi -i sine=frequency=500 -c:v libx264 -c:a ac3 -ar 22050 -t 100 in.mp4')
# # subprocess.run('ffmpeg -y -f lavfi -i mandelbrot=size=1280x720:rate=30 -f lavfi -i sine=frequency=1000 -c:v libx264 -c:a ac3 -ar 22050 -t 10 outro.mp4')
# ##############################################################
#
#
# main_video = ffmpeg.input('in.mp4')
# outro = ffmpeg.input('outro.mp4')
#
# # Assuming frame rate is 30 fps, 33.3 seconds applies 1000 frames.
# v1 = main_video.video.filter('trim',start=line[1],end=line[2])  # Use trim filter for the video.
# v2 = outro.video
# a2 = outro.audio
#
# joined = ffmpeg.concat(v1, a1, v2, a2, v=1, a=1).node
# v3 = joined[0]
# a3 = joined[1]
#
# out = ffmpeg.output(v3, a3, 'out.mp4')
# out.run()



# another reference

# https://stackoverflow.com/questions/22731999/python-video-editing-how-to-trim-videos
# https://www.programcreek.com/python/example/117479/ffmpeg.output
