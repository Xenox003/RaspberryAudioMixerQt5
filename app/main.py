import sys

from modules.ui.mainwindow import MainWindow

def main():
    window = MainWindow()
    

    sys.exit(window.app.exec())

if __name__ == "__main__":
    main()