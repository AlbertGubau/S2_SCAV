# This file is able to execute any of the Seminar 2 of SCAV exercises, Albert Gubau NIA: 229416
import os


def all_in_one(option):

    # Choose the command line taking into account the exercise
    if option == 1:
        os.system('python cut_N_seconds.py')
    elif option == 2:
        os.system('python yuv_histogram.py')
    elif option == 3:
        os.system('python resize_video.py')
    elif option == 4:
        os.system('python mono_stereo.py')

    # If the user doesn't write the correct value, exit the program
    else:
        print("Wrong input, exiting program...")


# Esthetics
print("")
print("############################## ALL IN ONE PROGRAM ############################################")
print("")

# Option input
opt = int(input("Choose the exercise you want to launch: "
                "\n\n1 --> Cut N seconds from the BBB video"
                "\n2 --> Create a video with the YUV histogram of the BBB video together with it"
                "\n3 --> Resize the BBB video"
                "\n4 --> Mono/Stereo converter"
                "\n\nWrite the number here: "))

# Call the function
all_in_one(opt)
