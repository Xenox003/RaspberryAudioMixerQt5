import sys

from modules.ui.mainwindow import UiMain

def main():
    window = UiMain()
    

    sys.exit(window.app.exec())

if __name__ == "__main__":
    main()