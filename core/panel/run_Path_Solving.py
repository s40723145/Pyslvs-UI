# -*- coding: utf-8 -*-
from ..QtModules import *
from .Ui_run_Path_Solving import Ui_Form as PathSolving_Form
from ..calculation.pathSolving import WorkerThread
from ..graphics.matplotlibGraphics import BasicChartDialog
from .run_Path_Solving_series import Path_Solving_series_show

class Path_Solving_show(QWidget, PathSolving_Form):
    addPathPoint = pyqtSignal(float, float)
    deletePathPoint = pyqtSignal(int)
    moveupPathPoint = pyqtSignal(int)
    movedownPathPoint = pyqtSignal(int)
    mergeMechanism = pyqtSignal(list)
    deleteResult = pyqtSignal(int)
    mergeResult = pyqtSignal(int)
    def __init__(self, mask, data, resultData, width, parent=None):
        super(Path_Solving_show, self).__init__(parent)
        self.setupUi(self)
        self.mechanism_data = resultData
        self.work = WorkerThread()
        self.work.done.connect(self.finish)
        self.X_coordinate.setValidator(mask)
        self.Y_coordinate.setValidator(mask)
        for e in data: self.Point_list.addItem('('+str(e['x'])+", "+str(e['y'])+')')
        for e in resultData: self.addResult(e)
        self.Point_list_Count()
        self.isGetResult()
    
    @pyqtSlot()
    def on_clearAll_clicked(self):
        self.Point_list.setCurrentRow(0)
        for i in reversed(range(self.Point_list.count()+1)): self.on_remove_clicked()
        self.Point_list_Count()
    
    @pyqtSlot()
    def on_series_clicked(self):
        dlg = Path_Solving_series_show()
        dlg.show()
        if dlg.exec_():
            for e in dlg.path: self.on_add_clicked(e[0], e[1])
    
    @pyqtSlot()
    def on_moveUp_clicked(self):
        n = self.Point_list.currentRow()
        if n>0 and self.Point_list.count()>1:
            self.moveupPathPoint.emit(n)
            x = self.Point_list.currentItem().text()[1:-1].split(', ')[0]
            y = self.Point_list.currentItem().text()[1:-1].split(', ')[1]
            self.Point_list.insertItem(n-1, '('+str(x)+", "+str(y)+')')
            self.Point_list.takeItem(n+1)
            self.Point_list.setCurrentRow(n-1)
    
    @pyqtSlot()
    def on_moveDown_clicked(self):
        n = self.Point_list.currentRow()
        if n<self.Point_list.count()-1 and self.Point_list.count()>1:
            self.movedownPathPoint.emit(n)
            x = self.Point_list.currentItem().text()[1:-1].split(', ')[0]
            y = self.Point_list.currentItem().text()[1:-1].split(', ')[1]
            self.Point_list.insertItem(n+2, '('+str(x)+", "+str(y)+')')
            self.Point_list.takeItem(n)
            self.Point_list.setCurrentRow(n+1)
    
    def addPath(self, x, y):
        self.Point_list.addItem('({}, {})'.format(x, y))
        self.Point_list_Count()
    
    @pyqtSlot()
    def on_add_clicked(self, x=False, y=False):
        if x is False:
            x=float(self.X_coordinate.text() if self.X_coordinate.text()!=str() else self.X_coordinate.placeholderText())
            y=float(self.Y_coordinate.text() if self.Y_coordinate.text()!=str() else self.Y_coordinate.placeholderText())
        self.addPathPoint.emit(x, y)
        self.Point_list.addItem("({}, {})".format(x, y))
        self.Point_list_Count()
    @pyqtSlot()
    def on_remove_clicked(self):
        if self.Point_list.currentRow()>-1:
            self.deletePathPoint.emit(self.Point_list.currentRow())
            self.Point_list.takeItem(self.Point_list.currentRow())
            self.Point_list_Count()
    
    def Point_list_Count(self):
        self.pointNum.setText(
            "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">"+str(self.Point_list.count())+"</span></p></body></html>")
        self.Generate.setEnabled(self.Point_list.count()>1)
    
    @pyqtSlot(list)
    def start(self, path):
        type_num = 0 if self.type0.isChecked() else (1 if self.type1.isChecked() else 2)
        upper = [self.AxMax.value(), self.AyMax.value(), self.DxMax.value(), self.DyMax.value()]+[self.LMax.value()]*5
        lower = [self.AxMin.value(), self.AyMin.value(), self.DxMin.value(), self.DyMin.value()]+[self.LMin.value()]*5
        self.work.setPath(path, upper, lower, self.AMin.value(), self.AMax.value(), type_num)
        print('Start Path Solving...')
        self.work.start()
        self.algorithmPanel.setEnabled(False)
        self.Tabs.setEnabled(False)
        self.Generate.setEnabled(False)
        self.timeShow.setText("<html><head/><body><p><span style=\" font-size:12pt; color:#ffff0000\">Calculating...</span></p></body></html>")
        self.timePanel.setEnabled(False)
        self.progressBar.setRange(0, 0)
    @pyqtSlot(bool)
    def stop(self, p0=True): self.work.stop()
    
    @pyqtSlot(dict, int)
    def finish(self, mechanism, time_spand):
        self.mechanism_data += [mechanism]
        self.mergeMechanism.emit([mechanism])
        self.addResult(mechanism)
        self.algorithmPanel.setEnabled(True)
        self.Tabs.setEnabled(True)
        self.Tabs.setCurrentIndex(self.Tabs.count()-1)
        self.Generate.setEnabled(True)
        self.timePanel.setEnabled(True)
        self.progressBar.setRange(0, 100)
        sec = time_spand%60
        mins = int(time_spand/60)
        self.timeShow.setText("<html><head/><body><p><span style=\" font-size:12pt\">"+str(mins)+" [min] "+str(sec)+" [s]</span></p></body></html>")
        print('Finished.')
    
    def addResult(self, e):
        item = QListWidgetItem(e['Algorithm']+(": {} ... {}".format(e['path'][:3], e['path'][-3:]) if len(e['path'])>6 else ": {}".format(e['path'])))
        item.setToolTip('\n'.join(['[{}]'.format(e['Algorithm'])]+[
            "{}: {}".format(k, v) for k, v in e.items() if not k in ['Algorithm', 'TimeAndFitness']]))
        self.Result_list.addItem(item)
        self.isGetResult()
    
    @pyqtSlot(int)
    def on_Result_list_currentRowChanged(self, cr): self.isGetResult()
    
    def isGetResult(self):
        n = self.Result_list.count()>0 and self.Result_list.currentRow()>-1
        self.mergeButton.setEnabled(n)
        self.getTimeAndFitness.setEnabled(n)
        self.deleteButton.setEnabled(n)
    
    @pyqtSlot()
    def on_deleteButton_clicked(self):
        row = self.Result_list.currentRow()
        del self.mechanism_data[row]
        self.deleteResult.emit(row)
        self.Result_list.takeItem(row)
        self.isGetResult()
    
    @pyqtSlot()
    def on_mergeButton_clicked(self):
        reply = QMessageBox.question(self, 'Prompt Message', "Merge this result to your canvas?\nDo you want to remove the results at the same time?",
            (QMessageBox.Apply | QMessageBox.Discard | QMessageBox.Cancel), QMessageBox.Apply)
        if reply==QMessageBox.Apply:
            self.mergeResult.emit(self.Result_list.currentRow())
            self.deleteResult.emit(self.Result_list.currentRow())
            self.Result_list.takeItem(self.Result_list.currentRow())
        elif reply==QMessageBox.Discard: self.mergeResult.emit(self.Result_list.currentRow())
    
    @pyqtSlot()
    def on_getTimeAndFitness_clicked(self):
        row = self.Result_list.currentRow()
        dlg = BasicChartDialog("Result{} Convergence Value Chart".format(row), self.mechanism_data[row]['TimeAndFitness'], self)
        dlg.show()
