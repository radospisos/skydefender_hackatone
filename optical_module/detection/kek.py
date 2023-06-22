import os
import numpy as np
import shutil

images_folder = '/Users/rodion/Downloads/shahed_dataset_1/images/'
annots_folder = '/Users/rodion/Downloads/shahed_dataset_1/txt/'

images = os.listdir(images_folder)
images = [x.split('.')[0] for x in images]
annots = os.listdir(images_folder)
annots = [x.split('.')[0] for x in annots]

print(images==annots)

#x = np.random.rand(100, 5)
np.random.shuffle(images)
images.remove('')
for i in images:
    if i == '':
        print('huevo')
#print(images)

#print(images==annots)
#print(set(images) == set(annots))
print(len(images))
#print(images[:5])
train, val, test = images[:4451], images[4451:4551], images[4551:4651]

print((len(train) + len(val) + len(test)) == len(images))

#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/train')
#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/train/images')
#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/train/txt')
#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/val')
#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/val/images')
#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/val/txt')
#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/test')
#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/test/images')
#os.mkdir('/Users/rodion/Downloads/shahed_dataset_1/test/txt')

for i in test:
    print(i)
    shutil.copyfile(images_folder + i + '.png', '/Users/rodion/Downloads/shahed_dataset_1/val/images/' + i + '.png')
    shutil.copyfile(annots_folder + i + '.png.txt', '/Users/rodion/Downloads/shahed_dataset_1/val/txt/' + i + '.png.txt')
