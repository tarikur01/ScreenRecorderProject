import sys
from PyQt5.QtWidgets import QApplication
from app.ui import LoginWindow, MainWindow

def main():
    # Create the application
    app = QApplication(sys.argv)

    # Show the login window
    login_window = LoginWindow()
    if login_window.exec_() == LoginWindow.Accepted:
        print("Login successful! Starting the application...")
        
        # Show the main window
        main_window = MainWindow()
        main_window.show()
    else:
        print("Login failed. Exiting the application...")

    # Execute the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()