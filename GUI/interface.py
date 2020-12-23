from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import platform

TIME_WINDOW_ms = 10000

# GUI FILE
from GUI.ui_vestidor import Ui_MainWindow
from GUI.ui_styles import Style
from GUI.itemsDialog import ItemsTableDialog

class VestidorWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        QtGui.QFontDatabase.addApplicationFont(u':/fonts/fonts/segoeui.ttf')
        QtGui.QFontDatabase.addApplicationFont(u':/fonts/fonts/segoeuib.ttf')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.parent = parent
        self.isMoving = False
        # Init graphic components
        self.ui.progressBar.setVisible(False)
        self.ui.noPositionLabel.setVisible(False)
        self.ui.userAddedFrame.setVisible(False)
        self.ui.loginPassLineEdit.setEchoMode(QLineEdit.Password)
        self.ui.newPassPassword.setEchoMode(QLineEdit.Password)
        self.ui.stackedWidget.setMinimumWidth(20)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.init_last_movements_table()
        self.init_check_control()
        # Connect to callbacks
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        self.ui.personIdLineEdit.textChanged.connect(self.check_personID)
        self.ui.goToPositionButton.clicked.connect(self.start_movement)
        self.ui.addUserButton.clicked.connect(self.add_user)
        self.ui.deleteNewUserButton.clicked.connect(self.erase_add_user)
        self.ui.doHomeButton.clicked.connect(self.parent.init_opc)
        self.ui.resetLXMButton.clicked.connect(self.parent.reset_opc)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerNewPasswordButton.clicked.connect(self.register_new_user_password)
        self.ui.assignNewPositionButton.clicked.connect(self.assign_new_position)
        self.ui.assignNewVelocity.clicked.connect(self.assign_new_velocity)

        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        UIFunctions.removeTitleBar(True)
        self.setWindowTitle('Control de un vestidor')
        UIFunctions.labelTitle(self, 'Control de un vestidor')

        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        # Add custom menus
        UIFunctions.addNewMenu(self, "Home", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Nuevo usuario", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Log in", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        # Select standard menu
        UIFunctions.selectStandardMenu(self, "btn_home")
        UIFunctions.userIcon(self, "", "url(:/16x16/icons/16x16/cil-user.png)", True)

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)

    # Change page
    def Button(self):
        btnWidget = self.sender()

        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_new_user)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Settings")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    def init_check_control(self):
        self.timer_checkControl = QtCore.QTimer()
        self.timer_checkControl.timeout.connect(self.check_control)
        isLocal_not, self.isStop = self.parent.get_isLocal()
        self.isLocal = not isLocal_not
        self.check_control()

    def check_control(self):
        isLocal_new, isStop_new = self.parent.get_isLocal()
        if self.isStop == isStop_new and self.isLocal == isLocal_new:
            return
        self.timer_checkControl.stop()
        self.isStop = isStop_new
        if self.isStop:
            self.ui.controlStackedWidget.setCurrentWidget(self.ui.page_stopped)
            self.timer_checkControl.start(300)
            return
        self.isLocal = isLocal_new
        if self.isLocal:
            self.ui.controlStackedWidget.setCurrentWidget(self.ui.page_localControl)
            self.timer_checkControl.start(300)
        else:
            self.ui.controlStackedWidget.setCurrentWidget(self.ui.page_pythonControl)
            self.timer_checkControl.start(2000)

    ### Events
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            pass

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def keyPressEvent(self, event):
        pass

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(VestidorWindow, self).resizeEvent(event)

    def resizeFunction(self):
        pass


    ### Callbacks
    def login(self):
        mail = self.ui.loginMailLineEdit.text()
        password = self.ui.loginPassLineEdit.text()
        if mail == "" or password == "":
            return
        isValidPassword = self.parent.check_password(mail, password)
        if isValidPassword:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            self.ui.loginMailLineEdit.setText("")
            self.ui.loginPassLineEdit.setText("")

    def register_new_user_password(self):
        personID = self.ui.newPassPersonID.text()
        password = self.ui.newPassPassword.text()
        if int(personID) not in self.parent.allPersonId or password == "":
            return
        self.parent.register_new_user_password_from_db(personID, password)
        self.ui.outputLabelNewPassword.setText("Success")
        QtCore.QTimer.singleShot(2000, lambda: self.ui.outputLabelNewPassword.setText(""))

    def assign_new_position(self):
        personID = self.ui.newPositionPersonID.text()
        if int(personID) not in self.parent.allPersonId:
            return
        newPosition = self.parent.new_position_from_db(personID)
        self.ui.outputPositionLabel.setText(f"Posicion: {newPosition}")
        QtCore.QTimer.singleShot(2000, lambda: self.ui.outputPositionLabel.setText(""))

    def assign_new_velocity(self):
        velocity = self.ui.newVelocitySpinBox.value()
        self.parent.change_velocity(velocity)
        self.ui.outputVelocityLabel.setText("Success")
        QtCore.QTimer.singleShot(2000, lambda: self.ui.outputVelocityLabel.setText(""))

    def launch_items_dialog(self, position):
        dlg = ItemsTableDialog(self.parent, position)
        if dlg.exec_():
            print("Success")
            movID = self.parent.get_last_movementId_from_db()
            itemIdArray_in = [row[0] for row in dlg.items_added]
            itemQuantityArray_in = [row[1] for row in dlg.items_added]
            itemIdArray_out = [row[0] for row in dlg.items_retrieved]
            itemQuantityArray_out = [row[1] for row in dlg.items_retrieved]
            self.parent.new_movement_detail_many_from_db(movID, itemIdArray_in, itemQuantityArray_in, 'I')
            self.parent.new_movement_detail_many_from_db(movID, itemIdArray_out, itemQuantityArray_out, 'O')
        else:
            print("Cancel")

    def check_personID(self):
        text = self.ui.personIdLineEdit.text()
        try:
            personID = int(text)
        except ValueError:
            personID = -1
        self.ui.tickOrCrossLabel.setVisible(False if text=="" else True)
        if int(personID) in self.parent.allPersonId:
            QtCore.QTimer.singleShot(500,lambda: self.greet_user(personID))
            self.ui.tickOrCrossLabel.setPixmap(QPixmap(u":/logos/icons/logos/tick.png"))
            self.ui.goToPositionButton.setEnabled(True)
        else:
            self.ui.tickOrCrossLabel.setPixmap(QPixmap(u":/logos/icons/logos/cross.png"))
            self.ui.goToPositionButton.setEnabled(False)
            self.ui.positionLabel.setText('')
            self.ui.greetingLabel.setText("")

    def greet_user(self, personID):
        if str(personID) == self.ui.personIdLineEdit.text():
            self.parent.update_person_details(personID)
            self.ui.greetingLabel.setText(f"Hola, <strong>{self.parent.personDetails[1]} {self.parent.personDetails[2]}<\strong>")

    def start_movement(self):
        retval = self.parent.start_movement(int(self.ui.personIdLineEdit.text()))
        if not retval:
            self.ui.noPositionLabel.setVisible(True)
            QtCore.QTimer.singleShot(3000, lambda: self.ui.noPositionLabel.setVisible(False))
            return
        self.ui.personIdLineEdit.setEnabled(False)
        self.ui.goToPositionButton.setEnabled(False)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setVisible(True)

        self.lastUser = self.ui.personIdLineEdit.text()
        self.isMoving = True
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(300)

    def stop_movement(self):
        global TIME_WINDOW_ms
        self.isMoving = False
        user = self.ui.personIdLineEdit.text()
        self.ui.progressBar.setVisible(False)
        self.ui.personIdLineEdit.setText("")
        self.ui.personIdLineEdit.setEnabled(True)
        self.ui.positionLabel.setText('')
        if self.parent.selectedPosition != 0:
            self.launch_items_dialog(self.parent.selectedPosition)
            QtCore.QTimer.singleShot(TIME_WINDOW_ms, lambda: self.return_home(user))

    def return_home(self, previousUser):
        if self.isLocal or self.isStop:
            return
        if not self.isMoving and previousUser == self.lastUser:
            self.parent.return_home()
            self.ui.personIdLineEdit.setEnabled(False)
            self.ui.goToPositionButton.setEnabled(False)
            self.ui.progressBar.setValue(0)
            self.ui.progressBar.setVisible(True)

            self.isMoving = True
            # TIMER IN MILLISECONDS
            self.timer.start(300)

    def progress(self):
        self.parent.update_actualPosition()
        percentage = 100 if self.parent.initialPosition==self.parent.selectedPosition else 100*abs((self.parent.initialPosition-self.parent.actualPosition)/(self.parent.selectedPosition-self.parent.initialPosition))
        self.ui.progressBar.setValue(percentage if percentage<=100 else 100)
        self.ui.positionLabel.setText(f"Posición: {self.parent.actualPosition}")
        if percentage >= 100:
            self.timer.stop()
            self.ui.progressBar.setValue(100)
            self.parent.stop_movement()
            self.update_movements_table()
            QtCore.QTimer.singleShot(1500, self.stop_movement)

    def add_user(self):
        name = self.ui.nameLineEdit.text()
        lastName = self.ui.lastNameLineEdit.text()
        mail = self.ui.correoLineEdit.text()
        if name != "" and lastName != "" and mail != "":
            phone = self.ui.telefonoLineEdit.text() if self.ui.telefonoLineEdit.text()!="" else None
            address = self.ui.direccionLineEdit.text() if self.ui.direccionLineEdit.text()!="" else None
            boolAssignPosition = self.ui.assignPositionRadioButton.isChecked()
            self.parent.add_new_person_to_db(name,lastName,mail,phone,address,boolAssignPosition)
            self.ui.userAddedFrame.setVisible(True)
            self.ui.newPersonIDLabel.setText(str(self.parent.personDetails[0]))
            if boolAssignPosition:
                self.ui.newPositionLabel.setText(str(self.parent.newAssignedPosition))
            else:
                self.ui.newPositionLabel.setText("Ninguna")
            self.ui.addUserOutcomeLabel.setText("Usuario creado correctamente")
            QtCore.QTimer.singleShot(5000, self.erase_add_user)
        else:
            self.ui.addUserOutcomeLabel.setText("Los campos Nombre, Apellidos y Correo son obligatorios.\nPor favor rellénelos para ser añadido")
            QtCore.QTimer.singleShot(4000, lambda: self.ui.addUserOutcomeLabel.setText(""))

    def erase_add_user(self):
        self.ui.userAddedFrame.setVisible(False)
        self.ui.addUserOutcomeLabel.setText("")
        self.ui.nameLineEdit.setText("")
        self.ui.lastNameLineEdit.setText("")
        self.ui.correoLineEdit.setText("")
        self.ui.telefonoLineEdit.setText("")
        self.ui.direccionLineEdit.setText("")
        self.ui.assignPositionRadioButton.setChecked(False)

    def init_last_movements_table(self):
        self.ui.lastMovementsTable.setColumnWidth(0,90)
        self.ui.lastMovementsTable.setColumnWidth(1,280)
        self.ui.lastMovementsTable.setColumnWidth(2,80)
        self.ui.lastMovementsTable.setColumnWidth(3,100)
        self.update_movements_table()

    def update_movements_table(self):
        last_movements = self.parent.get_last_movements_from_db()
        self.ui.lastMovementsTable.setRowCount(len(last_movements)+1)
        for row,tuple in enumerate(last_movements):
            for column, item in enumerate(tuple):
                new_widget = QtWidgets.QTableWidgetItem(str(item))
                if column == 0:
                    new_widget.setTextAlignment(Qt.AlignCenter)
                self.ui.lastMovementsTable.setItem(row+1, column, new_widget)




################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PyQt5
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################
## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1


class UIFunctions(VestidorWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()


    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ## ==> USER ICON
    ########################################################################
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # SET TEXT
            self.ui.label_user_icon.setText(initialsTooltip)

            # SET ICON
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())


    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
