"""
nama kelompok:
1. Kurnia Kharisma Agung Samiadjie | 2110511068
2. Rana Ekakurnia Fathin           | 2110511059
3. Wahyu Dhia Satwika              | 2110511066
"""

import curses
from curses import KEY_BACKSPACE, wrapper
import time
import random
# curses = library yang digunakan untuk membuat terminal independent dan melakukan styling pada terminal tersebut

# print diganti jadi .addstr()
# input diganti jadi .getkey()

def logo(stdscr):
    stdscr.addstr(0,0," $$$$$$\                                      $$\       $$$$$$$$\                  $$\                             $$\                           $$\     ")
    stdscr.addstr(1,0,"$$  __$$\                                     $$ |      \__$$  __|                 \__|                            $$ |                          $$ |    ")
    stdscr.addstr(2,0,"$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$ |         $$ |$$\   $$\  $$$$$$\  $$\ $$$$$$$\   $$$$$$\        $$$$$$\    $$$$$$\   $$$$$$$\ $$$$$$\   ")
    stdscr.addstr(3,0,"\$$$$$$\  $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$ |         $$ |$$ |  $$ |$$  __$$\ $$ |$$  __$$\ $$  __$$\       \_$$  _|  $$  __$$\ $$  _____|\_$$  _|  ")
    stdscr.addstr(4,0," \____$$\ $$ /  $$ |$$$$$$$$ |$$$$$$$$ |$$ /  $$ |         $$ |$$ |  $$ |$$ /  $$ |$$ |$$ |  $$ |$$ /  $$ |        $$ |    $$$$$$$$ |\$$$$$$\    $$ |    ")
    stdscr.addstr(5,0,"$$\   $$ |$$ |  $$ |$$   ____|$$   ____|$$ |  $$ |         $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |        $$ |$$\ $$   ____| \____$$\   $$ |$$\ ")
    stdscr.addstr(6,0,"\$$$$$$  |$$$$$$$  |\$$$$$$$\ \$$$$$$$\ \$$$$$$$ |         $$ |\$$$$$$$ |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |        \$$$$  |\$$$$$$$\ $$$$$$$  |  \$$$$  |")
    stdscr.addstr(7,0," \______/ $$  ____/  \_______| \_______| \_______|         \__| \____$$ |$$  ____/ \__|\__|  \__| \____$$ |         \____/  \_______|\_______/    \____/ ")
    stdscr.addstr(8,0,"          $$ |                                                 $$\   $$ |$$ |                    $$\   $$ |                                              ")
    stdscr.addstr(9,0,"          $$ |                                                 \$$$$$$  |$$ |                    \$$$$$$  |                                              ")
    stdscr.addstr(10,0,"          \__|                                                  \______/ \__|                     \______/                                               ")

def logoClose(stdscr): 
    stdscr.addstr(0,0," /$$$$$$$                                                                       /$$$$$$            /$$                               /$$ /$$")
    stdscr.addstr(1,0,"| $$__  $$                                                                     /$$__  $$          | $$                              |__/| $$")
    stdscr.addstr(2,0,"| $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$/$$$$       | $$  \__/  /$$$$$$ | $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$| $$")
    stdscr.addstr(3,0,"| $$$$$$$//$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$| $$_  $$_  $$      |  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$_____/ |____  $$| $$| $$")
    stdscr.addstr(4,0,"| $$____/| $$  \__/| $$  \ $$| $$  \ $$| $$  \__/ /$$$$$$$| $$ \ $$ \ $$       \____  $$| $$$$$$$$| $$| $$$$$$$$|  $$$$$$   /$$$$$$$| $$|__/")
    stdscr.addstr(5,0,"| $$     | $$      | $$  | $$| $$  | $$| $$      /$$__  $$| $$ | $$ | $$       /$$  \ $$| $$_____/| $$| $$_____/ \____  $$ /$$__  $$| $$    ")
    stdscr.addstr(6,0,"| $$     | $$      |  $$$$$$/|  $$$$$$$| $$     |  $$$$$$$| $$ | $$ | $$      |  $$$$$$/|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$ /$$")
    stdscr.addstr(7,0,"|__/     |__/       \______/  \____  $$|__/      \_______/|__/ |__/ |__/       \______/  \_______/|__/ \_______/|_______/  \_______/|__/|__/")
    stdscr.addstr(8,0,"                              /$$  \ $$                                                                                                     ")
    stdscr.addstr(9,0,"                             |  $$$$$$/                                                                                                     ")
    stdscr.addstr(10,0,"                              \______/                                                                                                      ")

def selesai(stdscr):
    stdscr.addstr(0,0," /$$$$$$$$                  /$$                               /$$   /$$                     /$$ /$$      ")
    stdscr.addstr(1,0,"|__  $$__/                 |__/                              | $$  /$$/                    |__/| $$      ")
    stdscr.addstr(2,0,"   | $$  /$$$$$$   /$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$       | $$ /$$/   /$$$$$$   /$$$$$$$ /$$| $$$$$$$ ")
    stdscr.addstr(3,0,"   | $$ /$$__  $$ /$$__  $$| $$| $$_  $$_  $$ |____  $$      | $$$$$/   |____  $$ /$$_____/| $$| $$__  $$")
    stdscr.addstr(4,0,"   | $$| $$$$$$$$| $$  \__/| $$| $$ \ $$ \ $$  /$$$$$$$      | $$  $$    /$$$$$$$|  $$$$$$ | $$| $$  \ $$")
    stdscr.addstr(5,0,"   | $$| $$_____/| $$      | $$| $$ | $$ | $$ /$$__  $$      | $$\  $$  /$$__  $$ \____  $$| $$| $$  | $$")
    stdscr.addstr(6,0,"   | $$|  $$$$$$$| $$      | $$| $$ | $$ | $$|  $$$$$$$      | $$ \  $$|  $$$$$$$ /$$$$$$$/| $$| $$  | $$")
    stdscr.addstr(7,0,"   |__/ \_______/|__/      |__/|__/ |__/ |__/ \_______/      |__/  \__/ \_______/|_______/ |__/|__/  |__/")

def start_screen(stdscr):
    stdscr.clear()
    stdscr.refresh()
    logo(stdscr)
    stdscr.addstr(15,67,"Tekan tombol apa saja untuk mulai!")
    stdscr.refresh()
    stdscr.getkey()

def close_screen(stdscr):
    stdscr.clear()
    stdscr.refresh()
    logoClose(stdscr)
    stdscr.refresh()
    time.sleep(5)
    stdscr.addstr(15, 45,"Tekan tombol apa saja untuk lanjut, tekan 'Q' untuk keluar...")

def display_text(stdscr, target, current,time,cps=0):
    stdscr.addstr(target)

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

    stdscr.addstr(2, 0, f"CPS : {cps}")
    stdscr.addstr(2, 15, f"Time : {round(60-time)}")

def load_text():
    with open("D:\VS CODE\KULIAH\PYTHON\Project\line.txt", "r") as t:
        baris = t.readlines()
        return random.choice(baris).strip()

def wpmchecker(temp_answer, temp_text):
    answer = temp_answer.split()
    text = temp_text.split()
    wpm = 0

    for i in range(len(answer)):
        if answer[i] == text[i]:
            wpm+=1
    return wpm

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    answer = ""
    text = ""
    stdscr.nodelay(True)
    time_start = time.time()
    total_char = 0

    # looping digunakan untuk meminta user memasukan input terus menerus sesuai target text
    while True:
        time_elapsed = max(time.time() - time_start, 1)
        cps = round(total_char/time_elapsed)

        if len(current_text) == len(target_text):
            # Ini digunakan untuk menyimpan seluruh jawaban dan teks lalu check per word antara total answer dan text
            answer += ''.join(current_text)
            answer += " "
            current_text = []
            text += ''.join(target_text)
            text += ' '
            target_text = load_text()
            continue

        if time_elapsed > 60:
            stdscr.nodelay(False)
            break

        stdscr.clear()
        display_text(stdscr, target_text, current_text, time_elapsed, cps)
        stdscr.refresh()

        try :
            key = stdscr.getkey()
        except :
            continue

        if ord(key) == 27: # esc key
            break

        if ord(key) == 10: # enter key
            continue

        if key in [KEY_BACKSPACE, "\b", "\x7f"]:
            try :
                current_text.pop()
            except:
                continue
        elif len(current_text) < len(target_text):
            current_text.append(key)
            total_char += 1

        stdscr.refresh()

    stdscr.addstr(4, 15, f"CPM : {round(total_char)}")

    return wpmchecker(answer, text)

def main(stdscr):
    # template init pair (id,foreground color(warna text), background color)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    while True:
        start_screen(stdscr)
        wpm = wpm_test(stdscr)
        stdscr.addstr(4, 0, f"WPM : {wpm}")
        close_screen(stdscr)

        key = stdscr.getkey()
        key.lower()

        if ord(key) == 113:
            stdscr.clear()
            stdscr.refresh()
            selesai(stdscr)
            stdscr.refresh()
            time.sleep(5)
            break

        else : 
            continue

wrapper(main)