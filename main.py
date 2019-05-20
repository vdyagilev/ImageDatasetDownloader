import os
import random
from pathlib import Path
from google_images_download import google_images_download

dataset_path = "C:/Users/Vladimir Dyagilev/Desktop/AI Projects/dataset/"

def main():
    query = input("Enter a class to search for (enter DONE to stop): ")

    classes = []
    while query != "DONE":
        classes.append(query)
        query = input("Enter a class to search for (enter DONE to quit): ")

    sample_num = int(input("How many images should we download for each class? "))
    create_folders(classes)
    download_images(classes, sample_num)

def remove_anomalies():
    pass

def organize_dataset():
    # send 10% of data into test set and 10% of data into validation set, randomly
    for root, dirs, files in os.walk(dataset_path+'train/'):
        for file_ in files:
            class_name = Path(root).stem

            chance = random.randint(1, 100)
            if chance <= 10:
                os.rename(dataset_path + 'train/' + class_name + '/'+ file_,
                          dataset_path + 'test/' + class_name + '/' + file_)
            elif chance <= 20:
                os.rename(dataset_path + 'train/' + class_name + '/' + file_,
                          dataset_path + 'valid/' + class_name + '/' + file_)
            else:
                pass


def download_images(classes: [str], sample_num: int):
    for query in classes:
        download_image(query, sample_num)
    organize_dataset()


def download_image(query: str, count: int):
    """Downloads 'count' number of images of the query into the dataset folder.
    Randomly places images into train, test, or valid folders.
    """
    response = google_images_download.googleimagesdownload()
    # we download all images initially into the test folder
    absolute_image_paths = response.download({'keywords': query, 'limit': count, 'output_directory': dataset_path + 'train/'})


def create_folders(classes: [str]):
    """Creates folders for the containment of the dataset, based on Imagenet"""
    path = dataset_path

    try:

        for query in classes:
            os.makedirs(path + 'train/' + query)
            os.makedirs(path + 'test/' + query)
            os.makedirs(path + 'valid/' + query)

    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        pass
        # print("Successfully created the directory %s" % path)


main()
