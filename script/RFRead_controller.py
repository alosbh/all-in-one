import MFRC522

# Badge reading function
class RFRead_controller:
    def RFRead():

        Read_ID = None

             # Instantiate the RFID reader class
        reader = MFRC522.MFRC522()

             # Get the badge id from the RFID reader
        Read_ID = reader.JABIL_Matricula() 

             # close the SPI slot 
        reader.close_SPI()

        return Read_ID