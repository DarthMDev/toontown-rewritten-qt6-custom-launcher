# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QUrl
import PySide6.QtGui
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtMultimedia import QSoundEffect
# QMouseEvent  from qtgui
from PySide6.QtGui import QMouseEvent
import rc_resources
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainLauncher

class Launcher(QMainWindow, Ui_MainLauncher):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       # make it frameless
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.offset = None

    def mousePressEvent(self, event: QMouseEvent) -> None:
       if event.button() == QtCore.Qt.LeftButton:
              self.offset = event.pos()
       else:
           super().mousePressEvent(event)
        
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
         if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
                  self.move(self.pos() + event.pos() - self.offset)
         else:
              super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.offset = None
        super().mouseReleaseEvent(event)
           
    
    def playSound(self, soundFile):
        # play sound file
        resources_dir = "./resources"
        soundFile = resources_dir + "/" + soundFile + ".wav"
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(soundFile))
        effect.play()    

    def playMusic(self, musicFile):
        # play music file 
        resources_dir = "./resources"
        musicFile = resources_dir + "/" + musicFile + ".wav"
        music = QSoundEffect()
        music.setSource(QUrl.fromLocalFile(musicFile))
        # loop the music
        music.setLoopCount(QSoundEffect.Infinite)
        music.play()



    def stopMusic(self):
        # stop the current music
        self.ui.musicPlayer.stop()

    def playClick(self):
        self.playSound("GUI_Click_Alt_v22")

    def playHover(self):
        # this is weirdly named 
        self.playSound("click.wav")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Launcher()
    widget.show()
    sys.exit(app.exec())
