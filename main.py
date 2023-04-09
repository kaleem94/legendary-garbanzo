"""_summary_
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("GUI Application")
        self.resize(800, 600)

        # Create a central widget to hold the layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a main layout to hold the two tabs
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Create a tab widget for the left part
        self.left_tab = QTabWidget()
        # Set the tabs to be on the left
        self.left_tab.setTabPosition(QTabWidget.TabPosition.West)
        # Connect a signal to handle tab changes
        # self.left_tab.currentChanged.connect(self.on_left_tab_changed)

        # Create some widgets for the left tab
        self.home_widget = QWidget()
        self.home_widget.setLayout(QVBoxLayout())
        self.home_widget.layout().addWidget(QLabel("This is the home page."))

        self.about_widget = QWidget()
        self.about_widget.setLayout(QVBoxLayout())
        self.about_widget.layout().addWidget(QLabel("This is the about page."))

        # Add the widgets to the left tab with labels
        self.left_tab.addTab(self.home_widget, "Home")
        self.left_tab.addTab(self.about_widget, "About")

        # Create a tab widget for the right part
        self.right_tab = QTabWidget()
        # Set the tabs to be on the right
        self.right_tab.setTabPosition(QTabWidget.TabPosition.East)
        self.right_tab.setTabsClosable(True)  # Set the tabs to be closable
        # Connect a signal to handle tab closing
        # self.right_tab.tabCloseRequested.connect(self.on_right_tab_close)

        # Add the two tabs to the main layout with stretch factors
        self.main_layout.addWidget(self.left_tab, 1)
        self.main_layout.addWidget(self.right_tab, 3)

    def on_left_tab_changed(self, index) -> None:
        # This method is called when the left tab changes
        # Get the current widget and its label from the left tab
        current_widget = self.left_tab.currentWidget()
        current_label = self.left_tab.tabText(index)

        # Check if the right tab already has a widget with the same label
        for i in range(self.right_tab.count()):
            if self.right_tab.tabText(i) == current_label:
                # If yes, set it as the current widget and return
                self.right_tab.setCurrentIndex(i)
                return

        # If not, create a new widget for the right tab with some content
        new_widget = QWidget()
        new_widget.setLayout(QVBoxLayout())
        new_widget.layout().addWidget(
            QLabel(f"This is the content for {current_label}."))

        # Add the new widget to the right tab with the same label as the left tab
        self.right_tab.addTab(new_widget, current_label)
        # Set it as the current widget
        self.right_tab.setCurrentWidget(new_widget)

    def on_right_tab_close(self, index) -> None:
        # This method is called when a right tab is closed
        # Remove the widget at the given index from the right tab
        self.right_tab.removeTab(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
