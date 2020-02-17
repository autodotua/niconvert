import sys
import os
import platform
import subprocess
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

    def __init__(self, av, folder,fileNameFormat):
        self.av = av
        self.folder = folder
        self.fileNameFormat=fileNameFormat
        if not bool(self.fileNameFormat):
            self. fileNameFormat = "[title] - [cid].xml"
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
                filePath=os.path.join(self.folder,self.fileNameFormat)
                filePath =  filePath.replace("[title]", info["title"]).replace( 
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
        self.setModels()
        self.setupEvents()
        self.MainWindow.show()

        self.txtAv.setText('https://www.bilibili.com/video/av37719500?p=41')
        icon = QIcon()
        icon.addPixmap(QPixmap("niconvert/fz/icon.ico"),
                       QIcon.Normal, QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        sys.exit(app.exec_())

    def setModels(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["时间", "内容"])
        self.tableView.setModel(model)

        model = QStringListModel()
        self.lvwConvertInput.setModel(model)

    def btnBrowseXmlOutputClicked(self):
        path = QFileDialog.getExistingDirectory(
            self.MainWindow, "保存位置")
        if path:
            self.txtDownloadOutput.setText(path)

    def btnBrowseConvertOutputClicked(self):
        path = QFileDialog.getExistingDirectory(
            self.MainWindow, "保存位置")
        if path:
            self.txtConvertOutput.setText(path)

    def btnBrowseConvertInputClicked(self):
        paths = QFileDialog.getOpenFileNames(
            self.MainWindow, "文件保存",  filter="XML文件 (*.xml);;json文件(*.json)")
        if bool(paths[0]):
            self.lvwConvertInput.model().setStringList(paths[0])
            self.updateOutputAndButtonEnable()

    def btnBrowseFilterClicked(self):
        path = QFileDialog.getOpenFileName(
            self.MainWindow, "文件保存",  filter="文本文件 (*.txt)")
        if path:
            self.txtFilter.setText(path[0])
            

    def downloadFinished(self):
        self.btnDownloadXml.setEnabled(True)
        self.lvwConvertInput.model().setStringList(self.t.files)
        self.updateOutputAndButtonEnable()
        # self.txtConvertInput.setText("|".join(self.t.files))

    def btnDownloadXmlClicked(self):
        self.t = DownloadThread(
            self.txtAv.text(), self.txtDownloadOutput.text(),self.txtFormat.text())
        self.t.printSignal.connect(lambda p:  self.txtLog.append(p))
        self.t.finished.connect(self.downloadFinished)
        self.btnDownloadXml.setEnabled(False)
        self.t.start()
        # self.txtConvertInput.setText("|".join(t.files))
        # self.stopRedirectPrint()

    def txtAvTextChanged(self):
        self.btnDownloadXml.setEnabled(bool(self.txtAv.text()))

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
    def updateOutputAndButtonEnable(self):
        buttonEnable=False
        if self.lvwConvertInput.model().rowCount()>0:
            path=self.lvwConvertInput.model().data(self.lvwConvertInput.model().index(0,0),Qt.DisplayRole)
            dir = os.path.dirname(path)
            self.txtConvertOutput.setText(os.path.abspath(dir))
            
            if bool(self.txtConvertOutput.text()):
                buttonEnable=True

        self.btnConvert.setEnabled(buttonEnable)
    def lvwConvertInputSelectionChanged(self,index):
        path=index.indexes()[0].data()
        self.loadDanmus(path)

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
    def btnOpenFolderClicked(self):
        if  self.txtConvertOutput.text():
            self.openFile(self.txtConvertOutput.text())
    def openFile(self,path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
    def convertButtonClicked(self):
        self.startRedirectPrint()
        for row in range(self.lvwConvertInput.model().rowCount()):
            path=self.lvwConvertInput.model().data(self.lvwConvertInput.model().index(row,0),Qt.DisplayRole)

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
        self.btnBrowseXmlOutput.clicked.connect(self.btnBrowseXmlOutputClicked)
        self.btnBrowseConvertInput.clicked.connect(self.btnBrowseConvertInputClicked)
        self.btnBrowseConvertOutput.clicked.connect(self.btnBrowseConvertOutputClicked)
        self.btnBrowseFilter.clicked.connect(self.btnBrowseFilterClicked)
        self.btnDownloadXml.clicked.connect(self.btnDownloadXmlClicked)
        self.txtAv.textChanged.connect(self.txtAvTextChanged)
        self.txtConvertOutput.textChanged.connect(self.updateOutputAndButtonEnable)
        self.btnConvert.clicked.connect(self.convertButtonClicked)
        self.lvwConvertInput.selectionModel().selectionChanged.connect(self.lvwConvertInputSelectionChanged)
        self.btnOpenFolder.clicked.connect(self.btnOpenFolderClicked)
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
