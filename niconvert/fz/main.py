import sys
import os
import threading
import asyncio
from io import StringIO
from pathlib import Path
from datetime import timedelta
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from niconvert.fz.window import Ui_MainWindow
from niconvert.fz.download import Download
from niconvert.fndcli.main import convert
from niconvert.libsite.producer import Producer


class DownloadThread(QThread):
    printSignal = pyqtSignal(str)

    def __init__(self, av, filePath):
        self.av = av
        self.filePath = filePath
        if not bool(self.filePath):
            self. filePath = "[title] - [cid].xml"
        super(DownloadThread, self).__init__()

    def run(self):
        d = Download()
        try:
            info = d.getInfo(self.av)
            print(info)
        except Exception as ex:
            self.printSignal.emit("解析HTML失败")
            self.printSignal.emit(str(ex))
            return
        files = []
        for page in info["pages"]:
            try:
                filePath = self. filePath.replace("[title]", info["title"]).replace(
                    "[cid]", page["cid"]).replace("[pagetitle]", page["title"])
                d.download(page["cid"], filePath)
                files.append(filePath)
                self .printSignal.emit("下载成功："+filePath)
            except Exception as ex:
                self.printSignal.emit("下载失败："+page["cid"])
                self.printSignal.emit(str(ex))
        self.files = files


class Application(Ui_MainWindow):
    def show(self):
        app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)
        self.setupEvents()
        self.MainWindow.show()

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["时间", "内容"])
        self.tableView.setModel(model)
        self.txtAv.setText('https://www.bilibili.com/video/av37719500?p=41')
        icon = QIcon()
        icon.addPixmap(QPixmap("niconvert/fz/icon.ico"),
                       QIcon.Normal, QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        sys.exit(app.exec_())

    def openSaveFileDialog(self, txt, filter):
        path = QFileDialog.getSaveFileName(
            self.MainWindow, "文件保存",  filter=filter)
        if path:
            txt.setText(path[0])

    def openSelectFolderDialog(self, txt):
        path = QFileDialog.getExistingDirectory(
            self.MainWindow, "保存位置")
        if path:
            txt.setText(path)

    def openOpenFileDialog(self, txt, filter):
        path = QFileDialog.getOpenFileName(
            self.MainWindow, "文件保存",  filter=filter)
        if path:
            txt.setText(path[0])

    def downloadFinished(self):
        self.btnDownloadXml.setEnabled(True)
        self.txtConvertInput.setText("|".join(self.t.files))

    def btnDownloadXmlClicked(self):
        self.t = DownloadThread(
            self.txtAv.text(), self.txtDownloadOutput.text())
        self.t.printSignal.connect(lambda p:  self.txtLog.append(p))
        self.t.finished.connect(self.downloadFinished)
        self.btnDownloadXml.setEnabled(False)
        self. t.start()
        # self.txtConvertInput.setText("|".join(t.files))
        # self.stopRedirectPrint()

    def txtAvTextChanged(self):
        self.btnDownloadXml.setEnabled(bool(self.txtAv.text()))

    def txtAssOutputTextChanged(self):
        xmlPath = self.txtConvertInput.text()
        self.btnConvert.setEnabled(
            bool(xmlPath) and bool(self.txtConvertOutput.text()))

    def txtXmlInputTextChanged(self):
        xmlPath = self.txtConvertInput.text()
        self.btnConvert.setEnabled(
            bool(xmlPath) and bool(self.txtConvertOutput.text()))
        if "|" in xmlPath:
            xmlPath = xmlPath.split("|")[0]
        if xmlPath and os.path.isfile(xmlPath):
            dir = os.path.dirname(xmlPath)
            # filename=Path(xmlPath).stem+".ass"
            #self.txtConvertOutput.setText(os.path.join(dir, filename))
            self.txtConvertOutput.setText(os.path.abspath(dir))
            self.loadDanmus(xmlPath)

    def loadDanmus(self, path):
        producer = Producer(self.getArgs(path)[0], path)
        producer.start_handle()
        index = 0
        for danmu in producer.all_danmakus:
            index += 1
            model = self.tableView.model()
            min = str(int(danmu.start/60))
            sec = str(int(danmu.start % 60))
            ms = str(int((danmu.start % 1)*100))
            model.setItem(index, 0, QStandardItem(min+":"+sec+"."+ms))
            model.setItem(index, 1, QStandardItem(danmu.content))
        self.tableView.resizeColumnsToContents()

    def getArgs(self, path):
        filename = Path(path).stem+".ass"
        ioArgs = {
            "input_filename": path,
            "output_filename": os.path.join(self.txtConvertOutput.text(), filename)
        }
        danmuArgs = {
            'bottom_filter': self.chkDisableBottom.isChecked(),
            'custom_filter': None,
            'guest_filter': self.chkDisableGuest.isChecked(),
            'top_filter': self.chkDisableTop.isChecked()
        }

        subtitleArgs = {
            'bottom_margin': int(10.8*self.txtMarginBottom.value()),
            'custom_offset': ("0-" if self.chkTimeOffsetNegetive.isChecked() else "")+self.txtTimeOffset.text(),
            'drop_offset': self.txtDropOffset.value(),
            'font_name': self.cbbFont.currentText(),
            'font_size': int(1.08*float(self.txtFontSize.text())),
            'header_file': None if not self.txtStyle.text() else self.txtStyle.text(),
            'layout_algorithm': "sync" if self.rbtnSync.isChecked() else "async",
            'line_count': self.txtMaxLines.value(),
            'play_resolution': "1920x1080",
            'tune_duration': self.txtSpeedOffset.value()
        }
        return(ioArgs, danmuArgs, subtitleArgs)

    def convertButtonClicked(self):
        self.startRedirectPrint()
        for path in self.txtConvertInput.text().split("|"):
            args = self.getArgs(path)
            try:
                convert(*args)
            except Exception as ex:
                print("转换失败")
                print(str(ex))
        self.stopRedirectPrint()

    def stopRedirectPrint(self):
        self.txtLog.append("\n")
        sys.stdout = self.stdout

    def startRedirectPrint(self):
        r = Redirect(lambda p: self.txtLog.append(p))
        self. stdout = sys.stdout
        sys.stdout = r

    def setupEvents(self):
        self.btnBrowseXmlOutput.clicked.connect(
            lambda state:  self.openSaveFileDialog(self.txtDownloadOutput, "XML文件 (*.xml)"))
        self.btnBrowseConvertInput.clicked.connect(
            lambda state:  self.openOpenFileDialog(self.txtConvertInput, "XML文件 (*.xml);;json文件(*.json)"))
        self.btnBrowseConvertOutput.clicked.connect(
            lambda state:  self.openSelectFolderDialog(self.txtConvertOutput))
        self.btnBrowseFilter.clicked.connect(
            lambda state:  self.openOpenFileDialog(self.txtFilter, "文本文件 (*.txt)"))
        self.btnDownloadXml.clicked.connect(self.btnDownloadXmlClicked)
        self.txtAv.textChanged.connect(self.txtAvTextChanged)
        self.txtConvertInput.textChanged.connect(self.txtXmlInputTextChanged)
        self.txtConvertOutput.textChanged.connect(self.txtAssOutputTextChanged)
        self.btnConvert.clicked.connect(self.convertButtonClicked)


class Redirect:
    def __init__(self, writed):
        self.writed = writed

    def write(self, str):
        self.writed(str)

    def flush(self):
        pass


def main():
    app = Application()
    app.show()


if __name__ == "__main__":
    main()
