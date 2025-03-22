
import json
import string
from curl_cffi import requests as requests_cffi
import random
import time
import re
from urllib.parse import unquote , quote


usernames_list = open('usernames.txt').readlines()
name1 = random.choice(usernames_list).strip('\n').lower()
name2 = random.choice(usernames_list).strip('\n').lower()

first_name = name1
last_name = name2
#username = 'sarkpamaria394'
password = "".join(random.sample(string.ascii_letters + string.digits , random.randint(8, 12)))




http_proxy = f"7ce84db36fdaa1799353__cr.us;sessttl.4;sessid.hghghg{random.randint(111111111111, 999999999999)}:f13be73436075d6f@gw.dataimpulse.com:10000"

byear = random.randint(1990, 1999)
bmonth = random.randint(1, 12)
bday = random.randint(1, 12)
reqid = str(random.randint(11111, 99999))
reqid2 = str(random.randint(11111, 99999))




headers = {
    'Host': 'accounts.google.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'navigate',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Dest': 'document',
}

accounts_google = requests_cffi.get('https://accounts.google.com/', headers=headers, allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")

h_gapz = re.findall('__Host-GAPS=(.*?)\;', accounts_google.headers['set-cookie'])[0]

constant_char1 = '102195078,102570576' # search again for this
timestamp1 = int(time.time()*1000) #1739774182609 # search again for this


cookies = {
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'navigate',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Dest': 'document',
    # 'Cookie': '__Host-GAPS=1:MlvfXMDgHqaFYvMZWSpkmZUdBHF2vA:fctVDK_L5oUiYJGd',
}

params = {
    'passive': '1209600',
    'continue': 'https://accounts.google.com/',
    'followup': 'https://accounts.google.com/',
}

service_login = requests_cffi.get('https://accounts.google.com/ServiceLogin', params=params, cookies=cookies, headers=headers,allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")
ifkv_service_login = re.findall('ifkv\=(.*?)$', service_login.headers['Location'])[0]


cookies = {
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'navigate',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Dest': 'document',
    # 'Cookie': '__Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

interactive_login = requests_cffi.get(
    f'https://accounts.google.com/InteractiveLogin?continue=https://accounts.google.com/&followup=https://accounts.google.com/&passive=1209600&ifkv={ifkv_service_login}',
    cookies=cookies,
    headers=headers,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



ifkv_interactive_login = re.findall('ifkv\=(.*?)\&', interactive_login.headers['Location'])[0]
passive_interactive_login = re.findall('passive\=(.*?)\&', interactive_login.headers['Location'])[0]
dsh_interactive_login = re.findall('dsh\=(.*?)\&', interactive_login.headers['Location'])[0]

cookies = {
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'navigate',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Dest': 'document',
    # 'Cookie': '__Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'continue': 'https://accounts.google.com/',
    'followup': 'https://accounts.google.com/',
    'ifkv': ifkv_interactive_login,
    'passive': passive_interactive_login,
    'flowName': 'GlifWebSignIn',
    'flowEntry': 'ServiceLogin',
    'dsh': unquote(dsh_interactive_login),
    'ddm': '1',
}

response = requests_cffi.get(
    'https://accounts.google.com/v3/signin/identifier',
    params=params,
    cookies=cookies,
    headers=headers,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")


cfb2h = re.findall('cfb2h\"\:\"(.*?)\"', response.text)[0]
fdrfje0 = re.findall('FdrFJe\"\:\"(.*?)\"', response.text)[0]
sNlM0e0 = re.findall('SNlM0e\"\:\"(.*?)\"', response.text)[0]

'''
tl_gb = re.findall('TL=(.*?)$', create_personal_use.headers["Location"])[0]
fdrfje = re.findall('FdrFJe\"\:\"(.*?)\"', redirect_to_get_tl.text)[0]
snlm0e = re.findall('SNlM0e\"\:\"(.*?)\"', redirect_to_get_tl.text)[0]
bl_find = re.findall('cfb2h\"\:\"(.*?)\"', redirect_to_get_tl.text)[0]

headers = {
    'Host': 'play.google.com',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Sec-Fetch-Mode': 'no-cors',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://accounts.google.com',
    # 'Content-Length': '466',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
}

params = {
    'hasfast': 'true',
    'authuser': '0',
    'format': 'json',
}

data = f'[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en-US",null,"45",null,null,[3,0]]],1828,[["1739774182609",null,null,null,null,null,null,"[[[\\"/client_streamz/bg/ec\\",null,[\\"en\\",\\"mk\\"],[[[[\\"t\\"],[\\"_\\"]],[1]]]],[\\"/client_streamz/bg/el\\",null,[\\"en\\",\\"rk\\",\\"mk\\"],[[[[\\"t\\"],[\\"\\"],[\\"_\\"]],[null,468]]]]]]",null,null,null,null,null,null,-12600,[null,null,null,"[null,null,[102195078,102570576]]"],null,null,null,null,1]],"1739774182609"]'

playgoogle_step1_1 = requests_cffi.post('https://play.google.com/log', params=params, headers=headers, data=data, allow_redirects=False, allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")

cookies = {
    'NID': '521=VFXTyK7JKrh-rKMTUHTmB8TQQ0NfL4aNWpOwoinwAr-QTndNuY57NJTn-CZPISV1Q-B74gsWort2CkTf2rVDwRew2oL7cj5vHfpAjLDXSSt5xJPz-73gIgcX_0mUqggTJ5sQ-SjwCI4ugQ08gRpuszWyVUHrQyI7eHlJk5FLL7TLbvEO6W6MI66ARcmGgGLRww',
}

headers = {
    'Host': 'play.google.com',
    'Content-Type': 'application/binary',
    'Accept': '*/*',
    'Content-Encoding': 'gzip',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Goog-Authuser': '0',
    'Origin': 'https://accounts.google.com',
    # 'Content-Length': '248',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': 'NID=521=VFXTyK7JKrh-rKMTUHTmB8TQQ0NfL4aNWpOwoinwAr-QTndNuY57NJTn-CZPISV1Q-B74gsWort2CkTf2rVDwRew2oL7cj5vHfpAjLDXSSt5xJPz-73gIgcX_0mUqggTJ5sQ-SjwCI4ugQ08gRpuszWyVUHrQyI7eHlJk5FLL7TLbvEO6W6MI66ARcmGgGLRww',
}

params = {
    'format': 'json',
    'hasfast': 'true',
    'authuser': '0',
}

data = '[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en-US",null,null,null,null,[4,0]]],558,[["1739776133000",null,null,null,null,null,null,"[[null,[1,\"accounts.google.com/v3/signin/identifier\",null,[\"\"],0]],\"-1225847987790032166\",3,[null,\"S1008237727:1739776129537314\"]]",null,null,null,null,null,null,-12600,null,null,null,null,null,1],["1739776133000",null,null,null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,\"accounts.google.com/v3/signin/identifier\"]],\"-1225847987790032166\",3,[null,\"S1008237727:1739776129537314\"]]",null,null,null,null,null,null,-12600,null,null,null,null,null,2],["1739776133001",null,null,null,null,null,null,"[[[79,54005,null,null,null,null,null,null,null,null,null,null,\"accounts.google.com/v3/signin/identifier\"]],\"-1225847987790032166\",3,[null,\"S1008237727:1739776129537314\"]]",null,null,null,null,null,null,-12600,null,null,null,null,null,3]],"1739776143105",null,null,null,null,null,null,null,null,null,null,null,null,null,[[null,[null,null,null,null,null,null,null,null,null,null,null,null,128566913]],9]]'

playgoogle_step1_2 = requests_cffi.post('https://play.google.com/log', params=params, cookies=cookies, headers=headers, data=data, allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")

'''

#tlrq=to(http_proxy, h_gapz)
#aswp=tlrq[0]



cookies = {
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '164',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
    # 'Cookie': '__Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'rpcids': 'UEkKwb',
    'source-path': '/v3/signin/identifier',
    'f.sid': fdrfje0,
    'bl': cfb2h,
    'hl': 'en-US',
    '_reqid': reqid2,
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22UEkKwb%22%2C%22%5B%5C%22{dsh_interactive_login}%5C%22%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={quote(sNlM0e0)}&'

response = requests_cffi.post(
    'https://accounts.google.com/v3/signin/_/AccountsSignInUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



cookies = {
    #'NID': '521=VFXTyK7JKrh-rKMTUHTmB8TQQ0NfL4aNWpOwoinwAr-QTndNuY57NJTn-CZPISV1Q-B74gsWort2CkTf2rVDwRew2oL7cj5vHfpAjLDXSSt5xJPz-73gIgcX_0mUqggTJ5sQ-SjwCI4ugQ08gRpuszWyVUHrQyI7eHlJk5FLL7TLbvEO6W6MI66ARcmGgGLRww',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    # 'Content-Length': '166',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': 'NID=521=VFXTyK7JKrh-rKMTUHTmB8TQQ0NfL4aNWpOwoinwAr-QTndNuY57NJTn-CZPISV1Q-B74gsWort2CkTf2rVDwRew2oL7cj5vHfpAjLDXSSt5xJPz-73gIgcX_0mUqggTJ5sQ-SjwCI4ugQ08gRpuszWyVUHrQyI7eHlJk5FLL7TLbvEO6W6MI66ARcmGgGLRww; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'f.sid': fdrfje0,
    'bl': cfb2h,
    'hl': 'en-US',
    '_reqid': '13'+reqid2,
    'rt': 'j',
}

data = f'f.req=%5B9%2C1%2C2%2C%5Bnull%2C1964%2C3024%5D%2C%5Bnull%2C795%2C1512%5D%2C%5B0%2C0%2Cnull%2C1%5D%2C%5B1%2C2%2C1%5D%5D&at={quote(sNlM0e0)}&'

response = requests_cffi.post(
    'https://accounts.google.com/v3/signin/_/AccountsSignInUi/browserinfo',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

    #f'https://accounts.google.com/lifecycle/steps/signup/name?continue=https://accounts.google.com/&ddm=1&dsh={unquote(dsh_interactive_login)}&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://accounts.google.com/&ifkv={ifkv_interactive_login}',
print('create personal account...')
create_personal_use = requests_cffi.get(
    f'https://accounts.google.com/lifecycle/flows/signup?biz=false&continue=https%3A%2F%2Faccounts.google.com%2F&ddm=1&dsh={unquote(dsh_interactive_login)}&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv={ifkv_interactive_login}',
    cookies=cookies,headers=headers,allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")

redirect_to_get_tl = requests_cffi.get(
    create_personal_use.headers["Location"],
    cookies=cookies,headers=headers,allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



tl_gb = re.findall('TL=(.*?)$', create_personal_use.headers["Location"])[0]
fdrfje = re.findall('FdrFJe\"\:\"(.*?)\"', redirect_to_get_tl.text)[0]
snlm0e = re.findall('SNlM0e\"\:\"(.*?)\"', redirect_to_get_tl.text)[0]
bl_find = re.findall('cfb2h\"\:\"(.*?)\"', redirect_to_get_tl.text)[0]



cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '231',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'rpcids': 'MjyMj',
    'source-path': '/lifecycle/steps/signup/name',
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': reqid,
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22MjyMj%22%2C%22%5B0%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C1%2C1%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={quote(snlm0e)}&'

response = requests_cffi.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")


cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    # 'Content-Length': '166',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '1'+reqid,
    'rt': 'j',
}

data = f'f.req=%5B9%2C1%2C2%2C%5Bnull%2C1964%2C3024%5D%2C%5Bnull%2C795%2C1512%5D%2C%5B0%2C0%2Cnull%2C1%5D%2C%5B1%2C2%2C1%5D%5D&at={quote(snlm0e)}&'

response = requests_cffi.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/browserinfo',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '201',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
}



params = {
    'rpcids': 'E815hb', #hardcoded , constant , available in https://www.gstatic.com/_/mss/boq-account-creation-evolution/_/js/k=boq-account-creation-evolution.AccountLifecyclePlatformSignupUi.en_US
    'source-path': '/lifecycle/steps/signup/name',
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '2'+reqid,
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{first_name}%5C%22%2C%5C%22{last_name}%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={quote(snlm0e)}&'

time.sleep(6)
print(f'filling firstname lastname {first_name} {last_name}...')
firstname_lastname = requests_cffi.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")

if 'birthdaygender' in firstname_lastname.text :
    pass
else :
    print(f'not birthdaygender in response , \n{firstname_lastname.text}')
    time.sleep(8888899)



cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '116',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'rpcids': 'ink9M',
    'source-path': '/lifecycle/steps/signup/birthdaygender',
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '3'+reqid,
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22ink9M%22%2C%22%5B%5D%22%2Cnull%2C%221%22%5D%5D%5D&at={quote(snlm0e)}&'

response = requests_cffi.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '5094',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
}

params = {
    'rpcids': 'eOY7Bb',
    'source-path': '/lifecycle/steps/signup/birthdaygender',
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '4'+reqid,
    'rt': 'c',
}

rand_str_long = "".join(random.sample(string.ascii_letters + string.digits , random.randint(30, 30)))
rand_str_long2 = "".join(random.sample(string.ascii_letters + string.digits , random.randint(30, 30)))
data = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{byear}%2C{bmonth}%2C{bday}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sC{rand_str_long}k81W6Ra0WdEYf-gR1s3oZe-nhWFVD5TqNRC5aOGB_38Jm6uIEwtQGFDokUNc6e3yVWtTg3WqYyMaBoK4W4WOVCNASaRYvtBA0VvEkimtcWcSA0j6WfqG_crAEVseyfYj_QYG3YY23N5FeE99ghrGRpt3G2rzL4X6cetyceCMtarKGW5CMWTgaaeqAG_DcdOoSIlJ5A4PMdf_7iFrCfoIN4tidCjimOQbLi5To62mQkKPRJbn_W-v8UhNQxQHUiJQ--IBiGDCcp9ASz8EfL6SMeizW9681FIhOX16FaoXsGBDqHJKSuZjete_HkhkayO8ttFPzDDhGm-EmJQMOJ6wvc88_1j_1JCq8jX4t9tCi7WtnmRpxKgMVPrAUUqV6_TQW_4liOe9q_VME9x-n5Rzpv6W6kpe_fpdftmYC5czGbHwkXanQ6gjPCpxp5mPG_XtavZUvKlUeduEvqMFURCuN5KQ-F_lzwPvpIK8xzzBhc%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Faccounts.google.com%2F%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={quote(snlm0e)}&'
#data = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{byear}%2C{bmonth}%2C{bday}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3CkFxqXAQCAAa0zFp7lMyNrABWwydLi2L0ADQBEArZ1Dft7usA0dhAbojDxTvN7V0t95gLtrImVlZyxMg575ohNZezZ438w_KJ3yR47BlJzQAAAHOdAAAADKcBB7EAS9xrLRbuVfL-gyarKUfx2ZaEGLQ3rU-FbA8l4iKW-UUDksz9hjBu61YDo0KsGEM5pAPE-paa9Ym3aXEHhQIDmv9qbh-e25reMtZtRlYMVHkq-lKJLS21D1l_OQKKx6USFAundFublgPyotTGBa-J47dkk451gVW5Igs2gvVrQqSbBr5wtVelJqTMdAc9fsgj73nqsBzBaNh4xN5DN5NKEajmJy4b8GADaaWACePShKCKc2PzFnW1RGiduai2CKaDcynS07LPAjGIOzVk8MK2NLQfQMSB5oaD_oM3roVXDLrFoM7cIOe3FhY-SsN8C9YWhKLqTRNyOnK8qiEwpR0V5MsaTVBSUUJyPpw_O7MK88XPHRVbf7duHsqT3XL9tEA-4QzCjI02wUlbk1Wl_B-_qYFfp6Tsi9RdAFQjUz7thjSRBwXTT2fgzOy7Npr_zf5QEkBe8bTgmbgrujJHQLr4lYCbNFcDmq9lt627Z4vvDO5SwP4vDWi65EYyWdm4zSdiLKzUslzCrC3uvz8mhjTPcLYMAHire2Nf5SknJ_l7O1ChrWpSpgZXVGCN_vnxCYXLjclpYF0VvMOg9FO-8mtljcM7e0VPJbozykXt75BQal9BfkyqbXVuQzUY2scgz5jjJ_r-nk6JHVlk-LlV5VDycpEDqX4bnhyj1Z4QvRnBxg2Cm56RlASZZp_GxbFep-lNG3-RBgWnlmjLhD_Li0VWiZXSfmxLPJUcMCLEWLVtBfp7cpF0solegMLtNkvvUVPdF2fZYwehrg52HXNCMxGTkm2V4015Ahakewtb28oVDTmieZ7gTlToggr4pcuKqvKwM8DIMQMsK7bKa50xVUKUzY77vW_miRZ0niA-dRGUnsOg2auG5QAjhLbVI4VEkVoZpC3WIUzzhd6zAbZMvt3rfh8mCjMxdFf2LPRtN-yCHaYBLZ0g_ZTFO7YoKZ5aZd81pyX_MNk8Rujfg3X9W6eKbR7pfFw5JJ908XcNttozF8CM_VQKMUFxIEy-wahU2ugdaAbLUhp4DhSV3fXHu-EgUfZqQG5muqcZ9m_QLzIiRal_qQRwm5qV8m3DabJZ2SA1Tx15XK31MY9rJMcPkqXzMn7C0DvgoHdInT42yZkQ2RptRgCHI_pu7tjo1uONWKnnKTDWpzpfqwqRhTBqw3LjoVqSeo-WptKpFxWDkX8bmr4Myqclq3w-SK0nX50UUSJtEXmIubwnqzb9tedW1ixGAsmYmj4uaRZU6LiPpTEWqXG5b8EGUMRYoC8KBfNoZ1DKea2qCNDLMy1dOUrj4OzCOUoywQEAt01Jzv8XJwPSJwRSnDAlGLRorhg1Saq_2YkuLrnRS8GIvYa3NNvCmRg_dr1zrhnW8mkk63DUdSwqU_rYKr9Ht5os7GTmAxK7H9ED2KGMNpC1lHZBffQAZa6bZ9Y_UAlm1SgxggYQPJoedXGOXDpbKG5rt5X4n2hBZ9cPssPLqqdZcmFzFUt5ThopipJcffhxAKG8XpOJVN7lT-YokK9_f7Xoq13VNxjFDKRsnw83RbbuQwExn19tm4_SLXZ3mVqTwLwWAxm1o5vY8mcPVzixbk1sHIc9cTy8KKftHXwV18g8WJclzZFDDxN1k9baLo5JVKz57VRh33AvI4Ez-HFTA4qZXxthNvYtZveqqqZAQ2EVIuGRWuMKHPCZ1ueD8pPy40jnzdjLPt2xV_5ofmQYVoBrBmv9UM6oiBPV254GWiReHp6vcx5spp6Z5yp72M23CZ0R3KkD2wdJdSDWn1NVhIN6MZdaJFR0lTcchrKvQnEJ-OZP96Rbxmp8zuDJnYO66xNqIvTkOtz__6DOXKu5wZK6OYMthCD48qVM78ZIlnRAZy7vleu8VaKBxPak-IzcznHVy7rHEgIYqSipPMXybMZDq0De9VUzVhiNZPy8a6a77MSqDUKOJ8kPyBAtuy1LDip9LxZiV3JHtkcEhtzcNfH0M_LuYye2FxTohll0h6TQz08ffuITlBxDmrveMgvKXDitXvJToxDWObqeOs8Dy19XQKHoW48wKmrmO5ih9_SfZAgZxzzz0ecjABRGwUVsuzutoPlpw4q4v4Qr7RuI8BDfGXA28c3pMEMdRl_o00FKv9cwEyXsKKUf9rbPa36b7pwo0p3kYIgxit94fUKJIroDkqRWevZGqBk3FWS-jEWaMiHtBN32cQ9-91yV5hLxt8M-Aq2tTkMRRZDs20LC31M7T6QAM2tO3siwy7eG8tGabut5GX2n6L5kYONBWEyE4j4Bp-_jHBPLs_dypcjjHh5FUXkZKwegyBVyiGeJD3DWQo8fzxWamzuIVG_NW5wMFRrVuFjyZ2A0Odyp0ENBPTfY6JvKDTII5_E7vgnjSxU4kmnUjTXEh7e0Gncdpg9jqcrucnQ7vD9--ZKMAbSFBcGVH6CinWbVD5BXYVmdzwzSVnpbEQjhJpgfKUglj4JxFUlEKGWl4ajU26Ulyi73iZxPmKwA_wyZYOq_C3L36LWCJXzu_eC0CijF_CeYhOJdB5bGgBEHiNhgynGPiFRoR289ILIiYNepSaLt73P8utCTB3KXb1e-RZWNOiIm4fLiDt4gy70HrppIIcbdAUn3XZGJriucISXgnJkvuvcHgKKTvspdPjxGDEsL2DmAF2W-GOcptBpyX0UUtTsvSdek5jZB-FiZusF7U200WGb5vv3mc30o09QbtylU8lSf8n9dOdgKwS2w4zO6mm_oFyfse2x-kERm_k09SR-TxCUIXsZqFLeIV8p6tw51eKY0GmuZC3QjebHLoBOgZyrqqbeQnt7DxdbvA2MsHdGVX7xa3ldQ3TOADC5-2fTXHciwEm41fc5F5KBxHF-z4NHX-M4iwKVYrabYAB4aDw4DOPY1a_vZV4MdB0kN_1WTCDddp2qgUb36hkbjh0Pf92gdRpbKrcJJkezG2bTDmxW60w1RdWDtdsiWpVycydkiiGdviiGWeo1r1vkazjvZ_K90mK8tJLuHLrkLOBM1hEl_-ISkv4NFEXe-EOSQrKjJRZizzjizyH8J9j0sG-_U80vRbhWEGJvTtrcXxCXLaMvG0CfGK30FDA4mDHZ1e8Au-l3HPIGXz76l39e3hFha_PmSXMxk52yFWT2A-Viqo7viiMkaZPzBi--7dMa9AK6unyEXP77H-pIeifPpV8BGUm74k7kzYT5LqMuFD6UlrPW3GkSLl73epKRzGyk5uVXqU_qmXmg0067aFPm_5CVHvBilt_S7Dxln60UNUSh70VtiodFA39b8lRPdo_SS37omjFncsO_4eg7UNB4eLstqHTWFwfSBGC2eCOaqR9mBAIQabvpMNBhGigrxAZZMHeNQrC5IC44tEjbECbIYUerMc3gq-pBZE-UxzrKv1t69lKwNUoa3B6MR9xwK7t5EJwIRgCHpUhzX2IUIClyE2FVy0jiX_I-EDxb9WQCyuzomyXNawkPpqCJQzCVgj41ba3SRsMW_jvqrtDGjAYKXBBiZQ1IMnWBJ0gHxWpBTFoLE6YKEL56qgXssekhFaeGgfbUjcBjNmg03BZ2cA0ixP6Iiu4pYpUafeiJRuW9f04VqPfpSpG2HKiMFqG4ZbvrhXcpxLbdi_v_eLmJugTe9btwzDqTaltFzlYWABrijsRfMbhuT0M5xgzmJOWhD1bHjrkAfmIo4Y51b4nUC48EJ7A2EL5-MxYaAaAUCf3YRItvKFR-a7bWRVAJ1CC2aPdM75GBOwoSbsgoZvc_scFV7WNtlqihChOnaWMg2MjA7KpTCrR7r8sgEFIZ4qJjs8FzKDCk_18uVwxttXU3HE3eUGj619D6FVZUYLSLyJg0aFYrKR00LntUeXV21g_Qy2yLxJnDRK2ZoVCqKVH8tt9xtXBz6vw0wionCtBBl1qaB9E3fulgTubv45SyUE9M5tOSLg1moV3-EcShyztl1h8pXZPRIH5dxcl2TM5zJKlrJPW_Fj4WPKubk-fym-Oadx9cm07HAIsFuiehptdXnyCv3lNUvbZe4jEfeyCg1OzpIrSRy4N559vvDQOm4vMhO9AMcAqOizFDGUt0GJGDVh9m6pGiQXa_ktTWmQeo4lbnaNEF9HulP0ck_piwptacmYgcF8kUvTI_pO0NKy_XsJpakTNGb4VOacSrxnwhHfTV6ON8Js86X0awhmc-w6VfTAbdfKE_d6UPPgya0JLUtBCRzQKPWB8rWq7ARGtUMHdxzzst7glnHAVvgJO49RGox6DAxcV1IWAuxvn8ZVNHh8xhf0QWNHuXLOdzOFJtGBHHhasVk5rhnkdomXBV3bvP7DANrHYhUmo4Y4g%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Faccounts.google.com%2F%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={quote(snlm0e)}&'

time.sleep(7)
print('filling birthday and gender...')
birthday_and_gender = requests_cffi.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '118',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'rpcids': 'xdYwpe',
    'source-path': '/lifecycle/steps/signup/username',
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '5'+reqid,
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22xdYwpe%22%2C%22%5B1%5D%22%2Cnull%2C%221%22%5D%5D%5D&at={quote(snlm0e)}&'

auto_suggest_addresses = requests_cffi.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")
try :
    print(re.findall('xdYwpe\"\,\"(\[.*\])\"', auto_suggest_addresses.text)[0])
    username = json.loads(re.findall('xdYwpe\"\,\"(\[.*\])\"', auto_suggest_addresses.text)[0].replace('\\',''))[0][0]
    print('\nsuggested username by gmail api : '+username)
    print(f'password : {password}')
except:
    import pdb; pdb.set_trace()




cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    # 'Content-Length': '166',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '6'+reqid,
    'rt': 'j',
}

data = f'f.req=%5B9%2C1%2C2%2C%5Bnull%2C1964%2C3024%5D%2C%5Bnull%2C795%2C1512%5D%2C%5B0%2C0%2Cnull%2C1%5D%2C%5B1%2C2%2C1%5D%5D&at={quote(snlm0e)}&'

response = requests_cffi.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/browserinfo',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")




cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '215',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'rpcids': 'NHJMOd',
    'source-path': '/lifecycle/steps/signup/username',
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '7'+reqid,
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{username}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C21684%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={quote(snlm0e)}&'
time.sleep(6)
print(f'submit gmail address {username} ...')
choose_address = requests_cffi.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',params=params,cookies=cookies,headers=headers,data=data,allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '227',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'rpcids': 'dOJftd',
    'source-path': '/lifecycle/steps/signup/password',
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '8'+reqid,
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22dOJftd%22%2C%22%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Faccounts.google.com%2F%5C%22%5D%5D%22%2Cnull%2C%221%22%5D%5D%5D&at={quote(snlm0e)}&'

response = requests_cffi.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



cookies = {
    #'NID': '521=H3D1MwH41NNezBEcrErXBaHx295Wzf30Ugg0fm8GCGAnHeyKq9IjSUOvGG0hpTQQeCC2Sjarp7wC0HaEyditV8rAeJWTV-CVbM0L_9joFL1Q2d-KpmqGs4iUqqeKoxdy5ShuRd9jBGKXzK3XIxwoGFojI05nldh8-LpXg8tQ4ZtZ8XW0NXmpvEbzugA3QwTsaOo2gKgB',
    #'OTZ': '7959396_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Accept': 'image/webp,image/avif,image/jxl,image/heic,image/heic-sequence,video/*;q=0.8,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Dest': 'image',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Mode': 'no-cors',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Cookie': 'NID=521=H3D1MwH41NNezBEcrErXBaHx295Wzf30Ugg0fm8GCGAnHeyKq9IjSUOvGG0hpTQQeCC2Sjarp7wC0HaEyditV8rAeJWTV-CVbM0L_9joFL1Q2d-KpmqGs4iUqqeKoxdy5ShuRd9jBGKXzK3XIxwoGFojI05nldh8-LpXg8tQ4ZtZ8XW0NXmpvEbzugA3QwTsaOo2gKgB; OTZ=7959396_42_42_114990_38_379890; __Host-GAPS=1:KT1EM6_iB3L6hwCy6I3p1ilRIycR-w:kRQq-X4Ea4PSEwTr',
}

params = {
    'tmambps': f'0.0000{random.randint(1111111111111111,9999999999999999)}',
    'rtembps': '-1',
    'rttms': f'86.{random.randint(11111111,99999999)}999999',
}

response = requests_cffi.get(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/gen204/',
    params=params,
    cookies=cookies,
    headers=headers,
    allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")



cookies = {
    #'NID': '521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA',
    #'OTZ': '7957836_42_42_114990_38_379890',
    '__Host-GAPS': h_gapz,
}

headers = {
    'Host': 'accounts.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Sec-Fetch-Dest': 'empty',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'X-Same-Domain': '1',
    'Origin': 'https://accounts.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',
    'Referer': 'https://accounts.google.com/',
    # 'Content-Length': '6021',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'X-Goog-Ext-391502476-Jspb': f'["{unquote(dsh_interactive_login)}",null,null,"{ifkv_interactive_login}"]',
    # 'Cookie': 'NID=521=O_ExhobbeRGhDOm9Qg11gS1BeTq0YtDULmL98-UewHxqk01KLrGndh0L1DuD0KKZS1ZZjzw28dQj3xMgGkwvyL9LsHJUJX9If0p1GIQRjlsNm9r3QvALJiSjT5OgRkeEfJQ_UBolb5DDkekhJ8g-OZPvu6Yq5aBGmEja_vbV1qLZ_ENqG9fXHhpaygqD5iSHewHBLqMduA; OTZ=7957836_42_42_114990_38_379890; __Host-GAPS=1:PUl9rtoxX-5saSaVY_UdlnOZWIP5IQ:YAaDjK_JBmOtQbVA',
}

params = {
    'rpcids': 'ZNd7Td',
    'source-path': '/lifecycle/steps/signup/password',
    'f.sid': str(fdrfje),
    'bl': bl_find,
    'hl': 'en-US',
    'TL': tl_gb,
    '_reqid': '9'+reqid,
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22ZNd7Td%22%2C%22%5B%5C%22{password}%5C%22%2C%5B%5C%22%3CWpZqls4CAAYBzfNKIc2N9JJZvr8d_yr0ADQBEArZ1PrTYg3iH{rand_str_long2}2Vi573vM2Y8x92PuThza4gQ%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={quote(snlm0e)}&'
#data = f'f.req=%5B%5B%5B%22ZNd7Td%22%2C%22%5B%5C%22quc-seJzav-2sivwy%5C%22%2C%5B%5C%22%3CB8tqy5MCAAa0zFp7lMyNrABWwydLi2L0ADQBEArZ1Dft7usA0dhAbojDxTvN7V0t95gLtrImVlZyxMg575ohNZezZ438w_KJ3yR47BlJzQAAAHOdAAAACacBB7EAS9xrLRbuVfL-gyarKUfx2ZaEGLQ3rU-FbA8l4iKW-UUDksz9hjBu61YDo0KsGEM5pAPE-paa9Ym3aXEHhQIDmv9qbh-e25reMtZtRlYQQHkq-lKJLS21D1l_OQKKx6USFAundFublgPyotTGBa-J47dkk451gVW5Igs2gvVrQqSbBr5wtVelJqTMdAc9fsgj73nqsBzBaNh4xN5DN5NKEajmJy4b8GADaaWACePShKCKc2PzFnW1RGiduai2CKaDcynS07LPAjGIOzVk8MK2NLQfQMSB5oaD_oM3roVXDLrFoM7cIOe3FhY-SsN8C9YWhKLqTRNyOnK8qiEwpR0V5MsaTVBSUUJyPpw_O7MK88XPHRVbf7duHsqT3XL9tEA-4QzCjI02wUlbk1Wl_B-_qYFfp6Tsi9RdAFQjUz7thjSRBwXTT2fgzOy7Npr_zf5QEkBe8bTgmbgrujJHQLr4lYCbNFcDmq9lt627Z4vvDO5SwP4vDWi65EYyWdm4zSdiLKzUslzCrC3uvz8mhjTPcLYMAHire2Nf5SknJ_l7O1ChrWpSpgZXVGCN_vnxCYXLjclpYF0VvMOg9FO-8mtljcM7e0VPJbozykXt75BQal9BfkyqbXVuQzUY2scgz5jjJ_r-nk6JHVlk-LlV5VDycpEDqX4bnhyj1Z4QvRnBxg2Cm56RlASZZp_GxbFep-lNG3-RBgWnlmjLhD_Li0VWiZXSfmxLPJUcMCLEWLVtBfp7cpF0solegMLtNkvvUVPdF2fZYwehrg52HXNCMxGTkm2V4015Ahakewtb28oVDTmieZ7gTlToggr4pcuKqvKwM8DIMQMsK7bKa50xVUKUzY77vW_miRZ0niA-dRGUnsOg2auG5QAjhLbVI4VEkVoZpC3WIUzzhd6zAbZMvt3rfh8mCjMxdFf2LPRtN-yCHaYBLZ0g_ZTFO7YoKZ5aZd81pyX_MNk8Rujfg3X9W6eKbR7pfFw5JJ908XcNttozF8CM_VQKMUFxIEy-wahU2ugdaAbLUhp4DhSV3fXHu-EgUfZqQG5muqcZ9m_QLzIiRal_qQRwm5qV8m3DabJZ2SA1Tx15XK31MY9rJMcPkqXzMn7C0DvgoHdInT42yZkQ2RptRgCHI_pu7tjo1uONWKnnKTDWpzpfqwqRhTBqw3LjoVqSeo-WptKpFxWDkX8bmr4Myqclq3w-SK0nX50UUSJtEXmIubwnqzb9tedW1ixGAsmYmj4uaRZU6LiPpTEWqXG5b8EGUMRYoC8KBfNoZ1DKea2qCNDLMy1dOUrj4OzCOUoywQEAt01Jzv8XJwPSJwRSnDAlGLRorhg1Saq_2YkuLrnRS8GIvYa3NNvCmRg_dr1zrhnW8mkk63DUdSwqU_rYKr9Ht5os7GTmAxK7H9ED2KGMNpC1lHZBffQAZa6bZ9Y_UAlm1SgxggYQPJoedXGOXDpbKG5rt5X4n2hBZ9cPssPLqqdZcmFzFUt5ThopiTtcfe5QDIJj9CvEg5jShDokn09T9D_tDL-lrVp2Y3Hvv3PatPTAVSLSFixDpmknpW3NOeKpuSl3_Bjhfzr1cefk3l-EDW3oG6B9JoXNyadxDmEvFhwdRzKYNoHhEtEMU93U2Q8qO2cycYx_6Ec9bRbBsFJhMdAGsZJG68AUqYjw7iZlSOM1mn7xaqIjR-3hktlplj-zfrwkLKkIJxm77UBwxa8JP3KZmYSkvucbOd8KIty66xqy6Lj1H90MCUJhBagtiP6zwuXJUB2iBYcjjCppFdI6E-MqaiE63CuatQt5wE___Jv38i0bkSUsLppr8Z66FCMQpuJfQgT53gcM89MvWGr027jv-nkCWLDhnf3kMcV_eURfnw3Z47gx-GIoLnaktp41JY0IHazlOnGNfSuMaZXxZ-wvWgNQIWJfNKluK81-qY1D5nbaAKLNbMqExixAFb2_ia3VmCqTP0q4TmCjYtRFg28pS4Kd3Qp9Pez2zECzA9LjLOqbhA6FvzibqwokjttXVLHJ8TseFR4x2WX9QfKfiFamw9q2Cq-YaDJtvqDTWXheJlQ6cZbwjiv6rWeOi30PgtqVdCjfflGQ7MAXRpXad6124zeeRC94At6NBr3PjXCUpMZw2i3C2Rf08QFNbjQXSQP7pnGMcXd13FHfKT3rzP1y9BVOoKuypRiy4ejIXiiwfblLMbv_j6FAOwBXj7EGX3K4H6_inPC-poIqbFMJpuQ8KZRODHRPaLJ5gnQyfZkJvcw7l08dOj8UH_kAjtM1U0yEZsCj1jRS0hsZwnntnQaQamMEkBZ4yyF4zaxdYj7Ss8GoTZx12dBQ5brNvR4uGD65tD7P4sVqpUPvQ5LG5l_vuX3NJ6mGxJvKWFO_SsKDCk2SzyndF3NDrBsx-f7gR9t6vq91vgSubfwFH3BC_Kz2rcYIwaUe8715IBMNU8GexHKBQiVnNFTL5F576Dy9o-o9of2Y1sLV1Qmr7z4aMaC7fx3jcYsPG0FsgO-HY-Bwwesem5sZaNLtlUvMp2emkQOakrjDESNvHGJEFf4PnTvMMm2ZRTBohZcNP89DESklUQIeIqhyx5c3ZIKzxdOLXyI5UwGMRt03rYINrqFh2ajoDPWtz-DIFJenPYSlXatTnBB-pIOaYoBGng8BGEJTpM-pxyHxoMVEI5fwJR_ubw5mmWNreria8PpnH6vvmP0J454HvgoACyaYVyQubKQ8UQzPnZe7nL14pWLlwydFznmVnIvNdW3XtP1g75nZe9lUmAhz45M9J5el3ilrNYpbhaYHtma3BN3EAISDFfCEspfSMVe3pUGXQLQdDTaWNRyfraIK2CiRkHifVwgbwN4QGDtHJAo5Q3BTACJo-Yf3ZUWusQD85cc857VEPVNzK_2eu904J7RXZmT97tHItVFiTOPlRdk0D6lWLnL-2MU6MljIJE4NdkPGFGyHeCL4mWYQw93aZ0u-mfsDQw1v7WiPr8cOcJLqqAx5t9G86uWHlIyl163x8CGAeydHJj6q3vbFk8C15-t3XqTTtUkjkzncbixHurOzbiSJOtLTgbGhnLojCbJSSFiuItoFtNBsOi-QqqPHmdvhXA9uFLtpVaHc3mOs752VUUEkNRCEp0PU-Mkw7N1LOJnnQDUomULToEwpkfGlADIMNsnGNQWV2yetFz2xq0m7xtBNa-aPDAFekVIpA8CVvKAluaSW4L-bx4bGCvH7fz6pcs1p79EqbjTgLuVyykegEXkWfngy5GLGh4CWSkw32uJztLHHNxs9JYUE6BUsK_fX6ep7AJo3FfH86kqBcClsSrsannLivot_V1EOxk9DTFu_Dl2AKq7cThQG3J5TqCx7A7hGtNEBgB0rlEcJWNOXMRLBmSwXpt03ZDJBJVpbTufJvQ1NlYds26bIXbvtgoVg6fLrCK2PfLfQYMrng2XPxXY_CcyHgiLrv050qfltRmFjbyndJc1E2ccRjm-voJNhL5LoUyKEEYxCf5eKDK79tS6VQgEmRH7pMtgKdW-71OFz1RcbJcT8oys8L4zWaRRdXasToDl93nIBeH35BhMnaHpkHhZ0_kFGV-S4gQGJvKeg-dZsg8jdkKRhXFEkjZsQ28fsva70tqZbEoIA5mJteZc-iFq6qCnmqPDQQkcHWzX1PsavWpFRRKrMvOreIny_D6pLnZYFHcZCNlbJ79EKlUh5UwUWJQecUrl6nGGmc3cj8mH2coA2_ZATKfMwmaNRoAOlYLCJ29YMkt8JZOLUx4r59Fi9KgPzLga6zqqsWGViCbTqODcaxpro9cnSWUxgv_AwkiNfcBmHWA8OmmUaG3dQj4ih_LMipmsHCqX8jnwsgD1W50tOuBNYUpvfp-cWzMLB1o5awqroF9HHzcdwaEnFRtZxmvXxhi-t54syUBjhSnrBufSApSxzckQSRV80QxWtgbR-jLlel_kpxgKFRR79KBpbIkmyKSv-Zojw4L1ezJLjfyvxDwVm-Nd8kxqYsWuEg-EhNXOINxDWQPnFgntDFlV6VmeU8nYz-BDxwxm4q2dlYM_DqTWL_Qn5Rvl1Qdy2jzHFZIMnNraBSH7kmOWhbChExUpknIx3Bz466i1DyOhhooBPCXlCBMfYxg1TI-Zh4UVE4grsChaiD4_W6D-ZLOyPG3CRyGV-1HXVdQYJvTarUZ9a0wFSc0HPU3yXmpAkaXowNx_1I_PAzhk2VlzB86q2WUhX5UJrQiZ4qGz7yXXQZQub4of_ovXU3G3vKthmDfiVU1VeWaDYdShsZa9wQqbxErJ7b1wgZ1vH9Ku1RB6__AP4fgbeT544JaP6xSInZ-C5FL8onhbFYCnXRpnSklIOWV_vgr27QXWgiPzPby5id8UibI4sN58vcXeG9vArPLZyFMXaYAl84ZllV2h84IFFDeZRJL8OAiwVGSTSWD_9R4rb2FTTrDXgQ90VG8Rn7lKxN0xuBscSk6TGO5GDTGwlxGkQ2komjIO3FSouUJ5htLfeHFtoeETvCkqa04zK2dkIg1Mm1wFV7joM8AFuGbW7p1naweXEwuki6PG4LPBjNfNIN9tEGpVUdcXnhcIVtIIkj6WRRQZStbVkBC2xuleEtJqrRFRMxnOFPEUziSmD4VoQj_DUtAi7l46jP8rK5-WrDbbTHEbn2yX_B8BXu5_FffoCaG8F-ZjXQf8v54eWKitHU0U8OBAHEz9J_3HLzCKjJwxTtDAvhXS99wOLMrzPKj8FWn48at2UkzMaB1zvrAxihutzq-hZKyEayGHv7K1w_WKRBSqdAv0V5Iv5khSiQKWrgNJTiYC8SRXuu9xDE4xfffpyL6YwCThMSdqSRl2m8tNwgxzIznDOusws2AoMKNeFB5EnEXK8pTs3CGMRbmcm1D1FxiiKIaqu3FYjt8ssASeW8yH4-V5kNqm-aBQozBtCOqIfgPt30WbtsXTZprgUy2AR-DmyFYppvJ8q5E4JOhMnVafh02M_Eyu9lq4izyElvGjvF9KsxecJWR8ksIRAvRUVHuX7kh2KQmMmekw7m5BymcK9CXoAYXBSquatV-NUJLrUaMamuTI5puKwXLz-1_VnkMuXIcrGPlYrx_6NbCObI4l2wl5oEBSMArEjlBT3mr62aWIK_7tNDD4SFHLG0-6D783WFTOvfUmRfeXg_6I6A6HA3K81qu37nQY2CaX52q5tOdn0uFNMQ8ylBBMTZ_a7_LhE7BSbLhojsKZ0P_Jmf7_CsReFK-tbbVE_QXTSSXc-Vyv6pGa-CH2FAb44Cx-PeeThhE_mCUFR5h1FGbVtPNQcEo2lTUFKjNQcb5IJD4bHzHZxb7n3C8-wK52NULaGlUNrrlulcyCizvMghEit8UaXqAxFMvpKMhCWFQj8iZ1k3wIcLnNYvuwumTqYa9dKjcczIJdyJVezCifMHrqJysvqtbVRslmJiHw4WXJfokY8JATz_846l4D0hAaj-DH20q8D_-mo7di-nXCRHj5EpZY8jHurlfy1S9hxpDG0BHjRXCFcf0sRlcQi5ZTPKxH05qAf39zNHlA8y6hDrrPGK8NZVPs4nRU_0qnPX905Z9OrH3QqwMBHLSv5eIMcEyQg7j7gwbyDyBGEbpzh3D-MCp4SSobXnTEv5j2FXd5wzzCY_US9FGodBKC82kW1Hp2Tm5okwq7-Qzh2%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={quote(snlm0e)}&'
print('filling password...')
time.sleep(6)
fill_password = requests_cffi.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',params=params,cookies=cookies,headers=headers,data=data,allow_redirects=False, proxies={'http':http_proxy, 'https':http_proxy}, impersonate ="safari17_0")
print(fill_password.text)

import pdb; pdb.set_trace()






'''
def to(http_proxy, hgapz):
    a = 'qwertyuiopasdfghjklzxcvbnm'

    try:
        s1 = "".join(random.choice(a) for _ in range(random.randrange(6, 9)))
        s2 = "".join(random.choice(a) for _ in range(random.randrange(6, 9)))
        s3 = "".join(random.choice(a) for _ in range(random.randrange(15, 30)))

        cookies = {
            '__Host-GAPS': hgapz,
        }

        headers = {
            'authority': 'accounts.google.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15',  
        }

        r = requests_cffi.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
            cookies=cookies,
            headers=headers,proxies={'http':http_proxy, 'https':http_proxy}, verify=False
        )

        match = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', r.text)
        if not match:
            return None

        tok = match.group(2)

        headers.update({
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?continue=https://www.google.com/search&q=dhduud&hl=ar',
        })

        data = {
            'f.req': f'["{tok}","{s1}","{s2}","{s1}","{s2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }

        response = requests_cffi.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,proxies={'http':http_proxy, 'https':http_proxy}, verify=False
        )

        try:
            tl = str(response.text).split('",null,"')[1].split('"')[0]
        except IndexError:
            return None

        host = response.cookies.get('__Host-GAPS', '')

        return tl, host
    except Exception as e:
        return None
'''