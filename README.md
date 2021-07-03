# ffmpeg_csv
Get video segments from an mp4 file using csv marks

## instructions:
In the same folder
put 'ffmpeg_csv.py' file AND 'segments.csv' file.

Enter the csv file, and set the path for the video, then choose start-end time points.
if you are using the same video in a row - you don't have to type it again.

After you have done listing all the segments - save the CSV and exit.

now run the python script with "python ffmpeg_csv.py"
the concatenated video will be called "edited_<LAST VIDEO SEGMENT NAME>.mp4" and will be found in the folder where the last video you filled is.
  
![This is how the CSV file should look like when opened in Excel:](https://raw.githubusercontent.com/omer-re/ffmpeg_csv/main/readme_images/csv%20on%20excel.png)
  
![This is how the CSV file should look like when opened in Notepad:](https://raw.githubusercontent.com/omer-re/ffmpeg_csv/main/readme_images/csv%20on%20notepad.png)
