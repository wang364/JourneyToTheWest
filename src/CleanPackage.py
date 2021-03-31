# coding=utf-8
import pyautogui
import time
import basic


# def saleShopDrawing():


# def saleOre():


# def saleJewel():


def sortPackage():
    basic.FindAndClick(1, 'resource\\fixed\\sortPackage.png', 0.6, 1)


def openPackage():
    basic.FindAndClick(1, 'resource\\fixed\\package.png', 0.6, 1)


def cleanPackage():
    basic.backToTop()
    openPackage()
    sortPackage()
    # saleJewel()
    # saleOre()
    # saleShopDrawing()
    # sortPackage()

# if __name__ == '__main__':
#     pyautogui.FAILSAFE = True
#     cleanPackage()
