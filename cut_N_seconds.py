# This file is able to cut N seconds of the BBB video, Albert Gubau NIA: 229416
import os


def cut_n_seconds(in_file, out_file, n):

    # Convert the seconds of the input to the format hours:minutes:seconds
    secs = n % (24 * 3600)
    hrs = secs // 3600
    secs %= 3600
    mins = secs // 60
    secs %= 60

    # Create the command line that uses ffmpeg to cut the video
    command_line = 'ffmpeg -ss 00:00:00 -i ' + str(in_file) \
                   + '.mp4 -to ' + str(hrs) + ':' + str(mins) + ':' + str(secs) \
                   + ' -c copy ' + str(out_file) + '.mp4'

    # Call the command line in the terminal
    os.system(command_line)


# Interactive menu
print("")
print("############################## CUT N SECONDS PROGRAM ############################################")
print("")
print("The input video file must be an mp4 in the same folder as this python script, ")
print("and the name of it needs to be 'BBB'. Please do not specify the format of the output ")
print("If we ask you for the name of the output, just write the name,")
print("for example, if you want the name to be frog, just write frog, do not write frog.mp4 ")
print("in the output name.")
print("")

# Number of seconds of the new duration
N = int(input("Choose the seconds that you want to cut from the BBB video: "))

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
cut_n_seconds(input_name, output_name, N)
