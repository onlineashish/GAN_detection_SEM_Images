import os
import shutil
import random

def split_data(folder_path, split_percentage):
    # Get the subfolder names
    # subfolders = [f.name for f in os.scandir(folder_path) if f.is_dir()]

    # for subfolder in subfolders:
        # subfolder_path = os.path.join(folder_path, subfolder)
        subfolder_path = folder_path
        # Get the list of files in the subfolder
        files = [f.name for f in os.scandir(subfolder_path) if f.is_file()]
        num_files = len(files)
        num_train = int(num_files * split_percentage[0] / 100)
        num_val = int(num_files * split_percentage[1] / 100)

        # Shuffle the files
        random.shuffle(files)

        # Split the files into train, val, and test sets
        train_files = files[:num_train]
        val_files = files[num_train:num_train + num_val]
        test_files = files[num_train + num_val:]

        # Create directories for train, val, and test sets if they don't exist
        for dataset in ['train', 'val', 'test']:
            dataset_path = os.path.join(folder_path, dataset)
            os.makedirs(dataset_path, exist_ok=True)

        # Move files to their respective directories
        for dataset, files_list in [('train', train_files), ('val', val_files), ('test', test_files)]:
            for file in files_list:
                src = os.path.join(subfolder_path, file)
                dest = os.path.join(folder_path, dataset, file)
                shutil.move(src, dest)

# Prompt the user for input
split_percentage_train = float(input("Enter the percentage for the training set: "))
split_percentage_val = float(input("Enter the percentage for the validation set: "))
split_percentage_test = 100 - (split_percentage_train + split_percentage_val)

# Folder path containing subfolders real and fake
folder_path = "/home/ashish/stylegan2-ada-pytorch/out1000"

# Split the data
split_data(folder_path, (split_percentage_train, split_percentage_val))

print("Data split successfully!")
