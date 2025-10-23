import math

def damage_compute(status_dict: dict): # 根据输入的属性计算最终伤害
    shuqiang =  1 + status_dict['属强'] / 220
    baoshang = status_dict['爆伤'] + 2 * max(0, status_dict['暴击']-100)
    baoji =     1 + min(status_dict['暴击']/100, 1) * baoshang / 100
    kezhi =     1 + status_dict['克制'] / 100
    shangti =   1 + status_dict['伤提'] / 100
    tiaojian =  1 + (status_dict['技伤'] + status_dict['共鸣伤']*0.9) / 100
    shushang =  1 + status_dict['属伤'] / 100
    gongji =    status_dict['破防攻击'] + status_dict['基础攻击'] * (1 + status_dict['攻击加成']/100) * (1 + status_dict['基础力量'] * (1+status_dict['力量加成']/100)/1000) * 3500 / (3500+status_dict['怪物防御']*(1-status_dict['穿透']/100)*(1-status_dict['防御降低']/100))
    fushang =   1 + status_dict['附伤'] / 100
    teshu =     1 + status_dict['特殊'] / 100
    return shuqiang * baoji * kezhi * shangti * tiaojian * shushang * gongji * fushang * teshu

def change_equipment(status_dict: dict, equipment: dict, add: bool): # 根据equipment中的装备进行属性变化，add=True表示穿上装备，否则表示脱下装备
    coeff = 1 if add == True else -1
    for key in equipment.keys():
        status_dict[key] = status_dict[key] + coeff * equipment[key]
    return status_dict 

def outfit_count(equip_list): # 根据装备部位计算激活套装情况
    count = {"苦毒I":0, "苦毒II":0, "闪鳞I":0, "闪鳞II":0, "恶欲I":0, "恶欲II":0}
    for e1 in equip_list:
        count[e1] += 1
        if e1 == '苦毒II':
            count['苦毒I'] += 1
        elif e1 == '闪鳞II':
            count['闪鳞I'] += 1
        elif e1 == '恶欲II':
            count['恶欲I'] += 1
    
    outfit = []
    if count['苦毒II'] >= 2:
        outfit.append(['套装2', '苦毒II'])
    if count['苦毒II'] >= 3:
        outfit.append(['套装3', '苦毒II'])
    if count['苦毒II'] >= 5:
        outfit.append(['套装5', '苦毒II'])
    
    if count['闪鳞II'] >= 2:
        outfit.append(['套装2', '闪鳞II'])
    if count['闪鳞II'] >= 3:
        outfit.append(['套装3', '闪鳞II'])
    if count['闪鳞II'] >= 5:
        outfit.append(['套装5', '闪鳞II'])
    
    if count['恶欲II'] >= 2:
        outfit.append(['套装2', '恶欲II'])
    if count['恶欲II'] >= 3:
        outfit.append(['套装3', '恶欲II'])
    if count['恶欲II'] >= 5:
        outfit.append(['套装5', '恶欲II'])
    
    if count['苦毒I'] >= 2 and count['苦毒II'] < 2:
        outfit.append(['套装2', '苦毒I'])
    if count['苦毒I'] >= 3 and count['苦毒II'] < 3:
        outfit.append(['套装3', '苦毒I'])
    if count['苦毒I'] >= 5 and count['苦毒II'] < 5:
        outfit.append(['套装5', '苦毒I'])
        
    if count['闪鳞I'] >= 2 and count['闪鳞II'] < 2:
        outfit.append(['套装2', '闪鳞I'])
    if count['闪鳞I'] >= 3 and count['闪鳞II'] < 3:
        outfit.append(['套装3', '闪鳞I'])
    if count['闪鳞I'] >= 5 and count['闪鳞II'] < 5:
        outfit.append(['套装5', '闪鳞I'])
    
    if count['恶欲I'] >= 2 and count['恶欲II'] < 2:
        outfit.append(['套装2', '恶欲I'])
    if count['恶欲I'] >= 3 and count['恶欲II'] < 3:
        outfit.append(['套装3', '恶欲I'])
    if count['恶欲I'] >= 5 and count['恶欲II'] < 5:
        outfit.append(['套装5', '恶欲I'])
    
    return outfit
        
    
    