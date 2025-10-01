################################################################################################################

# Copyright (C) 2025 by Uwe Martens * www.namecoin.pro * Web3 ID: https://dotbit.app

################################################################################################################

import requests
import json
import base64
import time

rpc_user = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
rpc_pass = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
url = "http://127.0.0.1:8336/"

file="namecoinfiles.org_logo_2.png"

with open('fragments.txt', 'r') as f:
	fragments = [line.strip() for line in f if line.strip()]
hex_parts = []

for name in fragments:
	hex_name = name.encode('utf-8').hex()
	payload = {
		"jsonrpc": "1.0",
		"id": "name_history",
		"method": "name_history",
		"params": [hex_name]
	}
	headers = {"Content-Type": "application/json"}
	response = requests.post(url, json=payload, auth=(rpc_user, rpc_pass))
	result = response.json()
	data = result['result']
	first_value = data[0]['value']
	hex_parts.append(first_value)

big_hex = ''.join(hex_parts)
base64_bytes = bytes.fromhex(big_hex)
base64_str = base64_bytes.decode('utf-8')
image_bytes = base64.b64decode(base64_str)

with open(file, 'wb') as f:
	f.write(image_bytes)
print(f"Image saved as {file}")
time.sleep(3)
