from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *  # 导入引用图标的函数
import sys
from gui import Ui_Form as GUI
import json
from utils_computer import *
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()  # 用于访问父类的方法和属性
        self.ui = GUI()
        self.ui.setupUi(self)
        self.setStyleSheet("background:rgb(199,237,204);color:black;")
        self.setWindowTitle("晶核面板计算器")  # 设置标题
        self.setWindowIcon(QIcon("icon\\icon.png"))  # 加载窗口图标
        
        self.default_equipment = ['' for i in range(115)]
        for i in range(6):
            self.default_equipment.append('-1.0')  
        self.default_equipment.append('0.0')  
        self.default_equipment.append('0') 
        for i in range(5):
            self.default_equipment.append('0')  
        
        self.default_equipment.append('')  
        self.default_equipment.append('0.0') 
        self.default_equipment.append('')  
        self.default_equipment.append('')  
        self.default_equipment.append('14000')
        
        for i in range(10):
            self.default_equipment.append('')
        
        self.previous_equipment = ['' for i in range(143)]
        self.current_equipment = ['' for i in range(143)]
        
        '''
        装备
        '''
        menu = QMenu()
        with open('data/装备-头盔.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_head, name, 0)
        self.ui.equip_head.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-胸甲.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_armor, name, 1)
        self.ui.equip_armor.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-手套.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_hand, name, 2)
        self.ui.equip_hand.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-裤子.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_leg, name, 3)
        self.ui.equip_leg.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-鞋子.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_shoe, name, 4)
        self.ui.equip_shoe.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-头盔.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_head_2, name, 133)
        self.ui.equip_head_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-胸甲.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_armor_2, name, 134)
        self.ui.equip_armor_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-手套.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_hand_2, name, 135)
        self.ui.equip_hand_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-裤子.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_leg_2, name, 136)
        self.ui.equip_leg_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-鞋子.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_shoe_2, name, 137)
        self.ui.equip_shoe_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-武器.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_weapon, name, 5)
        self.ui.equip_weapon.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-项链.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_necklace, name, 6)
        self.ui.equip_necklace.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-护腕.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_bracer, name, 7)
        self.ui.equip_bracer.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-戒指.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_ring, name, 8)
        self.ui.equip_ring.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-印章.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_seal, name, 9)
        self.ui.equip_seal.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-护符.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_amulet, name, 10)
        self.ui.equip_amulet.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-项链.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_necklace_2, name, 138)
        self.ui.equip_necklace_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-护腕.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_bracer_2, name, 139)
        self.ui.equip_bracer_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-戒指.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_ring_2, name, 140)
        self.ui.equip_ring_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-印章.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_seal_2, name, 141)
        self.ui.equip_seal_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/合铸-护符.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_amulet_2, name, 142)
        self.ui.equip_amulet_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/装备-秘宝.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.equip_treasure, name, 11)
        self.ui.equip_treasure.setMenu(menu)
        
        '''
        徽记
        '''
        menu = QMenu()
        with open('data/徽记-头盔.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_head, name, 12)
        self.ui.emblem_head.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-胸甲.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_armor, name, 13)
        self.ui.emblem_armor.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-手套.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_hand, name, 14)
        self.ui.emblem_hand.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-裤子.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_leg, name, 15)
        self.ui.emblem_leg.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-鞋子.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_shoe, name, 16)
        self.ui.emblem_shoe.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-武器.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_weapon, name, 17)
        self.ui.emblem_weapon.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-项链.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_necklace, name, 18)
        self.ui.emblem_necklace.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-护腕.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_bracer, name, 19)
        self.ui.emblem_bracer.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-戒指.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_ring, name, 20)
        self.ui.emblem_ring.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-印章.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_seal, name, 21)
        self.ui.emblem_seal.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-护符.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_amulet, name, 22)
        self.ui.emblem_amulet.setMenu(menu)
        
        menu = QMenu()
        with open('data/徽记-秘宝.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.emblem_treasure, name, 130)
        self.ui.emblem_treasure.setMenu(menu)
        
        '''
        强化
        '''
        menu = QMenu()
        with open('data/强化-力智.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_head, name, 23)
        self.ui.enhancement_head.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-生命.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_armor, name, 24)
        self.ui.enhancement_armor.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-力智.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_hand, name, 25)
        self.ui.enhancement_hand.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-生命.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_leg, name, 26)
        self.ui.enhancement_leg.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-力智.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_shoe, name, 27)
        self.ui.enhancement_shoe.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-武器.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_weapon, name, 28)
        self.ui.enhancement_weapon.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-力智.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_necklace, name, 29)
        self.ui.enhancement_necklace.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-力智.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_bracer, name, 30)
        self.ui.enhancement_bracer.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-力智.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_ring, name, 31)
        self.ui.enhancement_ring.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_seal, name, 32)
        self.ui.enhancement_seal.setMenu(menu)
        
        menu = QMenu()
        with open('data/强化-左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.enhancement_amulet, name, 33)
        self.ui.enhancement_amulet.setMenu(menu)
        
        '''
        铭刻
        '''
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_head_1, name, 34)
        self.ui.engrave_head_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_head_2, name, 35)
        self.ui.engrave_head_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_head_3, name, 36)
        self.ui.engrave_head_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-胸裤.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_armor_1, name, 37)
        self.ui.engrave_armor_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-胸裤.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_armor_2, name, 38)
        self.ui.engrave_armor_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-胸裤.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_armor_3, name, 39)
        self.ui.engrave_armor_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_hand_1, name, 40)
        self.ui.engrave_hand_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_hand_2, name, 41)
        self.ui.engrave_hand_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_hand_3, name, 42)
        self.ui.engrave_hand_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-胸裤.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_leg_1, name, 43)
        self.ui.engrave_leg_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-胸裤.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_leg_2, name, 44)
        self.ui.engrave_leg_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-胸裤.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_leg_3, name, 45)
        self.ui.engrave_leg_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_shoe_1, name, 46)
        self.ui.engrave_shoe_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_shoe_2, name, 47)
        self.ui.engrave_shoe_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-头胸鞋.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_shoe_3, name, 48)
        self.ui.engrave_shoe_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_weapon_1, name, 49)
        self.ui.engrave_weapon_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_weapon_2, name, 50)
        self.ui.engrave_weapon_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_weapon_3, name, 51)
        self.ui.engrave_weapon_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_necklace_1, name, 52)
        self.ui.engrave_necklace_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_necklace_2, name, 53)
        self.ui.engrave_necklace_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_necklace_3, name, 54)
        self.ui.engrave_necklace_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_bracer_1, name, 55)
        self.ui.engrave_bracer_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_bracer_2, name, 56)
        self.ui.engrave_bracer_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_bracer_3, name, 57)
        self.ui.engrave_bracer_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_ring_1, name, 58)
        self.ui.engrave_ring_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_ring_2, name, 59)
        self.ui.engrave_ring_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-首饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_ring_3, name, 60)
        self.ui.engrave_ring_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_seal_1, name, 61)
        self.ui.engrave_seal_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_seal_2, name, 62)
        self.ui.engrave_seal_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_seal_3, name, 63)
        self.ui.engrave_seal_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_amulet_1, name, 64)
        self.ui.engrave_amulet_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_amulet_2, name, 65)
        self.ui.engrave_amulet_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/铭刻-武器左右槽.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.engrave_amulet_3, name, 66)
        self.ui.engrave_amulet_3.setMenu(menu)
        
        '''
        宠物
        '''
        menu = QMenu()
        with open('data/宠物-名称.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_1, name, 67)
        self.ui.pet_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/宠物-名称.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_2, name, 68)
        self.ui.pet_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/宠物-星级.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_level_1, name, 69)
        self.ui.pet_level_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/宠物-星级.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_level_2, name, 70)
        self.ui.pet_level_2.setMenu(menu)
        
        '''
        魂印
        '''
        menu = QMenu()
        with open('data/宠物魂印-力.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_emblem_1_1, name, 71)
        self.ui.pet_emblem_1_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/宠物魂印-力.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_emblem_2_1, name, 72)
        self.ui.pet_emblem_2_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/宠物魂印-技.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_emblem_1_2, name, 73)
        self.ui.pet_emblem_1_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/宠物魂印-技.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_emblem_2_2, name, 74)
        self.ui.pet_emblem_2_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/宠物魂印-速.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_emblem_1_3, name, 75)
        self.ui.pet_emblem_1_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/宠物魂印-速.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.pet_emblem_2_3, name, 76)
        self.ui.pet_emblem_2_3.setMenu(menu)
        
        '''
        卡牌
        '''
        menu = QMenu()
        with open('data/卡牌.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.card_1, name, 77)
        self.ui.card_1.setMenu(menu)
        
        menu = QMenu()
        with open('data/卡牌.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.card_2, name, 78)
        self.ui.card_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/卡牌.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.card_3, name, 79)
        self.ui.card_3.setMenu(menu)
        
        menu = QMenu()
        with open('data/卡牌.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.card_4, name, 80)
        self.ui.card_4.setMenu(menu)
        
        menu = QMenu()
        with open('data/卡牌.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.card_5, name, 131)
        self.ui.card_5.setMenu(menu)
        
        '''
        时装
        '''
        menu = QMenu()
        with open('data/时装-称号.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.title, name, 81)
        self.ui.title.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装-武器.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.weapon, name, 82)
        self.ui.weapon.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装-光环.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.aureole, name, 83)
        self.ui.aureole.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装-头饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.headwear, name, 84)
        self.ui.headwear.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装-服装.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.cloth, name, 85)
        self.ui.cloth.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装-配饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.accessory, name, 86)
        self.ui.accessory.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装-面饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.facewear, name, 87)
        self.ui.facewear.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装-徽章.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.badge, name, 88)
        self.ui.badge.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装-足迹.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.footmark, name, 89)
        self.ui.footmark.setMenu(menu)
        
        '''
        时装徽记
        '''
        menu = QMenu()
        with open('data/时装徽记-称号.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.title_2, name, 90)
        self.ui.title_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装徽记-武器.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.weapon_2, name, 91)
        self.ui.weapon_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装徽记-光环.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.aureole_2, name, 92)
        self.ui.aureole_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装徽记-头饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.headwear_2, name, 93)
        self.ui.headwear_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装徽记-服装.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.cloth_2, name, 94)
        self.ui.cloth_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装徽记-配饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.accessory_2, name, 95)
        self.ui.accessory_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装徽记-面饰.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.facewear_2, name, 96)
        self.ui.facewear_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装徽记-徽章.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.badge_2, name, 97)
        self.ui.badge_2.setMenu(menu)
        
        menu = QMenu()
        with open('data/时装徽记-足迹.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.footmark_2, name, 98)
        self.ui.footmark_2.setMenu(menu)
        
        '''
        药酒矿战
        '''
        menu = QMenu()
        with open('data/增益-元素药.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.buff_stats, name, 99)
        self.ui.buff_stats.setMenu(menu)
        
        menu = QMenu()
        with open('data/增益-强袭药.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.buff_atk, name, 100)
        self.ui.buff_atk.setMenu(menu)
        
        menu = QMenu()
        with open('data/增益-酒.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.buff_wine, name, 101)
        self.ui.buff_wine.setMenu(menu)
        
        menu = QMenu()
        with open('data/增益-龙息.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.buff_dragon, name, 102)
        self.ui.buff_dragon.setMenu(menu)
        
        menu = QMenu()
        with open('data/增益-疾风.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.buff_wind, name, 103)
        self.ui.buff_wind.setMenu(menu)
        
        menu = QMenu()
        with open('data/增益-矿战.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.buff_mine, name, 104)
        self.ui.buff_mine.setMenu(menu)
        
        menu = QMenu()
        with open('data/增益-克制药.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.buff_counter, name, 105)
        self.ui.buff_counter.setMenu(menu)
        
        menu = QMenu()
        with open('data/神格.json', 'r', encoding='utf-8') as f:
            name_list=json.load(f).keys()
        for name in name_list:
            self.add_menu(menu, self.ui.eros_level, name, 128)
        self.ui.eros_level.setMenu(menu)
        
        self.ui.save.clicked.connect(self.save)
        self.ui.load.clicked.connect(self.load)
        self.ui.compute.clicked.connect(self.compute_damage_new)
        
        self.ui.add.clicked.connect(self.add)
        self.ui.remove.clicked.connect(self.remove)
        self.ui.reset.clicked.connect(self.reset)
        
        with open('data/辅助效果.json', 'r', encoding='utf-8') as f:
            self.data_fuzhu = json.load(f)
            buff_list = self.data_fuzhu.keys()
            menu = QMenu()
            for name in buff_list:
                self.add_menu_buff(menu, name)
            self.ui.buff_path_choose.setMenu(menu)
    
    def add(self):
        buff_list = self.ui.buff_list.toPlainText().split('\n')[:-1]
        data = self.ui.buff_path_choose.text()
        if data == '增益选择':
            return 0
        else:
            if data not in buff_list:
                buff_list.append(data)
        
        self.display_buff_list(buff_list)
    
    def remove(self):
        buff_list = self.ui.buff_list.toPlainText().split('\n')[:-1]
        data = self.ui.buff_path_choose.text()
        if data == '增益选择':
            return 0
        else:
            if data in buff_list:
                buff_list.remove(data)
        
        self.display_buff_list(buff_list)
    
    def reset(self):
        buff_list = []
        self.display_buff_list(buff_list)
    
    def add_menu_buff(self, menu: QMenu, name: str):
        action = QAction(name, self)
        action.triggered.connect(lambda: self.ui.buff_path_choose.setText(name))
        menu.addAction(action)
        return menu
    
    def display_buff_list(self, buff_list):
        string = ''
        
        for data in buff_list:
            string = string + data + '\n'
        
        self.ui.buff_list.setPlainText(string)
    
    def add_menu(self, menu: QMenu, button: QPushButton, name: str, rank: int):
        action = QAction(name, self)
        action.triggered.connect(lambda: self.trans_equipment(button, name, rank))
        menu.addAction(action)
        return menu
    
    def set_icon(self, button: QPushButton, equipment_list: list, rank: int):
        button.setText('')
        name = equipment_list[rank]
        button.setIcon(QIcon('icon\\'+name+'.png'))
        button.setIconSize(QSize(100,50))
    
    def trans_equipment(self, button: QPushButton, name: str, rank: int):
        button.setText('')
        button.setIcon(QIcon('icon\\'+name+'.png'))
        button.setIconSize(QSize(100,50))
        self.current_equipment[rank] = name
    
    def save(self,):
        # self.current_equipment[106] = str(self.ui.dot_ratio.value())
        self.current_equipment[107] = str(self.ui.loop_atk.value())
        self.current_equipment[108] = str(self.ui.loop_critical_damage.value())
        self.current_equipment[109] = str(self.ui.loop_critical.value())
        self.current_equipment[110] = str(self.ui.loop_stats.value())
        self.current_equipment[111] = str(self.ui.loop_cd.value())
        self.current_equipment[112] = str(self.ui.loop_agility.value())
        self.current_equipment[113] = str(self.ui.loop_strength.value())
        self.current_equipment[114] = str(self.ui.loop_skill_damage.value())
        # self.current_equipment[115] = str(self.ui.boost_bufan4.value())
        # self.current_equipment[116] = str(self.ui.boost_bufan6.value())
        # self.current_equipment[117] = str(self.ui.boost_zhuoyue4.value())
        # self.current_equipment[118] = str(self.ui.boost_zhuoyue7.value())
        # self.current_equipment[119] = str(self.ui.boost_zhuoyue9.value())
        # self.current_equipment[120] = str(self.ui.boost_chaoran9.value())
        # self.current_equipment[121] = str(self.ui.atk_boost.value())
        self.current_equipment[122] = str(self.ui.car_level.value())
        self.current_equipment[123] = str(self.ui.buff_atk_2.value())
        self.current_equipment[124] = str(self.ui.buff_base_pure_atk.value())
        self.current_equipment[125] = str(self.ui.buff_pure_atk.value())
        self.current_equipment[126] = str(self.ui.buff_damage_amp.value())
        self.current_equipment[127] = str(self.ui.buff_counter_2.value())
        self.current_equipment[129] = str(self.ui.buff_pure_attack_damage_boost.value())
        self.current_equipment[132] = str(self.ui.defense.value())
        
        self.previous_equipment = self.current_equipment
        
        with open('save.txt','w',encoding='utf-8') as file:
            for i in range(len(self.previous_equipment)):
                s = self.previous_equipment[i] +'\n'
                file.write(s)
        
        with open('save_fuzhu.txt','w',encoding='utf-8') as file:
            file.write(self.ui.buff_list.toPlainText())
        
        self.compute_damage_old()
        self.compute_damage_new()
    
    def load(self,):
        with open('save.txt','r',encoding='utf-8') as file:
            self.previous_equipment = file.readlines()
        
        with open('save_fuzhu.txt','r',encoding='utf-8') as file:
            self.ui.buff_list.setPlainText(file.read())
        
        for i in range(len(self.previous_equipment)):
            self.previous_equipment[i] = self.previous_equipment[i][:-1]
        
        if len(self.previous_equipment) < len(self.default_equipment):
            self.previous_equipment += self.default_equipment[len(self.previous_equipment):]
        
        self.current_equipment = self.previous_equipment
        
        self.set_icon(self.ui.equip_head, self.current_equipment, 0)
        self.set_icon(self.ui.equip_armor, self.current_equipment, 1)
        self.set_icon(self.ui.equip_hand, self.current_equipment, 2)
        self.set_icon(self.ui.equip_leg, self.current_equipment, 3)
        self.set_icon(self.ui.equip_shoe, self.current_equipment, 4)
        self.set_icon(self.ui.equip_weapon, self.current_equipment, 5)
        self.set_icon(self.ui.equip_necklace, self.current_equipment, 6)
        self.set_icon(self.ui.equip_bracer, self.current_equipment, 7)
        self.set_icon(self.ui.equip_ring, self.current_equipment, 8)
        self.set_icon(self.ui.equip_seal, self.current_equipment, 9)
        self.set_icon(self.ui.equip_amulet, self.current_equipment, 10)
        self.set_icon(self.ui.equip_treasure, self.current_equipment, 11)
        
        self.set_icon(self.ui.equip_head_2, self.current_equipment, 133)
        self.set_icon(self.ui.equip_armor_2, self.current_equipment, 134)
        self.set_icon(self.ui.equip_hand_2, self.current_equipment, 135)
        self.set_icon(self.ui.equip_leg_2, self.current_equipment, 136)
        self.set_icon(self.ui.equip_shoe_2, self.current_equipment, 137)
        self.set_icon(self.ui.equip_necklace_2, self.current_equipment, 138)
        self.set_icon(self.ui.equip_bracer_2, self.current_equipment, 139)
        self.set_icon(self.ui.equip_ring_2, self.current_equipment, 140)
        self.set_icon(self.ui.equip_seal_2, self.current_equipment, 141)
        self.set_icon(self.ui.equip_amulet_2, self.current_equipment, 142)
        
        self.set_icon(self.ui.emblem_head, self.current_equipment, 12)
        self.set_icon(self.ui.emblem_armor, self.current_equipment, 13)
        self.set_icon(self.ui.emblem_hand, self.current_equipment, 14)
        self.set_icon(self.ui.emblem_leg, self.current_equipment, 15)
        self.set_icon(self.ui.emblem_shoe, self.current_equipment, 16)
        self.set_icon(self.ui.emblem_weapon, self.current_equipment, 17)
        self.set_icon(self.ui.emblem_necklace, self.current_equipment, 18)
        self.set_icon(self.ui.emblem_bracer, self.current_equipment, 19)
        self.set_icon(self.ui.emblem_ring, self.current_equipment, 20)
        self.set_icon(self.ui.emblem_seal, self.current_equipment, 21)
        self.set_icon(self.ui.emblem_amulet, self.current_equipment, 22)
        self.set_icon(self.ui.enhancement_head, self.current_equipment, 23)
        self.set_icon(self.ui.enhancement_armor, self.current_equipment, 24)
        self.set_icon(self.ui.enhancement_hand, self.current_equipment, 25)
        self.set_icon(self.ui.enhancement_leg, self.current_equipment, 26)
        self.set_icon(self.ui.enhancement_shoe, self.current_equipment, 27)
        self.set_icon(self.ui.enhancement_weapon, self.current_equipment, 28)
        self.set_icon(self.ui.enhancement_necklace, self.current_equipment, 29)
        self.set_icon(self.ui.enhancement_bracer, self.current_equipment, 30)
        self.set_icon(self.ui.enhancement_ring, self.current_equipment, 31)
        self.set_icon(self.ui.enhancement_seal, self.current_equipment, 32)
        self.set_icon(self.ui.enhancement_amulet, self.current_equipment, 33)
        self.set_icon(self.ui.engrave_head_1, self.current_equipment, 34)
        self.set_icon(self.ui.engrave_head_2, self.current_equipment, 35)
        self.set_icon(self.ui.engrave_head_3, self.current_equipment, 36)
        self.set_icon(self.ui.engrave_armor_1, self.current_equipment, 37)
        self.set_icon(self.ui.engrave_armor_2, self.current_equipment, 38)
        self.set_icon(self.ui.engrave_armor_3, self.current_equipment, 39)
        self.set_icon(self.ui.engrave_hand_1, self.current_equipment, 40)
        self.set_icon(self.ui.engrave_hand_2, self.current_equipment, 41)
        self.set_icon(self.ui.engrave_hand_3, self.current_equipment, 42)
        self.set_icon(self.ui.engrave_leg_1, self.current_equipment, 43)
        self.set_icon(self.ui.engrave_leg_2, self.current_equipment, 44)
        self.set_icon(self.ui.engrave_leg_3, self.current_equipment, 45)
        self.set_icon(self.ui.engrave_shoe_1, self.current_equipment, 46)
        self.set_icon(self.ui.engrave_shoe_2, self.current_equipment, 47)
        self.set_icon(self.ui.engrave_shoe_3, self.current_equipment, 48)
        self.set_icon(self.ui.engrave_weapon_1, self.current_equipment, 49)
        self.set_icon(self.ui.engrave_weapon_2, self.current_equipment, 50)
        self.set_icon(self.ui.engrave_weapon_3, self.current_equipment, 51)
        self.set_icon(self.ui.engrave_necklace_1, self.current_equipment, 52)
        self.set_icon(self.ui.engrave_necklace_2, self.current_equipment, 53)
        self.set_icon(self.ui.engrave_necklace_3, self.current_equipment, 54)
        self.set_icon(self.ui.engrave_bracer_1, self.current_equipment, 55)
        self.set_icon(self.ui.engrave_bracer_2, self.current_equipment, 56)
        self.set_icon(self.ui.engrave_bracer_3, self.current_equipment, 57)
        self.set_icon(self.ui.engrave_ring_1, self.current_equipment, 58)
        self.set_icon(self.ui.engrave_ring_2, self.current_equipment, 59)
        self.set_icon(self.ui.engrave_ring_3, self.current_equipment, 60)
        self.set_icon(self.ui.engrave_seal_1, self.current_equipment, 61)
        self.set_icon(self.ui.engrave_seal_2, self.current_equipment, 62)
        self.set_icon(self.ui.engrave_seal_3, self.current_equipment, 63)
        self.set_icon(self.ui.engrave_amulet_1, self.current_equipment, 64)
        self.set_icon(self.ui.engrave_amulet_2, self.current_equipment, 65)
        self.set_icon(self.ui.engrave_amulet_3, self.current_equipment, 66)
        self.set_icon(self.ui.pet_1, self.current_equipment, 67)
        self.set_icon(self.ui.pet_2, self.current_equipment, 68)
        self.set_icon(self.ui.pet_level_1, self.current_equipment, 69)
        self.set_icon(self.ui.pet_level_2, self.current_equipment, 70)
        self.set_icon(self.ui.pet_emblem_1_1, self.current_equipment, 71)
        self.set_icon(self.ui.pet_emblem_2_1, self.current_equipment, 72)
        self.set_icon(self.ui.pet_emblem_1_2, self.current_equipment, 73)
        self.set_icon(self.ui.pet_emblem_2_2, self.current_equipment, 74)
        self.set_icon(self.ui.pet_emblem_1_3, self.current_equipment, 75)
        self.set_icon(self.ui.pet_emblem_2_3, self.current_equipment, 76)
        self.set_icon(self.ui.card_1, self.current_equipment, 77)
        self.set_icon(self.ui.card_2, self.current_equipment, 78)
        self.set_icon(self.ui.card_3, self.current_equipment, 79)
        self.set_icon(self.ui.card_4, self.current_equipment, 80)
        self.set_icon(self.ui.title, self.current_equipment, 81)
        self.set_icon(self.ui.weapon, self.current_equipment, 82)
        self.set_icon(self.ui.aureole, self.current_equipment, 83)
        self.set_icon(self.ui.headwear, self.current_equipment, 84)
        self.set_icon(self.ui.cloth, self.current_equipment, 85)
        self.set_icon(self.ui.accessory, self.current_equipment, 86)
        self.set_icon(self.ui.facewear, self.current_equipment, 87)
        self.set_icon(self.ui.badge, self.current_equipment, 88)
        self.set_icon(self.ui.footmark, self.current_equipment, 89)
        self.set_icon(self.ui.title_2, self.current_equipment, 90)
        self.set_icon(self.ui.weapon_2, self.current_equipment, 91)
        self.set_icon(self.ui.aureole_2, self.current_equipment, 92)
        self.set_icon(self.ui.headwear_2, self.current_equipment, 93)
        self.set_icon(self.ui.cloth_2, self.current_equipment, 94)
        self.set_icon(self.ui.accessory_2, self.current_equipment, 95)
        self.set_icon(self.ui.facewear_2, self.current_equipment, 96)
        self.set_icon(self.ui.badge_2, self.current_equipment, 97)
        self.set_icon(self.ui.footmark_2, self.current_equipment, 98)
        self.set_icon(self.ui.buff_stats, self.current_equipment, 99)
        self.set_icon(self.ui.buff_atk, self.current_equipment, 100)
        self.set_icon(self.ui.buff_wine, self.current_equipment, 101)
        self.set_icon(self.ui.buff_dragon, self.current_equipment, 102)
        self.set_icon(self.ui.buff_wind, self.current_equipment, 103)
        self.set_icon(self.ui.buff_mine, self.current_equipment, 104)
        self.set_icon(self.ui.buff_counter, self.current_equipment, 105)
        
        # self.ui.dot_ratio.setValue(float(self.current_equipment[106]))
        self.ui.loop_atk.setValue(int(self.current_equipment[107]))
        self.ui.loop_critical_damage.setValue(float(self.current_equipment[108]))
        self.ui.loop_critical.setValue(float(self.current_equipment[109]))
        self.ui.loop_stats.setValue(float(self.current_equipment[110]))
        self.ui.loop_cd.setValue(float(self.current_equipment[111]))
        self.ui.loop_agility.setValue(int(self.current_equipment[112]))
        self.ui.loop_strength.setValue(int(self.current_equipment[113]))
        self.ui.loop_skill_damage.setValue(int(self.current_equipment[114]))
        
        # self.ui.boost_bufan4.setValue(float(self.current_equipment[115]))
        # self.ui.boost_bufan6.setValue(float(self.current_equipment[116]))
        # self.ui.boost_zhuoyue4.setValue(float(self.current_equipment[117]))
        # self.ui.boost_zhuoyue7.setValue(float(self.current_equipment[118]))
        # self.ui.boost_zhuoyue9.setValue(float(self.current_equipment[119]))
        # self.ui.boost_chaoran9.setValue(float(self.current_equipment[120]))
        # self.ui.atk_boost.setValue(float(self.current_equipment[121]))
        self.ui.car_level.setValue(int(self.current_equipment[122]))
        
        self.ui.buff_atk_2.setValue(int(self.current_equipment[123]))
        self.ui.buff_base_pure_atk.setValue(int(self.current_equipment[124]))
        self.ui.buff_pure_atk.setValue(int(self.current_equipment[125]))
        self.ui.buff_damage_amp.setValue(int(self.current_equipment[126]))
        self.ui.buff_counter_2.setValue(int(self.current_equipment[127]))
        
        self.set_icon(self.ui.eros_level, self.current_equipment, 128)
        
        self.ui.buff_pure_attack_damage_boost.setValue(float(self.current_equipment[129]))
        
        self.set_icon(self.ui.emblem_treasure, self.current_equipment, 130)
        self.set_icon(self.ui.card_5, self.current_equipment, 131)
        
        self.ui.defense.setValue(int(self.current_equipment[132]))
        
        self.compute_damage_old()
        self.compute_damage_new()
    
    def compute_damage_new(self):
        # self.current_equipment[106] = str(self.ui.dot_ratio.value())
        self.current_equipment[107] = str(self.ui.loop_atk.value())
        self.current_equipment[108] = str(self.ui.loop_critical_damage.value())
        self.current_equipment[109] = str(self.ui.loop_critical.value())
        self.current_equipment[110] = str(self.ui.loop_stats.value())
        self.current_equipment[111] = str(self.ui.loop_cd.value())
        self.current_equipment[112] = str(self.ui.loop_agility.value())
        self.current_equipment[113] = str(self.ui.loop_strength.value())
        self.current_equipment[114] = str(self.ui.loop_skill_damage.value())
        # self.current_equipment[115] = str(self.ui.boost_bufan4.value())
        # self.current_equipment[116] = str(self.ui.boost_bufan6.value())
        # self.current_equipment[117] = str(self.ui.boost_zhuoyue4.value())
        # self.current_equipment[118] = str(self.ui.boost_zhuoyue7.value())
        # self.current_equipment[119] = str(self.ui.boost_zhuoyue9.value())
        # self.current_equipment[120] = str(self.ui.boost_chaoran9.value())
        # self.current_equipment[121] = str(self.ui.atk_boost.value())
        self.current_equipment[122] = str(self.ui.car_level.value())
        self.current_equipment[123] = str(self.ui.buff_atk_2.value())
        self.current_equipment[124] = str(self.ui.buff_base_pure_atk.value())
        self.current_equipment[125] = str(self.ui.buff_pure_atk.value())
        self.current_equipment[126] = str(self.ui.buff_damage_amp.value())
        self.current_equipment[127] = str(self.ui.buff_counter_2.value())
        self.current_equipment[129] = str(self.ui.buff_pure_attack_damage_boost.value())
        self.current_equipment[132] = str(self.ui.defense.value())
        
        final_boost_status, final_base_status, burst_damage, total_damage, accelerate, boost_buff_enhancement, base_buff_enhancement = self.compute_damage(self.current_equipment)
        
        self.ui.new_stats.setText(str(int(final_boost_status["属强"])))
        self.ui.new_critical.setText(str('%.1f'%final_boost_status["暴击"]))
        self.ui.new_critical_damage.setText(str(int(final_boost_status["暴伤"])))
        self.ui.new_counter.setText(str(int(final_boost_status["克制"])))
        self.ui.new_damage_amp.setText(str(int(final_boost_status["伤提"])))
        self.ui.new_skill_damage.setText(str(int(final_boost_status["技伤"])))
        
        self.ui.new_resonance_damage.setText(str(int(final_boost_status["共鸣伤"])))
        self.ui.new_stats_damage.setText(str(int(final_boost_status["属伤"])))
        self.ui.new_pure_atk.setText(str(int(final_boost_status["破防攻击"])))
        self.ui.new_atk.setText(str(int(final_boost_status["攻击"])))
        self.ui.new_addition_damage.setText(str(int(final_boost_status["附伤"])))
        self.ui.new_spetial_damage.setText(str(int(final_boost_status["特殊"])))
        
        self.ui.new_shuangyue.setText(str(int(final_boost_status["职业增伤"])))
        self.ui.new_amp.setText(str(int(final_boost_status["倍率"])))
        self.ui.new_skill_amp.setText(str(int(final_boost_status["技能伤害提升"])))
        self.ui.new_skill_acc.setText(str(int(final_boost_status["技能加速"])))
        self.ui.new_cd_reduction.setText(str(int(final_boost_status["冷却缩减"])))
        self.ui.new_dot_ratio.setText(str(int(final_boost_status["特效占比"])))
        
        self.ui.new_defense_ignore.setText(str(int(final_boost_status["穿透"])))
        self.ui.new_defense_reduction.setText(str(int(final_boost_status["减防"])))
        
        self.ui.new_huixin.setText(str(int(final_boost_status["会心"])))
        self.ui.new_huixin_damage.setText(str(int(final_boost_status["会心伤害"])))
        self.ui.new_buff_boost.setText(str(int(boost_buff_enhancement*100)))
        
        self.ui.delta_stats.setText('%d'%(float(self.ui.new_stats.toPlainText())-float(self.ui.old_stats.toPlainText())))
        self.ui.delta_critical.setText('%.1f'%(float(self.ui.new_critical.toPlainText())-float(self.ui.old_critical.toPlainText())))
        self.ui.delta_critical_damage.setText('%d'%(float(self.ui.new_critical_damage.toPlainText())-float(self.ui.old_critical_damage.toPlainText())))
        self.ui.delta_counter.setText('%d'%(float(self.ui.new_counter.toPlainText())-float(self.ui.old_counter.toPlainText())))
        self.ui.delta_damage_amp.setText('%d'%(float(self.ui.new_damage_amp.toPlainText())-float(self.ui.old_damage_amp.toPlainText())))
        self.ui.delta_skill_damage.setText('%d'%(float(self.ui.new_skill_damage.toPlainText())-float(self.ui.old_skill_damage.toPlainText())))
        self.ui.delta_resonance_damage.setText('%d'%(float(self.ui.new_resonance_damage.toPlainText())-float(self.ui.old_resonance_damage.toPlainText())))
        self.ui.delta_stats_damage.setText('%d'%(float(self.ui.new_stats_damage.toPlainText())-float(self.ui.old_stats_damage.toPlainText())))
        self.ui.delta_pure_atk.setText('%d'%(float(self.ui.new_pure_atk.toPlainText())-float(self.ui.old_pure_atk.toPlainText())))
        self.ui.delta_atk.setText('%d'%(float(self.ui.new_atk.toPlainText())-float(self.ui.old_atk.toPlainText())))
        self.ui.delta_addition_damage.setText('%d'%(float(self.ui.new_addition_damage.toPlainText())-float(self.ui.old_addition_damage.toPlainText())))
        self.ui.delta_spetial_damage.setText('%d'%(float(self.ui.new_spetial_damage.toPlainText())-float(self.ui.old_spetial_damage.toPlainText())))
        
        self.ui.delta_shuangyue.setText('%d'%(float(self.ui.new_shuangyue.toPlainText())-float(self.ui.old_shuangyue.toPlainText())))
        self.ui.delta_amp.setText('%d'%(float(self.ui.new_amp.toPlainText())-float(self.ui.old_amp.toPlainText())))
        self.ui.delta_skill_amp.setText('%d'%(float(self.ui.new_skill_amp.toPlainText())-float(self.ui.old_skill_amp.toPlainText())))
        self.ui.delta_skill_acc.setText('%d'%(float(self.ui.new_skill_acc.toPlainText())-float(self.ui.old_skill_acc.toPlainText())))
        self.ui.delta_cd_reduction.setText('%d'%(float(self.ui.new_cd_reduction.toPlainText())-float(self.ui.old_cd_reduction.toPlainText())))
        self.ui.delta_dot_ratio.setText('%d'%(float(self.ui.new_dot_ratio.toPlainText())-float(self.ui.old_dot_ratio.toPlainText())))
        
        self.ui.delta_defense_ignore.setText('%d'%(float(self.ui.new_defense_ignore.toPlainText())-float(self.ui.old_defense_ignore.toPlainText())))
        self.ui.delta_defense_reduction.setText('%d'%(float(self.ui.new_defense_reduction.toPlainText())-float(self.ui.old_defense_reduction.toPlainText())))
        
        self.ui.delta_huixin.setText('%d'%(float(self.ui.new_huixin.toPlainText())-float(self.ui.old_huixin.toPlainText())))
        self.ui.delta_huixin_damage.setText('%d'%(float(self.ui.new_huixin_damage.toPlainText())-float(self.ui.old_huixin_damage.toPlainText())))
        self.ui.delta_buff_boost.setText('%d'%(float(self.ui.new_buff_boost.toPlainText())-float(self.ui.old_buff_boost.toPlainText())))
 
        
        self.ui.new_stats_2.setText(str(int(final_base_status["属强"])))
        self.ui.new_critical_2.setText(str('%.1f'%final_base_status["暴击"]))
        self.ui.new_critical_damage_2.setText(str(int(final_base_status["暴伤"])))
        self.ui.new_counter_2.setText(str(int(final_base_status["克制"])))
        self.ui.new_damage_amp_2.setText(str(int(final_base_status["伤提"])))
        self.ui.new_skill_damage_2.setText(str(int(final_base_status["技伤"])))
        
        self.ui.new_resonance_damage_2.setText(str(int(final_base_status["共鸣伤"])))
        self.ui.new_stats_damage_2.setText(str(int(final_base_status["属伤"])))
        self.ui.new_pure_atk_2.setText(str(int(final_base_status["破防攻击"])))
        self.ui.new_atk_2.setText(str(int(final_base_status["攻击"])))
        self.ui.new_addition_damage_2.setText(str(int(final_base_status["附伤"])))
        self.ui.new_spetial_damage_2.setText(str(int(final_base_status["特殊"])))
        
        self.ui.new_shuangyue_2.setText(str(int(final_base_status["职业增伤"])))
        self.ui.new_amp_2.setText(str(int(final_base_status["倍率"])))
        self.ui.new_skill_amp_2.setText(str(int(final_base_status["技能伤害提升"])))
        self.ui.new_skill_acc_2.setText(str(int(final_base_status["技能加速"])))
        self.ui.new_cd_reduction_2.setText(str(int(final_base_status["冷却缩减"])))
        self.ui.new_dot_ratio_2.setText(str(int(final_base_status["特效占比"])))
        
        self.ui.new_defense_ignore_2.setText(str(int(final_base_status["穿透"])))
        self.ui.new_defense_reduction_2.setText(str(int(final_base_status["减防"])))
        
        self.ui.new_huixin_2.setText(str(int(final_base_status["会心"])))
        self.ui.new_huixin_damage_2.setText(str(int(final_base_status["会心伤害"])))
        self.ui.new_buff_boost_2.setText(str(int(base_buff_enhancement*100)))
        
        self.ui.delta_stats_2.setText('%d'%(float(self.ui.new_stats_2.toPlainText())-float(self.ui.old_stats_2.toPlainText())))
        self.ui.delta_critical_2.setText('%.1f'%(float(self.ui.new_critical_2.toPlainText())-float(self.ui.old_critical_2.toPlainText())))
        self.ui.delta_critical_damage_2.setText('%d'%(float(self.ui.new_critical_damage_2.toPlainText())-float(self.ui.old_critical_damage_2.toPlainText())))
        self.ui.delta_counter_2.setText('%d'%(float(self.ui.new_counter_2.toPlainText())-float(self.ui.old_counter_2.toPlainText())))
        self.ui.delta_damage_amp_2.setText('%d'%(float(self.ui.new_damage_amp_2.toPlainText())-float(self.ui.old_damage_amp_2.toPlainText())))
        self.ui.delta_skill_damage_2.setText('%d'%(float(self.ui.new_skill_damage_2.toPlainText())-float(self.ui.old_skill_damage_2.toPlainText())))
        self.ui.delta_resonance_damage_2.setText('%d'%(float(self.ui.new_resonance_damage_2.toPlainText())-float(self.ui.old_resonance_damage_2.toPlainText())))
        self.ui.delta_stats_damage_2.setText('%d'%(float(self.ui.new_stats_damage_2.toPlainText())-float(self.ui.old_stats_damage_2.toPlainText())))
        self.ui.delta_pure_atk_2.setText('%d'%(float(self.ui.new_pure_atk_2.toPlainText())-float(self.ui.old_pure_atk_2.toPlainText())))
        self.ui.delta_atk_2.setText('%d'%(float(self.ui.new_atk_2.toPlainText())-float(self.ui.old_atk.toPlainText())))
        self.ui.delta_addition_damage_2.setText('%d'%(float(self.ui.new_addition_damage_2.toPlainText())-float(self.ui.old_addition_damage_2.toPlainText())))
        self.ui.delta_spetial_damage_2.setText('%d'%(float(self.ui.new_spetial_damage_2.toPlainText())-float(self.ui.old_spetial_damage_2.toPlainText())))
        
        self.ui.delta_shuangyue_2.setText('%d'%(float(self.ui.new_shuangyue_2.toPlainText())-float(self.ui.old_shuangyue_2.toPlainText())))
        self.ui.delta_amp_2.setText('%d'%(float(self.ui.new_amp_2.toPlainText())-float(self.ui.old_amp_2.toPlainText())))
        self.ui.delta_skill_amp_2.setText('%d'%(float(self.ui.new_skill_amp_2.toPlainText())-float(self.ui.old_skill_amp_2.toPlainText())))
        self.ui.delta_skill_acc_2.setText('%d'%(float(self.ui.new_skill_acc_2.toPlainText())-float(self.ui.old_skill_acc_2.toPlainText())))
        self.ui.delta_cd_reduction_2.setText('%d'%(float(self.ui.new_cd_reduction_2.toPlainText())-float(self.ui.old_cd_reduction_2.toPlainText())))
        self.ui.delta_dot_ratio_2.setText('%d'%(float(self.ui.new_dot_ratio_2.toPlainText())-float(self.ui.old_dot_ratio_2.toPlainText())))
        
        self.ui.delta_defense_ignore_2.setText('%d'%(float(self.ui.new_defense_ignore_2.toPlainText())-float(self.ui.old_defense_ignore_2.toPlainText())))
        self.ui.delta_defense_reduction_2.setText('%d'%(float(self.ui.new_defense_reduction_2.toPlainText())-float(self.ui.old_defense_reduction_2.toPlainText())))
        
        self.ui.delta_huixin_2.setText('%d'%(float(self.ui.new_huixin_2.toPlainText())-float(self.ui.old_huixin_2.toPlainText())))
        self.ui.delta_huixin_damage_2.setText('%d'%(float(self.ui.new_huixin_damage_2.toPlainText())-float(self.ui.old_huixin_damage_2.toPlainText())))
        self.ui.delta_buff_boost_2.setText('%d'%(float(self.ui.new_buff_boost_2.toPlainText())-float(self.ui.old_buff_boost_2.toPlainText())))
        
        self.ui.new_burst_damage.setText(str(int(burst_damage)))
        self.ui.new_total_damage.setText(str(int(total_damage)))
        
        if self.ui.old_total_damage.toPlainText() != '':
            boost = (total_damage / int(self.ui.old_total_damage.toPlainText()) - 1) * 100
            self.ui.boost_ratio.setText(str('%.4f'%boost))
        
        if self.ui.old_burst_damage.toPlainText() != '':
            boost = (burst_damage / int(self.ui.old_burst_damage.toPlainText()) - 1) * 100
            self.ui.boost_ratio_burst.setText(str('%.4f'%boost))

    def compute_damage_old(self):
        final_boost_status, final_base_status, burst_damage, total_damage, accelerate, boost_buff_enhancement, base_buff_enhancement = self.compute_damage(self.current_equipment)
        
        self.ui.old_stats.setText(str(int(final_boost_status["属强"])))
        self.ui.old_critical.setText(str('%.1f'%final_boost_status["暴击"]))
        self.ui.old_critical_damage.setText(str(int(final_boost_status["暴伤"])))
        self.ui.old_counter.setText(str(int(final_boost_status["克制"])))
        self.ui.old_damage_amp.setText(str(int(final_boost_status["伤提"])))
        self.ui.old_skill_damage.setText(str(int(final_boost_status["技伤"])))
        
        self.ui.old_resonance_damage.setText(str(int(final_boost_status["共鸣伤"])))
        self.ui.old_stats_damage.setText(str(int(final_boost_status["属伤"])))
        self.ui.old_pure_atk.setText(str(int(final_boost_status["破防攻击"])))
        self.ui.old_atk.setText(str(int(final_boost_status["攻击"])))
        self.ui.old_addition_damage.setText(str(int(final_boost_status["附伤"])))
        self.ui.old_spetial_damage.setText(str(int(final_boost_status["特殊"])))
        
        self.ui.old_shuangyue.setText(str(int(final_boost_status["职业增伤"])))
        self.ui.old_amp.setText(str(int(final_boost_status["倍率"])))
        self.ui.old_skill_amp.setText(str(int(final_boost_status["技能伤害提升"])))
        self.ui.old_skill_acc.setText(str(int(final_boost_status["技能加速"])))
        self.ui.old_cd_reduction.setText(str(int(final_boost_status["冷却缩减"])))
        self.ui.old_dot_ratio.setText(str(int(final_boost_status["特效占比"])))
        
        self.ui.old_defense_ignore.setText(str(int(final_boost_status["穿透"])))
        self.ui.old_defense_reduction.setText(str(int(final_boost_status["减防"])))
        
        self.ui.old_huixin.setText(str(int(final_boost_status["会心"])))
        self.ui.old_huixin_damage.setText(str(int(final_boost_status["会心伤害"])))
        
        self.ui.old_buff_boost.setText(str(int(boost_buff_enhancement*100)))
        
        self.ui.old_stats_2.setText(str(int(final_base_status["属强"])))
        self.ui.old_critical_2.setText(str('%.1f'%final_base_status["暴击"]))
        self.ui.old_critical_damage_2.setText(str(int(final_base_status["暴伤"])))
        self.ui.old_counter_2.setText(str(int(final_base_status["克制"])))
        self.ui.old_damage_amp_2.setText(str(int(final_base_status["伤提"])))
        self.ui.old_skill_damage_2.setText(str(int(final_base_status["技伤"])))
        
        self.ui.old_resonance_damage_2.setText(str(int(final_base_status["共鸣伤"])))
        self.ui.old_stats_damage_2.setText(str(int(final_base_status["属伤"])))
        self.ui.old_pure_atk_2.setText(str(int(final_base_status["破防攻击"])))
        self.ui.old_atk_2.setText(str(int(final_base_status["攻击"])))
        self.ui.old_addition_damage_2.setText(str(int(final_base_status["附伤"])))
        self.ui.old_spetial_damage_2.setText(str(int(final_base_status["特殊"])))
        
        self.ui.old_shuangyue_2.setText(str(int(final_base_status["职业增伤"])))
        self.ui.old_amp_2.setText(str(int(final_base_status["倍率"])))
        self.ui.old_skill_amp_2.setText(str(int(final_base_status["技能伤害提升"])))
        self.ui.old_skill_acc_2.setText(str(int(final_base_status["技能加速"])))
        self.ui.old_cd_reduction_2.setText(str(int(final_base_status["冷却缩减"])))
        self.ui.old_dot_ratio_2.setText(str(int(final_base_status["特效占比"])))
        
        self.ui.old_defense_ignore_2.setText(str(int(final_base_status["穿透"])))
        self.ui.old_defense_reduction_2.setText(str(int(final_base_status["减防"])))
        
        self.ui.old_huixin_2.setText(str(int(final_base_status["会心"])))
        self.ui.old_huixin_damage_2.setText(str(int(final_base_status["会心伤害"])))
        
        self.ui.old_buff_boost_2.setText(str(int(base_buff_enhancement*100)))
        
        self.ui.old_burst_damage.setText(str(int(burst_damage)))
        self.ui.old_total_damage.setText(str(int(total_damage)))
    
    
    def compute_damage(self, equipment):
        equipment_list = equipment.copy()
        equipment_list[67] = equipment_list[69] + equipment_list[67]
        equipment_list[68] = equipment_list[70] + equipment_list[68]
        del equipment_list[70]
        del equipment_list[69]
        
        data = {'单件':{}, '套装':{}}
        json_list = os.listdir('data/')
        for file_name in json_list:
            with open('data/{}'.format(file_name), 'r', encoding='utf-8') as f:
                temp_data = json.load(f)
                for key in temp_data.keys():
                    if key not in data['单件'].keys():
                        data['单件'][key] = temp_data[key]
        
        with open('套装效果.json', 'r', encoding='utf-8') as f:
                data['套装'] = json.load(f)      
        
        base_status = {
            "属强": 24.8,
            "暴击": 0,
            "暴伤": 66.3,
            "克制": 0,
            "伤提": 3,
            "技伤": 4,
            "共鸣伤": 20,
            "属伤": 0,
            "最终伤害": 0,
            "基础攻击": 232,
            "攻击加成": 0,
            "力量": 685,
            "敏捷": 445,
            "力量加成": 0,
            "破防攻击": 0,
            "破防加成": 0,
            "破防伤害": 0,
            "穿透": 0,
            "附伤": 0,
            "防御降低": 0,
            "怪物防御": self.ui.defense.value(),
            "倍率": 0,
            "技能伤害提升": 0,
            "冷却": 0,
            "冷却速度": 0,
            "职业增伤": 21,
            "技能加速": 0,
            '特殊': 0,
            '装备特效': 0,
            '装备增伤': 0,
            '特效增伤': 0,
            "会心": 0,
            "会心伤害": 20,
            '波动': 0,
            '共鸣覆盖率': 0.5,
            "独立": 1}
        
        boost_status = {
            "属强": 24.8,
            "暴击": 0,
            "暴伤": 66.3,
            "克制": 0,
            "伤提": 3,
            "技伤": 4,
            "共鸣伤": 20,
            "属伤": 0,
            "最终伤害": 0,
            "基础攻击": 232,
            "攻击加成": 0,
            "力量": 685,
            "敏捷": 445,
            "力量加成": 0,
            "破防攻击": 0,
            "破防加成": 0,
            "破防伤害": 0,
            "穿透": 0,
            "附伤": 0,
            "防御降低": 0,
            "怪物防御": self.ui.defense.value(),
            "倍率": 0,
            "技能伤害提升": 0,
            "冷却": 0,
            "冷却速度": 0,
            "职业增伤": 21,
            "技能加速": 0,
            '特殊': 0,
            '装备特效': 0,
            '装备增伤': 0,
            '特效增伤': 0,
            "会心": 0,
            "会心伤害": 20,
            '波动': 0,
            '共鸣覆盖率': 0.5,
            "独立": 1}
        
        for equip in equipment_list:
            if equip in data['单件'].keys():
                add_equipment(base_status, data['单件'][equip], boost=False)
                add_equipment(boost_status, data['单件'][equip], boost=True)
        
        base_status['特效占比'] = 0
        base_status['基础攻击'] += int(equipment_list[107-2])
        base_status['暴伤'] += float(equipment_list[108-2])
        base_status['暴击'] += float(equipment_list[109-2])
        base_status['属强'] += float(equipment_list[110-2])
        base_status['冷却'] += float(equipment_list[111-2])
        base_status['敏捷'] += int(equipment_list[112-2])
        base_status['力量'] += int(equipment_list[113-2])
        base_status['技伤'] += int(equipment_list[114-2])
        base_status['攻击加成'] += float(equipment_list[121-2])
        base_status['载具收藏'] = int(equipment_list[122-2])
        
        base_status['攻击加成'] += float(equipment_list[123-2])
        base_status['破防攻击'] += float(equipment_list[124-2])
        base_status['破防加成'] += float(equipment_list[125-2])
        base_status['伤提'] += float(equipment_list[126-2])
        base_status['克制'] += float(equipment_list[127-2])
        base_status['破防伤害'] += float(equipment_list[129-2])
        
        boost_status['特效占比'] = 0
        boost_status['基础攻击'] += int(equipment_list[107-2])
        boost_status['暴伤'] += float(equipment_list[108-2])
        boost_status['暴击'] += float(equipment_list[109-2])
        boost_status['属强'] += float(equipment_list[110-2])
        boost_status['冷却'] += float(equipment_list[111-2])
        boost_status['敏捷'] += int(equipment_list[112-2])
        boost_status['力量'] += int(equipment_list[113-2])
        boost_status['技伤'] += int(equipment_list[114-2])
        boost_status['攻击加成'] += float(equipment_list[121-2])
        boost_status['载具收藏'] = int(equipment_list[122-2])
        
        boost_status['攻击加成'] += float(equipment_list[123-2])
        boost_status['破防攻击'] += float(equipment_list[124-2])
        boost_status['破防加成'] += float(equipment_list[125-2])
        boost_status['伤提'] += float(equipment_list[126-2])
        boost_status['克制'] += float(equipment_list[127-2])
        boost_status['破防伤害'] += float(equipment_list[129-2])
        
        outfits = outfit_count(base_status, outfit_dict=data['套装'])
        
        for outfit in outfits:
            add_equipment(base_status, data['套装'][outfit[0]][outfit[1]], boost=False)
            add_equipment(boost_status, data['套装'][outfit[0]][outfit[1]], boost=True)
        
        final_base_status = {
                "属强": base_status['属强'],
                "暴击": base_status['暴击'] - 6.51e-7*base_status['敏捷']**2 + 0.0102 * base_status['敏捷'] + 0.3713,
                "暴伤": base_status['暴伤'],
                "克制": base_status['克制'],
                "伤提": base_status['伤提'],
                "技伤": base_status['技伤'],
                "共鸣伤": base_status['共鸣伤'],
                "属伤": base_status['属伤'],
                "最终伤害": base_status['最终伤害'],
                "破防攻击": base_status['破防攻击'] * (1 + base_status['破防加成']/100) * (1 + base_status['破防伤害']/100),
                "攻击": base_status['基础攻击'] * (1 + base_status['攻击加成']/100) * (1 + base_status['力量'] * (1+base_status['力量加成']/100)/1000),
                "防御": base_status['怪物防御']*(1-base_status['穿透']/100)*(1-base_status['防御降低']/100),
                "穿透": base_status['穿透'],
                "减防": base_status['防御降低'],
                "附伤": base_status['附伤'],
                "特殊": base_status['特殊'],
                "职业增伤": base_status['职业增伤'],
                "倍率": base_status['倍率'],
                "波动": base_status['波动'],
                "会心": base_status['会心'],
                "会心伤害": base_status['会心伤害'],
                "技能伤害提升": base_status['技能伤害提升'],
                "技能加速": base_status['技能加速'],
                "冷却缩减": 100 * (1 - 1 / (1 + (-0.005 * (base_status['冷却'] / 10)**2 + 1.05 * base_status['冷却'] / 10 + base_status['冷却速度'])/100)),
                "特效占比": base_status['特效占比'],
                "装备特效": base_status['装备特效'] * (1 + base_status['特效增伤']/100),
                "装备增伤": base_status['装备增伤'],
                "共鸣覆盖率": base_status['共鸣覆盖率'],
                "独立增伤": base_status['独立']}
        
        final_boost_status = {
                "属强": boost_status['属强'],
                "暴击": boost_status['暴击'] - 6.51e-7*boost_status['敏捷']**2 + 0.0102 * boost_status['敏捷'] + 0.3713,
                "暴伤": boost_status['暴伤'],
                "克制": boost_status['克制'],
                "伤提": boost_status['伤提'],
                "技伤": boost_status['技伤'],
                "共鸣伤": boost_status['共鸣伤'],
                "属伤": boost_status['属伤'],
                "最终伤害": boost_status['最终伤害'],
                "破防攻击": boost_status['破防攻击'] * (1 + boost_status['破防加成']/100) * (1 + boost_status['破防伤害']/100),
                "攻击": boost_status['基础攻击'] * (1 + boost_status['攻击加成']/100) * (1 + boost_status['力量'] * (1+boost_status['力量加成']/100)/1000),
                "防御": boost_status['怪物防御']*(1-boost_status['穿透']/100)*(1-boost_status['防御降低']/100),
                "穿透": boost_status['穿透'],
                "减防": boost_status['防御降低'],
                "附伤": boost_status['附伤'],
                "特殊": boost_status['特殊'],
                "职业增伤": boost_status['职业增伤'],
                "倍率": boost_status['倍率'],
                "波动": boost_status['波动'],
                "会心": boost_status['会心'],
                "会心伤害": boost_status['会心伤害'],
                "技能伤害提升": boost_status['技能伤害提升'],
                "技能加速": boost_status['技能加速'],
                "冷却缩减": 100 * (1 - 1 / (1 + (-0.005 * (boost_status['冷却'] / 10)**2 + 1.05 * boost_status['冷却'] / 10 + boost_status['冷却速度'])/100)),
                "特效占比": boost_status['特效占比'],
                "装备特效": boost_status['装备特效'] * (1 + boost_status['特效增伤']/100),
                "共鸣覆盖率": boost_status['共鸣覆盖率'],
                "装备增伤": boost_status['装备增伤'],
                "独立增伤": boost_status['独立']}
        
        total_damage_without_buff, skill_accelerate_without_buff = damage_compute(final_base_status, boost=False)
        boost_damage_without_buff, _ = damage_compute(final_boost_status, boost=True)
        
        buff_list = self.ui.buff_list.toPlainText().split('\n')[:-1]
        for buff in buff_list:
            add_equipment(base_status, self.data_fuzhu[buff], boost=False)
            add_equipment(boost_status, self.data_fuzhu[buff], boost=True)
        
        final_base_status = {
                "属强": base_status['属强'],
                "暴击": base_status['暴击'] - 6.51e-7*base_status['敏捷']**2 + 0.0102 * base_status['敏捷'] + 0.3713,
                "暴伤": base_status['暴伤'],
                "克制": base_status['克制'],
                "伤提": base_status['伤提'],
                "技伤": base_status['技伤'],
                "共鸣伤": base_status['共鸣伤'],
                "属伤": base_status['属伤'],
                "最终伤害": base_status['最终伤害'],
                "破防攻击": base_status['破防攻击'] * (1 + base_status['破防加成']/100) * (1 + base_status['破防伤害']/100),
                "攻击": base_status['基础攻击'] * (1 + base_status['攻击加成']/100) * (1 + base_status['力量'] * (1+base_status['力量加成']/100)/1000),
                "防御": base_status['怪物防御']*(1-base_status['穿透']/100)*(1-base_status['防御降低']/100),
                "穿透": base_status['穿透'],
                "减防": base_status['防御降低'],
                "附伤": base_status['附伤'],
                "特殊": base_status['特殊'],
                "职业增伤": base_status['职业增伤'],
                "倍率": base_status['倍率'],
                "波动": base_status['波动'],
                "会心": base_status['会心'],
                "会心伤害": base_status['会心伤害'],
                "技能伤害提升": base_status['技能伤害提升'],
                "技能加速": base_status['技能加速'],
                "冷却缩减": 100 * (1 - 1 / (1 + (-0.005 * (base_status['冷却'] / 10)**2 + 1.05 * base_status['冷却'] / 10 + base_status['冷却速度'])/100)),
                "特效占比": base_status['特效占比'],
                "装备特效": base_status['装备特效'] * (1 + base_status['特效增伤']/100),
                "共鸣覆盖率": base_status['共鸣覆盖率'],
                "装备增伤": base_status['装备增伤'],
                "独立增伤": base_status['独立']}
        
        final_boost_status = {
                "属强": boost_status['属强'],
                "暴击": boost_status['暴击'] - 6.51e-7*boost_status['敏捷']**2 + 0.0102 * boost_status['敏捷'] + 0.3713,
                "暴伤": boost_status['暴伤'],
                "克制": boost_status['克制'],
                "伤提": boost_status['伤提'],
                "技伤": boost_status['技伤'],
                "共鸣伤": boost_status['共鸣伤'],
                "属伤": boost_status['属伤'],
                "最终伤害": boost_status['最终伤害'],
                "破防攻击": boost_status['破防攻击'] * (1 + boost_status['破防加成']/100) * (1 + boost_status['破防伤害']/100),
                "攻击": boost_status['基础攻击'] * (1 + boost_status['攻击加成']/100) * (1 + boost_status['力量'] * (1+boost_status['力量加成']/100)/1000),
                "防御": boost_status['怪物防御']*(1-boost_status['穿透']/100)*(1-boost_status['防御降低']/100),
                "穿透": boost_status['穿透'],
                "减防": boost_status['防御降低'],
                "附伤": boost_status['附伤'],
                "特殊": boost_status['特殊'],
                "职业增伤": boost_status['职业增伤'],
                "倍率": boost_status['倍率'],
                "波动": boost_status['波动'],
                "会心": boost_status['会心'],
                "会心伤害": boost_status['会心伤害'],
                "技能伤害提升": boost_status['技能伤害提升'],
                "技能加速": boost_status['技能加速'],
                "冷却缩减": 100 * (1 - 1 / (1 + (-0.005 * (boost_status['冷却'] / 10)**2 + 1.05 * boost_status['冷却'] / 10 + boost_status['冷却速度'])/100)),
                "特效占比": boost_status['装备特效'] * (1 + boost_status['特效增伤']/100) / (100 + boost_status['装备特效'] * (1 + boost_status['特效增伤']/100)),
                "装备特效": boost_status['装备特效'] * (1 + boost_status['特效增伤']/100),
                "共鸣覆盖率": boost_status['共鸣覆盖率'],
                "装备增伤": boost_status['装备增伤'],
                "独立增伤": boost_status['独立']}
        
        total_damage, skill_accelerate = damage_compute(final_base_status, boost=False)
        boost_damage, _ = damage_compute(final_boost_status, boost=True)

        return final_boost_status, final_base_status, boost_damage, total_damage*(skill_accelerate**0.5), skill_accelerate, \
            boost_damage/boost_damage_without_buff - 1, total_damage*(skill_accelerate**0.5) / total_damage_without_buff*(skill_accelerate_without_buff**0.5) - 1
        
if __name__ == '__main__':
    print(sys.argv)
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
 
