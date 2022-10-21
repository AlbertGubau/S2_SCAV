# This file is able to cut N seconds of the BBB video, Albert Gubau NIA: 229416
import os


def display_yuv_histogram(in_file, out_file):
    command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -vf "split=2[a][b], [b]histogram, format=yuva444p[hh],' \
                                                 '[a][hh]overlay=x=W-w:y=H-h" -c:a copy ' + str(out_file) + '.mp4 '

    # -c:a is due to re-encoding the video because we are filtering it

    os.system(command_line)


print("")
print("############################## YUV HISTOGRAM PROGRAM ############################################")
print("")
print("The input video file must be an mp4 in the same folder as this python script, ")
print("and the name of it needs to be 'BBB'. Please do not specify the format of the output ")
print("in the output name.")
print("")

input_name = "BBB"
boolean = False

while not boolean:
    output_name = str(input("Choose the name of the output file: "))
    if output_name != input_name:
        boolean = True

    print("")
    print("The chosen name is the same as the input, try with another name.")
    print("")

display_yuv_histogram(input_name, output_name)
