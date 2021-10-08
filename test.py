#Truy cap xu ly file tu he thong
import os
#Mở âm thanh
import playsound
#Chuyen giong noi thanh van ban
import speech_recognition as sr
from gtts import gTTS, tts
#Xu ly thoi gian
import time
import datetime
from datetime import date
from time import strftime
#Lay thong tin tu web
import requests
import json
#Truy cap web
import re
import webbrowser
#Truy cap web, Ho tro tim kiem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from wikipedia.wikipedia import languages
from youtube_search import YoutubeSearch
#Thong bao tren win10
from win10toast import ToastNotifier
import pyttsx3
import youtube_search
#Chon ngau nhien
import random
from PIL import Image, ImageTk
import wikipedia
from win10toast import ToastNotifier
import pyttsx3
import smtplib
import urllib
import urllib.request as urllib2
import sys
import ctypes
#Tao giao dien tkinder
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox


wikipedia.set_lang('vi')
language='vi'
path = ChromeDriverManager().install()
root = Tk()
text_area = Text(root, height=26, width=45)
scroll = Scrollbar(root, command=text_area.yview)

#Text to Audio
def speak(text):
    print("Bot: " ,text)
    text_area.insert(INSERT,"Bot: "+text+"\n")
    root.update()
    tts=gTTS(text=text,lang=language,slow=False)
    tts.save("bot.mp3")
    playsound.playsound("bot.mp3",True)
    os.remove("bot.mp3")
#Voice to Text
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bot: Đang lắng nghe...")
        audio = r.listen(source, phrase_time_limit=6)
        root.update()
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print("You:",text)
            root.update()
            return text
        except:
            print(" ")
            root.update()
            return 0        
    
#Tam biet
def stop():
    day_time = int(strftime('%H'))
    if  6 <= day_time < 12:
        speak(f"Tạm biệt bạn! Chúc bạn một ngày tốt lành.")
        root.update()
    elif 12 <= day_time <= 18:
        speak(f"Tạm biệt bạn! Chúc bạn một buồi chiều tốt lành.")
        root.update()
    elif 19 <= day_time < 22:
        speak(f"Tạm biệt bạn! Chúc bạn buổi tối tốt lành.")
        root.update()
    else:
        speak(f"Tạm biệt bạn! Chúc bạn ngủ ngon!")
        root.update()
#Chuyen am thanh thanh van ban
def get_text():
    for i in range(3):
        text=get_audio()
        root.update()
        if text:
            return text.lower()
        elif i<2:
            speak("Bot không nghe được! Bạn có thể nói lại không?")
            root.update()
    text_area.insert(INSERT,"Bot: "+text+"\n")
    root.update()
    time.sleep(5)
    stop()
    return 0

#Hello function
def hello(name):
    day_time = int(strftime('%H'))
    if  6 <= day_time < 12:
        speak(f"Chào bạn {name} . Chúc bạn một ngày tốt lành.")
        speak(f'Bot có thể giúp gì cho bạn?')
        root.update()
    elif 12 <= day_time <= 18:
        speak(f"Chào bạn {name} . Chúc bạn một buồi chiều tốt lành.")
        speak(f'Bot có thể giúp gì cho bạn?')
        root.update()
    elif 19 <= day_time < 22:
        speak(f"Chào bạn {name} .Chúc bạn buổi tối tốt lành.")
        speak(f'Bot có thể giúp gì cho bạn?')
        root.update()
    else:
            speak(f"Đã khuya rồi bạn nên đi ngủ sớm đi ! Tôi buồn ngủ rồi")
            root.update()
    root.update()
#Time function
def get_time(text):
    now=datetime.datetime.now()
    if 'giờ' in text or 'time' in text:
        speak(f"Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây")
        root.update()
    elif 'ngày' in text or 'day' in text:
        speak(f"Hôm nay là ngày {now.day} tháng {now.month} năm {now.year} ")
        root.update()
    else:
        speak("Bot chưa hiểu ý bạn!")
        root.update()
    root.update()
#Lay thu trong tuan
def get_day():
    today = datetime.datetime.today()
    wd=date.weekday(today)
    days = ['Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ nhật']
    speak(f"Hôm nay là: {days[wd]}")
    root.update()
#Open app
def open_app(text):
    if 'chrome' in text: 
        speak("OK!")
        os.startfile("D:\\Python\\Google\\Chrome\\Application\\chrome.exe")
    elif 'chỉnh sửa ảnh' in text: 
        speak("OK!")
        os.startfile("D:\Python\AdobePhotoshopCS6.lnk")  
    else: 
        speak("Ứng dụng này chưa được cài đặt! Tôi không thể mở")
    root.update()
    time.sleep(5)
#Open website
def open_website(text):
    reg_ex=re.search('mở website (.+)' , text)
    if reg_ex:
        domain=reg_ex.group(1)
        url="https://www." + domain
        webbrowser.open(url)
        speak("Website bạn yêu cầu đã được mở!")
        time.sleep(10)
        root.update()
        return True
    else:
        return False
    
#update Covid 19
def update():
     r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
     data=r.json()
     text=f'Số ca nhiễm: {data["cases"]} ca \nSố ca tử vong: {data["deaths"]} ca \nSố ca hồi phục: {data["recovered"]} ca'
     while True:
         speak("Đây là tình hình Covid 19 trên toàn Thế Giới được cập nhật tính tới hôm nay!")
         speak(text)
         break
     root.update()
#Search with Google
def google_search(text):
    search_for=str(text).split("kiếm",1)[1]
    url=f"https://www.google.com/search?q={search_for}"
    speak("Đã tìm kiếm thông tin bạn cần bằng Google")
    webbrowser.get().open(url)
    time.sleep(10)
    root.update()
#Play youtube
def play_youtube():
    speak("Bạn muốn xem gì trên Youtube")
    search=get_text()
    while True:
        result=YoutubeSearch(search, max_results=10).to_dict()
        if result:
            break
    url = f"https://www.youtube.com" + result[0]['url_suffix']
    speak("Video bạn muốn xem đang được mở")
    webbrowser.get().open(url)
    time.sleep(10)
    root.update()
#Weather
def get_weather():
    speak("Bạn muốn xem thời tiết ở đâu")
    root.update()
    ow_url="http://api.openweathermap.org/data/2.5/weather?"
    city=get_text()
    if not city:
        pass
    api_key="c7334951866002bfd6943b57ac017ade"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        speak(f"Thời tiết của {city}")
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_humidity=city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Ngày {day} tháng {month} năm {year} là:
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Độ ẩm trung bình là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature ,humidity=current_humidity)
        speak(content)
        root.update()
        time.sleep(5)
    else:
        speak("Không tìm thấy thành phố của bạn")
        root.update()
        time.sleep(2)
#Mo nhac
def play_happymusic():
    speak("Nhạc bạn yêu cầu đang được mở")
    root.update()
    myPath=r"D:\Python\Music\HappyMusic"
    ds=os.listdir(myPath)
    for i in ds:
        print("\nĐang phát: "+i)
        root.update()
        os.system(myPath + "\\" +i)
        time.sleep(10)
        root.update()
def play_sadmusic():
    speak("Nhạc bạn yêu cầu đang được mở")
    myPath=r"D:\Python\Music\SadMusic"
    ds=os.listdir(myPath)
    for i in ds:
        print("\nĐang phát: "+i)
        root.update()
        os.system(myPath + "\\" +i)
        time.sleep(10)
        root.update()
def play_rapmusic():
    speak("Nhạc bạn yêu cầu đang được mở")
    myPath=r"D:\Python\Music\RapMusic"
    ds=os.listdir(myPath)
    for i in ds:
        print("\nĐang phát: "+i)
        root.update()
        os.system(myPath + "\\" +i)
        time.sleep(10)
        root.update()
#Tro giup
def help_me():
    speak("""Bot có thể giúp bạn thực hiện các chức năng sau đây:
    1. Hiển thị ngày,giờ hiện tại
    2. Mở website, ứng dụng
    3. Tìm kiếm trên Google
    4. Dự báo thời tiết
    5. Mở video trên Youtube
    6. Thông tin về số ca nhiễm bệnh Covid 19 trên toàn Thế giới 
    7. Mở nhạc
    8. Gợi ý cách thả thính 
    9. Tìm định nghĩa trên wikipedia
    10. Chào tạm biệt
    """)
    root.update()
    time.sleep(3) 
#Tha thinh
def love_you():
    mylist = ["Thiếu 500 nghìn là em tròn một củ. Thiếu anh nữa là em đủ một đôi.",
    "Đố ai quyét sạch được lá rừng. Đố ai khuyên được em ngừng yêu anh!",
    "Trời không xanh, Mây cũng không trắng, Em không say nắng, Nhưng lại say anh.",
    "Cho em một cốc trà đào, Tiện cho em hỏi lối vào tim anh!",
    "Em đây rất thích đồng hồ, Thích luôn cả việc làm bồ của anh.",
    "Vector chỉ có một chiều, Em dân chuyên toán chỉ yêu 1 người.",
    "Hoa vô tình bỏ rơi cành lá, Người vô tình bỏ lỡ tơ duyên",
    "Ngoài kia bão táp mưa sa, Bôn ba mệt quá về nhà với em",
    "Trăng kia ai vẽ mà tròn, Lòng anh ai trộm mà hoài nhớ thương",
    "Nhân gian vốn lắm bộn bề. Sao không bỏ hết mà về với em.",
    "Thức khuya em tỉnh bằng trà, yêu anh em trả bằng tình được không?",
    "Suốt bao năm lòng em luôn yên tĩnh. Gặp anh rồi, tĩnh lặng hóa phong ba.",
    "Nắng kia là của ông trời, còn anh đã của ai rồi hay chưa? ",
    "Mây kia là của hạt mưa, anh xem đã thích em chưa hay rồi?",
    "Cánh đồng xanh xanh, làn mây trăng trắng. Tưởng là say nắng ai ngờ say em.",
    "Trứng rán cần mỡ bắp cần bơ, yêu không cần cớ cần cậu cơ."]
    love=random.choice(mylist)
    speak("Đây là gợi ý của tôi")
    speak(love)
    root.update()
    time.sleep(1)
    speak("Chúc bạn thành công!")
    root.update()
#Định nghĩa wikipedia
def tell_me_about():
    try:
        speak("Hãy nói cho tôi nghe bạn muốn tìm định nghĩa về gì ạ ?")
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0]) 
        dem = 0
        for content in contents[1:]:
            if dem < 2:
                speak("Bạn có muốn biết thêm không ???")
                ans = get_text()
                if 'có' not in ans:
                    break
            dem += 1
            speak(content)
            root.update()
        speak("Đây là thông tin tôi tìm được!")
        root.update()
    except:
        speak("Tôi không biết!")
        root.update()
#brain
def main_brain():
    speak("Xin chào mình là Bot! Cho hỏi bạn tên là gì?")     
    root.update()
    name=get_text()
    text_area.insert(INSERT,"You: "+name+"\n")
    root.update()
    if name:
        hello(name)
        text_area.insert(INSERT,"_____________________________________________")
        text=""
        while True:
            text=get_text()
            if not text:
                break
            elif 'có thể làm gì' in text:
                help_me()
            elif 'bây giờ' in text or 'hôm nay là' in text:
                if 'thứ' in text:
                    get_day()
                else:
                    get_time(text)
            elif 'tạm biệt' in text or 'hẹn gặp lại' in text:
                stop()
                break 
            elif 'mở website' in text:
                if '.' in text:
                    open_website(text)
                else:
                    speak("Tôi không hiểu! Bạn chọn chức năng khác đi")
            elif 'mở phần mềm' in text or 'mở ứng dụng' in text: 
                open_app(text)
            elif 'tìm kiếm' in text: 
                google_search(text)   
            elif 'xem' in text:
                play_youtube()
            elif 'thời tiết' in text:
                get_weather()
            elif 'dịch ' in text or 'số ca' in text or 'covid' in text:
                update()
            elif 'nhạc' in text:
                speak("Bạn muốn nghe thể loại nhạc gì")
                text1=get_text()
                if 'vui' in text1 or 'happy' in text1 or 'yêu đời' in text1:
                     play_happymusic()
                elif 'buồn' in text1 or 'tâm trạng' in text1:
                     play_sadmusic()
                elif 'rap' in text1:
                     play_rapmusic()
                else:
                     speak("Tôi không có thể loại nhạc này")
            elif 'thả thính' in text:
                love_you()      
            elif 'định nghĩa' in text:
                tell_me_about()
            else:
                speak("Mình chua có chức năng này! Bạn hỏi thứ khác đi!")
            text_area.insert(INSERT,"_____________________________________________")
            text=""
class Example(Frame):
   def __init__(self, parent):
     Frame.__init__(self, parent)
     self.parent = parent
     self.initUI()
  
   def initUI(self):
     self.parent.title("Bot AI")
     self.style = Style()
     self.style.theme_use("default")
  
     scroll.pack(side=RIGHT, fill=Y)
     text_area.configure(yscrollcommand=scroll.set)
     text_area.pack(side=RIGHT)

     frame = Frame(self, relief=RAISED, borderwidth=1)
     frame.pack(fill=BOTH, expand=True)
     self.pack(fill=BOTH, expand=True)

     closeButton = Button(self, text="Close", command=self.quit,width=20,bg='#009999',fg='White')
     closeButton.pack(side=LEFT, padx=5, pady=5)
     okButton = Button(self, text="Start",command=main_brain,width=20,bg='#009999',fg='White')
     okButton.pack(side=LEFT)
     
     image_1 = ImageTk.PhotoImage(Image.open("bot1.png"))    
     label1 = Label(self, image=image_1)
     label1.image = image_1
     label1.place(x=7, y=43)
     l = Label(root, text='Lịch sử trò chuyện', fg='White', bg='blue')
     l.place(x = 750, y = 10, width=120, height=25)
root.resizable(False, False)
root.geometry("1000x510+250+50")
root.iconbitmap("bot.ico")
app = Example(root)
root.mainloop()

