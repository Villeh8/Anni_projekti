import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont, QColor, QPalette
from counter import TimeCounter  # Import the TimeCounter class from the other file

class TimeCounterUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create an instance of the time counter
        self.counter = TimeCounter()

        # Create the UI
        self.init_ui()

        # Update the timer every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000ms (1 second)

    def init_ui(self):
        # Set up the window
        self.setWindowTitle('Time Counter')
        self.setGeometry(100, 100, 400, 200)

        # Set background color to pink
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#FFC0CB"))  # Pink color
        self.setPalette(palette)

        # Create a layout
        layout = QVBoxLayout()

        # Create a label for the time
        self.time_label = QLabel("Initializing...", self)
        self.time_label.setFont(QFont('Arial', 20))
        self.time_label.setStyleSheet("color: black;")
        layout.addWidget(self.time_label)

        # Create a button to reset the timer
        reset_button = QPushButton("Reset Timer", self)
        reset_button.setFont(QFont('Arial', 14))
        reset_button.setStyleSheet("background-color: white; color: black;")
        reset_button.clicked.connect(self.reset_timer)
        layout.addWidget(reset_button)

        # Set the layout
        self.setLayout(layout)

    def update_time(self):
        total_elapsed_time = self.counter.get_elapsed_time()

        # Convert total elapsed time into days, hours, minutes, and seconds
        days = int(total_elapsed_time // 86400)
        hours = int((total_elapsed_time % 86400) // 3600)
        minutes = int((total_elapsed_time % 3600) // 60)
        seconds = int(total_elapsed_time % 60)

        # Update the label with the new time
        self.time_label.setText(f"Days: {days} Hours: {hours} Minutes: {minutes} Seconds: {seconds}")

    def reset_timer(self):
        self.counter.reset_timer()

    def closeEvent(self, event):
        # Save the progress when closing the window
        self.counter.save_progress()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeCounterUI()
    window.show()
    sys.exit(app.exec_())
