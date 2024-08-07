import time
import pyautogui
import pytespiyseract
import pygetwindow as gw
import cv2

def select_and_operate_on_window(window_title, text_to_find):
    # 查找并激活窗口
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f'未找到标题包含 "{window_title}" 的窗口')
        return

    window = windows[0]
    window.activate()
    time.sleep(1)  # 等待窗口激活

    # 截图窗口区域
    screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
    screenshot_cv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 使用 OCR 识别窗口中的文本
    text = pytesseract.image_to_string(screenshot_cv)

    if text_to_find in text:
        # 识别文本的位置
        boxes = pytesseract.image_to_boxes(screenshot_cv)
        for b in boxes.splitlines():
            b = b.split(' ')
            if b[0] == text_to_find:
                x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

                # 计算点击的位置（相对于窗口的左上角）
                click_x = window.left + x + (w - x) // 2
                click_y = window.top + window.height - y - (y - h) // 2  # 调整y坐标

                # 点击识别到的文本区域
                pyautogui.click(click_x, click_y)
                print(f'点击了 "{text_to_find}" 文本区域')
                break
    else:
        print(f'未找到文本 "{text_to_find}"')

# 选择窗口并操作
select_and_operate_on_window('Your Window Title', 'YourTextHere')
