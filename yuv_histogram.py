# This file is able to display the YUV histogram together with the BBB video, Albert Gubau NIA: 229416
import os


def display_yuv_histogram(in_file, out_file):

    # Create the command line that uses ffmpeg to store a new video with the YUV histogram
    command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -vf "split=2[a][b], [b]histogram, format=yuva444p[hh],' \
                                                 '[a][hh]overlay=x=W-w:y=H-h" -c:a copy ' + str(out_file) + '.mp4 '

    # with split, que can choose the two variables a (video) and b (histogram to split)

    # the format specifies the chroma subsampling method, in this case 4:4:4

    # overlay=x=W-w:y=H-h ensures that the YUV histogram is shown at
    # the bottom right taking into account width and height

    # -c:a is due to re-encoding of the video because we are filtering it with the histogram overlay

    # Call the command line in the terminal
    os.system(command_line)


# Interactive menu
print("")
print("############################## YUV HISTOGRAM PROGRAM ############################################")
print("")
print("The input video file must be an mp4 in the same folder as this python script, ")
print("and the name of it needs to be 'BBB'. Please do not specify the format of the output ")
print("If we ask you for the name of the output, just write the name,")
print("for example, if you want the name to be frog, just write frog, do not write frog.mp4 ")
print("in the output name.")
print("")

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
display_yuv_histogram(input_name, output_name)
