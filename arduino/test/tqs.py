import usb.core
import usb.util
import Queue
from threading import Thread

from audio import AudioEvent

q = Queue.PriorityQueue()

# lsusb -> ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
device = usb.core.find(idVendor=0x1A86, idProduct=0x7523)

if device.is_kernel_driver_active(0):
    reattach = True
    device.detach_kernel_driver(0)
		
		
# use the first/default configuration
device.set_configuration()
# first endpoint
endpoint = device[0][(0,0)][0]


# A thread that produces data
def serial(out_q):
    # read a data packet
    data = None
    con = 0;
    don = 0;
    cmd = '';
    dat = '';
    while True:
        try:
            data = device.read(endpoint.bEndpointAddress,
                               endpoint.wMaxPacketSize)
            for d in data:
				cd = chr(d);
				if cd == '$':
				    con = 1
				elif cd == ':':
					con = 0
					don = 1
				elif cd == ';':
					don = 0
					print 'CMD ' + cmd + ' DAT ' + dat
					out_q.put(AudioEvent(5, cmd, dat))
					cmd = ''
					dat = ''
				elif d < 48 or (d > 57 and d < 65) or d > 90:
					a = 1
				else:
					if con == 1:
						cmd = cmd + cd
					if don == 1:
						dat = dat + cd
 #           print ''.join(chr(i) for i in data)

        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):

                continue


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        print data.cmd

def main():
    # lsusb -> ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
    device = usb.core.find(idVendor=0x1A86, idProduct=0x7523)

    if device.is_kernel_driver_active(0):
        reattach = True
        device.detach_kernel_driver(0)
		
		
   # use the first/default configuration
    device.set_configuration()
    # first endpoint
    endpoint = device[0][(0,0)][0]
    # Create the shared queue and launch both threads
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=serial, args=(q,))
    t1.start()
    t2.start()


if __name__ == '__main__':
  main()


