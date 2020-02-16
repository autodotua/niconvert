import sys
import os
from io import StringIO
from pathlib import Path
from datetime import timedelta
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from niconvert.fz.window import Ui_MainWindow
from niconvert.fz.download import Download
from niconvert.fndcli.main import convert
from niconvert.libsite.producer import Producer


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

    def openOpenFileDialog(self, txt, filter):
        path = QFileDialog.getOpenFileName(
            self.MainWindow, "文件保存",  filter=filter)
        if path:
            txt.setText(path[0])

    def btnDownloadXmlClicked(self):
        d = Download()
        try:
            cid = d.getCid(self.txtAv.text())
            filePath = d.download(cid, self.txtDownloadOutput.text())
            QMessageBox.information(
                self.MainWindow, "下载", "下载成功", QMessageBox.Ok)
            self.txtConvertInput.setText(filePath)
        except Exception as ex:
            QMessageBox.critical(self.MainWindow, "下载", "下载失败：" +
                                 str(ex), QMessageBox.Ok)

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

        if(xmlPath and os.path.isfile(xmlPath)):
            dir = os.path.dirname(xmlPath)
            filename = Path(xmlPath).stem+".ass"
            self.txtConvertOutput.setText(os.path.join(dir, filename))
            self.loadDanmus(xmlPath)

    def loadDanmus(self, path):
        producer = Producer(self.getArgs()[0], path)
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
    def getArgs(self):
        '''
        0:{'input_filename': 'C:\\Users\\autod\\D...07087.xml',
         'output_filename': 'C:\\Users\\autod\\D...07087.ass'}
        1:{'bottom_filter': False, 'custom_filter': None, 'guest_filter': False, 'top_filter': False}
        2:{'bottom_margin': 0, 'custom_offset': '00:00', 'drop_offset': 2,
        'font_name': '微软雅黑', 'font_size': 32, 'header_file': None,
        'layout_algorithm': 'sync', 'line_count': 4, 'play_resolution': '1920x1080',
         'tune_duration': 0}
        '''
        ioArgs={
            "input_filename": self.txtConvertInput.text(),
            "output_filename": self.txtConvertOutput.text()
        }
        danmuArgs={
            'bottom_filter': self.chkDisableBottom.isChecked(),
            'custom_filter': None,
            'guest_filter': self.chkDisableGuest.isChecked(),
            'top_filter': self.chkDisableTop.isChecked()
        }

        subtitleArgs={
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
        args=self.getArgs()
        r=redirect(lambda p: self.txtLog.append(p))
        self.txtLog.append("\n")
        raw=sys.stdout
        sys.stdout=r
        try:
            convert(*args)
        except Exception as ex:
            QMessageBox.critical(self.MainWindow, "转换", "转换失败：" +
                                 str(ex), QMessageBox.Ok)
        sys.stdout=raw

    def setupEvents(self):
        self.btnBrowseXmlOutput.clicked.connect(
            lambda state:  self.openSaveFileDialog(self.txtDownloadOutput, "XML文件 (*.xml)"))
        self.btnBrowseConvertInput.clicked.connect(
            lambda state:  self.openOpenFileDialog(self.txtConvertInput, "XML文件 (*.xml);;json文件(*.json)"))
        self.btnBrowseConvertOutput.clicked.connect(
            lambda state:  self.openSaveFileDialog(self.txtConvertOutput, "ASS文件 (*.ass)"))
        self.btnBrowseFilter.clicked.connect(
            lambda state:  self.openOpenFileDialog(self.txtFilter, "文本文件 (*.txt)"))
        self.btnDownloadXml.clicked.connect(self.btnDownloadXmlClicked)
        self.txtAv.textChanged.connect(self.txtAvTextChanged)
        self.txtConvertInput.textChanged.connect(self.txtXmlInputTextChanged)
        self.txtConvertOutput.textChanged.connect(self.txtAssOutputTextChanged)
        self.btnConvert.clicked.connect(self.convertButtonClicked)


class redirect:
    def __init__(self, writed):
        self.writed=writed

    def write(self, str):
        self.writed(str)

    def flush(self):
        pass


def main():
    app=Application()
    app.show()


if __name__ == "__main__":
    main()
