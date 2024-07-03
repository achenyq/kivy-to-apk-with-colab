
from kivy.clock import Clock
from tkinter import messagebox
from  kivy.app import App
import pyaudio
import wave

from kivy.uix.widget import Widget

from kivy.core.window import Window
import requests
Window.size = (360, 600)
class ImgeAPP_1(Widget):
    def __int__(self,**kwargs):
        super().__int__(**kwargs)
    # def show_popup2(self):
    #     answer = messagebox.askyesno("诊断结果为", "不健康")
    def show_popup(self):
        answer = messagebox.askyesno("提示", "是否诊断？")
        if answer:
            url = 'http://127.0.0.1:8000'
            file_path = 'output.wav'
            with open(file_path, 'rb') as f:
                files = {'file': (file_path, f)}
                response = requests.post(url, files=files)
                p=eval(response.text)
                print(p)
                print(type(p))
                if p['b']>=50:
                    print('不健康')
                    messagebox.askyesno("诊断结果为", "健康")
                else:
                    print('健康')
                    messagebox.askyesno("诊断结果为", "健康")

    def index_3(self,instance):
        if instance.text == 'Start recording':
            print(1)
            instance.text = 'Stop recording'
        elif instance.text == 'Stop recording':
            print(2)
            instance.text = 'Start recording'
        # now = datetime.now()
        # # 提取分钟和秒数
        # minutes = now.minute
        # seconds = now.second
        # print(1)
        # print("当前时间：{}分{}秒".format(minutes, seconds))
        print(instance.text)
    def index_1(self, instance):
        Clock.schedule_interval(self.index_2, 0.1)
    def index_2(self,instance):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 0.1
        self.p = pyaudio.PyAudio()
        self.device_index = 1
        try:
            self.frames= self.frames
        except :
            self.frames= []

        # 打开录音流
        self.stream = self.p.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True, frames_per_buffer=self.CHUNK ,input_device_index=self.device_index)
        # print("开始录音...")
        # 录音过程
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            # print(data)
            self.frames.append(data)
        # print("录音结束.")
    def  bc(self):
        wf = wave.open("output.wav", 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print("录音已保存到文件：", "output.wav")
        Clock.unschedule(self.index_2)
        self.frames= []
        self.show_popup()

class ImgeAPP(App):
    def build(self):

        return ImgeAPP_1()


if __name__=="__main__":
    ImgeAPP().run()