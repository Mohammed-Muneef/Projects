import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
#in this project i will use all the three module .it adds navbar with 3 buttons and the google is initialized as default browswr and url bar is also added to the navbar
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar=QToolBar()
        self.addToolBar(navbar)

        back_btn=QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn=QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn=QAction('Refresh',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn=QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(back_btn)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())



if __name__ == '__main__':
    app = QApplication([])
    QApplication.setApplicationName('My Web Browser')
    window = MainWindow()
    window.show()
    app.exec()