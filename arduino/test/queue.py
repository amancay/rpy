import usb.core
import usb.util
import Queue

from audio import AudioEvent
class AudioEvent(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'New job:', description
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Queue.PriorityQueue()

q.put( AudioEvent(3, 'Mid-level job') )
q.put( AudioEvent(10, 'Low-level job') )
q.put( AudioEvent(1, 'Important job') )

while not q.empty():
    next_job = q.get()
    print 'Processing job:', next_job.description


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
					cmd = ''
					dat = ''
				elif d < 48 or (d > 57 and d < 65) or d > 90:
					a = 1
				else:
					if con == 1:
						cmd = cmd + cd
					if don == 1:
						dat = dat + cd
            print ''.join(chr(i) for i in data)

        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):

                continue

if __name__ == '__main__':
  main()


