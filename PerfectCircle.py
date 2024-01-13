import math
import pyautogui
import time

# F11 To fullscreen your browser!

r = 380 # Radius of your circle
circle_steps = 100 # Corners? of your circle I guess?, lower = faster (2 linear 3 = triangle, 4 = square)
width, height = pyautogui.size() # Screen size X , Y
y_offset = (1 / 27) * height # Offset of the center white dot
center_x, center_y = width / 2, (height - y_offset) / 2 # Center point

def circle(radius, steps):
    pyautogui.mouseDown()
    for i in range(steps + 2): # +2 to fully finish the circle
        angle = i * (2.0 * math.pi / steps)
        dx = int(center_x + radius * math.cos(angle))
        dy = int(center_y + radius * math.sin(angle))
        pyautogui.moveTo(dx, dy)
        time.sleep(0.01)
    pyautogui.mouseUp()

time.sleep(5)
pyautogui.moveTo((center_x+ r), center_y) # Move mouse to Beginning of circle
circle(r, circle_steps)
