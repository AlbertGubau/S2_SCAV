# This file is able to cut N seconds of the BBB video, Albert Gubau NIA: 229416
import os


def display_yuv_histogram(in_file, out_file, option):

    if option == 1:  # Stereo to mono
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -ac 1 ' + str(out_file) + '.mp4 '

    elif option == 2:  # Mono to stereo
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -ac 2 ' + str(out_file) + '.mp4 '

    else:
        command_line = ''
        print("The option value is not valid, exiting program... ")

    os.system(command_line)


print("")
print("############################## MONO/STEREO PROGRAM ############################################")
print("")
print("The input video file must be an mp4 in the same folder as this python script, ")
print("and the name of it needs to be 'BBB'. Please do not specify the format of the output ")
print("in the output name.")
print("")

opt = int(input("Choose what do you want to do:\n1 --> Stereo to mono\n2 --> Mono to stereo"
                "\nWrite the number here: "))

input_name = "BBB"
boolean = False

while not boolean:
    output_name = str(input("Choose the name of the output file: "))
    if output_name != input_name:
        boolean = True

    print("")
    print("The chosen name is the same as the input, try with another name.")
    print("")

display_yuv_histogram(input_name, output_name, opt)
