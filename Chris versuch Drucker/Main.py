from escpos.printer import Usb
import time
import keyboard
def drucke_spruch(spruch):
    p = Usb(0x04b8, 0x0202)
    p.text(spruch)
    p.cut()

sprueche = ["Traditionen, oft so schön vertraut Doch manchmal alt und eng gebaut, Festhalten an Vergangenheit,Kann neue Wege uns versperren heit."]

try:

        while True:
            keyboard.wait("D")
            for spruch in sprueche:
                drucke_spruch(spruch)
                time.sleep(1)
except KeyboardInterrupt:
        pass




