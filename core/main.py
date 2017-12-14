# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2017 Yuan Chang
##E-mail: pyslvs@gmail.com
##
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU Affero General Public License as published by
##the Free Software Foundation; either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Affero General Public License for more details.
##
##You should have received a copy of the GNU Affero General Public License
##along with this program; if not, write to the Free Software
##Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from .QtModules import *
from .Ui_main import Ui_MainWindow
from .widgets.custom import initCustomWidgets

#Dialog
from .info.info import version_show
'''from .io.script import Script_Dialog'''
#Undo redo
from .io.undoRedo import (
    addTableCommand, deleteTableCommand,
    fixSequenceNumberCommand,
    editPointTableCommand, editLinkTableCommand,
    addPathCommand, deletePathCommand
)
#Entities
from .entities.edit_point import edit_point_show
from .entities.edit_link import edit_link_show
#Solve
from .calculation.planarSolving import (
    slvsProcess,
    SlvsException
)
'''
from .io.dxfType import dxfTypeSettings
from .io.slvsType import slvsTypeSettings
from .io.slvsForm.sketch import slvs2D
'''
#Logging
from .io.loggingHandler import XStream
#Write CSV
import csv
#Parser
from .io.larkParser import parser, ArgsTransformer

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, args, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.args = args
        #Console widget.
        self.showConsoleError.setChecked(self.args.w)
        if not self.args.debug_mode:
            self.on_connectConsoleButton_clicked()
        #Undo Stack
        self.FileState = QUndoStack()
        self.setLocate(QFileInfo(self.args.i if self.args.i else QDir.homePath()).canonicalFilePath())
        #Initialize custom UI.
        initCustomWidgets(self)
        self.Resolve()
        #Solve & DOF value.
        self.DOF = 0
        #Load workbook from argument.
        if self.args.r:
            self.FileWidget.read(self.args.r)
    
    #Adjust the canvas size after display.
    def show(self):
        super(MainWindow, self).show()
        self.DynamicCanvasView.SetIn()
    
    #Set environment variables
    def setLocate(self, locate):
        self.Default_Environment_variables = locate
        print("~Set workplace to: [\"{}\"]".format(self.Default_Environment_variables))
    
    #Drag file in to our window.
    def dragEnterEvent(self, event):
        mimeData = event.mimeData()
        if mimeData.hasUrls():
            for url in mimeData.urls():
                fileName = url.toLocalFile()
                if QFileInfo(fileName).suffix() in ('pyslvs',):
                    event.acceptProposedAction()
    
    #Drop file in to our window.
    def dropEvent(self, event):
        fileName = event.mimeData().urls()[-1].toLocalFile()
        self.FileWidget.read(fileName)
        event.acceptProposedAction()
    
    #Mouse position on canvace
    @pyqtSlot(float, float)
    def context_menu_mouse_pos(self, x, y):
        self.mouse_pos_x = x
        self.mouse_pos_y = y
    
    #Entities_Point context menu
    @pyqtSlot(QPoint)
    def on_point_context_menu(self, point):
        self.enablePointContext()
        selectionCount = len(self.Entities_Point.selectedRows())
        if selectionCount>1:
            self.popMenu_point.insertAction(self.action_point_right_click_menu_add, self.action_New_Link)
        self.popMenu_point.exec_(self.Entities_Point_Widget.mapToGlobal(point))
        if selectionCount>1:
            self.popMenu_point.removeAction(self.action_New_Link)
    
    #Entities_Link context menu
    @pyqtSlot(QPoint)
    def on_link_context_menu(self, point):
        self.enableLinkContext()
        self.popMenu_link.exec_(self.Entities_Link_Widget.mapToGlobal(point))
    
    #DynamicCanvasView context menu
    @pyqtSlot(QPoint)
    def on_canvas_context_menu(self, point):
        self.action_canvas_right_click_menu_path.setVisible(self.panelWidget.tabText(self.panelWidget.currentIndex())=="Dimensional")
        self.enablePointContext()
        selectionCount = len(self.Entities_Point.selectedRows())
        if selectionCount>1:
            self.popMenu_canvas.insertAction(self.action_canvas_right_click_menu_add, self.action_New_Link)
        self.popMenu_canvas.exec_(self.DynamicCanvasView.mapToGlobal(point))
        if selectionCount>1:
            self.popMenu_canvas.removeAction(self.action_New_Link)
    
    #What ever we have least one point or not, need to enable / disable QAction.
    def enablePointContext(self):
        selectionCount = len(self.Entities_Point.selectedRows())
        row = self.Entities_Point.currentRow()
        #If connecting with the ground.
        if selectionCount:
            fixed = all('ground' in self.Entities_Point.item(r, 1).text() for r in self.Entities_Point.selectedRows())
            self.action_point_right_click_menu_lock.setChecked(fixed)
        #If the point selected.
        for action in (
            self.action_point_right_click_menu_add,
            self.action_canvas_right_click_menu_add,
            self.action_canvas_right_click_menu_fix_add
        ):
            action.setVisible(selectionCount<=0)
        self.action_point_right_click_menu_lock.setVisible(row>-1)
        self.action_point_right_click_menu_delete.setVisible(row>-1)
        for action in (
            self.action_point_right_click_menu_edit,
            self.action_point_right_click_menu_copyPoint,
            self.action_point_right_click_menu_copydata
        ):
            action.setVisible(row>-1)
            action.setEnabled(selectionCount==1)
    
    #Enable / disable link's QAction, same as point table.
    def enableLinkContext(self):
        selectionCount = len(self.Entities_Link.selectedRows())
        row = self.Entities_Link.currentRow()
        self.action_link_right_click_menu_add.setVisible(selectionCount<=0)
        self.action_link_right_click_menu_edit.setEnabled(row>-1 and selectionCount==1)
        self.action_link_right_click_menu_delete.setEnabled(row>0 and selectionCount==1)
        self.action_link_right_click_menu_copydata.setEnabled(row>-1 and selectionCount==1)
        self.action_link_right_click_menu_release.setVisible(row==0 and selectionCount==1)
        self.action_link_right_click_menu_constrain.setVisible(row>0 and selectionCount==1)
    
    @pyqtSlot()
    def enableMenu(self):
        pointSelection = self.Entities_Point.selectedRows()
        linkSelection = self.Entities_Link.selectedRows()
        ONE_POINT = len(pointSelection)==1
        ONE_LINK = len(linkSelection)==1
        POINT_SELECTED = bool(pointSelection)
        LINK_SELECTED = bool(linkSelection) and not (ONE_LINK and 0 in linkSelection)
        #Edit
        self.action_Edit_Point.setEnabled(ONE_POINT)
        self.action_Edit_Link.setEnabled(ONE_LINK)
        #Delete
        self.action_Delete_Point.setEnabled(POINT_SELECTED)
        self.action_Delete_Link.setEnabled(LINK_SELECTED)
        #Others
        self.action_Batch_moving.setEnabled(ONE_POINT)
    
    #Copy text from point table.
    @pyqtSlot()
    def tableCopy_Points(self):
        self.tableCopy(self.Entities_Point)
    
    #Copy text from link table.
    @pyqtSlot()
    def tableCopy_Links(self):
        self.tableCopy(self.Entities_Link)
    
    #Copy item text to clipboard.
    def tableCopy(self, table):
        text = table.currentItem().text()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
    
    #Close Event
    def closeEvent(self, event):
        if self.checkFileChanged():
            event.ignore()
        else:
            if self.inputs_playShaft.isActive():
                self.inputs_playShaft.stop()
            XStream.back()
            self.setAttribute(Qt.WA_DeleteOnClose)
            print("Exit.")
            event.accept()
    
    #If the user has not saved the change. Return True if user want to Discard the operation.
    def checkFileChanged(self):
        if self.FileWidget.changed:
            reply = QMessageBox.question(self, "Message", "Are you sure to quit?\nAny changes won't be saved.",
                (QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel), QMessageBox.Save)
            if reply==QMessageBox.Save:
                self.on_action_Save_triggered()
                if self.FileWidget.changed:
                    return True
                else:
                    return False
            elif reply==QMessageBox.Discard:
                return False
            return True
        return False
    
    #The time of withdrawal and redo action.
    @pyqtSlot(int)
    def commandReload(self, index=0):
        self.action_Undo.setText("Undo - {}".format(self.FileState.undoText()))
        self.action_Redo.setText("Redo - {}".format(self.FileState.redoText()))
        if index!=self.FileWidget.Stack:
            self.workbookNoSave()
        else:
            self.workbookSaved()
        self.inputs_variable_autocheck()
        self.Resolve()
    
    #Resolve: Use Solvespace kernel.
    def Resolve(self):
        try:
            result, DOF = slvsProcess(
                self.Entities_Point.data(),
                self.Entities_Link.data(),
                self.variableConstraints() if not self.FreeMoveMode.isChecked() else ()
            )
        except SlvsException as e:
            if self.showConsoleError.isChecked():
                print(e)
            self.ConflictGuide.setToolTip(str(e))
            self.ConflictGuide.setStatusTip("Error: {}".format(e))
            self.ConflictGuide.setVisible(True)
            self.DOFview.setVisible(False)
            self.Reload_Canvas()
        else:
            self.Entities_Point.updateCurrentPosition(result)
            self.DOF = DOF
            self.DOFview.setText(str(self.DOF))
            self.ConflictGuide.setVisible(False)
            self.DOFview.setVisible(True)
            self.Reload_Canvas()
    
    #Reload Canvas, without resolving.
    def Reload_Canvas(self, *Args):
        pathIndex = self.inputs_record.currentRow()
        self.DynamicCanvasView.update_figure(
            self.Entities_Point.data(),
            self.Entities_Link.data(),
            self.FileWidget.pathData.get(self.inputs_record.item(pathIndex).text().split(':')[0], ()) if pathIndex>-1 else ()
        )
    
    #Workbook not saved signal.
    def workbookNoSave(self):
        self.FileWidget.changed = True
        not_yet_saved = " (not yet saved)"
        self.setWindowTitle(self.windowTitle().replace(not_yet_saved, '') + not_yet_saved)
    
    #Workbook saved signal.
    def workbookSaved(self):
        self.FileWidget.changed = False
        self.on_windowTitle_fullpath_clicked()
    
    @pyqtSlot()
    def on_windowTitle_fullpath_clicked(self):
        fileName = self.FileWidget.fileName
        self.setWindowTitle("Pyslvs - {}".format(
            fileName.absoluteFilePath() if self.windowTitle_fullpath.isChecked() else fileName.fileName()
        ) + (" (not yet saved)" if self.FileWidget.changed else ""))
    
    #Open website: http://mde.tw
    @pyqtSlot()
    def on_action_Get_Help_triggered(self):
        self.OpenURL("http://mde.tw")
    
    #Open website: https://pyslvs.com
    @pyqtSlot()
    def on_action_Pyslvs_com_triggered(self):
        self.OpenURL("https://pyslvs.com")
    
    #Open website: Github repository.
    @pyqtSlot()
    def on_action_github_repository_triggered(self):
        self.OpenURL("https://github.com/KmolYuan/Pyslvs-PyQt5")
    
    #Open Pyslvs about.
    @pyqtSlot()
    def on_action_About_Pyslvs_triggered(self):
        self.OpenDlg(version_show(self))
    
    #Open Qt about.
    @pyqtSlot()
    def on_action_About_Qt_triggered(self):
        QMessageBox.aboutQt(self)
    
    #Use to open link.
    def OpenURL(self, URL):
        print("Open - {{{}}}".format(URL))
        QDesktopServices.openUrl(QUrl(URL))
    
    #Use to open dialog widgets.
    def OpenDlg(self, dlg):
        dlg.show()
        dlg.exec()
    
    #Open GUI console.
    @pyqtSlot()
    def on_action_Console_triggered(self):
        self.OptionTab.setCurrentIndex(2)
        self.History_tab.setCurrentIndex(1)
    
    #Examples
    @pyqtSlot()
    def on_action_Example_triggered(self):
        self.FileWidget.loadExample()
    
    #Import a example.
    @pyqtSlot()
    def on_action_Import_Example_triggered(self):
        self.FileWidget.loadExample(isImport=True)
    
    #Create (Clean) a new workbook
    @pyqtSlot()
    def on_action_New_Workbook_triggered(self):
        if not self.checkFileChanged():
            self.clear()
            self.FileWidget.reset()
            self.FileWidget.colseDatabase()
            print("Created a new workbook.")
    
    #Clear to create commit stage.
    def clear(self):
        self.SynthesisCollections.clear()
        self.NumberAndTypeSynthesis.clear()
        self.inputs_record.clear()
        self.inputs_variable.clear()
        self.DimensionalSynthesis.clear()
        self.Entities_Point.clear()
        self.Entities_Link.clear()
        self.Resolve()
    
    #Load PMKS URL and turn it to expression.
    @pyqtSlot()
    def on_action_Import_PMKS_server_triggered(self):
        URL, ok = QInputDialog.getText(self, "PMKS URL input", "Please input link string:")
        if ok:
            dlg = QMessageBox(QMessageBox.Warning, "Loading failed", "Your link is in an incorrect format.", (QMessageBox.Ok), self)
            if URL:
                try:
                    textList = list(filter(lambda s: s not in ('', " ", '\n'),
                        tuple(filter(lambda s: 'mech=' in s, URL.split('?')[-1].split('&')))[0]
                        .replace('mech=', '').split('|')
                    ))
                    for i in range(len(textList)):
                        item = textList[i].split(',')[:-1]
                        isfloat = lambda s: s.replace('.','',1).isdigit()
                        hasAngle = isfloat(item[-1]) and isfloat(item[-2]) and isfloat(item[-3])
                        links = item[:-4] if hasAngle else item[:-3]
                        item = item[-4:] if hasAngle else item[-3:]
                        textList[i] = "J[{}, P[{}], L[{}]]".format(
                            "{}:{}".format(item[-4], item[-1]) if item[0]!='R' else 'R',
                            ", ".join((item[1], item[2])),
                            ", ".join(links)
                        )
                    textList = "M[{}]".format(", ".join(textList))
                except Exception as e:
                    dlg.show()
                    dlg.exec_()
                else:
                    self.parseExpression(textList)
            else:
                dlg.show()
                dlg.exec_()
    
    @pyqtSlot()
    def on_action_Import_Expression_triggered(self):
        expr, ok = QInputDialog.getText(self, "Expression input", "Please input expression string:")
        if ok:
            self.parseExpression(expr)
    
    #Parse expression.
    def parseExpression(self, expr):
        try:
            tree = parser.parse(expr)
            pointsArgs = ArgsTransformer().transform(tree)
        except Exception as e:
            print(e)
            dlg = QMessageBox(QMessageBox.Warning, "Loading failed", "Your expression is in an incorrect format.", (QMessageBox.Ok), self)
            dlg.show()
            dlg.exec_()
        else:
            for pointArgs in pointsArgs:
                linkNames = tuple(vlink.name for vlink in self.Entities_Link.data())
                links = pointArgs[0].split(',')
                for linkName in links:
                    #If link name not exist.
                    if linkName not in linkNames:
                        self.addLink(linkName, 'Blue')
                rowCount = self.Entities_Point.rowCount()
                self.FileState.beginMacro("Add {{Point{}}}".format(rowCount))
                self.FileState.push(addTableCommand(self.Entities_Point))
                self.FileState.push(editPointTableCommand(self.Entities_Point, rowCount, self.Entities_Link, pointArgs))
                self.FileState.endMacro()
    
    def emptyLinkGroup(self, linkcolor):
        for name, color in linkcolor.items():
            if name=='ground':
                continue
            self.addLink(name, color)
    
    #Load workbook.
    @pyqtSlot()
    def on_action_Load_Workbook_triggered(self):
        if not self.checkFileChanged():
            fileName, _ = QFileDialog.getOpenFileName(self, "Open file...", self.Default_Environment_variables, "Pyslvs workbook (*.pyslvs)")
            if fileName:
                self.FileWidget.read(fileName)
    
    #Import workbook.
    @pyqtSlot()
    def on_action_Import_Workbook_triggered(self):
        if not self.checkFileChanged():
            fileName, _ = QFileDialog.getOpenFileName(self, "Import file...", self.Default_Environment_variables, "Pyslvs workbook (*.pyslvs)")
            if fileName:
                self.FileWidget.importMechanism(fileName)
    
    #Save action.
    @pyqtSlot()
    def on_action_Save_triggered(self, isBranch=False):
        fileName = self.FileWidget.fileName.absoluteFilePath()
        suffix = self.FileWidget.fileName.suffix()
        if suffix=='pyslvs':
            self.FileWidget.save(fileName, isBranch)
        else:
            self.on_action_Save_as_triggered(isBranch)
    
    #Save as action.
    @pyqtSlot()
    def on_action_Save_as_triggered(self, isBranch=False):
        fileName = self.outputTo("workbook", ["Pyslvs workbook (*.pyslvs)"])
        if fileName:
            self.FileWidget.save(fileName, isBranch)
    
    @pyqtSlot()
    def on_action_Save_branch_triggered(self):
        self.on_action_Save_triggered(True)
    
    #TODO: Solvespace 2d save function.
    
    #TODO: DXF 2d save function.
    
    #Picture save function.
    @pyqtSlot()
    def on_action_Output_to_Picture_triggered(self):
        fileName = self.outputTo("picture", ["Portable Network Graphics (*.png)", "Joint Photographic Experts Group (*.jpg)", "Bitmap Image file (*.bmp)",
            "Business Process Model (*.bpm)", "Tagged Image File Format (*.tiff)", "Windows Icon (*.ico)", "Wireless Application Protocol Bitmap (*.wbmp)",
            "X BitMap (*.xbm)", "X Pixmap (*.xpm)"])
        if fileName:
            pixmap = self.DynamicCanvasView.grab()
            pixmap.save(fileName, format = QFileInfo(fileName).suffix())
            self.saveReplyBox('Picture', fileName)
    
    #Simple to support mutiple format.
    def outputTo(self, formatName, formatChoose):
        suffix0 = formatChoose[0].split('*')[-1][:-1]
        fileName, form = QFileDialog.getSaveFileName(self, "Save {}...".format(formatName),
            self.Default_Environment_variables+'/'+self.FileWidget.fileName.baseName()+suffix0, ';;'.join(formatChoose))
        if fileName:
            if QFileInfo(fileName).suffix()!=suffix0[1:]:
                fileName = fileName+suffix0
            self.setLocate(QFileInfo(fileName).absolutePath())
            print("Formate: {}".format(form))
        return fileName
    
    #Show message when successfully saved.
    def saveReplyBox(self, title, fileName):
        dlgbox = QMessageBox(QMessageBox.Information, title, "Successfully converted:\n{}".format(fileName), (QMessageBox.Ok), self)
        if dlgbox.exec_():
            print("Successful saved {}.".format(title))
    
    #Output to PMKS as URL.
    @pyqtSlot()
    def on_action_Output_to_PMKS_triggered(self):
        url = "http://designengrlab.github.io/PMKS/pmks.html?mech="
        urlTable = []
        for row in range(self.Entities_Point.rowCount()):
            TypeAndAngle = self.Entities_Point.item(row, 2).text().split(':')
            pointData = [
                self.Entities_Point.item(row, 1).text(),
                TypeAndAngle[0],
                self.Entities_Point.item(row, 4).text(),
                self.Entities_Point.item(row, 5).text(),
            ]
            if len(TypeAndAngle)==2:
                pointData.append(TypeAndAngle[1])
            pointData.append('tfff')
            urlTable.append(','.join(pointData))
        url += '|'.join(urlTable)+'|'
        text = '\n'.join([
            "Copy and past this link to web browser:\n", url+'\n',
            "If you have installed Microsoft Silverlight in Internet Explorer as default browser, "+
            "just click \"Open\" button to open it in PMKS website."
        ])
        dlg = QMessageBox(QMessageBox.Information, "PMKS web server", text, (QMessageBox.Save | QMessageBox.Open | QMessageBox.Close), self)
        dlg.show()
        action = dlg.exec()
        if action==QMessageBox.Open:
            self.OpenURL(url)
        elif action==QMessageBox.Save:
            clipboard = QApplication.clipboard()
            clipboard.setText(url)
    
    #Output as expression.
    @pyqtSlot()
    def on_action_Output_to_Expression_triggered(self):
        data = self.Entities_Point.data()
        expr = "M[{}]".format(", ".join(str(vpoint) for vpoint in data))
        text = "You can copy the expression and import to another workbook:\n\n{}\n\nClick the save button to copy it.".format(expr)
        dlg = QMessageBox(QMessageBox.Information, "Pyslvs Expression", text, (QMessageBox.Save | QMessageBox.Close), self)
        dlg.show()
        action = dlg.exec()
        if action==QMessageBox.Save:
            clipboard = QApplication.clipboard()
            clipboard.setText(expr)
    
    #TODO: Output to Python script for Jupyterhub.
    @pyqtSlot()
    def on_action_See_Python_Scripts_triggered(self):
        '''self.OpenDlg(Script_Dialog(self.FileWidget.fileName.baseName(), Point, Line, Chain, Shaft, Slider, Rod, self.Default_Environment_variables, self))'''
    
    #Add point group using alt key.
    @pyqtSlot()
    def qAddPointGroup(self):
        self.addPoint(self.mouse_pos_x, self.mouse_pos_y, False)
    
    #Add a point (not fixed).
    def addPointGroup(self):
        self.addPoint(self.mouse_pos_x, self.mouse_pos_y, False)
    
    #Add a point (fixed).
    def addPointGroup_fixed(self):
        self.addPoint(self.mouse_pos_x, self.mouse_pos_y, True)
    
    #Add an ordinary point.
    def addPoint(self, x, y, fixed=False, color=''):
        Args = ['ground' if fixed else '', 'R', color if color else ('Blue' if fixed else 'Green'), x, y]
        rowCount = self.Entities_Point.rowCount()
        self.FileState.beginMacro("Add {{Point{}}}".format(rowCount))
        self.FileState.push(addTableCommand(self.Entities_Point))
        self.FileState.push(editPointTableCommand(self.Entities_Point, rowCount, self.Entities_Link, Args))
        self.FileState.endMacro()
        return rowCount
    
    #Add a link.
    @pyqtSlot(list)
    def addLinkGroup(self, points):
        self.addLink(self.getLinkSerialNumber(), 'Blue', points)
    
    def addLink(self, name, color, points=[]):
        linkArgs = [name, color, ','.join(['Point{}'.format(i) for i in points])]
        self.FileState.beginMacro("Add {{Link: {}}}".format(name))
        self.FileState.push(addTableCommand(self.Entities_Link))
        self.FileState.push(editLinkTableCommand(self.Entities_Link, self.Entities_Link.rowCount()-1, self.Entities_Point, linkArgs))
        self.FileState.endMacro()
    
    def getLinkSerialNumber(self):
        name = 'link_0'
        names = [self.Entities_Link.item(row, 0).text() for row in range(self.Entities_Link.rowCount())]
        i = 0
        while name in names:
            i += 1
            name = 'link_{}'.format(i)
        return name
    
    #Create a point with arguments.
    @pyqtSlot()
    def on_action_New_Point_triggered(self):
        self.editPoint()
    
    #Edit a point with arguments.
    @pyqtSlot()
    def on_action_Edit_Point_triggered(self):
        row = self.Entities_Point.currentRow()
        self.editPoint(row if row>-1 else 0)
    
    #Edit point function.
    def editPoint(self, row=False):
        dlg = edit_point_show(self.Entities_Point.data(), self.Entities_Link.data(), row, self)
        dlg.show()
        if dlg.exec_():
            rowCount = self.Entities_Point.rowCount()
            Type = dlg.Type.currentText().split(" ")[0]
            if Type!='R':
                Type += ":{}".format(dlg.Angle.value()%360)
            Args = [
                ','.join([dlg.selected.item(row).text() for row in range(dlg.selected.count())]),
                Type,
                dlg.Color.currentText(),
                dlg.X_coordinate.value(),
                dlg.Y_coordinate.value()
            ]
            if row is False:
                self.FileState.beginMacro("Add {{Point{}}}".format(rowCount))
                self.FileState.push(addTableCommand(self.Entities_Point))
                row = rowCount
            else:
                self.FileState.beginMacro("Edit {{Point{}}}".format(rowCount))
            self.FileState.push(editPointTableCommand(self.Entities_Point, row, self.Entities_Link, Args))
            self.FileState.endMacro()
    
    #Turn a group of points to fixed on ground or not.
    def lockPoint(self):
        toFixed = self.action_point_right_click_menu_lock.isChecked()
        for row in self.Entities_Point.selectedRows():
            newLinks = self.Entities_Point.item(row, 1).text().split(',')
            if toFixed:
                if 'ground' not in newLinks:
                    newLinks.append('ground')
            else:
                if 'ground' in newLinks:
                    newLinks.remove('ground')
            Args = [
                ','.join(filter(lambda a: a!='', newLinks)),
                self.Entities_Point.item(row, 2).text(),
                self.Entities_Point.item(row, 3).text(),
                self.Entities_Point.item(row, 4).text(),
                self.Entities_Point.item(row, 5).text()
            ]
            self.FileState.beginMacro("Edit {{Point{}}}".format(row))
            self.FileState.push(editPointTableCommand(self.Entities_Point, row, self.Entities_Link, Args))
            self.FileState.endMacro()
    
    #Clone a point (with orange color).
    def clonePoint(self):
        row = self.Entities_Point.currentRow()
        Args = [
            self.Entities_Point.item(row, 1).text(),
            self.Entities_Point.item(row, 2).text(),
            'Orange',
            self.Entities_Point.item(row, 4).text(),
            self.Entities_Point.item(row, 5).text()
        ]
        rowCount = self.Entities_Point.rowCount()
        self.FileState.beginMacro("Clone {{Point{}}} as {{Point{}}}".format(row, rowCount))
        self.FileState.push(addTableCommand(self.Entities_Point))
        self.FileState.push(editPointTableCommand(self.Entities_Point, rowCount, self.Entities_Link, Args))
        self.FileState.endMacro()
    
    #Free move function.
    @pyqtSlot(tuple)
    def freemove_setCoordinate(self, coordinates):
        self.FileState.beginMacro("Moved {{{}}}".format(", ".join('Point{}'.format(c[0]) for c in coordinates)))
        for row, (x, y) in coordinates:
            Args = [
                self.Entities_Point.item(row, 1).text(),
                self.Entities_Point.item(row, 2).text(),
                self.Entities_Point.item(row, 3).text(),
                x,
                y
            ]
            self.FileState.push(editPointTableCommand(self.Entities_Point, row, self.Entities_Link, Args))
        self.FileState.endMacro()
    
    #Create a link with arguments.
    @pyqtSlot()
    def on_action_New_Link_triggered(self):
        selectedRows = self.Entities_Point.selectedRows()
        if len(selectedRows)>1:
            self.addLinkGroup(selectedRows)
        else:
            self.editLink()
    
    #Edit a link with arguments.
    @pyqtSlot()
    def on_action_Edit_Link_triggered(self):
        self.editLink(self.Entities_Link.currentRow())
    
    #Edit link function.
    def editLink(self, row=False):
        dlg = edit_link_show(self.Entities_Point.data(), self.Entities_Link.data(), row, self)
        dlg.show()
        if dlg.exec_():
            name = dlg.name_edit.text()
            Args = [
                name,
                dlg.Color.currentText(),
                ','.join([dlg.selected.item(p).text() for p in range(dlg.selected.count())])
            ]
            if row is False:
                self.FileState.beginMacro("Add {{Link: {}}}".format(name))
                self.FileState.push(addTableCommand(self.Entities_Link))
                row = self.Entities_Link.rowCount()-1
            else:
                self.FileState.beginMacro("Edit {{Link: {}}}".format(name))
            self.FileState.push(editLinkTableCommand(self.Entities_Link, row, self.Entities_Point, Args))
            self.FileState.endMacro()
    
    #Clone ground to a new link, then make ground no points.
    @pyqtSlot()
    def releaseGround(self):
        name = self.getLinkSerialNumber()
        Args = [name, 'Blue', self.Entities_Link.item(0, 2).text()]
        self.FileState.beginMacro("Release ground to {{Link: {}}}".format(name))
        #Free all points.
        self.FileState.push(editLinkTableCommand(self.Entities_Link, 0, self.Entities_Point, ['ground', 'White', '']))
        #Create new link.
        self.FileState.push(addTableCommand(self.Entities_Link))
        self.FileState.push(editLinkTableCommand(self.Entities_Link, self.Entities_Link.rowCount()-1, self.Entities_Point, Args))
        self.FileState.endMacro()
    
    #Turn a link to ground, then delete this link.
    @pyqtSlot()
    def constrainLink(self):
        row = self.Entities_Link.currentRow()
        name = self.Entities_Link.item(row, 0).text()
        linkArgs = [self.Entities_Link.item(row, 0).text(), self.Entities_Link.item(row, 1).text(), '']
        newPoints = sorted(set(self.Entities_Link.item(0, 2).text().split(','))|set(self.Entities_Link.item(row, 2).text().split(',')))
        groundArgs = ['ground', 'White', ','.join([e for e in newPoints if e])]
        self.FileState.beginMacro("Constrain {{Link: {}}} to ground".format(name))
        #Turn to ground.
        self.FileState.push(editLinkTableCommand(self.Entities_Link, 0, self.Entities_Point, groundArgs))
        #Free all points and delete the link.
        self.FileState.push(editLinkTableCommand(self.Entities_Link, row, self.Entities_Point, linkArgs))
        self.FileState.push(deleteTableCommand(self.Entities_Link, row, isRename=False))
        self.FileState.endMacro()
    
    @pyqtSlot()
    def on_action_Delete_Point_triggered(self):
        selections = self.Entities_Point.selectedRows()
        selections = tuple(p-i if p>selections[i-1] else p for i, p in enumerate(selections))
        for row in selections:
            Args = [
                '',
                self.Entities_Point.item(row, 2).text(),
                self.Entities_Point.item(row, 3).text(),
                self.Entities_Point.item(row, 4).text(),
                self.Entities_Point.item(row, 5).text()
            ]
            self.FileState.beginMacro("Delete {{Point{}}}".format(row))
            self.FileState.push(editPointTableCommand(self.Entities_Point, row, self.Entities_Link, Args))
            for i in range(self.Entities_Link.rowCount()):
                self.FileState.push(fixSequenceNumberCommand(self.Entities_Link, i, row))
            self.FileState.push(deleteTableCommand(self.Entities_Point, row, isRename=True))
            self.FileState.endMacro()
    
    @pyqtSlot()
    def on_action_Delete_Link_triggered(self):
        selections = self.Entities_Link.selectedRows()
        selections = tuple(
            p - i + int(0 in selections) if p>selections[i-1] else p
            for i, p in enumerate(selections)
        )
        for row in selections:
            if row!=0:
                Args = [
                    self.Entities_Link.item(row, 0).text(),
                    self.Entities_Link.item(row, 1).text(),
                    ''
                ]
                self.FileState.beginMacro("Delete {{Link: {}}}".format(self.Entities_Link.item(row, 0).text()))
                self.FileState.push(editLinkTableCommand(self.Entities_Link, row, self.Entities_Point, Args))
                self.FileState.push(deleteTableCommand(self.Entities_Link, row, isRename=False))
                self.FileState.endMacro()
    
    @pyqtSlot()
    def canvasCapture(self):
        clipboard = QApplication.clipboard()
        pixmap = self.DynamicCanvasView.grab()
        clipboard.setPixmap(pixmap)
        dlg = QMessageBox(QMessageBox.Information, "Captured!", "Canvas widget picture is copy to clipboard.", QMessageBox.Ok, self)
        dlg.show()
        dlg.exec_()
    
    @pyqtSlot(int)
    def on_ZoomBar_valueChanged(self, value):
        self.ZoomText.setText('{}%'.format(value))
    
    #Wheel Event
    def wheelEvent(self, event):
        if self.DynamicCanvasView.underMouse():
            a = event.angleDelta().y()
            self.ZoomBar.setValue(self.ZoomBar.value() + self.ScaleFactor.value()*a/abs(a))
    
    @pyqtSlot(bool)
    def on_action_Display_Dimensions_toggled(self, p0):
        if p0:
            self.action_Display_Point_Mark.setChecked(True)
    @pyqtSlot(bool)
    def on_action_Display_Point_Mark_toggled(self, p0):
        if not p0:
            self.action_Display_Dimensions.setChecked(False)
    
    @pyqtSlot()
    def on_action_Path_data_show_triggered(self):
        self.DynamicCanvasView.Path.show = self.action_Path_data_show.isChecked()
        self.Reload_Canvas()
    
    @pyqtSlot()
    def on_action_Path_style_triggered(self):
        self.DynamicCanvasView.Path.mode = self.action_Path_style.isChecked()
        self.Reload_Canvas()
    
    @pyqtSlot(tuple)
    def inputs_points_setSelection(self, selections):
        self.inputs_points.setCurrentRow(
            selections[0]
            if selections[0] in self.Entities_Point.selectedRows()
            else -1
        )
    
    @pyqtSlot()
    def inputs_points_clearSelection(self):
        self.inputs_points.setCurrentRow(-1)
    
    @pyqtSlot(int)
    def on_inputs_points_currentRowChanged(self, row):
        self.inputs_baseLinks.clear()
        if row>-1:
            if row not in self.Entities_Point.selectedRows():
                self.Entities_Point.setSelections((row,), False)
            for linkName in filter(lambda x: x!='', self.Entities_Point.item(row, 1).text().split(',')):
                self.inputs_baseLinks.addItem(linkName)
    
    @pyqtSlot(int)
    def on_inputs_baseLinks_currentRowChanged(self, row):
        self.inputs_driveLinks.clear()
        if row>-1:
            for linkName in self.Entities_Point.item(self.inputs_points.currentRow(), 1).text().split(','):
                if linkName==self.inputs_baseLinks.currentItem().text():
                    continue
                self.inputs_driveLinks.addItem(linkName)
    
    @pyqtSlot(int)
    def on_inputs_driveLinks_currentRowChanged(self, row):
        if row>-1:
            typeText = self.inputs_points.currentItem().text().split(" ")[0]
            self.inputs_variable_add.setEnabled(typeText=='[R]')
        else:
            self.inputs_variable_add.setEnabled(False)
    
    @pyqtSlot()
    def on_inputs_variable_add_clicked(self):
        row = self.inputs_points.currentRow()
        text = '->'.join([
            self.Entities_Point.item(self.inputs_points.currentRow(), 0).text(),
            self.inputs_baseLinks.currentItem().text(),
            self.inputs_driveLinks.currentItem().text(),
            "{:.02f}".format(self.getLinkAngle(row, self.inputs_driveLinks.currentItem().text()))
        ])
        if (self.inputs_variable.count()<self.DOF) and (not self.inputs_variable.findItems(text, Qt.MatchExactly)):
            self.inputs_variable.addItem(text)
    
    def getLinkAngle(self, row, link):
        Point = self.Entities_Point.data()
        Link = self.Entities_Link.data()
        LinkIndex = [vlink.name for vlink in Link]
        relate = Link[LinkIndex.index(link)].points
        base = Point[row]
        drive = Point[relate[relate.index(row)-1]]
        return base.slopeAngle(drive)
    
    @pyqtSlot()
    def on_inputs_variable_remove_clicked(self):
        row = self.inputs_variable.currentRow()
        if row>-1:
            self.inputs_variable_stop.click()
            self.inputs_variable.takeItem(row)
            self.Entities_Point.getBackOrigin()
            self.Resolve()
    
    def inputs_variable_autocheck(self):
        self.inputs_points.clear()
        for i in range(self.Entities_Point.rowCount()):
            text = "[{}] Point{}".format(self.Entities_Point.item(i, 2).text(), i)
            self.inputs_points.addItem(text)
        for i in range(self.inputs_variable.count()):
            itemText = self.inputs_variable.item(i).text().split('->')
            row = int(itemText[0].replace('Point', ''))
            try:
                links = self.Entities_Point.item(row, 1).text()
            except:
                links = ''
            #If this is not origin point any more.
            if (itemText[1] not in links) or (itemText[2] not in links):
                self.inputs_variable.takeItem(i)
        self.variableValueReset()
    
    @pyqtSlot(int)
    def on_inputs_variable_currentRowChanged(self, row):
        enabled = row>-1
        rotatable = enabled and not self.FreeMoveMode.isChecked()
        self.inputs_Degree.setEnabled(rotatable)
        self.inputs_variable_play.setEnabled(rotatable)
        self.inputs_variable_speed.setEnabled(rotatable)
        self.inputs_Degree.setValue(float(self.inputs_variable.currentItem().text().split('->')[-1])*100. if enabled else 0.)
    
    #Update the value when rotating QDial.
    def variableValueUpdate(self, value):
        item = self.inputs_variable.currentItem()
        value /= 100.
        if item:
            itemText = item.text().split('->')
            itemText[-1] = str(value)
            item.setText('->'.join(itemText))
            self.Resolve()
        if self.inputs_record_record.isChecked():
            self.DynamicCanvasView.recordPath()
    
    def variableValueReset(self):
        if self.inputs_playShaft.isActive():
            self.inputs_variable_play.setChecked(False)
            self.inputs_playShaft.stop()
        self.Entities_Point.getBackOrigin()
        for i in range(self.inputs_variable.count()):
            itemText = self.inputs_variable.item(i).text().split('->')
            row = int(itemText[0].replace('Point', ''))
            text = '->'.join([
                itemText[0],
                itemText[1],
                itemText[2],
                "{:.02f}".format(self.getLinkAngle(row, itemText[2]))
            ])
            self.inputs_variable.item(i).setText(text)
        self.on_inputs_variable_currentRowChanged(self.inputs_variable.currentRow())
        self.Resolve()
    
    #Generate constraint symbols.
    def variableConstraints(self):
        constraints = []
        for i in range(self.inputs_variable.count()):
            item = self.inputs_variable.item(i)
            itemText = item.text().split('->')
            itemText[0] = int(itemText[0].replace('Point', ''))
            itemText[3] = float(itemText[-1])
            constraints.append(tuple(itemText))
        return tuple(constraints)
    
    #Triggered when play button was changed.
    @pyqtSlot(bool)
    def on_inputs_variable_play_toggled(self, toggled):
        self.inputs_Degree.setEnabled(not toggled)
        if toggled:
            self.inputs_playShaft.start()
        else:
            self.inputs_playShaft.stop()
    
    #QTimer change index.
    @pyqtSlot()
    def inputs_change_index(self):
        index = self.inputs_Degree.value()
        speed = self.inputs_variable_speed.value()
        extremeRebound = self.ConflictGuide.isVisible() and self.extremeRebound.isChecked()
        if extremeRebound:
            speed *= -1
            self.inputs_variable_speed.setValue(speed)
        index += int(speed * 6 * (3 if extremeRebound else 1))
        index %= self.inputs_Degree.maximum()
        self.inputs_Degree.setValue(index)
    
    #Save to file path data.
    @pyqtSlot(bool)
    def on_inputs_record_record_toggled(self, toggled):
        if toggled:
            self.DynamicCanvasView.recordStart(self.inputs_record_limit.value())
        else:
            path = self.DynamicCanvasView.getRecordPath()
            name, ok = QInputDialog.getText(self, "Recording completed!", "Please input name tag:")
            if not name:
                nameList = [self.inputs_record.item(i).text() for i in range(self.inputs_record.count())]
                i = 0
                name = "Record_{}".format(i)
                while name in nameList:
                    i += 1
                    name = "Record_{}".format(i)
            self.addPath(name, path)
    
    def addPath(self, name, path):
        self.FileState.beginMacro("Add {{Path: {}}}".format(name))
        self.FileState.push(addPathCommand(self.inputs_record, name, self.FileWidget.pathData, path))
        self.FileState.endMacro()
        self.inputs_record.setCurrentRow(self.inputs_record.count()-1)
    
    def loadPaths(self, paths):
        for name, path in paths.items():
            self.addPath(name, path)
    
    #Remove path data.
    @pyqtSlot()
    def on_inputs_record_remove_clicked(self):
        row = self.inputs_record.currentRow()
        if row>-1:
            self.FileState.beginMacro("Delete {{Path: {}}}".format(self.inputs_record.item(row).text()))
            self.FileState.push(deletePathCommand(row, self.inputs_record, self.FileWidget.pathData))
            self.FileState.endMacro()
            self.inputs_record.setCurrentRow(self.inputs_record.count()-1)
            self.Reload_Canvas()
    
    #View path data.
    @pyqtSlot(QListWidgetItem)
    def on_inputs_record_itemDoubleClicked(self, item):
        data = self.FileWidget.pathData[item.text()]
        reply = QMessageBox.question(self, "Path data",
            "This path data including {}.".format(", ".join("Point{}".format(i) for i in range(len(data)) if data[i])),
            (QMessageBox.Save | QMessageBox.Close), QMessageBox.Close)
        if reply==QMessageBox.Save:
            fileName = self.outputTo("path data", ["Comma-Separated Values (*.csv)", "Text file (*.txt)"])
            if fileName:
                with open(fileName, 'w', newline='') as stream:
                    writer = csv.writer(stream)
                    for point in data:
                        for coordinate in point:
                            writer.writerow(coordinate)
                        writer.writerow(())
                print("Output path data: {}".format(fileName))
    
    @pyqtSlot(QPoint)
    def on_inputs_record_context_menu(self, point):
        row = self.inputs_record.currentRow()
        if row>-1:
            data = self.FileWidget.pathData[self.inputs_record.item(row).text().split(":")[0]]
            for actionName in ("Copy data from Point{}".format(i) for i in range(len(data)) if data[i]):
                self.popMenu_inputs_record.addAction(actionName)
        else:
            a = self.popMenu_inputs_record.addAction("No any path")
            a.setEnabled(False)
        action = self.popMenu_inputs_record.exec_(self.inputs_record.mapToGlobal(point))
        if action:
            copyIndex = int(action.text().replace("Copy data from Point", ''))
            clipboard = QApplication.clipboard()
            clipboard.setText('\n'.join("{},{}".format(x, y) for x, y in data[copyIndex]))
        self.popMenu_inputs_record.clear()
    
    @pyqtSlot(int)
    def on_panelWidget_currentChanged(self, index):
        self.DynamicCanvasView.setShowSlvsPath(self.panelWidget.tabText(self.panelWidget.currentIndex())=="Dimensional")
    
    def PathSolving_add_rightClick(self):
        self.DimensionalSynthesis.on_add_clicked(self.mouse_pos_x, self.mouse_pos_y)
    
    @pyqtSlot(int, tuple, tuple)
    def PathSolving_mergeResult(self, row, answer, path):
        pointNum = tuple(self.addPoint(x, y, i<2) for i, (x, y) in enumerate(answer))
        if self.FileWidget.Designs.result[row]['type']=='8Bar':
            expression = self.DimensionalSynthesis.mechanismParams_8Bar['Expression'].split(',')
        else:
            expression = self.DimensionalSynthesis.mechanismParams_4Bar['Expression'].split(',')
        expression_tag = tuple(tuple(expression[i+j] for j in range(5)) for i in range(0, len(expression), 5))
        #(('A', 'L0', 'a0', 'D', 'B'), ('B', 'L1', 'L2', 'D', 'C'), ('B', 'L3', 'L4', 'C', 'E'))
        exp_symbol = (expression_tag[0][0], expression_tag[0][3])+tuple(exp[-1] for exp in expression_tag)
        #('A', 'D', 'B', 'C', 'E')
        for i, exp in enumerate(expression_tag):
            #Dimensional synthesis link merge function.
            if i==0:
                self.addLinkGroup(pointNum[exp_symbol.index(exp[n])] for n in (0, 4))
            elif i%3==0:
                self.addLinkGroup(pointNum[exp_symbol.index(exp[n])] for n in (0, 4))
                self.addLinkGroup(pointNum[exp_symbol.index(exp[n])] for n in (3, 4))
            elif i%3==1:
                self.addLinkGroup(pointNum[exp_symbol.index(exp[n])] for n in (3, 4))
            else:
                self.addLinkGroup(pointNum[exp_symbol.index(exp[n])] for n in (0, 3, 4))
        #Add the path.
        nameList = [self.inputs_record.item(i).text() for i in range(self.inputs_record.count())]
        i = 0
        name = "Algorithm_{}".format(i)
        while name in nameList:
            i += 1
            name = "Algorithm_{}".format(i)
        self.addPath(name, path)
    
    @pyqtSlot()
    def pointSelection(self):
        self.DynamicCanvasView.changePointsSelection(self.Entities_Point.selectedRows())
    
    @pyqtSlot()
    def on_connectConsoleButton_clicked(self):
        print("Connect to GUI console.")
        XStream.stdout().messageWritten.connect(self.appendToConsole)
        XStream.stderr().messageWritten.connect(self.appendToConsole)
        self.connectConsoleButton.setEnabled(False)
        self.disconnectConsoleButton.setEnabled(True)
        print("Connect to GUI console.")
    
    @pyqtSlot()
    def on_disconnectConsoleButton_clicked(self):
        print("Disconnect from GUI console.")
        XStream.back()
        self.connectConsoleButton.setEnabled(True)
        self.disconnectConsoleButton.setEnabled(False)
        print("Disconnect from GUI console.")
    
    @pyqtSlot(str)
    def appendToConsole(self, log):
        self.consoleWidgetBrowser.moveCursor(QTextCursor.End)
        self.consoleWidgetBrowser.insertPlainText(log)
        self.consoleWidgetBrowser.moveCursor(QTextCursor.End)
    
    @pyqtSlot(bool)
    def on_action_Full_Screen_toggled(self, fullscreen):
        if fullscreen:
            self.showFullScreen()
        else:
            self.showMaximized()
