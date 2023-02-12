#프로젝트 - 윈도우 시간 알리미
 
#---------------------------------------------------------------------------------------------------------------------------#
 
# import 목록
import os
import sys
import time
import datetime
import getpass
import psutil
import tkinter.ttk as ttk
import tkinter as tk
 
from tkinter import *
from logging import root
from cProfile import label
 
from datetime import datetime
from datetime import timedelta
from win10toast import ToastNotifier

from tkinter import messagebox as msgbox
 
from turtle import st
from unittest import result
from setuptools import Command
from pkg_resources import working_set
 
#---------------------------------------------------------------------------------------------------------------------------#
#윈도우창 생성및 크기설정
window = tk.Tk()
window.title("윈도우 시간 관리자")
window.geometry('300x250')
window.resizable(width=False,height=False) #윈도우창 크기 고정
 
file_root = "C:/Wtm_Setting/" #사용자의 바탕화면의 Setting파일에 접근(추후 경로 변경)
 
try:
    if not os.path.exists(file_root):
        os.makedirs(file_root)
 
    if not os.path.exists(file_root+"set_time.txt"): #**
        file1 = open(file_root+"set_time.txt","w")
        file1.write("60") #1시간을 기본으로 설정
        file1.close()
       
    if not os.path.exists(file_root+"set_process.txt"):#**
         file2 = open(file_root+"set_process.txt","w")
         file2.write(" ")
         file2.close()
   
    if not os.path.exists(file_root+"stop_watch.txt"):#**
         file3 = open(file_root+"stop_watch.txt","w")
         file3.write(" ")
         file3.close()
 
    if not os.path.exists(file_root+"memo.txt"):#**
         file4 = open(file_root+"memo.txt","w")
         file4.write(" ")
         file4.close()
 
    if not os.path.exists(file_root+"eye_health.txt"):#**
         file5 = open(file_root+"eye_health.txt","w")
         file5.write("30") #30분을 기본으로 설정
         file5.close()
   
    if not os.path.exists(file_root+"water_eat.txt"):#**
         file6 = open(file_root+"water_eat.txt","w")
         file6.write("30") #30분을 기본으로 설정
         file6.close()
 
    if not os.path.exists(file_root+"memo_time.txt"):#**
         file7 = open(file_root+"memo_time.txt","w")
         file7.write("30") #30분을 기본으로 설정
         file7.close()
    
    if not os.path.exists(file_root+"main_time_save.txt"):#**
        file8 = open(file_root+"main_time_save.txt","w")
        file8.write(" ") #30분을 기본으로 설정
        file8.close()
        
 
except OSError:
    print('error')
#---------------------------------------------------------------------------------------------------------------------------#
#메인 윈도우 레이아웃 설정
window['bg'] = "gray"
 
#---------------------------------------------------------------------------------------------------------------------------#
#메뉴바 - 시스템 카테고리 설정
 
def root_print():
    msgbox.showinfo("파일경로","저장소 파일의 경로는 C:/Wtm_Setting 입니다.")
 
def memo():
    memo_win=tk.Tk()
    memo_win.title("메모장")
    memo_win.geometry("250x150")
 
    def reg():
        msgbox.showinfo("완료","메모가 저장되었습니다.")
        memo_file = open(file_root+"memo.txt","w")
        memo_time_file = open(file_root+"memo_time.txt","w")
        memo_file.write(str(work_memo_box.get()))
        memo_time_file.write(str(memo_time_entry.get()))
        memo_file.close()
        memo_time_file.close()
 
    work_memo = tk.Label(memo_win,text="메모를 입력하세요")
    work_memo_box = tk.Entry(memo_win,width=30)
    memo_time = tk.Label(memo_win,text="시간 입력: ")
    memo_time_entry = tk.Entry(memo_win,width=5)
    min_after = tk.Label(memo_win,text="분 후 알림")
    work_memo_button = tk.Button(memo_win,text="등록",command=reg)
 
    work_memo.place(x=70,y=10)
    work_memo_box.place(x=20,y=40)
    memo_time.place(x=10,y=80)
    memo_time_entry.place(x=70,y=80)
    min_after.place(x=110,y=80)
    work_memo_button.place(x=175,y=80)
 
#######################################################################################################
#알람 시간 설정
def alarm_time():
    alarm_setting = tk.Tk()
    alarm_setting.title("알림 설정")
    alarm_setting.geometry("250x170")
    alarm_setting.resizable(width=False,height=False)
 
    def Stretching_time():
        req_msg = msgbox.askquestion("설정","시간을 설정하시겠습니까?")
        if req_msg == 'yes': #yes(예)를 클릭하면?
            msgbox.showinfo("완료","시간 설정이 완료되었습니다.")
            time_file = open(file_root+"set_time.txt",'w') #윈도우 바탕화면에 시간 저장용 텍스트파일 만들기(추후 경로 조정)
            time_file.write(alarm_time_set.get()) #Entry 값을 메모장에 쓰기
            time_file.close() #파일 닫기
 
    alarm_time_text = tk.Label(alarm_setting,text="스트레칭 주기: ", font="Geneva 11")
    min_text = tk.Label(alarm_setting, text="분", font="Geneva 11")
 
    alarm_time_set = tk.Entry(alarm_setting, text="", width=3, takefocus=True)
    time_set_button = Button(alarm_setting, text="등록", width=5, takefocus=True, command=Stretching_time) #시간 등록 버튼 ==> 51번 줄의 함수 실행
 
    alarm_time_text.place(x=10,y=25)
    min_text.place(x=155, y=25)
    alarm_time_set.place(x=125,y=25)
    time_set_button.place(x=190,y=25)
 
    #######################################################################################################
 
    def eye_health_time():
        eye_msg = msgbox.askquestion("설정","시간을 설정하시겠습니까?")
        if eye_msg == 'yes': #yes(예)를 클릭하면?
            msgbox.showinfo("완료","시간 설정이 완료되었습니다.")
            eye_file = open(file_root+"eye_health.txt","w")
            eye_file.write(eye_health_entry.get())
            eye_file.close()
 
    eye_health_text = tk.Label(alarm_setting,text="눈 휴식 주기: ", font="Geneva 11")
    eye_health_min = tk.Label(alarm_setting, text="분", font="Geneva 11")
    eye_health_entry = tk.Entry(alarm_setting, text="", width=3, takefocus=True)
    eye_health_button = Button(alarm_setting, text="등록", width=5, takefocus=True, command=eye_health_time)
 
    eye_health_text.place(x=10,y=60)
    eye_health_min.place(x=155,y=60)
    eye_health_entry.place(x=125,y=60)
    eye_health_button.place(x=190,y=60)
 
    #######################################################################################################
 
    def water_time():
        water_msg = msgbox.askquestion("설정","시간을 설정하시겠습니까?")
        if water_msg == 'yes': #yes(예)를 클릭하면?
            msgbox.showinfo("완료","시간 설정이 완료되었습니다.")
            water_file = open(file_root+"water_eat.txt","w")
            water_file.write(water_entry.get())
            water_file.close()
 
    water_text = tk.Label(alarm_setting,text="수분 섭취 주기: ", font="Geneva 11")
    water_min = tk.Label(alarm_setting, text="분", font="Geneva 11")
    water_entry = tk.Entry(alarm_setting, text="", width=3, takefocus=True)
    water_button = Button(alarm_setting, text="등록", width=5, takefocus=True, command=water_time)
 
    water_text.place(x=10,y=95)
    water_min.place(x=155,y=95)
    water_entry.place(x=125,y=95)
    water_button.place(x=190,y=95)
 
    def time_load():
        save_time = tk.Tk()
        save_time.title("등록된 시간")
        save_time.geometry("250x150")
 
        old_str_time = open(file_root+"set_time.txt","r")
        old_str_text = tk.Label(save_time,text="설정된 스트레칭 주기: " + str(old_str_time.read()) + "분", font="Geneva 11")
        old_str_text.place(x=30,y=10)
 
        old_eye_time = open(file_root+"eye_health.txt","r")
        old_eye_text = tk.Label(save_time,text="설정된 눈 휴식 주기: " + str(old_eye_time.read()) + "분", font="Geneva 11")
        old_eye_text.place(x=30,y=60)
 
        old_water_time = open(file_root+"water_eat.txt","r")
        old_water_text = tk.Label(save_time,text="설정된 수분섭취 주기: " + str(old_water_time.read()) + "분", font="Geneva 11")
        old_water_text.place(x=30,y=110)
 
 
    save_time_load = tk.Button(alarm_setting,text="설정된 시간 확인",command=time_load)
    save_time_load.place(x=70,y=130)
 
#######################################################################################################
def manual():
    use_manual = tk.Tk()
    use_manual.title("사용설명서")
    use_manual.geometry("700x300")
    use_manual.resizable(width=False,height=False)
 
    manual_item1 = tk.Label(use_manual,text="1. 본 프로그램은 사소한 오류가 있을 수 있습니다." , font = "Geneva 12 bold")
    manual_item2 = tk.Label(use_manual,text="2. 사용중 오류가 있을 경우 C:/Wtm_Setting 파일을 삭제 후 프로그램을 재시작 해주세요", font = "Geneva 12 bold")
    manual_item3 = tk.Label(use_manual,text="3. 알림 시간의 등록은 분단위만 지원되며 적용후 프로그램을 재시작 해주세요.", font = "Geneva 12 bold")
    manual_item4 = tk.Label(use_manual,text="4. 시간을 측정할 수 있는 최대 프로세스는 4개 입니다.", font = "Geneva 12 bold")
    manual_item5 = tk.Label(use_manual,text="5. 알림을 설정항수 있는 것은 최대 60분입니다.", font = "Geneva 12 bold")
 
    manual_item1.place(x=10,y=30)
    manual_item2.place(x=10,y=55)
    manual_item3.place(x=10,y=80)
    manual_item4.place(x=10,y=105)
    manual_item5.place(x=10,y=130)
 
#---------------------------------------------------------------------------------------------------------------------------#
#메뉴바 - 프로세스 카테고리 설정
 
def process_list():
        process_list_tk = tk.Tk()
        process_list_tk.title("작업 목록")
        process_list_tk.geometry("250x300")
        process_list_tk.resizable(width=False,height=False)
 
        process_menu = tk.Menu(process_list_tk)
        process_menu.add_command(label="추가",command=process_add) #프로세스 카테고리의 1번항목
        process_menu.add_command(label="수정",command=process_modi) #프로세스 카테고리의 2번 항목
        process_menu.add_command(label="삭제",command=process_delete) #프로세스 카테고리의 3번 항목
        process_list_tk.config(menu=process_menu) #메뉴바를 보이게 하기 위한 명령어
 
        process_list_val = open(file_root+"set_process.txt","r")
        process_list_label = tk.Label(process_list_tk,text=process_list_val.read(),font="Geneva 13 bold")
        process_list_label.place(x=0,y=10)
 
#######################################################################################################
#프로세스 추가
def process_add():
    process = tk.Tk()
    process.title("작업 추가")
    process.geometry("250x100")
    process.resizable(width=False,height=False)
 
    def process_add_func():
        text_compare_read = file_root+"set_process.txt"
        with open(text_compare_read) as text_compare:
            text_comp = text_compare.readlines()
        text_comp = [comp.rstrip("\n") for comp in text_comp]
 
        for comp in text_comp:
            if(comp.strip() == textbox1.get()):
                msgbox.showinfo("오류","이미 설정된 항목입니다.")
                break
            else:
                req_msg = msgbox.askquestion("설정","프로그램을 추가하시겠습니까?")
                if req_msg == 'yes': #yes(예)를 클릭하면?
                    msgbox.showinfo("완료","프로그램 추가가 완료되었습니다.")
                    process_add = open(file_root+"set_process.txt","a")
                    process_add.write(textbox1.get().strip())
                    process_add.write("\n")
                    process_add.close()
                    break
   
    #프로세스 목록 입력 텍스트 박스 영역
    textbox1_text = tk.Label(process,text="작업 이름 입력", font = "Geneva 13 bold")
    textbox1 = tk.Entry(process,width=17,text="프로세스")
 
    textbox1_text.place(x=30,y=15)
    textbox1.place(x=35,y=50)
 
    #프로세스 추가 버튼
    button1 = Button(process,text="추가",command=process_add_func)
    button1.place(x=170, y=50)
 
#######################################################################################################
#프로세스 수정
def process_modi():
    modi_win = tk.Tk()
    modi_win.title("작업 수정")
    modi_win.geometry("250x200")
    modi_win.resizable(width=False,height=False)
 
    target_read = file_root+"set_process.txt"
    with open(target_read) as target_list:
        Listread = target_list.readlines()
    Listread = [Lin.rstrip('\n') for Lin in Listread]
 
    target_text = tk.Label(modi_win,text="수정할 항목을 선택하세요.", font = "Geneva 12 bold")
    target_combo = ttk.Combobox(modi_win)
    target_combo.config(values=Listread,width = 15,height=5,state="readonly")
    target_combo.set("항목 선택")
    modi_text = tk.Label(modi_win,text="수정후 이름을 입력하세요", font = "Geneva 12 bold")
    modi_entry = tk.Entry(modi_win,width=17,text="")
 
    target_text.place(x=25,y=20)
    target_combo.place(x=60, y=45)
    modi_text.place(x=25,y=85)
    modi_entry.place(x=60, y=110)
 
    def modi():
        cnt = 0
        #파일을 불러와 리스트 형식으로 변경
        file_path = file_root + "set_process.txt"
        with open(file_path) as f:
            FiletToList = f.readlines()
        FiletToList = [line.rstrip('\n') for line in FiletToList]
 
        for i in FiletToList:
            if(i==target_combo.get()):
                msg = msgbox.askquestion("수정","해당 항목을 변경하시겠습니까?")
                if msg == 'yes': #yes(예)를 클릭하면?
                    msgbox.showinfo("알림","해당 항목의 변경이 완료되었습니다.")
                    FiletToList[cnt] = str(modi_entry.get().strip())
                    file_update = open(file_root+"set_process.txt","w")
 
                    result_file = '\n'.join(str(s) for s in FiletToList)
 
                    file_update.write(str(result_file))
                    file_update.write("\n")
                    file_update.close()
            cnt += 1    
           
    modi_button = Button(modi_win,width=20, text="변경",command=modi)
    modi_button.place(x=50,y=140)
 
#######################################################################################################
#프로세스 삭제
def process_delete():
    delete_win = tk.Tk()
    delete_win.title("작업 삭제")
    delete_win.geometry("250x150")
    delete_win.resizable(width=False,height=False)
 
    delete_text = tk.Label(delete_win,text="삭제할 항목을 입력하세요", font = "Geneva 12 bold")
    delete_entry = tk.Entry(delete_win,width=17,text="")
 
    delete_text.place(x=20,y=20)
    delete_entry.place(x=60,y=50)
 
    def process_del():
        count = 0
        txtfile_path = file_root+"set_process.txt"
        with open(txtfile_path) as f1:
            Filelist = f1.readlines()
        Filelist = [Line.rstrip('\n') for Line in Filelist]
 
        for j in Filelist:
            if(j.strip() == delete_entry.get()):
                del_msg = msgbox.askquestion("삭제","해당 목록을 삭제하시겠습니까?")
                if del_msg == 'yes':
                    msgbox.showinfo("알림","삭제가 완료되었습니다.")
                    del Filelist[count]
                    update_list = open(file_root+"set_process.txt","w")
 
                    result_list = '\n'.join(str(n).strip() for n in Filelist)
 
                    update_list.write(str(result_list))
                    update_list.close()
            count += 1
 
    def all_delete():
        delete_msg = msgbox.askquestion("전체 삭제","전체 목록을 삭제하사겠습니까?")
        if delete_msg == 'yes':
            msgbox.showinfo("알림","삭제가 완료되었습니다.")
            all_del = open(file_root+"set_process.txt","w")
            all_del.write(" ")
            all_del.close()
 
 
    delete_button = tk.Button(delete_win,width=20,text="삭제",command=process_del)
    delete_button.place(x=47,y=80)
 
    all_delete_button = tk.Button(delete_win,width=20,text="전체 삭제",command=all_delete)
    all_delete_button.place(x=47,y=110)
 
def time_log():
    log_win = tk.Tk()
    log_win.title("로그기록")
    log_win.geometry("300x500")
    log_win.resizable(width=False,height=False)

    log_open = open(file_root+"stop_watch.txt","r")
    log_load = tk.Label(log_win,text=log_open.read())
    log_load.place(x=0,y=10)

def log_del():
    logdel_msg = msgbox.askquestion("기록삭제","사용시간 기록을 삭제하시겠습니까?")
    if logdel_msg == 'yes':
        msgbox.showinfo("알림","삭제가 완료되었습니다.")
        log_del = open(file_root+"stop_watch.txt","w")
        log_del.write("")
        log_del.close()
 
#######################################################################################################
#저장한 프로세스의 시간 측정
 
counter1=0
running1 = False
main1 = True
 
counter2=0
running2=False
main2=True
 
counter3=0
running3=False
main3=True
 
counter4=0
running4=False
main4=True
 
counter5=0
running5=False
main5=True
 
def process_timecheck():
    time_check_win = tk.Tk()
    time_check_win.title("작업별 시간 측정")
    time_check_win.geometry("250x610")
    time_check_win.resizable(width=False,height=False)

    time_check_menubar = tk.Menu(time_check_win)

    time_check_menu_object = tk.Menu(time_check_menubar,tearoff=0)
    time_check_menu_object.add_command(label="로그 확인",command=time_log)
    time_check_menu_object.add_command(label="로그 삭제",command=log_del)
    time_check_menubar.add_cascade(label="로그설정",menu=time_check_menu_object)
    time_check_win.config(menu=time_check_menubar)
 
    set_process_file = file_root+"set_process.txt"
    with open(set_process_file) as process_file_list:
        ProcessList = process_file_list.readlines()
    ProcessList = [Liner.rstrip('\n') for Liner in ProcessList]
 
    #######################################################################################################
   
    obj1 = tk.Label(time_check_win,text="작업1: ",font="Geneva 12 bold")
    pro_combo1 = ttk.Combobox(time_check_win)
    pro_combo1.config(values = ProcessList,width = 15,height=5,state="readonly")
    pro_combo1.set("작업 선택")
 
    def counter_label1(elapsed_time1):
        def count():
            if running1:
                global counter1
                tt1 = datetime.fromtimestamp(counter1)
                if(counter1 > 600):
                    date_object1 = tt1.strftime('%H:%M:%S')
 
                elif(counter1 > 60):
                    date_object1 = tt1.strftime('%M:%S.%f')[:-4]
 
                else:
                    date_object1 = tt1.strftime('%S.%f')[:-4]
 
                display1 = date_object1
           
                elapsed_time1['text'] = display1
                elapsed_time1.after(10,count)
                counter1 += 0.01
        count()
 
   
    def clocktime1(elapsed_time1):
        def count1():
            if main1 == True:
                elapsed_time1['text']=time.strftime('%H:%M:%S')
                elapsed_time1.after(500,count1)
        count1()
 
    def Start1(elapsed_time1):
        global running1,main1
        running1=True
        main1 = False
        counter_label1(elapsed_time1)
        start1['state']='disabled'
        stop1['state']='normal'
        reset1['state']='normal'
 
    def Stop1():
        global running1,main1
        start1['state']='normal'
        stop1['state']='disabled'
        save1['state']='normal'
        reset1['state']='normal'
        running1 = False
 
 
    def Reset1(elapsed_time1):
        global counter1,main1
        counter1=00000
        if running1==False:      
            reset1['state']='disabled'
            save1['state']='disabled'
            main1 = True
            clocktime1(elapsed_time1)
 
    def Save1():
        msgbox.showinfo("알림","저장되었습니다.")
        time_save1 = open(file_root+"stop_watch.txt","a")
        time_save1.write("이름: " + str(pro_combo1.get()) + "\n" + "날짜: "+ str(datetime.today().strftime("%Y-%m-%d")) + "\n" + "사용시간: " + str(elapsed_time1.cget("text")))
        time_save1.write("\n")
        time_save1.write("------------------------------------------------------")
        time_save1.write("\n")
        time_save1.close()
       
 
    elapsed_time_text1 = tk.Label(time_check_win, text="사용 시간: ",font = "Geneva 15 bold")
    elapsed_time1 = tk.Label(time_check_win, text=time.strftime('%H:%M:%S'),font="Geneva 15 bold")
    clocktime1(elapsed_time1)
 
    #스톱워치 스타트, 리셋, 스탑 버튼 생성
    start1 = Button(time_check_win, text='Start', width=5,height=1, command=lambda:Start1(elapsed_time1),font="Geneva 10 bold") #start버튼을 생성, command는 start함수라는 수식을 command기능으로 가져온다
    reset1 = Button(time_check_win, text='Reset',width=5,height=1, state='disabled', command=lambda:Reset1(elapsed_time1),font="Geneva 10 bold")
    stop1 = Button(time_check_win, text='Stop',width=5,height=1,state='disabled',command=Stop1,font="Geneva 10 bold")
    save1 = Button(time_check_win,text="Save",width=5,height=1,state='disabled',command=Save1,font="Geneva 10 bold")
 
 
    #######################################################################################################
 
    obj2 = tk.Label(time_check_win,text="작업2: ",font="Geneva 12 bold")
    pro_combo2 = ttk.Combobox(time_check_win)
    pro_combo2.config(values = ProcessList,width = 15,height=5,state="readonly")
    pro_combo2.set("작업 선택")
   
    def counter_label2(elapsed_time2):
        def count2():
            if running2:
                global counter2
                tt2 = datetime.fromtimestamp(counter2)
                if(counter2 > 600):
                    date_object2 = tt2.strftime('%H:%M:%S')
 
                elif(counter2 > 60):
                    date_object2 = tt2.strftime('%M:%S.%f')[:-4]
 
                else:
                    date_object2 = tt2.strftime('%S.%f')[:-4]
 
                display2 = date_object2
           
                elapsed_time2['text'] = display2
                elapsed_time2.after(10,count2)
                counter2 += 0.01
        count2()
   
   
    def clocktime2(elapsed_time2):
        def count2():
            if main2 == True:
                elapsed_time2['text']=time.strftime('%H:%M:%S')
                elapsed_time2.after(500,count2)
        count2()
   
    def Start2(elapsed_time2):
        global running2,main2
        running2=True
        main2 = False
        counter_label2(elapsed_time2)
        start2['state']='disabled'
        stop2['state']='normal'
        reset2['state']='normal'
 
    def Stop2():
        global running2,main2
        start2['state']='normal'
        stop2['state']='disabled'
        save2['state']='normal'
        reset2['state']='normal'
        running2 = False
 
    def Reset2(elapsed_time2):
        global counter2,main2
        counter2=00000
        if running2==False:      
            reset2['state']='disabled'
            save2['state']='disabled'
            main2 = True
            clocktime2(elapsed_time2)
 
    def Save2():
        msgbox.showinfo("알림","저장되었습니다.")
        time_save2 = open(file_root+"stop_watch.txt","a")
        time_save2.write("이름: "+str(pro_combo2.get()) + "\n" + "날짜: "+ str(datetime.today().strftime("%Y-%m-%d")) + "\n"  + "사용시간: " + str(elapsed_time2.cget("text")))
        time_save2.write("\n")
        time_save2.write("------------------------------------------------------")
        time_save2.write("\n")
        time_save2.close()
 
    elapsed_time_text2 = tk.Label(time_check_win, text="사용 시간: ",font = "Geneva 15 bold")
    elapsed_time2 = tk.Label(time_check_win, text=time.strftime('%H:%M:%S'),font="Geneva 15 bold")
    clocktime2(elapsed_time2)
 
    #스톱워치 스타트, 리셋, 스탑 버튼 생성
    start2 = Button(time_check_win, text='Start', width=5,height=1, command=lambda:Start2(elapsed_time2),font="Geneva 10 bold") #start버튼을 생성, command는 start함수라는 수식을 command기능으로 가져온다
    reset2 = Button(time_check_win, text='Reset',width=5,height=1, state='disabled', command=lambda:Reset2(elapsed_time2),font="Geneva 10 bold")
    stop2 = Button(time_check_win, text='Stop',width=5,height=1,state='disabled',command=Stop2,font="Geneva 10 bold")
    save2 = Button(time_check_win,text="Save",width=5,height=1,state='disabled',command=Save2,font="Geneva 10 bold")
   
    #######################################################################################################
 
    obj3 = tk.Label(time_check_win,text="작업3: ",font="Geneva 12 bold")
    pro_combo3 = ttk.Combobox(time_check_win)
    pro_combo3.config(values = ProcessList,width = 15,height=5,state="readonly")
    pro_combo3.set("작업 선택")
   
    def counter_label3(elapsed_time3):
        def count3():
            if running3:
                global counter3
                tt3 = datetime.fromtimestamp(counter3)
                if(counter3 > 600):
                    date_object3 = tt3.strftime('%H:%M:%S')
 
                elif(counter3 > 60):
                    date_object3 = tt3.strftime('%M:%S.%f')[:-4]
 
                else:
                    date_object3 = tt3.strftime('%S.%f')[:-4]
 
                display3 = date_object3
           
                elapsed_time3['text'] = display3
                elapsed_time3.after(10,count3)
                counter3 += 0.01
        count3()
   
   
    def clocktime3(elapsed_time3):
        def count3():
            if main3 == True:
                elapsed_time3['text']=time.strftime('%H:%M:%S')
                elapsed_time3.after(500,count3)
        count3()
   
    def Start3(elapsed_time3):
        global running3,main3
        running3=True
        main3 = False
        counter_label3(elapsed_time3)
        start3['state']='disabled'
        stop3['state']='normal'
        reset3['state']='normal'
 
    def Stop3():
        global running3,main3
        start3['state']='normal'
        stop3['state']='disabled'
        save3['state']='normal'
        reset3['state']='normal'
        running3 = False
 
    def Reset3(elapsed_time3):
        global counter3,main3
        counter3=00000
        if running3==False:      
            reset3['state']='disabled'
            save3['state']='disabled'
            main3 = True
            clocktime3(elapsed_time3)
 
    def Save3():
        msgbox.showinfo("알림","저장되었습니다.")
        time_save3 = open(file_root+"stop_watch.txt","a")
        time_save3.write("이름: "+str(pro_combo3.get()) + "\n" + str(datetime.today().strftime("%Y-%m-%d")) + "\n" + "사용시간: " + str(elapsed_time3.cget("text")))
        time_save3.write("\n")
        time_save3.write("------------------------------------------------------")
        time_save3.write("\n")
        time_save3.close()
 
    elapsed_time_text3 = tk.Label(time_check_win, text="사용 시간: ",font = "Geneva 15 bold")
    elapsed_time3 = tk.Label(time_check_win, text=time.strftime('%H:%M:%S'),font="Geneva 15 bold")
    clocktime3(elapsed_time3)
 
    #스톱워치 스타트, 리셋, 스탑 버튼 생성
    start3 = Button(time_check_win, text='Start', width=5,height=1, command=lambda:Start3(elapsed_time3),font="Geneva 10 bold") #start버튼을 생성, command는 start함수라는 수식을 command기능으로 가져온다
    reset3 = Button(time_check_win, text='Reset',width=5,height=1, state='disabled', command=lambda:Reset3(elapsed_time3),font="Geneva 10 bold")
    stop3 = Button(time_check_win, text='Stop',width=5,height=1,state='disabled',command=Stop3,font="Geneva 10 bold")
    save3 = Button(time_check_win,text="Save",width=5,height=1,state='disabled',command=Save3,font="Geneva 10 bold")
   
    #######################################################################################################
 
    obj4 = tk.Label(time_check_win,text="작업4: ",font="Geneva 12 bold")
    pro_combo4 = ttk.Combobox(time_check_win)
    pro_combo4.config(values = ProcessList,width = 15,height=5,state="readonly")
    pro_combo4.set("작업 선택")
 
    def counter_label4(elapsed_time4):
        def count4():
            if running4:
                global counter4
                tt4 = datetime.fromtimestamp(counter4)
                if(counter4 > 600):
                    date_object4 = tt4.strftime('%H:%M:%S')
 
                elif(counter4 > 60):
                    date_object4 = tt4.strftime('%M:%S.%f')[:-4]
 
                else:
                    date_object4 = tt4.strftime('%S.%f')[:-4]
 
                display4 = date_object4
           
                elapsed_time4['text'] = display4
                elapsed_time4.after(10,count4)
                counter4 += 0.01
        count4()
   
   
    def clocktime4(elapsed_time4):
        def count4():
            if main4 == True:
                elapsed_time4['text']=time.strftime('%H:%M:%S')
                elapsed_time4.after(500,count4)
        count4()
   
    def Start4(elapsed_time4):
        global running4,main4
        running4=True
        main4 = False
        counter_label4(elapsed_time4)
        start4['state']='disabled'
        stop4['state']='normal'
        reset4['state']='normal'
 
    def Stop4():
        global running4,main4
        start4['state']='normal'
        stop4['state']='disabled'
        save4['state']='normal'
        reset4['state']='normal'
        running4 = False
 
    def Reset4(elapsed_time4):
        global counter4,main4
        counter4=00000
        if running4==False:      
            reset4['state']='disabled'
            save4['state']='disabled'
            main4 = True
            clocktime4(elapsed_time4)
 
    def Save4():
        msgbox.showinfo("알림","저장되었습니다.")
        time_save4 = open(file_root+"stop_watch.txt","a")
        time_save4.write("이름: "+str(pro_combo4.get()) + "\n" + str(datetime.today().strftime("%Y-%m-%d")) + "\n" + "사용시간: " + str(elapsed_time4.cget("text")))
        time_save4.write("\n")
        time_save4.write("------------------------------------------------------")
        time_save4.write("\n")
        time_save4.close()
 
    elapsed_time_text4 = tk.Label(time_check_win, text="사용 시간: ",font = "Geneva 15 bold")
    elapsed_time4 = tk.Label(time_check_win, text=time.strftime('%H:%M:%S'),font="Geneva 15 bold")
 
    clocktime4(elapsed_time4)
 
    #스톱워치 스타트, 리셋, 스탑 버튼 생성
    start4 = Button(time_check_win, text='Start', width=5,height=1, command=lambda:Start4(elapsed_time4),font="Geneva 10 bold") #start버튼을 생성, command는 start함수라는 수식을 command기능으로 가져온다
    reset4 = Button(time_check_win, text='Reset',width=5,height=1, state='disabled', command=lambda:Reset4(elapsed_time4),font="Geneva 10 bold")
    stop4 = Button(time_check_win, text='Stop',width=5,height=1,state='disabled',command=Stop4,font="Geneva 10 bold")
    save4 = Button(time_check_win,text="Save",width=5,height=1,state='disabled',command=Save4,font="Geneva 10 bold")
   
    #######################################################################################################
   
    #프로세스 1~4 텍스트
    obj1.place(x=10,y=30)
    obj2.place(x=10, y=180)
    obj3.place(x=10,y=330)
    obj4.place(x=10,y=480)
 
    #콤보박스 위치 레이아웃
    pro_combo1.place(x=70,y=33)
    pro_combo2.place(x=70,y=183)
    pro_combo3.place(x=70,y=333)
    pro_combo4.place(x=70,y=483)
 
    #사용시간 출력 위치 레이아웃
    elapsed_time_text1.place(x=10, y=60) #사용시간 텍스트의 좌표 설정
    elapsed_time1.place(x=110,y=60) #사용시간의 좌표 설정
 
    elapsed_time_text2.place(x=10, y=210) #사용시간 텍스트의 좌표 설정
    elapsed_time2.place(x=110,y=210) #사용시간의 좌표 설정
 
    elapsed_time_text3.place(x=10, y=360) #사용시간 텍스트의 좌표 설정
    elapsed_time3.place(x=110,y=360) #사용시간의 좌표 설정
 
    elapsed_time_text4.place(x=10, y=510) #사용시간 텍스트의 좌표 설정
    elapsed_time4.place(x=110,y=510) #사용시간의 좌표 설정
 
    #버튼 위치 레이아웃
    start1.place(x=10,y=100)
    reset1.place(x=60,y=100)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    stop1.place(x=110,y=100)
    save1.place(x=160,y=100)
 
    tk_liner1 = tk.Label(time_check_win,text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",font="Geneva 12 bold")
    tk_liner1.place(x=0,y=150)
 
    start2.place(x=10,y=250)
    reset2.place(x=60,y=250)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    stop2.place(x=110,y=250)
    save2.place(x=160,y=250)
 
    tk_liner2 = tk.Label(time_check_win,text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",font="Geneva 12 bold")
    tk_liner2.place(x=0,y=300)
 
    start3.place(x=10,y=400)
    reset3.place(x=60,y=400)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    stop3.place(x=110,y=400)
    save3.place(x=160,y=400)
 
    tk_liner3 = tk.Label(time_check_win,text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",font="Geneva 12 bold")
    tk_liner3.place(x=0,y=450)
 
    start4.place(x=10,y=550)
    reset4.place(x=60,y=550)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    stop4.place(x=110,y=550)
    save4.place(x=160,y=550)
#---------------------------------------------------------------------------------------------------------------------------#
#메뉴바 - 윈도우 카테고리 설정
 
#윈도우 카테고리의 창닫기 기능을 위한 함수
def exit():
    str = msgbox.askquestion("닫기","종료하시겠습니까?") #종료를 물어보는 메시지 박스
    if str == 'yes': #yes(예)를 클릭하면?
        sys.exit(0) #프로그램 종료
 
#######################################################################################################
#윈도우 자체 창닫기 기능을 위한 함수
def exit_window_x():
    str = msgbox.askquestion("닫기","종료하시겠습니까?") #종료를 물어보는 메시지 박스
    if str == 'yes': #yes(예)를 클릭하면?
        sys.exit(0) #프로그램 종료
window.protocol('WM_DELETE_WINDOW',exit_window_x)
 
#---------------------------------------------------------------------------------------------------------------------------#
#시간 관련 기능 설정코드
 
counter = 0
 
file_open = open(file_root+"set_time.txt","r") #저장한 시간 파일 열기
set_time_open = file_open.read() #저장한 시간 불러오기
 
eye_health_open = open(file_root+"eye_health.txt","r")
eye_health_time = eye_health_open.read()
 
water_open = open(file_root+"water_eat.txt","r")
water_time = water_open.read()
 
memo_open = open(file_root+"memo_time.txt","r")
memo_time = memo_open.read()
 
memo_text_open = open(file_root+"memo.txt","r",encoding='cp949').read()
 
f1 = int(open(file_root+"set_time.txt","r").read())
f2 = int(open(file_root+"eye_health.txt","r").read())
f3 = int(open(file_root+"water_eat.txt","r").read())
f4 = int(open(file_root+"memo_time.txt","r").read())
 
alarm_time_sett = int(set_time_open) * 60  # 60을 곱하는 이유: 분을 초로 변환하기 위함
eye_time_sett = int(eye_health_time) * 60
water_time_sett = int(water_time) * 60
memo_sett = int(memo_time) * 60
 
cnt = int(f1) * 60  #스트레칭 알림주기 시간을 갱신할 변수 EX) 5분 -> 10분 -> 15분...
eye_cnt = int(f2) * 60#눈 휴식 알림주기 갱신 변수
water_cnt = int(f3)* 60
memo_cnt = int(f4) * 60
 
running = False
main = True
 
def counter_label(elapsed_time_main):
    def count():
        if running:
 
            global counter
            global eye_cnt
            global water_cnt
            global memo_cnt
            global cnt
 
            tt = datetime.fromtimestamp(counter)
            if(counter > 600):
                date_object = tt.strftime('%H:%M:%S')
 
            elif(counter > 60):
                date_object = tt.strftime('%M:%S.%f')[:-4]
 
            else:
                date_object = tt.strftime('%S.%f')[:-4]
 
            display = date_object
       
            elapsed_time_main['text'] = display
           
            #---------------------------------------------------------------------------------------------------------------------------#
            # 스트레칭 알림 기능 파트
            if(round(counter,3) == cnt + 0.01):
                cnt = cnt + alarm_time_sett
                toaster = ToastNotifier()
                toaster.show_toast("스트레칭 알리미","허리, 목 건강을 위한 스트레칭을 권장드립니다.", icon_path=None, duration=3, threaded=True)
 
            if(round(counter,3) == eye_cnt + 0.01):
                eye_cnt = eye_cnt + eye_time_sett
                toaster1 = ToastNotifier()
                toaster1.show_toast("눈 휴식 알리미","눈 건강을 위한 휴식을 권장드립니다.", icon_path=None, duration=3, threaded=True)
 
            if(round(counter,3) == water_cnt + 0.01):
                water_cnt = water_cnt + water_time_sett
                toaster2 = ToastNotifier()
                toaster2.show_toast("수분 섭취 알리미","건강 관리를 위한 수분 섭취를 권장드립니다.", icon_path=None, duration=3, threaded=True)
           
            if(round(counter,3) == memo_cnt + 0.01):
                memo_cnt = memo_cnt + memo_sett
                toaster3 = ToastNotifier()
                toaster3.show_toast("메모 알림",str(memo_text_open), icon_path=None, duration=3, threaded=True)
           
            #---------------------------------------------------------------------------------------------------------------------------#
            elapsed_time_main.after(10,count)
            counter += 0.01
 
    count()
 
def clocktime(elapsed_time_main):
    def count():
        if main == True:
            elapsed_time_main['text']=time.strftime('%H:%M:%S')
            elapsed_time_main.after(500, count)
    count()
 
 
def Start(elapsed_time_main):
    global running,main
    running=True
    main = False
    counter_label(elapsed_time_main)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
 
def Stop():
    global running,main
    start['state']='normal'
    stop['state']='disabled'
    save['state']='normal'
    reset['state']='normal'
    running = False
 
 
def Reset(elapsed_time_main):
    global counter,main
    counter=00000
    if running==False:      
        reset['state']='disabled'
        save['state']='disabled'
        main = True
        clocktime(elapsed_time_main)

def Save():
    msgbox.showinfo("알림","저장되었습니다.")
    main_time_save = open(file_root+"main_time_save.txt","a")
    main_time_save.write("날짜: "+ str(datetime.today().strftime("%Y-%m-%d")) + "\n" + "사용시간: " + str(elapsed_time_main.cget("text")))
    main_time_save.write("\n")
    main_time_save.write("------------------------------------------------------")
    main_time_save.write("\n")
    main_time_save.close()

def mainlog_check():
    mainlog_check_tk = tk.Tk()
    mainlog_check_tk.title("로그기록")
    mainlog_check_tk.geometry("300x500")
    mainlog_check_tk.resizable(width=False,height=False)
    
    mainlog_open = open(file_root+"main_time_save.txt","r").read()
    mainlog_load = tk.Label(mainlog_check_tk,text=mainlog_open)
    mainlog_load.place(x=0,y=10)
  

def mainlog_del():
    main_logdel_msg = msgbox.askquestion("기록삭제","사용시간 기록을 삭제하시겠습니까?")
    if main_logdel_msg == 'yes':
        msgbox.showinfo("알림","삭제가 완료되었습니다.")
        main_log_delete = open(file_root+"main_time_save.txt","w")
        main_log_delete.write(" ")
        main_log_delete.close()

#---------------------------------------------------------------------------------------------------------------------------#
 
#시간 화면 레이아웃 - 시작시간
starttime_text = tk.Label(window, text="시작 시간: ", fg = "white", font = "Geneva 15 bold", bg = "#282828" )
starttime_time = tk.Label(window, text=time.strftime('%H:%M:%S'), fg="white", font="Geneva 15 bold",bg="#282828")
 
starttime_text.place(x=40, y=30) #시작시간 텍스트의 좌표 설정
starttime_time.place(x=140, y=32) #시작시간의 좌표 설정
 
#---------------------------------------------------------------------------------------------------------------------------#
 
#시간 화면 레이아웃 - 사용시간 & 현재시간
elapsed_time_text = tk.Label(window, text="사용 시간: ", fg = "white", font = "Geneva 15 bold", bg = "#282828" )
elapsed_time_main = tk.Label(window, text=time.strftime('%H:%M:%S'), fg="white", font="Geneva 15 bold",bg="#282828")
 
elapsed_time_text.place(x=40, y=70) #사용시간 텍스트의 좌표 설정
elapsed_time_main.place(x=140,y=70) #사용시간의 좌표 설정
 
#---------------------------------------------------------------------------------------------------------------------------#
#윈도우 메뉴바 설정
menubar = tk.Menu(window)
 
menu_object = tk.Menu(menubar,tearoff=0) #메뉴바의 첫번째 항목 설정
menu_object.add_command(label="메모장",command=memo)
menu_object.add_command(label="알람설정",command=alarm_time)
menu_object.add_command(label="파일경로",command=root_print)
menu_object.add_command(label="사용설명서",command=manual)
menubar.add_cascade(label="시스템",menu=menu_object) #첫번째 카테고리 이름을 시스템으로 설정
 
#######################################################################################################
 
menu_object2 = tk.Menu(menubar,tearoff=0) # 메뉴바의 두번째 항목 설정
menu_object2.add_command(label="작업관리",command=process_list)
menu_object2.add_command(label="시간측정",command=process_timecheck)
menubar.add_cascade(label="작업",menu=menu_object2) #두번째 카테고리의 이름을 프로세스로 설정
#######################################################################################################

menu_object3 = tk.Menu(menubar,tearoff=0) # 메뉴바의 두번째 항목 설정
menu_object3.add_command(label="로그확인",command=mainlog_check)
menu_object3.add_command(label="로그삭제",command=mainlog_del)
menubar.add_cascade(label="로그",menu=menu_object3)
#######################################################################################################
 
menu_object4 = tk.Menu(menubar,tearoff=0) # 메뉴바의 세번째 항목 설정
menu_object4.add_command(label="창 닫기",command=exit) #윈도우 카테고리의 두번째 항목, command는 항을 닫기 위한 함수, 81번줄 참조
menubar.add_cascade(label="윈도우",menu=menu_object4) #세번째 카테고리의 이름을 윈도우로 설정
window.config(menu=menubar) #메뉴바를 보이게 하기 위한 명령어


#---------------------------------------------------------------------------------------------------------------------------#
window.attributes("-alpha", 0.90)
clocktime(elapsed_time_main)
 
f = Frame(window) #위젯들을 포함하는 frame생성
window.config(bg="#282828")
f.configure(background="#282828")
 
#스톱워치 스타트, 리셋, 스탑 버튼 생성
start = Button(f, text='Start', width=5,height=1, command=lambda:Start(elapsed_time_main),font="Geneva 15 bold") #start버튼을 생성, command는 start함수라는 수식을 command기능으로 가져온다
reset = Button(f, text='Reset',width=5,height=1, state='disabled', command=lambda:Reset(elapsed_time_main),font="Geneva 15 bold")
stop = Button(f, text='Stop',width=5,height=1,state='disabled',command=Stop,font="Geneva 15 bold")
save = Button(text="save",width=22,height=1,state='disabled',command=Save,font="Geneva 12 bold")
 
f.place(x=30,y=120)
start.pack(side="left",padx=5)
reset.pack(side="left", padx=5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
stop.pack(side ="left", padx=5)
save.place(x=35,y=175)

window.mainloop()