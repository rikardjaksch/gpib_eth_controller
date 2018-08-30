from driver.gpib_eth import GpibEthernet


# Create an instance of the controller driver
controller = GpibEthernet()

# Define the configuration for the controller
config = {
    'mode': 1,
    'auto': 1,
    'addr': 11
}

# Connect to the controller (and check if the connection succeeded)
if controller.connect('192.168.1.132', 1234):
    # Configure the device before we start communicating with it
    controller.configure(config)

    # Send some SCPI commands to the instrument on
    # the configured GPIB address
    controller.write_instrument('ROUT:MON (@101)')
    controller.write_instrument('ROUT:MON:STATE ON')

    temp = controller.query_instrument('ROUT:MON:DATA?')

    # Remove first and last character and convert to float
    temp = temp[1:]
    temp = temp[:-1]
    print(float(temp))

    # Disconnect in order to clean up the internal socket
    controller.disconnect()
