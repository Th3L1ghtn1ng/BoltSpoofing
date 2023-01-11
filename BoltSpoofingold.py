import struct
import bluetooth._bluetooth as bt
a = """

  ___      _ _   ___                 __ _           
 | _ ) ___| | |_/ __|_ __  ___  ___ / _(_)_ _  __ _ 
 | _ \/ _ \ |  _\__ \ '_ \/ _ \/ _ \  _| | ' \/ _` |
 |___/\___/_|\__|___/ .__/\___/\___/_| |_|_||_\__, |   
                    / /_                        / /
                   |__  /                      /_/
                     | /
                     |/
                     '

"""
print(a)

# Get the bluetooth address as a command-line argument
bluetooth_address = input("Enter the bluetooth address: ")

# Split the bluetooth address into its bytes
baddr = [int(b, 16) for b in bluetooth_address.split(":")]

# Open hci socket
sock = bt.hci_open_dev(0)

# CSR vendor command to change address
cmd = struct.pack("<BBBBBBBBBBBBBBBBBBBBBB",
                  0xc2, 0x02, 0x00, 0x0c, 0x00, 0x11,
                  0x47, 0x03, 0x70, 0x00, 0x00, 0x01,
                  0x00, 0x04, 0x00, 0x00, 0x00, 0x00,
                  baddr[5], baddr[4], baddr[3], baddr[2], baddr[1], baddr[0])

# Send HCI request
bt.hci_send_req(sock, bt.OGF_VENDOR_CMD, 0, bt.EVT_VENDOR, 2000, cmd)

# Close the socket
sock.close()

# Notify the user to reset the device
print("Please reset the device")
