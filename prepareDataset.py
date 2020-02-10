import glob
import os
from PIL import Image
from tqdm import tqdm
import random
import subprocess
import sys


def main():
    process_dir = "./data/img/"
    
    try:
        os.mkdir("./data")
    except OSError:
        print("Creation of the directory failed")
    else:
        print("Successfully created the directory")

    try:
        os.mkdir(process_dir)
    except OSError:
        print("Creation of the directory failed")
    else:
        print("Successfully created the directory")


    dir = input("Enter image directory: ")
    image_path = "{}/*.jpg".format(dir)

    for file_path in tqdm(glob.glob(image_path)):

        file, ext = os.path.splitext(file_path)
        file_name = file_path.split("\\")[-1].split(".")[0]

        # file_name = file_path.split("\\")[-1]
        im = Image.open(file_path)
        width, height = im.size

        im.thumbnail((width / 2, height / 2))
        im.save(process_dir + file_name + ".resize.jpeg", "JPEG")

        rotate_image90 = im.rotate(angle=90)
        rotate_image90.save(process_dir +
                            file_name + ".rotate90.jpeg", "jpeg")

        rotate_image180 = im.rotate(angle=180)
        rotate_image180.save(process_dir +
                             file_name + ".rotate180.jpeg", "jpeg")

        rotate_image270 = im.rotate(angle=270)
        rotate_image270.save(process_dir +
                             file_name + ".rotate270.jpeg", "jpeg")

    split_data_set(process_dir)


def split_data_set(image_dir):

    f_val = open("data/test.txt", 'w')
    f_train = open("data/train.txt", 'w')

    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    count = 0
    for f in os.listdir(image_dir):
        count += 1
        print(count)
        file_extension = f.split(".")[-1]
        local_file_reference = image_dir.split("/")

        if(file_extension == "jpg" or file_extension == "jpeg"):
            ind += 1

            if ind in test_array:
                f_val.write(local_file_reference[1]+ '/' + local_file_reference[2] + '/' +f+'\n')
            else:
                f_train.write(local_file_reference[1]+ '/' + local_file_reference[2] + '/' +f+'\n')

if __name__ == "__main__":
    main()