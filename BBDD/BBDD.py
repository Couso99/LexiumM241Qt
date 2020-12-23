# -*- coding: utf-8 -*-

import sqlite3 as sql
import os

from datetime import datetime
from passlib.hash import bcrypt

class VestidorBaseDatos:
    def __init__(self, db_path):
        self.name = db_path
        exist = os.path.exists(self.name)

        self.connect()

        if not exist:
            self.c.execute('''CREATE TABLE "Personas" (
            	"PersonaID"	INTEGER NOT NULL UNIQUE,
            	"Nombre"	TEXT NOT NULL,
            	"Apellidos"	TEXT NOT NULL,
            	"Correo"	TEXT,
            	"Telefono"	TEXT,
            	"Direccion"	TEXT,
            	"FechaHoraIngreso"	TEXT NOT NULL,
            	PRIMARY KEY("PersonaID" AUTOINCREMENT))''')
            self.c.execute('''CREATE TABLE "Posiciones" (
            	"PersonaID"	INTEGER NOT NULL,
            	"PosicionNumber"	INTEGER NOT NULL,
            	"Posicion"	INTEGER NOT NULL,
            	"FechaHoraAsignacion"	TEXT NOT NULL,
            	"FechaHoraDesasignacion"	TEXT,
            	FOREIGN KEY("PersonaID") REFERENCES "Personas"("PersonaID"),
            	PRIMARY KEY("PosicionNumber","PersonaID"))''')
            self.c.execute('''CREATE TABLE "Movimientos" (
            	"MovimientoID"	INTEGER NOT NULL,
            	"PersonaID"	INTEGER NOT NULL,
            	"FechaHora"	TEXT NOT NULL,
            	FOREIGN KEY("PersonaID") REFERENCES "Personas"("PersonaID"),
            	PRIMARY KEY("MovimientoID" AUTOINCREMENT))''')
            self.c.execute('''CREATE TABLE "Items" (
            	"ItemID"	INTEGER NOT NULL,
            	"ItemNombre"	TEXT NOT NULL,
            	"ItemDescripcion"	TEXT,
            	PRIMARY KEY("ItemID" AUTOINCREMENT))''')
            self.c.execute('''CREATE TABLE "MovimientoDetalles" (
            	"MovimientoID"	INTEGER NOT NULL,
            	"MovimientoItemNumber"	INTEGER NOT NULL,
            	"ItemID"	INTEGER NOT NULL,
            	"InOrOut"	TEXT NOT NULL,
            	"Quantity"	INTEGER NOT NULL,
            	FOREIGN KEY("MovimientoID") REFERENCES "Movimientos"("MovimientoID"),
            	PRIMARY KEY("MovimientoID","MovimientoItemNumber"))''')
            self.c.execute('''CREATE TABLE "Passwords" (
            	"PersonaID"	INTEGER NOT NULL,
            	"Password"	TEXT NOT NULL,
            	FOREIGN KEY("PersonaID") REFERENCES "Personas"("PersonaID"),
            	PRIMARY KEY("PersonaID"))''')
            self.conn.commit()
            print("Database does not exist")

    def connect(self):
        self.conn = sql.connect(self.name) # Conexión
        self.c = self.conn.cursor() # Cursor

    def disconnect(self):
        self.conn.close()

    def new_person(self, name, last_name, mail, phone='NULL', address='NULL', dateTime=str(datetime.now())):
        self.c.execute(f'''INSERT INTO Personas (Nombre, Apellidos, Correo, Telefono, Direccion, FechaHoraIngreso) VALUES
                    ("{name}","{last_name}","{mail}",{'NULL' if phone==None else str(f"'{phone}'")},
                    {'NULL' if address==None else address},"{dateTime}")''')
        new_personId = self.c.execute(f"Select PersonaID from Personas where Nombre='{name}' and Apellidos='{last_name}' and FechaHoraIngreso='{dateTime}'").fetchone()[0]
        self.conn.commit()
        return new_personId

    def remove_position(self, personID, dateTime=str(datetime.now())):
        self.c.execute(f"UPDATE Posiciones SET FechaHoraDesasignacion = '{dateTime}' WHERE FechaHoraDesasignacion is NULL and PersonaID = {personID}")
        self.conn.commit()

    def new_position(self, personID, dateTime=str(datetime.now()), position=False):
        ocuppied_positions = self.get_all_occupied_positions()
        if not position:
            first_posible_position = 20000
            assignedPosition = first_posible_position
            while assignedPosition in ocuppied_positions:
                assignedPosition += 80000
            position = assignedPosition
        self.c.execute(f"UPDATE Posiciones SET FechaHoraDesasignacion = '{dateTime}' WHERE FechaHoraDesasignacion is NULL and PersonaID = {personID}")
        newPositionNumber = self.c.execute(f"SELECT COALESCE(MAX(PosicionNumber),0)+1 FROM Posiciones WHERE PersonaID={personID}").fetchone()[0]
        self.c.execute(f'''INSERT INTO Posiciones (PersonaID, Posicion, FechaHoraAsignacion, PosicionNumber) VALUES ({personID},{position},"{dateTime}",{newPositionNumber})''')
        self.conn.commit()
        return position

    def new_movement(self, personID, dateTime=str(datetime.now())):
        self.c.execute(f"INSERT INTO Movimientos (PersonaID, FechaHora) VALUES ({personID},'{dateTime}')")
        self.conn.commit()

    def new_movement_detail(self, movementID, itemID, inOrOut, datetime=str(datetime.now())):
        newItemNumber = self.c.execute(f"SELECT COALESCE(MAX(MovimientoItemNumber),0)+1 FROM MovimientoDetalles WHERE MovimientoID={movementID}").fetchone()[0]
        self.c.execute(f"INSERT INTO Movimientos (MovimientoID, MovimientoItemNumber, ItemID, InOrOut) VALUES ({movementID},{newItemNumber},{itemID},{inOrOut})")
        self.conn.commit()

    def new_item(self, itemName, itemDescription):
        self.c.execute(f"INSERT INTO Items (ItemNombre, ItemDescripcion) VALUES ({itemName},{itemDescription})")
        self.conn.commit()

    def new_movement_detail_many(self, movementID, itemIdArray, itemQuantityArray, inOrOut):
        all_items_row = []
        newItemNumber = self.c.execute(f"SELECT COALESCE(MAX(MovimientoItemNumber),0)+1 FROM MovimientoDetalles WHERE MovimientoID={movementID}").fetchone()[0]
        for row, itemId in enumerate(itemIdArray):
            tuple = (movementID, newItemNumber,itemId,itemQuantityArray[row],inOrOut)
            newItemNumber+=1
            all_items_row.append(tuple)
        self.c.executemany(f'''INSERT INTO MovimientoDetalles (MovimientoID, MovimientoItemNumber, ItemID, Quantity, InOrOut)
                            VALUES (?,?,?,?,?)''', all_items_row)
        self.conn.commit()

    def get_all_personId(self):
        all_personId = self.c.execute("SELECT PersonaID from Personas").fetchall()
        return [personId_tuple[0] for personId_tuple in all_personId]

    def get_all_movementId(self):
        all_movementId = self.c.execute("SELECT MovimientoID from Movimientos").fetchall()
        return [movementId_tuple[0] for movementId_tuple in all_movementId]

    def get_all_itemId(self):
        all_itemId = self.c.execute("SELECT ItemID from Items order by ItemID").fetchall()
        return [itemId_tuple[0] for itemId_tuple in all_itemId]

    def get_all_occupied_positions(self):
        posiciones = self.c.execute(f"SELECT Posicion FROM Posiciones where FechaHoraDesasignacion is NULL").fetchall()
        return [posicion_tuple[0] for posicion_tuple in posiciones]

    def get_item_details(self, itemID):
        item_details = self.c.execute(f"SELECT ItemNombre, ItemDescripcion from Items where ItemID={itemID}").fetchone()
        return item_details

    def get_all_movement_details_from_personId(self, personID, position=None):
        items_pre_datetime_filter = self.c.execute(f'''select MovimientoDetalles.ItemID, Items.ItemNombre, Quantity,
                                Items.ItemDescripcion, InOrOut, Movimientos.FechaHora, Posiciones.PersonaID,
                                Posiciones.FechaHoraAsignacion, Posiciones.FechaHoraDesasignacion, Posiciones.Posicion
                                from MovimientoDetalles
                                inner join Items on Items.ItemID=MovimientoDetalles.ItemID
                                inner join Movimientos on Movimientos.MovimientoID = MovimientoDetalles.MovimientoID
                                inner join Posiciones on Posiciones.PersonaID = Movimientos.PersonaID
                                where Posiciones.PersonaID={personID} {f"and Posicion={position}" if postion else ""}''').fetchall()

        items_in_and_out = __class__.__datetime_filter(items_pre_datetime_filter, 5, 7, 8)
        return items_in_and_out

    def get_items_from_position(self, position):
        items_pre_datetime_filter = self.c.execute(f'''select MovimientoDetalles.ItemID, Items.ItemNombre, Quantity,
                                Items.ItemDescripcion, InOrOut, Movimientos.FechaHora, Posiciones.PersonaID,
                                Posiciones.FechaHoraAsignacion, Posiciones.FechaHoraDesasignacion, Posiciones.Posicion
                                from MovimientoDetalles
                                inner join Items on Items.ItemID=MovimientoDetalles.ItemID
                                inner join Movimientos on Movimientos.MovimientoID = MovimientoDetalles.MovimientoID
                                inner join Posiciones on Posiciones.PersonaID = Movimientos.PersonaID
                                where Posicion={position}''').fetchall()
        items_in_and_out = __class__.__datetime_filter(items_pre_datetime_filter, 5, 7, 8)#[]

        items_in_raw = [row[0:4] for row in items_in_and_out if row[4]=='I']
        items_out_raw = [row[0:4] for row in items_in_and_out if row[4]=='O']

        items_in_grouped = __class__.__group_item_array(items_in_raw)
        items_out = __class__.__group_item_array(items_out_raw)

        itemId_out = [row_item_out[0] for row_item_out in items_out]
        items_total = []
        for row in items_in_grouped:
            quantity = row[2]
            if row[0] in itemId_out:
                index_item_out = itemId_out.index(row[0])
                quantity -= items_out[index_item_out][2]
            if quantity < 0:
                quantity=0
            if quantity == 0:
                continue
            row = (row[0],row[1],quantity,row[3])
            items_total.append(row)
        return items_total

    def get_position_from_personId(self, personID):
        try:
            position = self.c.execute(f"SELECT Posicion FROM Posiciones where FechaHoraDesasignacion is NULL and PersonaID = {personID}").fetchone()[0]
        except TypeError:
            print("There is no position associated to that personID")
            return False
        return position

    def get_person_details(self, personID):
        details = self.c.execute(f"SELECT * FROM Personas where PersonaID = {personID}").fetchone()
        return details

    def get_last_movements(self, limitOfRows=10):
        last_movements_raw = self.c.execute(f'''SELECT Movimientos.PersonaID, Apellidos, Nombre, FechaHora
                                    from Personas
                                    inner join Movimientos on Movimientos.PersonaID = Personas.PersonaID
                                    order by FechaHora DESC
                                    LIMIT {limitOfRows}''').fetchall()

        last_movements = []
        for row in last_movements_raw:
            personID = row[0]
            fullName = str(f"{row[1]}, {row[2]}")
            dateAndTime = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S.%f')
            hourAndMinute = str(f"{dateAndTime.hour}:{dateAndTime.minute}")
            date = dateAndTime.date()
            processed_row = (personID, fullName, hourAndMinute, date)
            last_movements.append(processed_row)
        return last_movements

    def get_last_movementId(self):
        lastMovementID = self.c.execute("SELECT MovimientoID from Movimientos ORDER BY MovimientoID DESC").fetchone()[0]
        return lastMovementID

    def encrypt(self, pass_plain):
        pass_encrypted = bcrypt.using(rounds=13).hash(pass_plain)
        return pass_encrypted

    def check_encrypted(self, pass_plain,pass_encrypted):
        return bcrypt.verify(pass_plain, pass_encrypted)

    def check_password(self, mail, password):
        try:
            pass_encrypted = self.c.execute(f"SELECT Password From Passwords inner join Personas on Passwords.PersonaID=Personas.PersonaID where Correo='{mail}'").fetchone()[0]
        except TypeError:
            print("No matching mail")
            return False
        return self.check_encrypted(pass_plain=password, pass_encrypted=pass_encrypted)

    def new_password(self, personID, password):
        pass_encrypted = self.encrypt(password)
        self.c.execute(f"INSERT INTO Passwords (PersonaID,Password) VALUES ({personID},'{pass_encrypted}')")
        self.conn.commit()

    ###### PRIVATE FUNCTIONS
    @staticmethod
    def __datetime_filter(pre_datetime_filter, movementDateIndex, assignmentDateIndex, deassignmentDateIndex):
        output = []
        for row in pre_datetime_filter:
            movementDate = datetime.strptime(row[movementDateIndex],'%Y-%m-%d %H:%M:%S.%f')
            positionAssignmentDate = datetime.strptime(row[assignmentDateIndex],'%Y-%m-%d %H:%M:%S.%f')
            if movementDate < positionAssignmentDate:
                continue
            if not row[deassignmentDateIndex]:
                output.append(row)
                continue
            positionDeassignmentDate = datetime.strptime(row[deassignmentDateIndex],'%Y-%m-%d %H:%M:%S.%f')
            if movementDate < positionDeassignmentDate:
                output.append(row)
        return output

    @staticmethod
    def __group_item_array(items_array):
        items_grouped = []
        for row in items_array:
            item_id = [item[0] for item in items_grouped]
            if row[0] in item_id:
                index_items_grouped = item_id.index(row[0])
                items_grouped[index_items_grouped][2] += row[2]
            else:
                items_grouped.append([x for x in row])
        return items_grouped
