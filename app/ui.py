from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, 
    QComboBox, QWidget, QMainWindow, QStackedWidget, QProgressBar, QHBoxLayout
)
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
import pyautogui
import cv2
import numpy as np

# ডার্ক থিম সেটআপ
def set_dark_theme(app):
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("""
            QDialog {
                background-color: #2E3440;
            }
            QLabel {
                color: #ECEFF4;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #4C566A;
                color: #ECEFF4;
                border: 1px solid #81A1C1;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #81A1C1;
                color: #2E3440;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #5E81AC;
            }
        """)

        layout = QVBoxLayout()

        self.username_label = QLabel('Username:', self)
        self.username_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.username_label)

        self.username_input = QLineEdit(self)
        self.username_input.setFont(QFont("Arial", 12))
        layout.addWidget(self.username_input)

        self.password_label = QLabel('Password:', self)
        self.password_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.password_label)

        self.password_input = QLineEdit(self)
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton('Login', self)
        self.login_button.setFont(QFont("Arial", 12))
        self.login_button.clicked.connect(self.check_credentials)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "password":
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ScreenRecorderProject')
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E3440;
            }
            QLabel {
                color: #ECEFF4;
                font-size: 16px;
            }
            QPushButton {
                background-color: #81A1C1;
                color: #2E3440;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #5E81AC;
            }
            QComboBox {
                background-color: #4C566A;
                color: #ECEFF4;
                border: 1px solid #81A1C1;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_menu = MainMenu(self)
        self.trading_interface = TradingInterface(self)

        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.trading_interface)

        self.stacked_widget.setCurrentWidget(self.main_menu)

class MainMenu(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        heading = QLabel('Main Menu', self)
        heading.setAlignment(Qt.AlignCenter)
        heading.setFont(QFont("Arial", 20, QFont.Bold))
        layout.addWidget(heading)

        self.platform_combo = QComboBox(self)
        self.platform_combo.addItems(["Binary Options", "Forex", "Cryptocurrency", "Stock Market", "Others"])
        self.platform_combo.setFont(QFont("Arial", 14))
        self.platform_combo.currentTextChanged.connect(self.select_platform)
        layout.addWidget(self.platform_combo)

        self.broker_combo = QComboBox(self)
        self.broker_combo.addItems(["Select a platform first"])
        self.broker_combo.setFont(QFont("Arial", 14))
        layout.addWidget(self.broker_combo)

        self.record_button = QPushButton('Start Screen Recording', self)
        self.record_button.setFont(QFont("Arial", 14))
        self.record_button.clicked.connect(self.start_screen_recording)
        layout.addWidget(self.record_button)

        self.trading_button = QPushButton('Go to Trading Interface', self)
        self.trading_button.setFont(QFont("Arial", 14))
        self.trading_button.clicked.connect(self.go_to_trading_interface)
        layout.addWidget(self.trading_button)

        self.setLayout(layout)

    def select_platform(self, platform):
        self.selected_platform = platform
        self.broker_combo.clear()

        if platform == "Binary Options":
            self.broker_combo.addItems([
                "IQ Option", "ExpertOption", "Deriv", "Binomo", "Olymp Trade", 
                "QX Broker", "Binary.com", "Pocket Option", "RaceOption", "BinaryCent", "Others"
            ])
        elif platform == "Forex":
            self.broker_combo.addItems([
                "Exness", "IC Markets", "XM", "FXTM", "Pepperstone", 
                "Forex.com", "AvaTrade", "HotForex", "FBS", "OctaFX", "Others"
            ])
        elif platform == "Cryptocurrency":
            self.broker_combo.addItems([
                "Binance", "Coinbase", "Kraken", "KuCoin", "Bitfinex", 
                "Huobi", "Gemini", "Bitstamp", "Bybit", "OKEx", "Others"
            ])
        elif platform == "Stock Market":
            self.broker_combo.addItems([
                "Alpha Vantage", "Interactive Brokers", "Robinhood", "E*TRADE", 
                "TD Ameritrade", "Fidelity", "Charles Schwab", "Webull", "TradeStation", "Saxo Bank", "Others"
            ])
        elif platform == "Others":
            self.broker_combo.addItems([
                "Others"
            ])

    def start_screen_recording(self):
        QMessageBox.information(self, "Screen Recording", "Screen recording started!")
        
        screen_size = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, screen_size)

        self.recording = True

        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)

            if cv2.waitKey(1) == ord('q'):
                break

        out.release()
        cv2.destroyAllWindows()
        QMessageBox.information(self, "Screen Recording", "Screen recording stopped!")

    def go_to_trading_interface(self):
        self.main_window.stacked_widget.setCurrentWidget(self.main_window.trading_interface)

class TradingInterface(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        heading = QLabel('Trading Interface', self)
        heading.setAlignment(Qt.AlignCenter)
        heading.setFont(QFont("Arial", 20, QFont.Bold))
        layout.addWidget(heading)

        self.buy_button = QPushButton('Buy', self)
        self.buy_button.clicked.connect(self.buy_trade)
        layout.addWidget(self.buy_button)

        self.sell_button = QPushButton('Sell', self)
        self.sell_button.clicked.connect(self.sell_trade)
        layout.addWidget(self.sell_button)

        self.buy_light = QLabel(self)
        self.buy_light.setFixedSize(20, 20)
        self.buy_light.setStyleSheet("background-color: gray; border-radius: 10px;")
        layout.addWidget(self.buy_light)

        self.sell_light = QLabel(self)
        self.sell_light.setFixedSize(20, 20)
        self.sell_light.setStyleSheet("background-color: gray; border-radius: 10px;")
        layout.addWidget(self.sell_light)

        self.back_button = QPushButton('Back to Main Menu', self)
        self.back_button.setFont(QFont("Arial", 14))
        self.back_button.clicked.connect(self.go_to_main_menu)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_lights)
        self.timer.start(500)

    def buy_trade(self):
        self.buy_light.setStyleSheet("background-color: green; border-radius: 10px;")
        print("Buy Trade Executed")

    def sell_trade(self):
        self.sell_light.setStyleSheet("background-color: red; border-radius: 10px;")
        print("Sell Trade Executed")

    def update_lights(self):
        if self.get_trading_signal() == "BUY":
            self.buy_light.setStyleSheet("background-color: green; border-radius: 10px;")
            self.sell_light.setStyleSheet("background-color: gray; border-radius: 10px;")
        elif self.get_trading_signal() == "SELL":
            self.buy_light.setStyleSheet("background-color: gray; border-radius: 10px;")
            self.sell_light.setStyleSheet("background-color: red; border-radius: 10px;")

    def get_trading_signal(self):
        return "BUY"

    def go_to_main_menu(self):
        self.main_window.stacked_widget.setCurrentWidget(self.main_window.main_menu)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    set_dark_theme(app)
    login_window = LoginWindow()
    if login_window.exec_() == LoginWindow.Accepted:
        main_window = MainWindow()
        main_window.show()
    sys.exit(app.exec_())