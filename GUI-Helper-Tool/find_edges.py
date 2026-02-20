import argparse        # one line to let the user choose any picture. Without it, hard-code the filename
import cv2
import os              # clean & correct filenames on every operating system. Without it, write filenames by hand

from gui_utils import EdgeFinder


def main():
    file = "GUI-Helper-Tool/yellow.jpg"
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)         # read the photo whose name is in the args box.

    if img is None:
        print("Cannot find the picture: ", file)
        return
    
    cv2.imshow('input', img)

    edge_finder = EdgeFinder(img, filter_size=13, threshold1=28, threshold2=115)     # (image, start with three numbers on its sliders)

    print ("Edge parameters:")                          # After the slider window is closed (you pressed any key), write on the black screen:
    print (f"GaussianBlur Filter Size: {edge_finder.filterSize()}")        # then the three numbers you chose with the sliders
    print (f"Threshold1: {edge_finder.threshold1()}")              # what number is on the 1st threshold
    print (f"Threshold2: {edge_finder.threshold2()}")              # what number is on the 2nd?

    (head, tail) = os.path.split(file)             # Take the picture name (example: "pictures/cat.jpg"). Cut it in two pieces: head = "pictures" , tail = "cat.jpg"

    (root, ext) = os.path.splitext(tail)                  # Now, take only "cat.jpg" and split it.

    smoothed_filename = os.path.join("output_images", + "/" + root + "-smoothed" + ext)         # Glue new names together
    edge_filename = os.path.join("output_images", + "/" + root + "-edges" + ext)

    cv2.imwrite(smoothed_filename, edge_finder.smoothedImage())         # cv2.imwrite(label , photo )
    cv2.imwrite(edge_filename, edge_finder.edgeImage())

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()