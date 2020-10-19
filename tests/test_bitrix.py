import pytest
from client_bitrix import Bitrix24


@pytest.mark.parametrize("domain, webhook, user_id", (("b24-0p69tp.bitrix24.ru", "ipyqiuokoygxp8cs", '1'),))
class TestClient:

	# def test_blogpost(self,domain, webhook, user_id):
	# 	client = Bitrix24(domain, webhook, user_id)
	# 	data = client.log_blogpost_add("Title","Hello World!")
	# 	print(data)
	# 	assert data['result'] != False

	# def test_create_client(self,domain, webhook, user_id):
	# 	client = Bitrix24(domain, webhook, user_id)
	# 	data = client.get_me()
	# 	print(data)
	# 	assert data["result"]["NAME"] == "James"

	# def test_im_notify(self,domain, webhook, user_id):
	# 	client = Bitrix24(domain, webhook, user_id)
	# 	data = client.im_notify("1","Купи слона") 
	# 	print(data)
	# 	assert data['result'] != False

	def test_get_users(self,domain, webhook, user_id):
		import json
		client = Bitrix24(domain, webhook, user_id)
		data = client.get_users() 
		# for item in data:
			# print(item)
		print(json.dumps(data, indent=2))
		assert data[0]['ACTIVE'] == True





