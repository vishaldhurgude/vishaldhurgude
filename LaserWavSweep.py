# THIS IS A CODE TO PERFORM WAVELNEGTH SWEEP FROM 765 nm to 781 mn on NewFocus 6312 GT27 H0.39 C0.39 laser.


import pyvisa
import time
rm = pyvisa.ResourceManager()
#print(rm.list_resources())

laser = rm.open_resource('GPIB0::2::INSTR') # GPIB ADDRESS IS 0::2

def opc():
 integer = 0
 while integer == 0:
  abc = int(laser.query("OPC?"))
  #if abc == 1:
   #print("OPC COMPLETE:", abc)
  integer = abc

def setDiodeCurrent():
    #set 100 mA current
    laser.write(":SOUR:CURR:LEV:DIOD 100.000") 
    opc()
    print("Diode Current :", laser.query(":SOUR:CURR:LEV:DIOD?"), " mA")
def startWavelength():
    
    laser.write(":SOUR:WAVE:STAR 764.000")
    opc()
    print("Start Wavelength :", laser.query(":SOUR:WAVE:STAR?"), " nm")

def stopWavelength():
    
    laser.write(":SOUR:WAVE:STOP 781.000")
    opc()
    print("Stop Wavelength :",laser.query(":SOUR:WAVE:STOP?"), " nm")

def forwardSlew():
   
    laser.write(":SOUR:WAVE:SLEW:FORW 0.500")
    opc()
    print("Forward Slew Rate: ", laser.query(":SOUR:WAVE:SLEW:FORW?"))

def retSlew():
    
    laser.write(":SOUR:WAVE:SLEW:RET 14.170")
    opc()
    print("Return Slew Rate: ", laser.query(":SOUR:WAVE:SLEW:RET?"))

def scanReset():
    
    laser.write(":OUTP:SCAN:RESET")
    opc()
    print("Scan Reset Complete:")

def scanStart():
    
    laser.write(":OUTPut:SCAN:STARt")
    opc()
    print("SCAN Complete:")

def turnOffDiodeCurrent():
    #set 100 mA current
    laser.write(":SOUR:CURR:LEV:DIOD 0.000") 
    opc()
    print("Diode Current :", laser.query(":SOUR:CURR:LEV:DIOD?"), " mA")

    
def sweep():
 setDiodeCurrent()
 startWavelength()
 stopWavelength()
 forwardSlew()
 retSlew()
 scanReset()
 scanStart()
 turnOffDiodeCurrent()

#Start Sweep
sweep()
laser.close()
