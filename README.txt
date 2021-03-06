# Bitrix client
Description
Bitrix24 REST API wrapper

Is a client for working with bitrix24 rest.

Bitrix24 API documentation - English: https://training.bitrix24.com/rest_help/
Bitrix24 API documentation - Russian: http://dev.1c-bitrix.ru/rest_help/

### How to install
1.  You need to download the repository `git clone https://github.com/DImasBo/bitrix24-rest`
2.  Go to the repository `cd bitrix24-rest`
3.  You need to install `python setup.py install`
### Methods
The following methods are implemented here:
  - get_me() -Allows to return basic Information about the current user . More for Method **profile**.  more https://training.bitrix24.com/rest_help/general/profile.php
  - get_users() - This method will return all users, except: bots, users for e-mail and users for Open Channels. More for Method **user.get** https://training.bitrix24.com/rest_help/users/user_get.php
  - im_notify(to, message) - sending Notifies the specified user. more for Method **im.notify**  https://training.bitrix24.com/rest_help/im/im_notify.php
  - log_blogpost_add(title, message) - Adds a record to the Activity Stream on behalf of the current user. More for Method **log.blogpost.add.json** https://training.bitrix24.com/rest_help/im/im_notify.php

### Tuttorial
```
from client_bitrix import Bitrix24
client = Bitrix24("domain", "webhook", "user_id")
data = client.get_me()
print(data)
# output
#{'result': {'ID': '1', 'ADMIN': True, 'NAME': 'Test', 'LAST_NAME': 'Last', 'PERSONAL_GENDER': '', 'TIME_ZONE': '', 'TIME_ZONE_OFFSET': 10800}, 'time': {'start': 1602087129.169014, 'finish': 1602087129.207644, 'duration': 0.038630008697509766, 'processing': 0.004441022872924805, 'date_start': '2020-10-07T19:12:09+03:00', 'date_finish': '2020-10-07T19:12:09+03:00'}}
#
```
