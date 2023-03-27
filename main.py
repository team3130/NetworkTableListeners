import logging
from networktables import NetworkTables
import csv
import time
#TODO: run pip install pynetworktables


def main():
    NetworkTables.initialize(server="roborio-3130-frc.local")
    logging.basicConfig(level=logging.DEBUG)
    
    navy = NetworkTables.getTable('Shuffleboard/Navx')
    
    previousTimeTaken = 0

    with open('Matches/' + str(time.time()) + '.csv', '+w') as f:
        writer = csv.writer(f)
        header = ["time", "pitch", "yaw", "pitchVelocity", "roll", "rollVelocity", "positionX", "positionY", "module0Perc", "module1Perc", "module2Perc", "module3Perc"]
        writer.writerow(header)
        while (True):
            timeTaken = navy.getNumber("timeTaken", 0)
            if (timeTaken != previousTimeTaken):
                previousTimeTaken = timeTaken
                
                pitch = navy.getNumber("pitch", 0)
                roll = navy.getNumber("roll", 0)
                pitchVelocity = navy.getNumber("pitchVelocity", 0)
                rollVelocity = navy.getNumber("rollVelocity", 0)
                PositionX = navy.getNumber("positionX", 0)
                PositionY = navy.getNumber("positionY", 0)
                yaw = navy.getNumber("yaw", 0)
                
                module0Perc = navy.getNumber("module0Perc", 0)
                module1Perc = navy.getNumber("module1Perc", 0)
                module2Perc = navy.getNumber("module2Perc", 0)
                module3Perc = navy.getNumber("module3Perc", 0)
                
                row = [timeTaken, pitch, yaw, pitchVelocity, roll, rollVelocity, PositionX, PositionY, module0Perc, module1Perc, module2Perc, module3Perc]
                
                writer.writerow(row)
        f.close()
        
main()
