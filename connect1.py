import pyautogui as pg
import time
from peewee import *
from dic import *


def facebook(email,password):
	time.sleep(2)
	pg.hotkey('win','r')
	time.sleep(1)
	pg.typewrite("chrome",0.2)
	pg.press('enter')
	time.sleep(3)
	pg.typewrite("www.facebook.com",0.2)
	pg.press('enter')
	time.sleep(5)
	pg.click(820,115)
	pg.typewrite(email)
	pg.press('tab')
	pg.typewrite(password)
	time.sleep(2)
	pg.press('enter')

