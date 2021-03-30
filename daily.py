# coding=utf-8
import pyautogui
import time
import random
import datetime
import threading
nobuleguy = 0
key_up = 82
key_down = 81
key_left = 80
key_right = 79
key_n = 17
key_space = 44
key_F12 = 69
My_png = 'item\Xiaomei.png'
isweek = 0
key_esc = 41
timer_team = 0
team_login_onebyone_flag = 0
def thread_timer():
    global team_login_onebyone_flag
    team_login_onebyone_flag = 1
def cleanpage():
    pyautogui.press('esc', 7, 0.7)

def HasItem(item,conf):
    HasSaiLiYa=pyautogui.locateOnScreen(image=item, confidence=conf, grayscale = True)
    try:
        x,y=pyautogui.center(HasSaiLiYa)
    except:
        return 0,0,0
    else:
        return 1,x,y

def FindAndClick(NeedPrint,item,conf,clickcnt):
    ret,x,y = HasItem(item,conf)
    if(ret == 1):
        My_MoveMouse("left", x, y,  clickcnt)
    else:
        if(NeedPrint == 1):
            print('not found'+str(item))
            log_money = 'log\error' + '_' + str(item)[str(item).find('MHXY'):-4] + '_'+datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S') + '.png'
            pyautogui.screenshot(log_money)
    return ret

def HasItemRegion(item,conf,x,y,long,width):
    HasSaiLiYa=pyautogui.locateOnScreen(image=item, confidence=conf, region = (x,y,long,width))
    try:
        x,y=pyautogui.center(HasSaiLiYa)
    except:
        return 0,0,0
    else:
        return 1,x,y
def My_MoveMouse(leftorright,x,y,cnt):
    if(leftorright == "left"):
        pyautogui.moveTo(x, y, duration=0.5, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
    if(leftorright == "right"):
        pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.rightClick()

'''
menghuanxiyou的脚本
'''
def Login(name):
    ret,x,y=HasItem('accountall\MHXYIcon.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x, y,  2)
        pyautogui.doubleClick()
    else:
        print('cannot find menghuanxiyou Icon')
    for i in range(0,60):
        ret,x,y=HasItem('accountall\MHXY_Login.png', 0.8)
        if(ret == 1):
            print('find Login Icon')
            My_MoveMouse("left", x, y,  2)
            break
        else:
            time.sleep(2)
            ret1 = FindAndClick(0,'team\MHXY_team_lianggekehuduan.png', 0.8, 1)
            time.sleep(2)
            ret2 = FindAndClick(0,'team\MHXY_team_lianggekehuduan.png', 0.8, 1)
            if(ret1 == 1 or ret2 == 1):
                print('find lianggekehuduan Icon')
                time.sleep(10)
                ret,x,y=HasItem('accountall\MHXYIcon.png', 0.8)
                if(ret == 1):
                    print('find menghuanxiyou Icon, login'+name)
                    My_MoveMouse("left", x, y,  2)
                    pyautogui.doubleClick()
    for i in range(0,30):        
        if(name[5:8] == 'IOS'):
            ret,x,y=HasItem('accountall\MHXY_Login_IOS.png', 0.8)
            if(ret == 1):
                My_MoveMouse("left", x, y,  2)
                break
        elif(name[5:8] == 'AND'):
            ret,x,y=HasItem('accountall\MHXY_Login_Android.png', 0.8)
            if(ret == 1):
                My_MoveMouse("left", x, y,  2)
                break
        else:
            time.sleep(2)
    for i in range(0,30):   
        ret,x,y=HasItem('accountall\MHXY_Login_xuanfu.png', 0.8)
        if(ret == 1):
            My_MoveMouse("left", x, y,  1)
            time.sleep(1)
        else:
            time.sleep(2)    
        ret,x,y=HasItem('accountall\MHXY_Login_'+ name[0:4] + '.png', 0.6)
        if(ret == 1):
            My_MoveMouse("left", x, y,  1)
            break
        else:
            print('cantnot find '+name[0:4]+ 'zone')
            time.sleep(2)
    for i in range(0,30):         
        ret,x,y=HasItem('accountall\MHXY_Login_'+ name +'.png', 0.9)
        if(ret == 1):
            My_MoveMouse("left", x, y,  1)
            break
        else:
            time.sleep(2)
    time.sleep(10)
    cleanpage()
    
def XinFuXXX():
    ret,x,y = HasItem('accountall\MHXY_huodong_xinfu_2.png',0.7)
    if(ret == 1):
        My_MoveMouse("left", x + 387, y,  1)
    ret,x,y = HasItem('accountall\MHXY_huodong_xinfu.png',0.7)
    if(ret == 1):
        My_MoveMouse("left", x + 868, y,  1)
    return ret
    
def WaitBaoTuTillBattelEnd():
    cnt = 0
    while(1):
        XinFuXXX()
        ret,x,y=HasItem('accountall\MHXY_huodong.png', 0.8)
        if(ret == 1):
            ret,x,y=HasItemRegion('accountall\MHXY_huodong_baotu_3.png', 0.8,960,0,960,1020)
            if(ret == 0):
                cnt = cnt + 1
                time.sleep(3)
                if(cnt >= 10):
                    print('cangbaotu or zhuagui battle end')
                    cleanpage()
                    return
                continue
            else:
                cnt = 0
                My_MoveMouse("left", x, y,  1)
        time.sleep(3)
def login_onebyone(name2,name3,name4):
    for name in [name2,name3,name4]:
        Login(name)
        EndAwindow()
        time.sleep(10)
def WaitZhuaGuiTillBattelEnd(name1,name2,name3,name4):
    cnt = 0
    global team_login_onebyone_flag
    global timer_team
    while(1):
        if(team_login_onebyone_flag == 1):
            login_onebyone(name2,name3,name4)
            team_login_onebyone_flag = 0
            ret,x,y=HasItem('team\MHXY_' + name1 + '_leader.png', 0.8)
            if(ret == 1):
                print('I am leader,and ,press')
                My_MoveMouse("right", x, y,  1)
                cleanpage()
            print('Im restart a timer')
            timer_team = threading.Timer(15*60,thread_timer)
            timer_team.start()
        XinFuXXX()
        FindAndClick(0,'team\MHXY_team_zhuagui_quxiao.png',0.8,1)
        ret,x,y=HasItem('accountall\MHXY_huodong.png', 0.8)
        if(ret == 1):
            ret,x,y=HasItemRegion('accountall\MHXY_huodong_baotu_3.png', 0.8,960,0,960,1020)
            if(ret == 0):
                print('not found zhan')
                cnt = cnt + 1
                time.sleep(3)
                if(cnt >= 10):
                    print('cangbaotu or zhuagui battle end')
                    cleanpage()
                    return
                continue
            else:
                cnt = 0
                My_MoveMouse("left", x, y,  1)
        time.sleep(3)
def GotoCangbaotu():
    FindAndClick(1,'accountall\MHXY_huodong.png', 0.8, 1)
    time.sleep(3)
    ret,x,y=HasItem('accountall\MHXY_huodong_baotu.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x+200, y,  1)
    else:
        print('not found baotu icon')
    time.sleep(20)
    FindAndClick(1,'accountall\MHXY_huodong_baotu_tingtingwufang.png', 0.8, 2)
    time.sleep(2)
    cleanpage()
    time.sleep(4)
    
def IsBaotuEnd():
    cnt = 0
    while(1):
        ret,x,y=HasItem('accountall\MHXY_huodong.png', 0.8)
        if(ret == 1):
            ret,x,y=HasItem('accountall\MHXY_huodong_baotu_dashiyong.png', 0.8)
            if(ret == 0):
                cnt = cnt + 1
                time.sleep(3)
                if(cnt >= 15):
                    print('cangbaotu end')
                    return 1
                continue
            else:
                cnt = 0
                return 0
        else:
            time.sleep(3)
            return 0
def OpenBaoTuOnebyOne():
    ret = 0
    while(1):
        XinFuXXX()
        FindAndClick(0,'accountall\MHXY_huodong_baotu_dashiyong.png',0.8,1)
        if(ret == 1):
            time.sleep(3)
        else:
            IsEnd = IsBaotuEnd()
            if(IsEnd == 0):
                time.sleep(3)
                continue
            else:
                return

def OpenBaoTu():
    cleanpage()
    FindAndClick(1,'accountall\MHXY_huodong_baotu_baoguo.png', 0.6, 1)
    time.sleep(2)
    ret = FindAndClick(1,'accountall\MHXY_huodong_baotu_wupin.png', 0.8, 1)
    if(ret != 1):
        print('did not find cangbaotu')
        FindAndClick(1,'accountall\MHXY_zhengli.png', 0.8, 1)
        time.sleep(2)
        FindAndClick(1,'accountall\MHXY_huodong_baotu_wupin.png', 0.8, 1)
    time.sleep(2)
    FindAndClick(1,'accountall\MHXY_huodong_baotu_shiyong.png', 0.8, 1)
    OpenBaoTuOnebyOne()

def CangBaotu():
    cleanpage()
    print('go to cangbaotu')
    GotoCangbaotu()
    print('wating cangbaotu battle')
    WaitBaoTuTillBattelEnd()
    print('open baotu')
    OpenBaoTu()
    print('baotu end')
def waitYaBiaoEnd():
    while(1):
        XinFuXXX()
        ret,x,y=HasItem('accountall\MHXY_huodong.png', 0.8)
        if(ret == 1):
            return
        else:
            time.sleep(5)
def YaBiao():
    print('begin yabiao')
    cleanpage()
    cnt = 0
    FindAndClick(1,'accountall\MHXY_huodong.png', 0.8, 1)
    time.sleep(3)
    ret,x,y=HasItem('accountall\MHXY_huodong_YaBiao.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x+200, y,  1)
    time.sleep(5)
    while(1):
        XinFuXXX()
        ret,x,y=HasItem('accountall\MHXY_huodong_YaBiao_2.png', 0.8)
        if(ret == 1):
            My_MoveMouse("left", x, y,  1)
            time.sleep(2)
            ret,x,y=HasItem('accountall\MHXY_huodong_YaBiao_3.png', 0.8)
            if(ret == 1):
                My_MoveMouse("left", x, y,  1)
                cnt = cnt + 1
                time.sleep(1)
                if(cnt >= 3):
                    waitYaBiaoEnd()
                    return
        else:
            time.sleep(5)

def MijingPrepare():
    FindAndClick(1,'accountall\MHXY_huodong.png', 0.8, 1)
    time.sleep(3)
    ret,x,y=HasItem('accountall\MHXY_huodong_Mijing.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x+200, y,  1)
    time.sleep(5)
    FindAndClick(1,'accountall\MHXY_huodong_Mijing_2.png', 0.8, 1)
    time.sleep(5)
    ret,x,y=HasItem('accountall\MHXY_huodong_Mijing_3.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x, y - 50,  1)
    time.sleep(2)
    FindAndClick(1,'accountall\MHXY_huodong_Mijing_4.png', 0.8, 1)
    time.sleep(3)

def Mijing():
    print('begin mijing')
    cleanpage()
    MijingPrepare()
    out = 0
    ret = FindAndClick(1,'accountall\MHXY_huodong_Mijing_Boss1.png', 0.8, 1)
    if(ret != 1):
        print('cannot find mijing icon')
        return
    while(1):
        XinFuXXX()
        ret,x,y=HasItem('accountall\MHXY_huodong_Mijing_zhongjian.png', 0.8)
        if(ret == 1):
            My_MoveMouse("left", x, y,  1)
            time.sleep(1)
            My_MoveMouse("left", x+56, y-375,  1)
        ret = FindAndClick(0,'accountall\MHXY_huodong_Mijing_End.png',0.8,1)
        if(ret == 1):
            time.sleep(5)
            continue
        if(out == 1):
            FindAndClick(1,'accountall\MHXY_huodong_Mijing_End_2.png',0.8,2)
            return
        ret = FindAndClick(0,'accountall\MHXY_huodong_Mijing_End_3.png',0.8,1)
        if(ret == 1):
            out = 1
        time.sleep(5)

def Sanjie():
    print('begin sanjie qiyuan')
    cleanpage()
    time.sleep(2)
    ret,x,y=HasItem('accountall\MHXY_huodong.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x, y,  1)
    time.sleep(3)
    ret,x,y=HasItem('accountall\MHXY_huodong_Sanjie.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x + 180, y,  1)
    else:
        print('not found sanjie icon')
        return
    time.sleep(3)
    ret,x1,y1=HasItem('accountall\MHXY_huodong_Sanjie_2.png', 0.8)
    ret = 0
    while(ret == 0):
        XinFuXXX()
        ret,x,y=HasItem('accountall\MHXY_huodong_Sanjie_1.png', 0.8)
        if(ret == 0):
            My_MoveMouse("left", x1 + random.choice([400, 500, 700]), y1,  1)
        time.sleep(3)
    cleanpage()
    print('sanjie out')

def EndAwindow():
    cleanpage()
    ret,x,y=HasItem('accountall\MHXY_Logout_1.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x, y,  1)
    else:
        print('cannot find out window')
    time.sleep(5)
    ret,x,y=HasItem('accountall\MHXY_Logout_2.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x, y,  1)
    else:
        print('cannot find out confirm window')
    time.sleep(5)

def BuildTeam(name1,name2,name3,name4):
   #登陆第一个角色看到活动后右移
    Login(name1)
    ret,x,y=HasItem('team\MHXY_team_title.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x, y,  1)
        time.sleep(2)
        pyautogui.dragTo(x + 300, y, 2, button='left')
    for name in [name2,name3,name4]:
        Login(name)
        ret,x,y=HasItem('team\MHXY_' + name1 + '_leader.png', 0.8)
        if(ret == 1):
            My_MoveMouse("right", x, y,  1)
            cleanpage()
            My_MoveMouse("left", x-950, y+500,  1)
        time.sleep(1)
        FindAndClick(1,'team\MHXY_team_lianxiren.png',0.8,1)
        time.sleep(1)
        ret = FindAndClick(0,'team\MHXY_team_quanbu_lianxiren.png',0.8,1)
        time.sleep(1)
        if(ret == 1):
            FindAndClick(1,'team\MHXY_team_wuwuwu.png',0.8,1)
            time.sleep(1)
        ret,x,y=HasItem('team\MHXY_' + name + '.png', 0.8)
        if(ret == 1):
            My_MoveMouse("left", x + 286, y,  1)
            time.sleep(1)
        FindAndClick(1,'team\MHXY_team_yaoqingrudui.png',0.8,1)
        cleanpage()
        time.sleep(1)
        ret,x,y=HasItem('accountall\MHXY_Logout_1.png', 0.8)
        if(ret == 1):
            My_MoveMouse("left", x - 1100, y,  1)
            time.sleep(1)
        FindAndClick(1,'team\MHXY_team_jiehsou.png',0.8,1)
        time.sleep(1)
        EndAwindow()
        time.sleep(3)

   #登陆第二个角色看到活动后切第一个角色右键点人头
   #找到好友，联系人，找到第二个角色，邀请入队，esc
   #第二个人头坐标左移切第二个角色点击同意
   #退出当前角色
def DoZhuagui(name1,name2,name3,name4):
    ret,x,y=HasItem('team\MHXY_' + name1 + '_leader.png', 0.8)
    if(ret == 1):
        My_MoveMouse("right", x, y,  1)
        cleanpage()
    FindAndClick(1,'accountall\MHXY_huodong.png',0.8,1)
    time.sleep(1)
    FindAndClick(1,'team\MHXY_team_richang.png',0.8,1)
    time.sleep(1)
    ret,x,y=HasItem('team\MHXY_huodong_Zhuagui.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x + 200, y,  1)
    else:
        print('not found Zhuagui icon')
        return
    time.sleep(20)
    FindAndClick(1,'team\MHXY_team_zhuaguirenwu.png',0.8,1)
    time.sleep(1)
    FindAndClick(0,'team\MHXY_team_quxiao.png',0.8,1)
    time.sleep(1)
    global timer_team
    timer_team = threading.Timer(60*14,thread_timer)
    timer_team.start()
    WaitZhuaGuiTillBattelEnd(name1,name2,name3,name4)


def EndTeam(name1):
    cleanpage()
    ret,x,y=HasItem('team\MHXY_' + name1 + '_leader.png', 0.8)
    if(ret == 1):
        My_MoveMouse("right", x, y,  1)
        cleanpage()
        My_MoveMouse("left", x, y+70,  1)
        time.sleep(1)
        for i in range(0,3):
            My_MoveMouse("left", x-30, y+200,  1)
            time.sleep(1)
            FindAndClick(1,'team\MHXY_team_kick_other.png',0.8,1)
            time.sleep(1)
            FindAndClick(1,'team\MHXY_team_kick_confirm.png',0.8,1)
            time.sleep(1)
        My_MoveMouse("left", x-30, y+140,  1)
        time.sleep(1)
        FindAndClick(1,'team\MHXY_team_kick_myself.png',0.8,1)
        time.sleep(1)
        FindAndClick(1,'team\MHXY_team_kick_confirm.png',0.8,1)
        time.sleep(1)
        EndAwindow()
        time.sleep(3)
def DoFubenlvmeng(name1,name2,name3,name4):
    cleanpage()
    FindAndClick(1,'team\MHXY_team_richang.png',0.8,1)
    time.sleep(1)
    FindAndClick(1,'accountall\MHXY_huodong.png',0.8,1)
    time.sleep(2)
    ret,x,y=HasItem('team\MHXY_team_lvmeng.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x + 150, y,  1)
    else:
        print('not found icon')
    time.sleep(10)
    FindAndClick(1,'team\MHXY_team_xuanzefuben.png',0.8,1)
    time.sleep(2)
    ret,x,y=HasItem('team\MHXY_team_lvmeng_jinru.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x , y+288,  1)
        time.sleep(10)
    else:
        print('not found jinru')
    FindAndClick(1,'team\MHXY_team_tiaoguojuqing.png',0.8,1)
    time.sleep(3)
    FindAndClick(1,'accountall\MHXY_huodong_baotu_3.png',0.8,1)
    ret = 0
    while(ret == 0):
        FindAndClick(0,'team\MHXY_team_dianjijixu.png',0.8,3)
        time.sleep(2)
        ret = FindAndClick(0,'team\MHXY_team_lvmeng_dezuile.png',0.8,1)
        time.sleep(2)
    ret = 0
    while(ret == 0):
        XinFuXXX()
        ret = FindAndClick(0,'team\MHXY_team_tiaoguojuqing.png',0.8,1)
        time.sleep(3)
    FindAndClick(1,'accountall\MHXY_huodong_baotu_3.png',0.8,1)
    ret = 0
    while(ret == 0):
        ret = FindAndClick(0,'team\MHXY_team_lvmeng_xuekoupenren.png',0.8,1)
        time.sleep(2)
    while(1):
        XinFuXXX()
        ret,x,y=HasItem('team\MHXY_team_tiaoguojuqing.png', 0.8)
        if(ret == 1):
            break
        ret = FindAndClick(0,'accountall\MHXY_huodong_Mijing_End_3.png',0.8,1)
        if(ret == 1):
            break
        time.sleep(3)
    print('lvmeng fuben end')
    FindAndClick(1,'team\MHXY_team_lvmeng_out_guanghangong.png',0.8,1)
    time.sleep(2)
    FindAndClick(1,'team\MHXY_team_lvmeng_out_changancheng.png',0.8,1)
    print('lvmeng fuben end')
def DoFubenliulisui(name1,name2,name3,name4):
    cleanpage()
    FindAndClick(1,'team\MHXY_team_richang.png',0.8,1)
    time.sleep(1)
    FindAndClick(1,'accountall\MHXY_huodong.png',0.8,1)
    time.sleep(2)
    ret,x,y=HasItem('team\MHXY_team_liulisui.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x + 150, y,  1)
    else:
        print('not found icon')
    time.sleep(10)
    FindAndClick(1,'team\MHXY_team_xuanzefuben.png',0.8,1)
    time.sleep(2)
    ret,x,y=HasItem('team\MHXY_team_liulisui_jinru.png', 0.8)
    if(ret == 1):
        My_MoveMouse("left", x , y+288,  1)
        time.sleep(10)
    else:
        print('not found jinru')
    FindAndClick(1,'team\MHXY_team_tiaoguojuqing.png',0.8,1)
    time.sleep(3)
    FindAndClick(1,'accountall\MHXY_huodong_baotu_3.png',0.8,1)
    ret = 0
    while(ret == 0):
        ret = FindAndClick(0,'team\MHXY_team_liulisui_dangrankeyi.png',0.8,1)
        time.sleep(2)
    ret = 0
    while(ret == 0):
        XinFuXXX()
        ret = FindAndClick(0,'team\MHXY_team_tiaoguojuqing.png',0.8,1)
        time.sleep(3)
    time.sleep(8)
    cleanpage()
    FindAndClick(1,'accountall\MHXY_huodong_baotu_3.png',0.8,1)
    time.sleep(8)
    FindAndClick(1,'team\MHXY_team_dianjijixu.png',0.8,3)
    while(1):
        XinFuXXX()
        ret,x,y=HasItem('team\MHXY_team_tiaoguojuqing.png', 0.8)
        if(ret == 1):
            break
        ret = FindAndClick(0,'accountall\MHXY_huodong_Mijing_End_3.png',0.8,1)
        if(ret == 1):
            break    
        time.sleep(3)
    print('liulisui fuben end')
    FindAndClick(0,'team\MHXY_team_liulisui_out_yudiyuqian.png',0.8,1)
    time.sleep(2)
    FindAndClick(0,'team\MHXY_team_lvmeng_out_changancheng.png',0.8,1)
def ZhuaGui(name1,name2,name3,name4):
    BuildTeam(name1,name2,name3,name4)
    #执行抓鬼脚本一轮
    DoZhuagui(name1,name2,name3,name4)
    DoZhuagui(name1,name2,name3,name4)
    #login_onebyone(name2,name3,name4)
    EndTeam(name1)
    team_login_onebyone_flag = 0
    timer_team = threading.Timer(15*60,thread_timer)#TBD
    timer_team.cancel()

def Fuben(name1,name2,name3,name4):
    BuildTeam(name1,name2,name3,name4)
    DoFubenlvmeng(name1,name2,name3,name4)
    DoFubenliulisui(name1,name2,name3,name4)
    EndTeam(name1)

def ZhuaGuiList(namelist):
    for name in namelist:
        print('start zhuagui '+name['Name1']+'_'+datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S'))
        ZhuaGui(name['Name1'],name['Name2'],name['Name3'],name['Name4'])
def FubenList(namelist):
    for name in namelist:
        print('start fuben '+name['Name1']+'_'+datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S'))
        Fuben(name['Name1'],name['Name2'],name['Name3'],name['Name4'])
def Dailylist(name):
#点击图标进号,选择角色
    print('start daily '+name+'_'+datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S'))
    Login(name)
#好感度点击(对话)先不做
#藏宝图
    CangBaotu()
#秘境
    Mijing()
#三界
    #Sanjie()
#押镖
    time.sleep(2)
    YaBiao()
#换号
def GoOne_Room(accountInfo):
    #for name in accountInfo[0]:0是第一个，[2:5]第三个到第5个
    for name in accountInfo:
        Dailylist(name)
        EndAwindow()

def main():
    #截图区名称
    #截图四个角色名称
    #截图队长头像
    #制作呜呜呜呜联系人组
    #截图三个队友在呜呜呜呜中的头像
    #角色升级到40手动进一次秘境即可
    
    time.sleep(2*60*60)
    DailyAccountInfo1 = [
                   'XNKL_IOS_1', 
                   'XNKL_IOS_2', 
                   'XNKL_AND_3', 
                   'XNKL_AND_4',
                   ]
    DailyAccountInfo2 = [
                   'TSYD_IOS_1',
                   'TSYD_IOS_2',
                   'TSYD_IOS_3',
                   'TSYD_IOS_4',
                   ]
    ZhuaguiAcconutInfo1 = [
                        {'Name1': 'XNKL_IOS_1', 'Name2': 'XNKL_IOS_2', 'Name3': 'XNKL_AND_3', 'Name4': 'XNKL_AND_4'},
                        ]
    ZhuaguiAcconutInfo2 = [
                        {'Name1': 'TSYD_IOS_1', 'Name2': 'TSYD_IOS_2', 'Name3': 'TSYD_IOS_3', 'Name4': 'TSYD_IOS_4'},
                        ]
    FubenAcconutInfo1 = [
                        {'Name1': 'XNKL_IOS_1', 'Name2': 'XNKL_IOS_2', 'Name3': 'XNKL_AND_3', 'Name4': 'XNKL_AND_4'},
                        ]
    FubenAcconutInfo2 = [
                        {'Name1': 'TSYD_IOS_1', 'Name2': 'TSYD_IOS_2', 'Name3': 'TSYD_IOS_3', 'Name4': 'TSYD_IOS_4'},
                        ]
    DailyAccountInfo3 = [
                   'BTHL_IOS_1', 
                   'BTHL_IOS_2', 
                   'BTHL_AND_3',  
                   'BTHL_AND_5', 
                   ]
    ZhuaguiAcconutInfo3 = [
                        {'Name1': 'BTHL_IOS_1', 'Name2': 'BTHL_IOS_2', 'Name3': 'BTHL_AND_3', 'Name4': 'BTHL_AND_5'},
                        ]
    FubenAcconutInfo3 = [
                        {'Name1': 'BTHL_IOS_1', 'Name2': 'BTHL_IOS_2', 'Name3': 'BTHL_AND_3', 'Name4': 'BTHL_AND_5'},
                        ]
    ZhuaGuiList(ZhuaguiAcconutInfo1)
    GoOne_Room(DailyAccountInfo1)
    FubenList(FubenAcconutInfo1)
    ZhuaGuiList(ZhuaguiAcconutInfo2)
    GoOne_Room(DailyAccountInfo2)
    FubenList(FubenAcconutInfo2)
    ZhuaGuiList(ZhuaguiAcconutInfo3)
    GoOne_Room(DailyAccountInfo3)
    FubenList(FubenAcconutInfo3)

if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    main()