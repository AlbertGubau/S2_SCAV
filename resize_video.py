# This file is able to resize the BBB video, Albert Gubau NIA: 229416
import os


def display_yuv_histogram(in_file, out_file, option):

    # We check what resolution is the one that the user wants, and we store the correspondent command line
    if option == 1:
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -vf scale=1280:720 ' + str(out_file) + '.mp4 '

    elif option == 2:
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -vf scale=854:420 ' + str(out_file) + '.mp4 '

    elif option == 3:
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -vf scale=360:240 ' + str(out_file) + '.mp4 '

    elif option == 4:
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -vf scale=160:120 ' + str(out_file) + '.mp4 '

    # If the user doesn't write the correct value, exit the program
    else:
        command_line = ''
        print("The option value is not valid, exiting program... ")

    # Call the command line in the terminal
    os.system(command_line)


# Interactive menu
print("")
print("############################## RESIZE VIDEO PROGRAM ############################################")
print("")
print("The input video file must be an mp4 in the same folder as this python script, ")
print("and the name of it needs to be 'BBB'. Please do not specify the format of the output ")
print("If we ask you for the name of the output, just write the name,")
print("for example, if you want the name to be frog, just write frog, do not write frog.mp4 ")
print("in the output name.")
print("")

# Input for the option
opt = int(input("Choose what resize do you want:"
                "\n1 --> 1280x720"
                "\n2 --> 854x420"
                "\n3 --> 360x240"
                "\n4 --> 160x120 "
                "\nWrite the number here: "))

# Input filename
input_name = "BBB"

# We check that the output name chosen by the user is not the same as the input name
boolean = False
while not boolean:
    output_name = str(input("Choose the name of the output file: "))
    if output_name != input_name:
        boolean = True

    print("")
    print("The chosen name is the same as the input, try with another name.")
    print("")

# Call the function
display_yuv_histogram(input_name, output_name, opt)
