# This file is able to cut N seconds of the BBB video, Albert Gubau NIA: 229416
import os


def display_yuv_histogram(in_file, out_file):
    if os.path.exists(out_file):
        os.remove(out_file)

    command_line1 = 'ffmpeg -i ' + str(in_file) + '.mp4 -ac 1 ' + str(out_file) + '.mp4 '

    command_line2 = 'ffmpeg -i ' + str(in_file) + '.mp4 -ac 2 ' + str(out_file) + '.mp4 '

    # Choose between command_line1 and command_line2! DUEE TO!!!


    os.system(command_line2)


input_name = "BBB"
boolean = False

while not boolean:
    output_name = str(input("Choose the name of the output file: "))
    if output_name != input_name:
        boolean = True

display_yuv_histogram(input_name, output_name)
