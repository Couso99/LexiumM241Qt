# LexiumM241Qt
 Program to control Lexium M241 through desktop app and digital and analog inputs in the variator itself.

The arquitecture is made up of a Lexium M241 variator, a SIEMENS PLC and a computer running OPC Ua Expert and custom Python code.

The computer communicates with the PLC through OPC Ua Expert, and is controlled thanks to the library opcua, used in Python.

From here, the PLC is capable of communicating with the Lexium M241 following the code created for this purpose (project stored in folder SoMachine). A local control is also allowed so that it is possible to control the desired motor even without a computer, but only with the variator and PLC.

 Desktop app implemented with Python, library PyQt5 for interface.

 Registers are stored in relational database (controlled through Python program using sqlite3)

 Project made for university assignment, that's why PDF with brief explanation is in Spanish.
