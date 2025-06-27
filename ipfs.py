import requests
import json
import io

jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI5MzgxMzFiZS00ZTQwLTRiZDctYmQzMy0wNzEwNTc1MmZkMTQiLCJlbWFpbCI6ImF1dG5hcGhhdEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJGUkExIn0seyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJOWUMxIn1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiYjRhY2RhMjcwYmQ2OGYxNGNjMDEiLCJzY29wZWRLZXlTZWNyZXQiOiJlMDMxNTQ3YWQwZjg3N2M2NTljZDJkYjdjMWQ1YzliNDJkYWQ1MDRiZDVmYmU5OTZkNzI2Mjk4YzIyYjcxMjNiIiwiZXhwIjoxNzgyNTMyMTA2fQ.UHQqS1s-uU79KSn-4-wnZ_7NQ-t7yz09Q3TdDmy9hoo"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_string = json.dumps(data, indent=4)
	json_bytes = json_string.encode("utf-8")
	file_setting = io.BytesIO(json_bytes)

  # Construct the multipart/form-data payload
	files = {'file': ('testing.json', file_setting, 'application/json')}
	data = {'network': 'public'}
	headers = {'Authorization': f'Bearer {jwt}'}

  # Send the POST request
	response = requests.post('https://uploads.pinata.cloud/v3/files', headers=headers, files=files, data=data)
	response.raise_for_status()  # Raise an error for bad responses

  # Parse response and return the CID or file ID
	return response.json().get('data').get('cid')

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	# Send the GET request
	url = "https://gateway.pinata.cloud/ipfs/" + cid
	headers = {'Authorization': f'Bearer {jwt}'}

	data = requests.get(url, headers=headers)
	data.raise_for_status()  # Raise an error for bad responses

	data = data.json()
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data

if __name__ == "__main__":
	get_from_ipfs("bafkreiaqxgprbh35ef4labvcxcukjpnqh7blzuxzwyu3rmsjs6ee4h3y4i")
