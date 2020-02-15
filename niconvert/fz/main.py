import sys
from PyQt5.QtWidgets import *
from window import Ui_MainWindow
from download import Download
# import PyQt5.QtWidgets as qt


class Application(Ui_MainWindow):
    def show(self):
        app = QApplication(sys.argv)
        w = QMainWindow()
        self.MainWindow = w
        w.resize(250, 150)
        w.move(300, 300)
        self.setupUi(w)
        self.setupEvents()
        w.show()
        sys.exit(app.exec_())

    def openSaveFileDialog(self, txt, filter):
        path = QFileDialog.getSaveFileName(
            self.MainWindow, "文件保存",  filter=filter)
        if path:
            txt.setText(path[0])

    def openOpenFileDialog(self, txt, filter):
        path = QFileDialog.getOpenFileName(
            self.MainWindow, "文件保存",  filter=filter)
        if path:
            txt.setText(path[0])

    def btnDownloadXmlClicked(self):
        d = Download()
        try:
            d.download(self.txtAv.toPlainText(), self.txtXml.toPlainText)
            QMessageBox.information(
                self.MainWindow, "下载", "下载成功", QMessageBox.Ok)
        except Exception as ex:
            QMessageBox.critical(self.MainWindow, "下载", "下载失败：" +
                                 str(ex), QMessageBox.Ok)

    def txtAvTextChanged(self):
        self.btnDownloadXml.setEnabled(len(self.txtAv.text()) > 0)

    def setupEvents(self):
        self.btnBrowseXmlOutput.clicked.connect(
            lambda state:  self.openSaveFileDialog(self.txtXmlOutput, "XML文件 (*.xml)"))
        self.btnBrowseXmlInput.clicked.connect(
            lambda state:  self.openOpenFileDialog(self.txtXmlInput, "XML文件 (*.xml)"))
        self.btnBrowseAssOutput.clicked.connect(
            lambda state:  self.openSaveFileDialog(self.txtAssOutput, "ASS文件 (*.ass)"))
        self.btnDownloadXml.clicked.connect(self.btnDownloadXmlClicked)
        self.txtAv.textChanged.connect(self.txtAvTextChanged)


def main():
    app = Application()
    app.show()


if __name__ == "__main__":

    main()
    # import window

    # app = QApplication(sys.argv)
    # w = QMainWindow()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('BiliBili 弹幕下载&转换')

    # window.Ui_MainWindow().setupUi(w)
    # w.show()
    # sys.exit(app.exec_())
