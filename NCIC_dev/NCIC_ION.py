def ncio():
	import urllib.request;import urllib.error as uer;import json;
	access = True;
	try:
		res = urllib.request.urlopen('https://nghichcode.com/status.json'); res_body = res.read();
		try:
			rj = json.loads(res_body.decode("utf-8")); access = (rj['status'] != "deny");
		except (ValueError): print("V-Error --- ")
	except (uer.HTTPError, uer.URLError): print("U-Error --- ")
	return access
