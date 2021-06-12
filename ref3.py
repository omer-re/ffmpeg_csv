import ffmpeg
file_path=r"\cat movie.mp4"

in_file = ffmpeg.input(file_path)
(
    ffmpeg
    .concat(
        in_file.trim(start_pts ='00:00:10'),
        in_file.trim(end_pts ='00:00:22'),
    )
    .drawbox(50, 50, 120, 120, color='red', thickness=5)
    .output('out.mp4')
    .run()
)
