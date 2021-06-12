import pandas as pd
import ffmpeg
file_path=r"\cat movie.mp4"

main_video = ffmpeg.input(file_path)
outro = ffmpeg.input('outro.mp4')
# Assuming frame rate is 30 fps, 33.3 seconds applies 1000 frames.
v1 = main_video.video.filter('trim',start="00:00:10", end="00:00:20")  # Use trim filter for the video.
v2 = outro.video
a2 = outro.audio

joined = ffmpeg.concat(v1, v2, a2, v1).node
v3 = joined[0]
a3 = joined[1]

out = ffmpeg.output(v3, a3, 'out.mp4')
