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
        self.setEvents()
        w.show()
        sys.exit(app.exec_())

    def btnBrowseXmlClicked(self):
        path = QFileDialog.getSaveFileName(
            self.MainWindow, "文件保存",  filter="所有文件 (*);;XML文件 (*.xml)")
        if path is not None and len(path) > 0:
            self.txtXml.setPlainText(path[0])

    def btnDownloadXmlClicked(self):
        d = Download()
        try:
            d.download(self.txtAv.toPlainText(), self.txtXml.toPlainText)
            QMessageBox.information(
                self.MainWindow, "下载", "下载成功", QMessageBox.Ok)
        except BaseException as ex:
            QMessageBox.critical(self.MainWindow, "下载", "下载失败：" +
                                 str(ex), QMessageBox.Ok)

    def txtAvTextChanged(self):
        self.btnDownloadXml.setEnabled(len(self.txtAv.toPlainText()) > 0)

    def setEvents(self):
        self.btnBrowseXml.clicked.connect(self.btnBrowseXmlClicked)
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
