import pygetwindow as gw

def print_window_titles():
    windows = gw.getAllTitles()
    for title in windows:
        print(title)

print_window_titles()
