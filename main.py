#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
import os, sys

from GUI.interface import VestidorWindow
from OPC.opc_ua import OPC_Ua
from BBDD.BBDD import VestidorBaseDatos

def resource_path(relative_path):
    BASE = os.path.dirname(__file__)
    return os.path.join(BASE, relative_path)

# PARAMETERS
OPC_TCP = "opc.tcp://10.0.0.41:4840"
DATABASE_PATH = resource_path("BBDD/vestidor.db")

class Vestidor:
    def __init__(self):
        self.opc_conn = OPC_Ua(opc_address=OPC_TCP)
        self.db = VestidorBaseDatos(db_path=DATABASE_PATH)
        self.update_db_attributes()
        self.personDetails=[]

    def run(self):
        #try:
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = VestidorWindow(self)
        self.window.show()
        self.app.exec_()
        #finally:
        self.db.disconnect()
        self.opc_conn.shutdown()

    ##### OPC METHODS
    def init_opc(self):
        self.opc_conn.init_opc()

    def reset_opc(self):
        self.opc_conn.reset()

    def move_to(self, position):
        self.selectedPosition = position
        self.opc_conn.update_selected_position(self.selectedPosition)
        self.opc_conn.start_movement()
        self.initialPosition = self.opc_conn.get_actual_position()
        self.actualPosition = self.initialPosition

    def start_movement(self, personID):
        self.update_person_details(personID)
        self.selectedPosition = self.db.get_position_from_personId(self.personDetails[0])
        if self.selectedPosition:
            self.move_to(self.selectedPosition)
            return True
        else:
            return False

    def stop_movement(self):
        self.opc_conn.stop_movement()
        if self.selectedPosition:
            self.db.new_movement(self.personDetails[0])
            self.update_db_attributes()

    def return_home(self):
        self.move_to(0)

    def update_person_details(self, personID):
        self.personDetails = self.db.get_person_details(personID)

    def update_actualPosition(self):
        self.actualPosition = self.opc_conn.get_actual_position()

    def change_velocity(self, new_vel):
        self.opc_conn.change_velocity(new_vel)

    def get_isLocal(self):
        return self.opc_conn.get_isLocal()

    ##### DATABASE METHODS
    def update_db_attributes(self):
        self.allPersonId = self.db.get_all_personId()
        self.allItemId = self.db.get_all_itemId()

    def add_new_person_to_db(self, name, lastName, mail=None, phone=None, address=None, boolAssignPosition=False):
        newPersonID = self.db.new_person(name, lastName, mail, phone, address)
        ocuppied_positions = self.db.get_all_occupied_positions()
        if boolAssignPosition:
            assignedPosition = self.db.new_position(newPersonID)
        else:
            assignedPosition = None
        self.newAssignedPosition = assignedPosition
        self.update_db_attributes()
        self.update_person_details(newPersonID)

    def get_items_from_position_from_db(self, position):
        return self.db.get_items_from_position(position)

    def get_item_details_from_db(self, itemID):
        return self.db.get_item_details(itemID)

    def get_last_movements_from_db(self, limitOfRows=10):
        return self.db.get_last_movements(limitOfRows)

    def get_last_movementId_from_db(self):
        return self.db.get_last_movementId()

    def new_movement_detail_many_from_db(self, movementID, itemIdArray, itemQuantityArray, inOrOut):
        self.db.new_movement_detail_many(movementID, itemIdArray, itemQuantityArray, inOrOut)

    def new_position_from_db(self, personID):
        return self.db.new_position(personID)

    def check_password(self, mail, password):
        #if mail == "admin" and password == "1234":
        #    return True
        return self.db.check_password(mail, password)

    def register_new_user_password_from_db(self, personID, password):
        self.db.new_password(personID, password)


if __name__ == '__main__':
    v = Vestidor()
    v.run()
