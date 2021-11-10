import pyautogui
import time
size = pyautogui.size()
s_flag = False
while 1:
    now_time = time.asctime( time.localtime(time.time()) ).split(' ')[-2]
    print('\r当前时间:',now_time,end = "")
    time.sleep(1)
    now_time = now_time.split(':')
    if not s_flag and now_time[0] == '00' and now_time[1] == '00':
        pyautogui.click(960,997,duration = 0.1)
        pyautogui.click(783,997,duration = 0.1)
        s_flag = True
    if s_flag and now_time[0] == '06' and now_time[1] == '00':
        pyautogui.click(867,997,duration = 0.1)
        break
