import sys

from modules.ui.ui_main import MainWindow

def main():
    window = MainWindow()
    

    sys.exit(window.app.exec())

if __name__ == "__main__":
    main()