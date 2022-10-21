# This file is able to cut N seconds of the BBB video, Albert Gubau NIA: 229416
import os


def cut_n_seconds(in_file, out_file, n):

    secs = n % (24 * 3600)
    hrs = secs // 3600
    secs %= 3600
    mins = secs // 60
    secs %= 60

    command_line = 'ffmpeg -ss 00:00:00 -i ' + str(in_file) \
                   + '.mp4 -to ' + str(hrs) + ':' + str(mins) + ':' + str(secs) \
                   + ' -c copy ' + str(out_file) + '.mp4'

    print(command_line)
    os.system(command_line)


print("")
print("############################## CUT N SECONDS PROGRAM ############################################")
print("The input video file must be an mp4 "
      "in the same folder as this python script, ")
print("and the name of it needs to be 'BBB'. Please do not specify the format of the output ")
print("in the output name.")
print("")

N = int(input("Choose the seconds that you want to cut from the BBB video: "))

input_name = "BBB"
boolean = False
while not boolean:
    output_name = str(input("Choose the name of the output file: "))
    if output_name != input_name:
        boolean = True

cut_n_seconds(input_name, output_name, N)
