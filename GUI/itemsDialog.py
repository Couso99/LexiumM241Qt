from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.ui_items import Ui_Dialog

class ItemsTableDialog(QtWidgets.QDialog):
    def __init__(self, parent, position):
        #super(ItemsTableDialog, self).__init__(parent)
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1,140)
        self.ui.tableWidget.setColumnWidth(2,70)
        self.ui.tableWidget.setColumnWidth(3,200)

        self.items_added = []
        self.items_retrieved = []
        self.new_items_added = []

        self.set_items_spinbox_range()
        self.load_data(position)

        self.ui.addButton.clicked.connect(self.add_item)
        self.ui.retrieveButton.clicked.connect(self.retrieve_item)

        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_movement.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def add_item(self):
        newItemId = self.ui.itemIdSpinBox.value()
        newItemQuantity = self.ui.quantitySpinBox.value()
        onlyItemsId = [row[0] for row in self.items_array]
        onlyItemsId_items_added = [item[0] for item in self.new_items_added]
        itemsCount = len(onlyItemsId)+len(self.new_items_added)
        self.items_added.append([newItemId, newItemQuantity])
        if newItemId in onlyItemsId:
            index = onlyItemsId.index(newItemId)
            quantity = int(self.itemWidgetRowArray[index][2].text())
            quantity += newItemQuantity
            newItem = self.itemWidgetRowArray[index][2].setText(str(quantity))
        elif newItemId in onlyItemsId_items_added:
            index = len(onlyItemsId)+onlyItemsId_items_added.index(newItemId)
            quantity = int(self.itemWidgetRowArray[index][2].text())
            quantity += newItemQuantity
            newItem = self.itemWidgetRowArray[index][2].setText(str(quantity))
        else:
            self.new_items_added.append([newItemId, newItemQuantity])
            details = self.parent.get_item_details_from_db(newItemId)
            nombre = details[0]
            description = details[1] if details[1] else ""
            newRow = [newItemId, nombre, newItemQuantity, description]
            itemsWidgetArray = []
            for column, item in enumerate(newRow):
                itemsWidgetArray.append(QtWidgets.QTableWidgetItem(str(item)))
                self.ui.tableWidget.setItem(itemsCount, column, itemsWidgetArray[-1])
            self.itemWidgetRowArray.append(itemsWidgetArray)

    def retrieve_item(self):
        newItemId = self.ui.itemIdSpinBox.value()
        newItemQuantity = self.ui.quantitySpinBox.value()
        onlyItemsId = [row[0] for row in self.items_array]
        if newItemId in onlyItemsId:
            index = onlyItemsId.index(newItemId)
            quantity = int(self.itemWidgetRowArray[index][2].text())
            quantity -= newItemQuantity
            if quantity < 0:
                newItemQuantity += quantity
                quantity = 0
            self.items_retrieved.append([newItemId, newItemQuantity])
            newItem = self.itemWidgetRowArray[index][2].setText(str(quantity))

    def set_items_spinbox_range(self):
        allItemsId = self.parent.allItemId
        self.ui.itemIdSpinBox.setRange(allItemsId[0], allItemsId[-1])

    def load_data(self, position):
        # ItemID ItemNombre Cantidad ItemDescripcion
        items_tuple_array = self.parent.get_items_from_position_from_db(position)
        self.items_array = [column for column in [row for row in items_tuple_array]]
        self.rowCount = len(self.items_array) + 6
        self.ui.tableWidget.setRowCount(self.rowCount)
        self.itemWidgetRowArray = []
        for row,row_array in enumerate(self.items_array):
            itemsWidgetArray = []
            for column, item in enumerate(row_array):
                itemsWidgetArray.append(QtWidgets.QTableWidgetItem(str(item)))
                self.ui.tableWidget.setItem(row, column, itemsWidgetArray[-1])
            self.itemWidgetRowArray.append(itemsWidgetArray)
