import urllib.request
import json
import os

response = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json")

hero_json = json.loads(response.read())
hero_num = len(hero_json)
# print(hero_num)

save_dir = 'C:\heroavatar\\'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

for i in range(hero_num):
    # avatar_name = hero_json[i]['ename']
    save_file_name = save_dir + hero_json[i]['cname'] + '-' + str(hero_json[i]['ename']) + '.jpg'
    # print(save_file_name)
    avatar_url = 'http://game.gtimg.cn/images/yxzj/img201606/heroimg/' + str(hero_json[i]['ename']) + '/' + str(hero_json[i]['ename']) + '.jpg'
    # print(avatar_url)
    if not os.path.exists(save_file_name):
        urllib.request.urlretrieve(avatar_url, save_file_name)