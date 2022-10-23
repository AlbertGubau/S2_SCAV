# This file is able to  convert from mono to stereo and vice-versa the BBB video, Albert Gubau NIA: 229416
import os


def display_yuv_histogram(in_file, out_file, option):

    if option == 1:  # Stereo to mono command line
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -ac 1 ' + str(out_file) + '.mp4 '

    elif option == 2:  # Mono to stereo command line
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -ac 2 ' + str(out_file) + '.mp4 '

    # If the user doesn't write the correct value, exit the program
    else:
        command_line = ''
        print("The option value is not valid, exiting program... ")

    # Call the command line in the terminal
    os.system(command_line)


# Interactive menu
print("")
print("############################## MONO/STEREO PROGRAM ############################################")
print("")
print("The input video file must be an mp4 in the same folder as this python script.")
print("Please do not specify the format of the input/output. ")
print("If we ask you for the name of the input/output, just write the name,")
print("for example, if you want the name to be frog, just write frog, do not write frog.mp4 ")
print("in the input/output name.")
print("")

# Option input
opt = int(input("Choose what do you want to do:\n1 --> Stereo to mono\n2 --> Mono to stereo"
                "\nWrite the number here: "))

# Input filename
input_name = str(input("Write the name of the input file: "))

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
