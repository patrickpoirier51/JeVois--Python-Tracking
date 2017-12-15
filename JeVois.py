
import serial
import string


class JeVois(object):

        def __init__(self):
            self.ser = serial.Serial(port='/dev/ttyAMA0',baudrate=9600, timeout = 0.2)

        def balloon_xysize(self):
            balloon_found = False
            balloon_x = 0
            balloon_y = 0
            balloon_radius = 0
            ID = 0
            DATA = 0
            

            
            line = self.ser.readline()
            #print line
            words = string.split(line , " ")    # Fields split
            if len(words) > 2:
                    if str (words [0]) == "ArUco":
                            ID = int (words [1])
                            DATA = str (words [2])
                            position = string.split(DATA , ",")
                            balloon_x = int (position [0])
                            balloon_y = int (position [1])
                            balloon_found = True
                    else:
                        pass
               
            # Waiting for JeVois on how to pass W & H
            #print ID
            balloon_radius = ID

            #print balloon_found, balloon_x, balloon_y, balloon_radius
            
            self.ser.close
            #print "closed"
            return balloon_found, balloon_x, balloon_y, balloon_radius
        
              
        # main - tests the Openmv class
        def main(self):
                while True:
                    self.balloon_xysize()


   
# create the global balloon_finder object
JeVois = JeVois()

# run a test if this file is being invoked directly from the command line
if __name__ == "__main__":
    JeVois.main()
