import os
import glob
import cv2

all_mp4 = sorted(glob.glob('*.mp4'))
print(all_mp4)
for mp4 in all_mp4:
    category = mp4.split('_')[0]
    id = mp4.split('_')[-1][:-4]
    print(category)
    print(id)
    if category != 'Selfie':
        img = cv2.imread(r'C:/Users/user/Documents/Alex/Research/VideoDeblurring/NUS_frames/'+category+'/'+id+'/00001.png')
        cv2.imwrite(category+'_'+id+'.jpg', img)
    else:
        img = cv2.imread(r'C:/Users/user/Documents/Alex/Research/VideoDeblurring/ECCV2018/' + id + '/00001.png')
        cv2.imwrite(category + '_' + id + '.jpg', img)