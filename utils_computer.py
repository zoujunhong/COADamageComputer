import math

def damage_compute(status_dict: dict, boost=False): # 根据输入的属性计算最终伤害
    shuqiang =  1 + status_dict['属强'] / 220
    baoji    =  1 + min(status_dict['暴击']/100, 1) * status_dict['暴伤'] / 100
    kezhi    =  1 + status_dict['克制'] / 100
    shangti  =  1 + status_dict['伤提'] / 100
    if boost:
        tiaojian =  1 + (status_dict['技伤'] + status_dict['共鸣伤']) / 100
    else:
        tiaojian =  1 + (status_dict['技伤'] + min(1, status_dict['共鸣覆盖率'])**0.5 * status_dict['共鸣伤']) / 100
    shushang =  1 + status_dict['属伤'] / 100
    gongji   =  status_dict['破防攻击'] + status_dict['攻击'] * 4000 / (4000+status_dict['防御'])
    fushang  =  1 + status_dict['附伤'] / 100
    teshu    =  1 + status_dict['特殊'] / 100
    bodong   =  1 + status_dict['波动'] / 100
    shuangyue = 1.08 + status_dict['职业增伤'] / 100
    beilv =  1 + status_dict['倍率'] / 100
    jinengshanghai =  1 + status_dict['技能伤害提升'] / 100
    jinengjiasu =  1 + status_dict['技能加速'] / 100
    lengque =  1 / (1 - status_dict['冷却缩减']/100)
    texiao = 1 + status_dict['特效占比'] / (100 - status_dict['特效占比'])
    zhongshang = 1 + status_dict['最终伤害'] / 100
    zhuangbeizengshang = 1 + status_dict['装备增伤'] / 100
    zhuangbeitexiao = 1 + status_dict['装备特效'] / 100
    huixin = 1 + min(status_dict['会心']/100, 1) * status_dict['会心伤害'] / 100
    burst_damage = shuqiang * baoji * kezhi * shangti * tiaojian * shushang * gongji * fushang * teshu * shuangyue * beilv * jinengshanghai * texiao * bodong * zhongshang * zhuangbeizengshang * huixin * zhuangbeitexiao * status_dict['独立增伤']
    return burst_damage, jinengjiasu * lengque


def add_equipment(status_dict: dict, equipment: dict, boost=False): 
    for key in equipment.keys():
        if '_' in key:
            key_target = key.split('_')[0]
        else:
            key_target = key

        if key_target not in status_dict.keys():
            status_dict[key_target] = 0
        
        if isinstance(equipment[key], list):
            if boost:
                value = equipment[key][0]
            else:
                value = equipment[key][0] * (equipment[key][1]**0.5)
        else:
            value = equipment[key]
        
        if key_target == '独立':
            status_dict[key_target] = status_dict[key_target] * (1 + value / 100)
        else:
            status_dict[key_target] = status_dict[key_target] + value
        
    return status_dict 

def remove_equipment(status_dict: dict, equipment: dict): 
    for key in equipment.keys():
        if key not in status_dict.keys():
            status_dict[key] = equipment[key]
        else:
            status_dict[key] = status_dict[key] - equipment[key]
    return status_dict 

def outfit_count(status: dict, outfit_dict: dict): # 根据装备部位计算激活套装情况
    outfits = []
    
    for outfit_name in outfit_dict.keys():
        if outfit_name in status.keys():
            for num in outfit_dict[outfit_name].keys():
                if status[outfit_name] >= int(num):
                    outfits.append((outfit_name, num))
        
    if ('老天空','2') in outfits and ('新天空','2') in outfits:
        outfits.remove(('老天空','2'))
    
    if ('老天空','3') in outfits and ('新天空','3') in outfits:
        outfits.remove(('老天空','3'))
        
    if ('老天空','5') in outfits and ('新天空','5') in outfits:
        outfits.remove(('老天空','5'))
    return outfits
        
    
    