import pandas as pd
import numpy as np

import os
import shutil

for i in range(1,5):
    os.makedirs('train_images/'+str(i))

os.makedirs('train_images/tempcopies')

train_data = pd.read_csv('train.csv')

encoded_pixels = train_data.EncodedPixels

# print(train_data)
# print(train_data.EncodedPixels)
# print(encoded_pixels[1])
# print(train_data.iloc[0,0])
# print(range(len(encoded_pixels)))

included_rows =[]

# print(type(encoded_pixels[1]))
#
# if isinstance(encoded_pixels[0],str):
#     print('it worked')

for index in range(len(encoded_pixels)):
    if isinstance(encoded_pixels[index], str):
        included_rows.append(index)

# print(included_rows)

# print(train_data.iloc[included_rows[0],0])
#
# example = train_data.iloc[included_rows[0],0]
#
# print(type(example))
# example_split = example.split('_')
# print(example_split)

# example_split[0] is img name, [1] is class, both are str
# want to move [0] into folder of [1]

#first copy file into holding folder so name is consistent
#move orig file into first class
#if FileNotFoundError occurs then access from holding folder
#delete holding folder at the end

for row in included_rows:
    img_data = train_data.iloc[row,0].split('_')
    img_name = img_data[0]
    img_class = img_data[1]
    try:
        shutil.copy('train_images/'+img_name,'train_images/tempcopies')
        shutil.move('train_images/'+img_name,'train_images/'+img_class)
    except FileNotFoundError:
        shutil.copy('train_images/tempcopies/'+img_name,'train_images/'+img_class)

shutil.rmtree('train_images/tempcopies')

print('DONE')
