import tkinter as tk
from functions import preds
from web_auto import _init_, capture_full_page_screenshot
import os, io
from PIL import Image
import time
import winsound
from threading import Thread
from enum import Enum, auto
from queue import Queue
from typing import Union

class TicketPurpose(Enum):
    Update_Text = auto()
    Update_Image = auto()

class Ticket:
    '''
    Class to create tickets to store tkinter label and images (obtained from subthreads) to be input into a queue (to update the tkinter window in main thread)
    '''
    def __init__(self,
                 ticket_type: TicketPurpose,
                 ticket_value: Union[str, tk.PhotoImage],
                 table: int):
        self.ticket_type = ticket_type
        self.ticket_value = ticket_value
        self.table = table

class MainWindow(tk.Tk):
    '''
    Class to create the tkinter application and selenium webdriver
    '''
    def __init__(self):
        super().__init__()
        self.driver = _init_()

        self.geometry('%dx%d+%d+%d' % (400, 600, 0, 0))
        self.wm_attributes('-topmost', True)
        self.queue_message = Queue()

        window = tk.Tk()
        window.title('Counter')
        self.window = window

        self.create_frame()
        self.bind("<<WidgetLoad>>", self.check_queue)

        path = os.path.join('Casino-live', 'data', 'bell.png')
        img2 = tk.PhotoImage(file=path)
        img2 = img2.subsample(15, 15)
        self.img2 = img2

        # Run function initiation
        self.run(coords, t_preds, t_counter)
    
    def check_queue(self, event):
        '''
        Read the queue and update the tkinter window
        '''
        msg: Ticket
        msg = self.queue_message.get()

        print(f'queue reached {msg.ticket_value}')

        if msg.ticket_type == TicketPurpose.Update_Text:
            if msg.table == 1:
                self.counter1_string.set(msg.ticket_value)
            elif msg.table == 2:
                self.counter2_string.set(msg.ticket_value)
            elif msg.table == 3:
                self.counter3_string.set(msg.ticket_value)
            elif msg.table == 4:
                self.counter4_string.set(msg.ticket_value)
            elif msg.table == 5:
                self.counter5_string.set(msg.ticket_value)
            elif msg.table == 6:
                self.counter6_string.set(msg.ticket_value)
            elif msg.table == 7:
                self.counter7_string.set(msg.ticket_value)
            elif msg.table == 8:
                self.counter8_string.set(msg.ticket_value)
            self.window.update()
        elif msg.ticket_type == TicketPurpose.Update_Image:
            if msg.table == 1:
                self.bell1.configure(image=self.img2)
                self.window.update()
                time.sleep(3)
                self.bell1.configure(image='')
            elif msg.table == 2:
                self.bell2.configure(image=self.img2)
                self.window.update()
                time.sleep(3)
                self.bell2.configure(image='')
            elif msg.table == 3:
                self.bell3.configure(image=self.img2)
                self.window.update()
                time.sleep(3)
                self.bell3.configure(image='')
            elif msg.table == 4:
                self.bell4.configure(image=self.img2)
                self.window.update()
                time.sleep(3)
                self.bell4.configure(image='')
            elif msg.table == 5:
                self.bell5.configure(image=self.img2)
                self.window.update()
                time.sleep(3)
                self.bell5.configure(image='')
            elif msg.table == 6:
                self.bell6.configure(image=self.img2)
                self.window.update()
                time.sleep(3)
                self.bell6.configure(image='')
            elif msg.table == 7:
                self.bell7.configure(image=self.img2)
                self.window.update()
                time.sleep(3)
                self.bell7.configure(image='')
            elif msg.table == 8:
                self.bell8.configure(image=self.img2)
                self.window.update()
                time.sleep(3)
                self.bell8.configure(image='')
            self.window.update()

    def create_frame(self) -> tk.Frame:
        '''
        Create and return a tkinter frame that contains the content
        '''
        counter1_string, counter2_string, counter3_string, counter4_string, counter5_string, counter6_string, counter7_string, counter8_string = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
        self.counter1_string = counter1_string
        self.counter2_string = counter2_string
        self.counter3_string = counter3_string
        self.counter4_string = counter4_string
        self.counter5_string = counter5_string
        self.counter6_string = counter6_string
        self.counter7_string = counter7_string
        self.counter8_string = counter8_string

        label1 = tk.Label(self, text = 'DG01: ')
        label2 = tk.Label(self, text = 'DG02: ')
        label3 = tk.Label(self, text = 'DG03: ')
        label4 = tk.Label(self, text = 'DG05: ')
        label5 = tk.Label(self, text = 'DG06: ')
        label6 = tk.Label(self, text = 'DG07: ')
        label7 = tk.Label(self, text = 'DG08: ')
        label8 = tk.Label(self, text = 'DG09: ')

        bell1 = tk.Label(self, image="")
        bell2 = tk.Label(self, image="")
        bell3 = tk.Label(self, image="")
        bell4 = tk.Label(self, image="")
        bell5 = tk.Label(self, image="")
        bell6 = tk.Label(self, image="")
        bell7 = tk.Label(self, image="")
        bell8 = tk.Label(self, image="")

        counter1 = tk.Label(self, textvariable=counter1_string)
        counter2 = tk.Label(self, textvariable=counter2_string)
        counter3 = tk.Label(self, textvariable=counter3_string)
        counter4 = tk.Label(self, textvariable=counter4_string)
        counter5 = tk.Label(self, textvariable=counter5_string)
        counter6 = tk.Label(self, textvariable=counter6_string)
        counter7 = tk.Label(self, textvariable=counter7_string)
        counter8 = tk.Label(self, textvariable=counter8_string)

        # grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=4, uniform='a')
        self.columnconfigure(3, weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure(2, weight=1, uniform='a')
        self.rowconfigure(3, weight=1, uniform='a')
        self.rowconfigure(4, weight=1, uniform='a')
        self.rowconfigure(5, weight=1, uniform='a')
        self.rowconfigure(6, weight=1, uniform='a')
        self.rowconfigure(7, weight=1, uniform='a')

        label1.grid(row=0, column=1)
        label2.grid(row=1, column=1)
        label3.grid(row=2, column=1)
        label4.grid(row=3, column=1)
        label5.grid(row=4, column=1)
        label6.grid(row=5, column=1)
        label7.grid(row=6, column=1)
        label8.grid(row=7, column=1)
        counter1.grid(row=0, column=2)
        counter2.grid(row=1, column=2)
        counter3.grid(row=2, column=2)
        counter4.grid(row=3, column=2)
        counter5.grid(row=4, column=2)
        counter6.grid(row=5, column=2)
        counter7.grid(row=6, column=2)
        counter8.grid(row=7, column=2)

        bell1.grid(row=0, column=0, sticky='E')
        bell2.grid(row=1, column=0, sticky='E')
        bell3.grid(row=2, column=0, sticky='E')
        bell4.grid(row=3, column=0, sticky='E')
        bell5.grid(row=4, column=0, sticky='E')
        bell6.grid(row=5, column=0, sticky='E')
        bell7.grid(row=6, column=0, sticky='E')
        bell8.grid(row=7, column=0, sticky='E')

    def text_subthread(self, output, preds, counter):
        '''
        Function to create a subthread to run a function (text_updater) to store the tkinter label information
        '''
        text_thread = Thread(target=self.text_updater,
                            args=(output, preds, counter),
                            daemon=True)
        print('text thread')
        text_thread.start()

    def image_subthread(self, counter, num):
        '''
        Function to create a subthread to run a function (image_updater) to store the tkinter image information
        '''
        image_thread = Thread(target=self.image_updater,
                            args=(counter, num),
                            daemon=True)
        print('image thread')
        image_thread.start()
    
    def bell_subthread(self):
        '''
        Function to create a subthread to run a function (bell) to ring a bell notification sound
        '''
        bell_thread = Thread(target=self.bell,
                            args=(),
                            daemon=True)
        bell_thread.start()

    def text_updater(self, output, preds, counter):
        '''
        A function initiated from a subthread (text_subthread).

        This function initiates the following functions:
        - checker 
          (to check previous prediction, curent output and return strings to be displayed in tkinter window)
        - image_subthread
          (to initiate the function to check if threshold is reached, if so then display a bell image and ring a bell)

        This function creates a ticket (output from checker function) which is then put into the queue to be executed.
        '''
        for i in range(1, 9):
            coords_text = ''
            # self.image_updater(counter, i)
            self.image_subthread(counter, i)
            coords_text, coords_text2 = self.checker(preds, output, i, coords_text)
            if i == 1:
                sentence1 = f'{counter[1]}, p:{coords_text2}, o:{coords_text}'
                # self.counter1_string.set(sentence1)
                ticket = Ticket(ticket_type=TicketPurpose.Update_Text,
                                ticket_value=sentence1,
                                table=i)
                self.queue_message.put(ticket)
                self.event_generate("<<WidgetLoad>>")
            if i == 2:
                sentence2 = f'{counter[2]}, p:{coords_text2}, o:{coords_text}'
                # self.counter2_string.set(sentence2)
                ticket = Ticket(ticket_type=TicketPurpose.Update_Text,
                                ticket_value=sentence2,
                                table=i)
                self.queue_message.put(ticket)
                self.event_generate("<<WidgetLoad>>")
            if i == 3:
                sentence3 = f'{counter[3]}, p:{coords_text2}, o:{coords_text}'
                # self.counter3_string.set(sentence3)
                ticket = Ticket(ticket_type=TicketPurpose.Update_Text,
                                ticket_value=sentence3,
                                table=i)
                self.queue_message.put(ticket)
                self.event_generate("<<WidgetLoad>>")
            if i == 4:
                sentence4 = f'{counter[4]}, p:{coords_text2}, o:{coords_text}'
                # self.counter4_string.set(sentence4)
                ticket = Ticket(ticket_type=TicketPurpose.Update_Text,
                                ticket_value=sentence4,
                                table=i)
                self.queue_message.put(ticket)
                self.event_generate("<<WidgetLoad>>")
            if i == 5:
                sentence5 = f'{counter[5]}, p:{coords_text2}, o:{coords_text}'
                # self.counter5_string.set(sentence5)
                ticket = Ticket(ticket_type=TicketPurpose.Update_Text,
                                ticket_value=sentence5,
                                table=i)
                self.queue_message.put(ticket)
                self.event_generate("<<WidgetLoad>>")
            if i == 6:
                sentence6 = f'{counter[6]}, p:{coords_text2}, o:{coords_text}'
                # self.counter6_string.set(sentence6)
                ticket = Ticket(ticket_type=TicketPurpose.Update_Text,
                                ticket_value=sentence6,
                                table=i)
                self.queue_message.put(ticket)
                self.event_generate("<<WidgetLoad>>")
            if i == 7:
                sentence7 = f'{counter[7]}, p:{coords_text2}, o:{coords_text}'
                # self.counter7_string.set(sentence7)
                ticket = Ticket(ticket_type=TicketPurpose.Update_Text,
                                ticket_value=sentence7,
                                table=i)
                self.queue_message.put(ticket)
                self.event_generate("<<WidgetLoad>>")
            if i == 8:
                sentence8 = f'{counter[8]}, p:{coords_text2}, o:{coords_text}'
                # self.counter8_string.set(sentence8)
                ticket = Ticket(ticket_type=TicketPurpose.Update_Text,
                                ticket_value=sentence8,
                                table=i)
                self.queue_message.put(ticket)
                self.event_generate("<<WidgetLoad>>")
            print(i)
    
    def bell():
        winsound.Beep(440, 1000)

    def image_updater(self, counter, number):
        '''
        A function initiated from a subthread (image_subthread).

        This function checks whether the counter number is above/below threshold.
        If it is then the function creates a ticket which is then put into the queue to be executed.
        The function (bell_subthread) is also initiated (to ring a notification bell).
        '''
        if number == 1:
            try:
                count1 = (self.counter1_string.get()).split(",", 1)
                if (int(count1[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)):
                    ticket = Ticket(ticket_type=TicketPurpose.Update_Image,
                                    ticket_value=self.img2,
                                    table=number)
                    self.queue_message.put(ticket)
                    self.event_generate("<<WidgetLoad>>")
                    self.bell_subthread()
            except:
                pass
        if number == 2:
            try:
                count2 = (self.counter2_string.get()).split(",", 1)
                if (int(count2[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                    ticket = Ticket(ticket_type=TicketPurpose.Update_Image,
                                    ticket_value=self.img2,
                                    table=number)
                    self.queue_message.put(ticket)
                    self.event_generate("<<WidgetLoad>>")
                    self.bell_subthread()
            except:
                pass
        if number == 3:
            try:
                count3 = (self.counter3_string.get()).split(",", 1)
                if (int(count3[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                    ticket = Ticket(ticket_type=TicketPurpose.Update_Image,
                                    ticket_value=self.img2,
                                    table=number)
                    self.queue_message.put(ticket)
                    self.event_generate("<<WidgetLoad>>")
                    self.bell_subthread()
            except:
                pass
        if number == 4:
            try:
                count4 = (self.counter4_string.get()).split(",", 1)
                if (int(count4[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                    ticket = Ticket(ticket_type=TicketPurpose.Update_Image,
                                    ticket_value=self.img2,
                                    table=number)
                    self.queue_message.put(ticket)
                    self.event_generate("<<WidgetLoad>>")
                    self.bell_subthread()
            except:
                pass
        if number == 5:
            try:
                count5 = (self.counter5_string.get()).split(",", 1)
                if (int(count5[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                    ticket = Ticket(ticket_type=TicketPurpose.Update_Image,
                                    ticket_value=self.img2,
                                    table=number)
                    self.queue_message.put(ticket)
                    self.event_generate("<<WidgetLoad>>")
                    self.bell_subthread()
            except:
                pass
        if number == 6:
            try:
                count6 = (self.counter6_string.get()).split(",", 1)
                if (int(count6[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                    ticket = Ticket(ticket_type=TicketPurpose.Update_Image,
                                    ticket_value=self.img2,
                                    table=number)
                    self.queue_message.put(ticket)
                    self.event_generate("<<WidgetLoad>>")
                    self.bell_subthread()
            except:
                pass
        if number == 7:
            try:
                count7 = (self.counter7_string.get()).split(",", 1)
                if (int(count7[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                    ticket = Ticket(ticket_type=TicketPurpose.Update_Image,
                                    ticket_value=self.img2,
                                    table=number)
                    self.queue_message.put(ticket)
                    self.event_generate("<<WidgetLoad>>")
                    self.bell_subthread()
            except:
                pass
        if number == 8:
            try:
                count8 = (self.counter8_string.get()).split(",", 1)
                if (int(count8[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                    ticket = Ticket(ticket_type=TicketPurpose.Update_Image,
                                    ticket_value=self.img2,
                                    table=number)
                    self.queue_message.put(ticket)
                    self.event_generate("<<WidgetLoad>>")
                    self.bell_subthread()
            except:
                pass

    def checker(self, preds, output, number, coords_text):
        '''
        This function is initiated from the function (text_updater)

        It retrieves the previous prediction and curent output.
        It returns strings to be displayed in tkinter window.
        '''
        if (preds[number] is not None):
            coords_text2 = ''
            if preds[number] == 0:
                coords_text2 = 'Blue'
            elif preds[number] == 2:
                coords_text2 = 'Red'
            elif preds[number] == 5:
                coords_text2 = 'Error'
            if 5 in output[number]:
                if output[number][5] == 5:
                    coords_text = 'Error'
            if (coords_text != 'Error'):
                if 0 in output[number]:
                    coords_text = 'Blue'
                elif 1 in output[number]:
                    coords_text = 'Draw'
                elif 2 in output[number]:
                    coords_text = 'Red'
                else:
                    if number == 1:
                        coords_text = self.counter1_string.get()
                    elif number == 2:
                        coords_text = self.counter2_string.get()
                    elif number == 3:
                        coords_text = self.counter3_string.get()
                    elif number == 4:
                        coords_text = self.counter4_string.get()
                    elif number == 5:
                        coords_text = self.counter5_string.get()
                    elif number == 6:
                        coords_text = self.counter6_string.get()
                    elif number == 7:
                        coords_text = self.counter7_string.get()
                    elif number == 8:
                        coords_text = self.counter8_string.get()
                    if 'Blue' in coords_text[12:]:
                        coords_text = 'Blue'
                    elif 'Draw' in coords_text[12:]:
                        coords_text = 'Draw'
                    elif 'Red' in coords_text[12:]:
                        coords_text = 'Red'
                    else:
                        coords_text = coords_text[12:]
            print(f'1: {coords_text}, 2: {coords_text2}')
            return coords_text, coords_text2
        else:
            coords_text = ""
            coords_text2 = ""
            return coords_text, coords_text2

    def screenshot(self):
        '''
        Function initiated from the function (run)
        It screenshots the selenium webdriver browser.
        '''
        img_url = capture_full_page_screenshot(self.driver)
        img = Image.open(io.BytesIO(img_url))
        img.save(image_path)

    def run(self, coords, t_preds, t_counter):
        '''
        Function initiated from the class init function
        It loops through the functions; screenshot, preds and text_subthread.
        (To screenshot every second the live stream, create predictions from it and update tkinter window)
        '''
        # repeater = 0
        while self:
            self.screenshot()
            coords, t_preds, t_counter = preds(image_path, coords, t_preds, t_counter)
            # self.text_updater(coords, t_preds, t_counter)
            self.text_subthread(coords, t_preds, t_counter)
        
# Variable Definition
image_path = os.path.join('Casino-live', 'data', 'casino.png')
global output_list
global coords, t_preds, t_counter
output_list = []
coords, t_preds, t_counter = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}, {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

if __name__ == "__main__":
    main_window = MainWindow()
    # main_window.mainloop()
