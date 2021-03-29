import time, random, utime
import picoexplorer as explorer

width = explorer.get_width()
height = explorer.get_height()

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
explorer.init(display_buffer)

explorer.set_audio_pin(0)

i = 1

while True:
    explorer.set_pen(0, 0, 32)    
    explorer.clear()

    explorer.set_pen(255, 255, 255)

    explorer.text("Welcome to", 20, 20, 200)
    
    if i == 0:
        explorer.set_pen(128, 255, 0)
        explorer.text("@therke.com", 20, 40, 300)
        i = 1
    elif i == 1:
        explorer.set_pen(255, 128, 0)
        explorer.text("The Random Knowledge Enthusiast", 20, 40, 300)
        i = 0
    
    explorer.set_pen(0, 128, 200)
    explorer.text("Please follow me for cool projects like this one.", 20, 80, 220)

    if i == 0:
        explorer.set_pen(128, 255, 0)
        explorer.text("Discover new ideas, and information with my TikTok Channel. Please like follow for more content!", 20, 130, 220)
    elif i == 1:
        explorer.set_pen(255, 128, 0)
        explorer.text("Enjoy comedy videos, sketches and Satire. Please like follow for more content!", 20, 130, 220)


    explorer.update()
    time.sleep(3)