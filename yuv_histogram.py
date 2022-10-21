# This file is able to cut N seconds of the BBB video, Albert Gubau NIA: 229416
import os


def display_yuv_histogram(in_file, out_file):
    if os.path.exists(out_file):
        os.remove(out_file)

    command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -vf "split=2[a][b], [b]histogram, format=yuva444p[hh],' \
                                                 '[a][hh]overlay=x=W-w:y=H-h" -c:a copy ' + str(out_file) + '.mp4 '

    # -c:a is due to re-encoding the video because we are filtering it

    os.system(command_line)


input_name = "BBB"
boolean = False

while not boolean:
    output_name = str(input("Choose the name of the output file: "))
    if output_name != input_name:
        boolean = True

display_yuv_histogram(input_name, output_name)
