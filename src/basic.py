# coding=utf-8
import pyautogui
import datetime


def backToTop():
    pyautogui.press('esc', 7, 0.7)

 
def My_MoveMouse(leftorright, x, y, cnt):
    if(leftorright == "left"):
        pyautogui.moveTo(x, y, duration=0.5, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
    if(leftorright == "right"):
        pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.rightClick()


def FindAndClick(NeedPrint, item, conf, clickcnt):
    print('abc')
    ret, x, y = HasItem(item, conf)
    if(ret == 1):
        My_MoveMouse("left", x, y,  clickcnt)
    else:
        if(NeedPrint == 1):
            print('not found'+str(item))
            log_money = 'log\error' + '_' + str(item)[str(item).find('MHXY'):-4] + '_' + datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S') + '.png'
            pyautogui.screenshot(log_money)
    return ret


def HasItem(item, conf):
    HasSaiLiYa = pyautogui.locateOnScreen(image=item, confidence=conf, grayscale=True)
    try:
        x, y = pyautogui.center(HasSaiLiYa)
    except:
        return 0, 0, 0
    else:
        return 1, x, y
