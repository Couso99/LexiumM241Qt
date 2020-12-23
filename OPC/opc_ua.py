from opcua import Client
from opcua import ua

class OPC_Ua:
    def __init__(self, opc_address):
        self.client = Client(opc_address) # construye un objeto cliente OPC UA para un servidor
        ############################ OPC UA VARIABLES ############################
        self.isLocal = "Main.isLocal (%IX12.5)"
        self.isStop = "Main.isStop"
        self.boolPowerOn = "Ua_control.boolPowerOn"
        self.boolReset = "Ua_control.boolReset"
        self.boolHome = "Ua_control.boolHome"
        self.boolMoveAbsolute = "Ua_control.boolMoveAbsolute"
        self.selectedPosition = "Ua_control.selectedPosition"
        self.actualPosition = "Ua_control.actualPosition"

        self.velocity = "Ua_control.new_velocity"
        self.boolChangeVelocity = "Ua_control.boolChangeVelocity"

        self.boolTrue = ua.DataValue(ua.Variant(True,ua.VariantType.Boolean))
        self.boolFalse = ua.DataValue(ua.Variant(False,ua.VariantType.Boolean))

    def init_opc(self):
        self.reset()
        self.do_home()

    def connect(self):
        self.client.connect()
        root = self.client.get_root_node()
        objects = root.get_child(['0:Objects'])
        self.m241 = objects.get_child(['2:M241-M251 data'])

    def disconnect(self):
        self.client.disconnect()

    def reset(self):
        self.connect()
        child = self.m241.get_child(['2:'+self.boolReset])
        child.set_value(self.boolTrue)
        self.disconnect()

    def shutdown(self):
        self.connect()
        self.__power_off()
        self.disconnect()

    def do_home(self):
        self.connect()
        self.__power_on()
        child = self.m241.get_child(['2:'+self.boolHome])
        child.set_value(self.boolTrue)
        self.disconnect()

    def update_selected_position(self, position):
        self.connect()
        child = self.m241.get_child(['2:'+self.selectedPosition])
        newSelectedPosition = ua.DataValue(ua.Variant(position,ua.VariantType.Int32))
        child.set_value(newSelectedPosition)
        self.disconnect()

    def stop_movement(self):
        self.connect()
        child = self.m241.get_child(['2:'+self.boolMoveAbsolute])
        child.set_value(self.boolFalse)
        self.__power_off()
        self.disconnect()

    def start_movement(self):
        self.connect()
        self.__power_on()
        child = self.m241.get_child(['2:'+self.boolMoveAbsolute])
        child.set_value(self.boolTrue)
        self.disconnect()

    def get_actual_position(self):
        self.connect()
        child = self.m241.get_child(['2:'+self.actualPosition])
        actualP = child.get_value()
        self.disconnect()
        return actualP

    def get_isLocal(self):
        self.connect()
        child_isLocal = self.m241.get_child(['2:'+self.isLocal])
        isLocal_value = child_isLocal.get_value()
        child_isStop = self.m241.get_child(['2:'+self.isStop])
        isStop_value = child_isStop.get_value()
        self.disconnect()
        return isLocal_value, isStop_value

    def change_velocity(self, new_vel):
        self.connect()
        child = self.m241.get_child(['2:'+self.velocity])
        newVelocity = ua.DataValue(ua.Variant(new_vel,ua.VariantType.Int16))
        child.set_value(newVelocity)
        boolChangeVel_child = self.m241.get_child(['2:'+self.boolChangeVelocity])
        boolChangeVel_child.set_value(self.boolTrue)
        self.disconnect()

    ###### PRIVATE FUNCTIONS
    def __power_on(self):
        child = self.m241.get_child(['2:'+self.boolPowerOn])
        child.set_value(self.boolTrue)

    def __power_off(self):
        child = self.m241.get_child(['2:'+self.boolPowerOn])
        child.set_value(self.boolFalse)
