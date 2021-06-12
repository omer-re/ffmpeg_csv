import pandas as pd
import ffmpeg
file_path=r"\cat movie.mp4"

in_file = ffmpeg.input(file_path)
trim1 = ffmpeg.trim(in_file, start="00:00:10", end="00:00:20")
trim2 = ffmpeg.trim(in_file, start="00:00:40", end="00:00:50")
trim3 = ffmpeg.trim(in_file, start="00:00:52", end="00:00:55")
concatted = ffmpeg.concat(trim1, trim2, trim3)
output = ffmpeg.output(concatted, 'dummy2.mp4')

def test_node_repr():
    file_path=r"cat movie.mp4"
    in_file = ffmpeg.input(file_path)
    trim1 = ffmpeg.trim(in_file, start="00:00:10", end="00:00:20")
    trim2 = ffmpeg.trim(in_file, start="00:00:40", end="00:00:50")
    trim3 = ffmpeg.trim(in_file, start="00:00:52", end="00:00:55")
    concatted = ffmpeg.concat(trim1, trim2, trim3)
    output = ffmpeg.output(concatted, 'dummy2.mp4')

    assert repr(in_file.node) == 'input(filename={!r}) <{}>'.format(
        file_path, in_file.node.short_hash
    )

    assert repr(concatted.node) == 'concat(n=3) <{}>'.format(concatted.node.short_hash)
    assert repr(output.node) == 'output(filename={!r}) <{}>'.format(
        'dummy2.mp4', output.node.short_hash
    )


test_node_repr()
