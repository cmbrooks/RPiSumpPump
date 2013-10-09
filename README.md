RPiSumpPump
===========

Raspberry Pi that will be monitoring a sump pump in case it breaks

Raspberry Pi will be hooked up to the float switch of a sump pump.
The pi will be monitoring that switch for any normal or unusual activity
and keep a log of everything that happens to a text file on a flash drive.
The switch will be deemed broken if:
  
  1. The swith is left on for more than three minutes
      (Meaning that it is not pumping out excess water)
  2. The switch turns on more than 10 times in three minutes
      (Meaning that the pump is pumping water back into itself)
      
Once the sump pump has been deemed broken, an email will be sent to preset
recipiants through a gmail account.

Also, the user will be able to interact with the embeded Raspberry Pi through
the script over SSH from a different computer and get real-time updates without
having to stop the process in order to look at the data log.

The Raspberry Pi will also be responsible for monitoring the AC power to the house
and alert someone if the power is out at the house. The Raspberry Pi will be run off
of a DC power supply in case of a power outage.
  
