import os
import cv2
import numpy as np

namelist = os.listdir('./icon_origin/')
for name in namelist:
    img = cv2.imdecode(np.fromfile(os.path.join('./icon_origin/', name), dtype=np.uint8), 1)
    img = cv2.resize(img, (128,128), interpolation=cv2.INTER_AREA)
    empty = np.zeros((128,24,3))
    # print(empty.shape, img.shape)
    img = np.concatenate((empty, img), axis=1)
    cv2.imencode('.png', img)[1].tofile(os.path.join('./icon/', name))