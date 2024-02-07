import tkinter as tk
from functions import preds
from web_auto import _init_, capture_full_page_screenshot
import os, io
from PIL import Image
import time
import winsound
import threading

global img2
path = os.path.join('Casino-live', 'data', 'bell.png')
# img2 = Image.open(path)
# img2.resize((0.00005,0.00005))

def update(output, preds, counter):
    # output_list.append(f'update: {output}, {preds}, {counter}')
    # print(f'update: {output}, {preds}, {counter}')
    # print(output_list)
    coords_text = ''
    ringer(counter, 1)
    coords_text, coords_text2 = checker(preds, output, 1, coords_text)
    sentence1 = f'{counter[1]}, p:{coords_text2}, o:{coords_text}'
    counter1_string.set(sentence1)
    coords_text = ''
    
    ringer(counter, 2)
    coords_text, coords_text2 = checker(preds, output, 2, coords_text)
    sentence2 = f'{counter[2]}, p:{coords_text2}, o:{coords_text}'
    counter2_string.set(sentence2)
    coords_text = ''
    
    ringer(counter, 3)
    coords_text, coords_text2 = checker(preds, output, 3, coords_text)
    sentence3 = f'{counter[3]}, p:{coords_text2}, o:{coords_text}'
    counter3_string.set(sentence3)
    coords_text = ''
    
    ringer(counter, 4)
    coords_text, coords_text2 = checker(preds, output, 4, coords_text)
    sentence4 = f'{counter[4]}, p:{coords_text2}, o:{coords_text}'
    counter4_string.set(sentence4)
    coords_text = ''
    
    ringer(counter, 5)
    coords_text, coords_text2 = checker(preds, output, 5, coords_text)
    sentence5 = f'{counter[5]}, p:{coords_text2}, o:{coords_text}'
    counter5_string.set(sentence5)
    coords_text = ''
    
    ringer(counter, 6)
    coords_text, coords_text2 = checker(preds, output, 6, coords_text)
    sentence6 = f'{counter[6]}, p:{coords_text2}, o:{coords_text}'
    counter6_string.set(sentence6)
    coords_text = ''
   
    ringer(counter, 7)
    coords_text, coords_text2 = checker(preds, output, 7, coords_text)
    sentence7 = f'{counter[7]}, p:{coords_text2}, o:{coords_text}'
    counter7_string.set(sentence7)
    coords_text = ''
    
    ringer(counter, 8)
    coords_text, coords_text2 = checker(preds, output, 8, coords_text)
    sentence8 = f'{counter[8]}, p:{coords_text2}, o:{coords_text}'
    counter8_string.set(sentence8)
    coords_text = ''
    
    window.update()

def ringer(counter, number):
    if number == 1:
        try:
            count1 = (counter1_string.get()).split(",", 1)
            if (int(count1[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)):
                bell1.configure(image=img2)
                window.update()
                winsound.Beep(440, 1000)
                # time.sleep(3)
                bell1.configure(image='')
                window.update()
        except:
            pass
    if number == 2:
        try:
            count2 = (counter2_string.get()).split(",", 1)
            if (int(count2[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                bell2.configure(image=img2)
                window.update()
                winsound.Beep(440, 1000)
                # time.sleep(3)
                bell2.configure(image='')
                window.update()
        except:
            pass
    if number == 3:
        try:
            count3 = (counter3_string.get()).split(",", 1)
            if (int(count3[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                bell3.configure(image=img2)
                window.update()
                winsound.Beep(440, 1000)
                # time.sleep(3)
                bell3.configure(image='')
                window.update()
        except:
            pass
    if number == 4:
        try:
            count4 = (counter4_string.get()).split(",", 1)
            if (int(count4[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                bell4.configure(image=img2)
                window.update()
                winsound.Beep(440, 1000)
                # time.sleep(3)
                bell4.configure(image='')
                window.update()
        except:
            pass
    if number == 5:
        try:
            count5 = (counter5_string.get()).split(",", 1)
            if (int(count5[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                bell5.configure(image=img2)
                window.update()
                winsound.Beep(440, 1000)
                # time.sleep(3)
                bell5.configure(image='')
                window.update()
        except:
            pass
    if number == 6:
        try:
            count6 = (counter6_string.get()).split(",", 1)
            if (int(count6[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                bell6.configure(image=img2)
                window.update()
                winsound.Beep(440, 1000)
                # time.sleep(3)
                bell6.configure(image='')
                window.update()
        except:
            pass
    if number == 7:
        try:
            count7 = (counter7_string.get()).split(",", 1)
            if (int(count7[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                bell7.configure(image=img2)
                window.update()
                winsound.Beep(440, 1000)
                # time.sleep(3)
                bell7.configure(image='')
                window.update()
        except:
            pass
    if number == 8:
        try:
            count8 = (counter8_string.get()).split(",", 1)
            if (int(count8[0]) != counter[number]) & ((counter[number] > 0) | (counter[number] < 0)): 
                bell8.configure(image=img2)
                window.update()
                winsound.Beep(440, 1000)
                # time.sleep(3)
                bell8.configure(image='')
                window.update()
        except:
            pass

def checker(preds, output, number, coords_text):
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
                    coords_text = counter1_string.get()
                elif number == 2:
                    coords_text = counter2_string.get()
                elif number == 3:
                    coords_text = counter3_string.get()
                elif number == 4:
                    coords_text = counter4_string.get()
                elif number == 5:
                    coords_text = counter5_string.get()
                elif number == 6:
                    coords_text = counter6_string.get()
                elif number == 7:
                    coords_text = counter7_string.get()
                elif number == 8:
                    coords_text = counter8_string.get()
                if 'Blue' in coords_text[12:]:
                    coords_text = 'Blue'
                elif 'Draw' in coords_text[12:]:
                    coords_text = 'Draw'
                elif 'Red' in coords_text[12:]:
                    coords_text = 'Red'
                else:
                    coords_text = coords_text[12:]
        return coords_text, coords_text2
    else:
        coords_text = ""
        coords_text2 = ""
        return coords_text, coords_text2

def screenshot():
    img_url = capture_full_page_screenshot(driver)
    img = Image.open(io.BytesIO(img_url))
    img.save(image_path)

def run(coords, t_preds, t_counter):
    # repeater = 0
    while window:
        screenshot()
        # time.sleep(1)
        coords, t_preds, t_counter = preds(image_path, coords, t_preds, t_counter)
        # time.sleep(5)
        # if repeater < 1:
        update(coords, t_preds, t_counter)
        #     repeater += 1
        # else:
        #     repeater = 0
    # time.sleep(2)
    # window.after(1000, run(coords, t_preds, t_counter))

window = tk.Tk()
window.title('Counter')

# Screen width and height
# ws = window.winfo_screenwidth()
# hs = window.winfo_screenheight()
img2 = tk.PhotoImage(file=path)
img2 = img2.subsample(15, 15)

window.geometry('%dx%d+%d+%d' % (400, 600, 0, 0))
# window.geometry('600x600')

window.wm_attributes('-topmost', True)

# UI
# counter1_int, counter2_int, counter3_int, counter4_int, counter5_int, counter6_int, counter7_int, counter8_int = tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()
counter1_string, counter2_string, counter3_string, counter4_string, counter5_string, counter6_string, counter7_string, counter8_string = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()

label1 = tk.Label(window, text = 'DG01: ')
label2 = tk.Label(window, text = 'DG02: ')
label3 = tk.Label(window, text = 'DG03: ')
label4 = tk.Label(window, text = 'DG05: ')
label5 = tk.Label(window, text = 'DG06: ')
label6 = tk.Label(window, text = 'DG07: ')
label7 = tk.Label(window, text = 'DG08: ')
label8 = tk.Label(window, text = 'DG09: ')

bell1 = tk.Label(window, image="")
bell2 = tk.Label(window, image="")
bell3 = tk.Label(window, image="")
bell4 = tk.Label(window, image="")
bell5 = tk.Label(window, image="")
bell6 = tk.Label(window, image="")
bell7 = tk.Label(window, image="")
bell8 = tk.Label(window, image="")

counter1 = tk.Label(window, textvariable=counter1_string)
counter2 = tk.Label(window, textvariable=counter2_string)
counter3 = tk.Label(window, textvariable=counter3_string)
counter4 = tk.Label(window, textvariable=counter4_string)
counter5 = tk.Label(window, textvariable=counter5_string)
counter6 = tk.Label(window, textvariable=counter6_string)
counter7 = tk.Label(window, textvariable=counter7_string)
counter8 = tk.Label(window, textvariable=counter8_string)

# grid
window.columnconfigure(0, weight=1, uniform='a')
window.columnconfigure(1, weight=1, uniform='a')
window.columnconfigure(2, weight=4, uniform='a')
window.columnconfigure(3, weight=1, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=1, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=1, uniform='a')
window.rowconfigure(4, weight=1, uniform='a')
window.rowconfigure(5, weight=1, uniform='a')
window.rowconfigure(6, weight=1, uniform='a')
window.rowconfigure(7, weight=1, uniform='a')
# window.rowconfigure(8, weight=1, uniform='a')
# window.rowconfigure(9, weight=1, uniform='a')

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

# Selenium webdriver initiation
driver = _init_()

# Variable Definition
image_path = os.path.join('Casino-live', 'data', 'casino.png')
global output_list
global coords, t_preds, t_counter
output_list = []
coords, t_preds, t_counter = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}, {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

# Run function initiation
run(coords, t_preds, t_counter)