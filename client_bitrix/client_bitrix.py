import requests
import json

class Bitrix24:
	headers = {
		"Content-Type": "application/json",
		"Accept": "application/json"
		}

	def __init__(self, domain="b24-0p69tp.bitrix24.ru", webhook="ipyqiuokoygxp8cs", user_id='1'):
		''' parmas: 
				domain - company.bitrix24.ua
				webhook - webhook
				user_id - user_id is id user with webhook
		'''
		self.user_id = user_id
		self.webhook = webhook
		self.domain = domain

	def _call_method(self, method_name, method="GET", data=None,params=None):
		url = f"https://{self.domain}/rest/{self.user_id}/{self.webhook}/{method_name}/" 
		if method=="GET":
			responce = requests.get(url,params=params,data=data)
		else:
			responce = requests.post(url, params=params,json=data)
		return responce


	def get_me(self):
		r = self._call_method("profile")
		try:
			return r.json()
		except Exception as e:
			print("Error: get_me. {}".format(e))

	def im_notify(self, to, message):
		r = self._call_method("im.notify",params={"to":to,"message":message})
		try:
			return r.json() 
		except Exception as e:
			print("Error: im_notify. {}".format(e))

	def log_blogpost_add(self, title, message, DEST=['SG1', 'U2']):
		r = self._call_method(
			"log.blogpost.add.json",
			params={"POST_TITLE": title, "POST_MESSAGE": message}
			)
		try:
			return r.json() 
		except Exception as e:
			print("Error: blogpost_add. {}".format(e))

	def get_users(self):
		#  data={"FILTER":{"USER_TYPE":"employee","ACTIVE":1}}
		#  data={"FILTER":{"USER_TYPE":"employee","ACTIVE":1}}
		responce = self._call_method("user.get", method="POST")
		try:
			data = responce.json()
			if 50 < int(data['total']):
				result = data["result"]
				l = int(data['total'] / 50) + 1
				for i in range(1,l):
					result+=self._call_method("user.get", method="POST",params={"start":50*i}).json()["result"]	
				return result
			else:
				return data['result']
		except Exception as e:
			print("Error: get_users {}".format(e))