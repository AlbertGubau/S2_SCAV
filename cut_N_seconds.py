# This file is able to cut N seconds of the BBB video, Albert Gubau NIA: 229416
import os


def cut_n_seconds(in_file, out_file, n):
    if os.path.exists(out_file):
        os.remove(out_file)

    command_line = 'ffmpeg -ss 00:00:00 -i ' + str(in_file) + '.mp4 -t 00:00:' + str(n) + ' -c copy ' + str(
        out_file) + '.mp4'
    print(command_line)
    os.system(command_line)


N = input("Choose the seconds that you want to cut from the video: ")
input_name = "BBB"
boolean = False
while not boolean:
    output_name = str(input("Choose the name of the output file: "))
    if output_name != input_name:
        boolean = True

cut_n_seconds(input_name, output_name, N)
