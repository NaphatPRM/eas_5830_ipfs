import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_string = json.dumps(data, indent=4)
	api_key = "b4acda270bd68f14cc01"
	api_secret = "e031547ad0f877c659cd2db7c1d5c9b42dad504bd5fbe996d726298c22b7123b"
	jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI5MzgxMzFiZS00ZTQwLTRiZDctYmQzMy0wNzEwNTc1MmZkMTQiLCJlbWFpbCI6ImF1dG5hcGhhdEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJGUkExIn0seyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJOWUMxIn1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiYjRhY2RhMjcwYmQ2OGYxNGNjMDEiLCJzY29wZWRLZXlTZWNyZXQiOiJlMDMxNTQ3YWQwZjg3N2M2NTljZDJkYjdjMWQ1YzliNDJkYWQ1MDRiZDVmYmU5OTZkNzI2Mjk4YzIyYjcxMjNiIiwiZXhwIjoxNzgyNTMyMTA2fQ.UHQqS1s-uU79KSn-4-wnZ_7NQ-t7yz09Q3TdDmy9hoo"

	try {
		const formData = new FormData();

		const blob = new Blob([json_string]);
		const file = new File([blob], "testing.json", { type: "application/json" });

		formData.append("file", file);

		formData.append("network", "public");

		const request = await fetch("https://uploads.pinata.cloud/v3/files", {
			method: "POST",
			headers: {
				Authorization: `Bearer ${jwt}`,
			},
			body: formData,
		});
		const response = await request.json();
		return response.id
	} catch (error) {
		console.log(error);
	}

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	try {
		const payload = json.stringify({
			url: "https://example.mypinata.cloud/files/" + cid,
			expires: 500000,
			method: "GET"
		})

		const request = await fetch(
			"https://api.pinata.cloud/v3/files/download_link",
		{
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				Authorization: `Bearer ${jwt}`,
			},
			body: payload
		});
		const data = await request.json();
		assert isinstance(data,dict), f"get_from_ipfs should return a dict"
		return data
	} catch (error) {
		console.log(error);
	}
