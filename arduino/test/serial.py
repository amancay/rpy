import usb.core
import usb.util

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
    while True:
        try:
            data = device.read(endpoint.bEndpointAddress,
                               endpoint.wMaxPacketSize)
            print ''.join(chr(i) for i in data)

        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):

                continue

if __name__ == '__main__':
  main()


