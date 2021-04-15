#This API is not officially prepared

# -*- coding: utf-8 -*-

import requests

token_txt = open('token.txt', 'r', encoding='utf_8')
token = token_txt.read()
token_txt.close()

status_list_txt = open('status_list.txt', 'r', encoding='utf_8')
status_list = status_list_txt.read().splitlines()
status_list_txt.close()

status_list.append('(指定しない)')
break_switch = 0

user_status_list = ['online', 'idle', 'dnd', 'invisible']

for cnt, status_name_list in enumerate(status_list):
    print(str(cnt + 1).zfill(2) + ': ' + status_name_list)
    status_list_finalindex = cnt

def input_index(index):
    input_return = input('\n1から' + str(index + 1) + 'までのステータスを指定してください\nPlease specify a status from 1 to ' + str(index + 1) + ': ')
    return input_return

def input_status():
    print('\n01: オンライン / Online\n02: 退席中 / Idle\n03: 取り込み中 / Do Not Disturb\n04: オンライン状態を隠す / Invisible')
    input_return = input('\n1から4までのステータスを指定してください\nPlease specify a status from 1 to 4: ')
    return input_return

while True:

    while True:
        status_list_index = str(input_index(status_list_finalindex))
        if status_list_index.isdecimal() is True:
            if int(status_list_index) <= int(status_list_finalindex) + 1 and int(status_list_index) >= 1:

                while True:
                    user_status = str(input_status())
                    if  user_status.isdecimal() is True:
                        if int(user_status) <= 4 and int(user_status) >= 1:
                            break_switch = 1
                            break

                        for cnt, user_status_name_list in enumerate(user_status_list):
                            print(str(cnt + 1).zfill(2) + ': ' + user_status_name_list)

            if break_switch == 1:
                break

            for cnt, status_name_list in enumerate(status_list):
                print(str(cnt + 1).zfill(2) + ': ' + status_name_list)
                status_list_finalindex = cnt


    headers = {'Content-Type': 'application/json', 'authorization': token}

    if status_list_finalindex == int(status_list_index) - 1:
        custom_status_json = {"custom_status": {'text': None}}
    else:
        custom_status_json = {"custom_status": {'text': status_list[int(status_list_index) - 1]}}
    cs_patch = requests.patch('https://canary.discord.com/api/v8/users/@me/settings', json = custom_status_json, headers = headers)

    custom_status_json = {'status': user_status_list[int(user_status) - 1]}
    cs_patch = requests.patch('https://canary.discord.com/api/v8/users/@me/settings', json = custom_status_json, headers = headers)

    if cs_patch.status_code == 200:
        print('\n設定が完了しました\nSetting is complete')
    else:
        print('\nエラーが発生しました\nAn error has occurred')

    print('\n\n---------------------------------------------------------------------\n\n')

    for cnt, status_name_list in enumerate(status_list):
        print(str(cnt + 1).zfill(2) + ': ' + status_name_list)
        status_list_finalindex = cnt

    break_switch = 0
