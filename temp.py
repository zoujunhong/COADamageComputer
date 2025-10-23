# -*- coding: utf-8 -*-
name_list = ['荣光祭礼风帽', '进化祭礼头盔', '罪火深牢头盔', '兽灵咒歌头盔', '审判圣卫头盔', '裁决寒影头盔', '永恒罪火胸甲', '进化祭礼胸甲', '罪火深牢胸甲', '兽灵咒歌胸甲', '审判圣卫胸甲', '裁决寒影胸甲', '兽灵圣诗护手', '进化祭礼护手', '罪火深牢护手', '兽灵咒歌护手', '审判圣卫护手', '裁决寒影护手', '神谕圣卫护腿', '进化祭礼裤子', '罪火深牢裤子', '兽灵咒歌裤子', '审判圣卫裤子', '裁决寒影裤子', '裁决神使长靴', '进化祭礼鞋子', '罪火深牢鞋子', '兽灵咒歌鞋子', '审判圣卫鞋子', '裁决寒影鞋子']

import cv2
import numpy as np
for name in name_list:
    img = cv2.imdecode(np.fromfile(name+'.png', dtype=np.uint8), 1)
    new_name = "合铸-"+name+'.png'
    print(new_name)
    cv2.imencode('.png', img)[1].tofile(new_name)
    # cv2.imwrite(new_name, img)