#!/usr/bin/env python3

import sys
# import this

hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert the hex string to bytes
byte_data = bytes.fromhex(hex_string)

# Convert the bytes to a string
flag = byte_data.decode('ascii')

print(flag)