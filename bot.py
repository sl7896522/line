# -*- coding: utf-8 -*-
from Linephu.linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from time import strftime
from googletrans import Translator
botStart = time.time()
cl = LINE()
cl.log("Auth Token : " + str(cl.authToken))
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
print ("""
✄▒█▀▀█ ▒█░░▒█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ ▀▀█▀▀ ▒█░▄▀
✄▒█░░░ ▒█▄▄▄█ ▒█▀▀▄ ▒█▀▀▀ ▒█▄▄▀ ░▒█░░ ▒█▀▄░
✄▒█▄▄█ ░░▒█░░ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█ ░▒█░░ ▒█░▒█

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▒▒░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
______▒_______________▒▒▒▒▒▒▒▒
_____▒________________▒▒▒▒▒▒▒▒
____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
___▒
__▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
\n
Login śєʟғ =====[̴̘̤̫̼̗̯͎̲̈́͑͑̅̂͊͐̾͆ͥͮ͟͠C̼̟̭͓͚̮̝͙̲̞͇̻̦̟͔̫ͯ̿̅̈́ͬ͊̓ͦ͌̌͗̆ͮ͂̍̚]̣̅[҉̷͚͓̼͉̮̲̟̝̬̱̱͖̅ͩ̎̀̈́̋ͣ̂̋ͩͮ̉Ý̢̲͇͚̦̻̰̻ͫ̍ͮ̅]̨̃ͯͨ̂̋ͪ̅[̪̲̘̲ͣͯ̑̅̑̎B̧̡̘͇͚̹̖̣͎̼̖̫̲̦̪̹̺̠̰̓ͬ̿̅ͯ̓̾́̍͋ͤ̒͋̆̈́̽̅][̧̤̘̮̪̮̟̠̻̲̘̻̥̲̬̑̍͑̐̈̓̿̅̐͑̿ͬͮͫE̪̙͖̫̲̣̥͔̊͒̏͊̅ͦͯ̋]̠̖̭̳͇̑́̉̆͛[͇̩̘̖͕̝̖̱̲̌ͧ̉ͬ̅̃̀ͦ̎́̅ͫ̉̇ͬ̏͋͝Ŗ̛̱̜̭͔̻̼̦̲̅]͡[͔͓̳̪̟͔̲̤̮͙̅ͬͫ̌̊͑ͧ́ͪṬ̢͍͇̠̩̮̪͇͚̱̫̖̲͆͛ͧ̃̓̑̅̎̓ͦ̈́̊̿̎̋̉̑̍̓̌]͆̈́ͧ͛[̯͉̬͈̱̪̞̺̥̲̲͕̗̆́̀̅̎̊ͬͭͧ͌͌̔ͭ̀͌͞ͅK̨̦̣͉͍͚̳̗̫̘͉̲ͣ͗̄̅̚͞]====
""")
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
wait = {
      "ban":False,
      "unban":False,
      "op":False,
      "unop":False
}
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
try:
    settings['bot'] = {}
    settings["bot"][clMID] = True
    settings["Admin"][clMID] = True

    backupData()
    print ("設置bot清單成功")
except:
    print ("設置bot清單失敗")
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
Bots=[clMID]
Owner=[clMID]
Admin=[clMID]
mulai = time.time()

msg_dict = {}
bl = [""]

def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return cl.sendMessage(to, text, contentMetadata, 0)
def sendMessageWithFooter(to, text):
 cl.reissueUserTicket()
 dap = cl.getProfile()
 ticket = "http://line.me/ti/p/"+cl.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+dap.pictureStatus
 name = dap.displayName
 dapi = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 cl.sendMessage(to, text, contentMetadata=dapi)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mid")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """
《云云的粉絲機器人》指令表
〘查看指令表〙
【Help】查看全部指令
【wind:help】查看全部指令(辨識用)
【HelpTag】查看標註指令
【HelpKick】查看踢人指令
【creator】查看作者
【修改者】查看修改作者
【時間】查看現在的時間
〘狀態〙
【Rebot】重新啟動機器
【Runtime】查看機器運行時間
【Speed】查看機器速度
【Set】查看設定
【About】查看自己的狀態
【wind:bye】主機退群
〘設定〙
【Add On/Off】自動加入好友 開啟/關閉
【Join On/Off】邀請自動進入群組 開啟/關閉
【Leave On/Off】自動離開副本 開啟/關閉
【Read On/Off】自動已讀 開啟/關閉
【Inviteprotect On/Off】群組邀請保護 開啟/關閉
【Reread On/Off】查看收回 開啟/關閉
【Qr On/Off】群組網址保護 開啟/關閉
【Qrjoin On/Off】網址自動入群 開啟/關閉
【Ck On/Off】貼圖資料查詢 開啟/關閉
〘自己〙
【Me】丟出自己好友資料
【MyMid】查看自己系統識別碼
【MyName】查看自己名字
【MyBio】查看自己個簽
【MyPicture】查看自己頭貼網址
【MyCover】查看自己封面網址
【Contact @】標註查看好友資料
【Mid @】標註查看系統識別碼
【Name @】標註查看名稱
【Bio @】標註查看狀態消息
【Picture @】標註查看頭貼
【Cover @】標注查看封面
【Friendlist】查看好友清單
〘群組〙
【Gowner】查看群組擁有者
【Gurl】丟出群組網址
【O/Curl】打開/關閉群組網址
【Lg】查看所有群組
【Gb】查看群組成員
【Ginfo】查看群組狀態
【Ri @】標註來回機票
【Tk @】標注踢出成員(多踢)
【Mk @】標注踢出成員(單踢)
【Vk @】標註踢出並清除訊息
【Vk:mid】使用系統識別碼踢出並清除訊息
【Nk Name】使用名子踢出成員
【Uk mid】使用系統識別碼踢出成員
【NT Name】使用名子標註成員
【Zt】標註名字0字成員
【Zm】丟出0字成員的系統識別碼
【Cancel】取消所有成員邀請
【Gn Name】更改群組名稱
【Gc @】標註查看個人資料
【Inv mid】使用系統識別碼邀請進入群組
【Ban @】標註加入黑單
【Unban @】標註解除黑單
【Clear Ban】清空黑單
【Kill Ban】剔除黑單
【Ban】丟出友資加入黑名單
【Unban】丟出友資移除黑名單
【Zk】踢出名字0字成員
【Banlist】查看黑名單
〘特別〙
【Tagall】標註群組所有成員
【S N/F/R】已讀點 開啟/關閉/重設
【R】查看已讀
【F/Gbc】好友/群組廣播
【add_wc:】進群歡迎顯示
【add_gc:】退群歡迎顯示
【del_wc】刪除進群歡迎詞
【del_gc】刪除退群歡迎詞
〘權限〙
【adminadd @】標註加入權限
【admindel @】標註移除權限
【adminadd: 】mid增加權限
【admindel: 】mid移除權限
【op】丟出友資增加權限
【Unop】丟出友資移除權限
【adminlist】查看權限
⇒Credits By.⇐
"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""
〘標注指令〙
【Ri @】標註來回機票
【Tk @】標注踢出成員(多踢)
【Mk @】標注踢出成員(單踢)
【Vk @】標註踢出並清除訊息
【Gc @】標註查看個人資料
【Mid @】標註查看系統識別碼
【Name @】標註查看名稱
【Bio @】標註查看狀態消息
【Picture @】標註查看頭貼
【Cover @】標注查看封面
【Ban @】標註加入黑單
【Unban @】標註解除黑單
⇒Credits By.ShengYe™⇐
"""
    return helpMessageTag
def helpmessagekick():
    helpMessageKick ="""
〘踢人指令〙
【Ri @】標註來回機票
【Tk @】標注踢出成員(多踢)
【Mk @】標注踢出成員(單踢)
【Vk @】標註踢出並清除訊息
【Vk:mid】使用系統識別碼踢出並清除訊息
【Nk Name】使用名子踢出成員
【Uk mid】使用系統識別碼踢出成員
【Kill ban】踢出黑單成員
【Zk】踢出名字0字成員
⇒Credits By.ShengYe™⇐
"""
    return helpMessageKick

def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(param2)
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "你好 {} 謝謝你加我為好友 :D\n       金合發 kgj666.jf68.net ".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"][op.param1] == True:
                    gs = cl.getGroup(op.param1)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
        if op.type == 13:
            if clMID in op.param3:
                group = cl.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "Hi~~everyone")
            elif settings["inviteprotect"][op.param1] == True:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
            else:
                group = cl.getGroup(op.param1)
                gInviMids = []
                for z in group.invitee:
                    if z.mid in settings["blacklist"]:
                        gInviMids.append(z.mid)
                if gInviMids == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, gInviMids)
                    cl.sendMessage(op.param1,"被邀請者黑單中...")
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print(cl.getContact(op.param2).displayName)
            if settings["kick"] == True:
                msg = op.message
                chiya = []
                chiya.append(op.param2)
                chiya.append(op.param3)
                cmem = cl.getContacts(chiya)
                zx = ""
                zxc = ""
                zx2 = []
                xpesan ='警告!'
                for x in range(len(cmem)):
                    xname = str(cmem[x].displayName)
                    pesan = ''
                    pesan2 = pesan+"@x 踢"
                    xlen = str(len(zxc)+len(xpesan))
                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                    zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                    zx2.append(zx)
                    zxc += pesan2
                text = xpesan+ zxc + "出群組"
                try:
                    cl.sendMessage(op.param1, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                except:
                    cl.sendMessage(op.param1,"Notified kick out from group")
            if settings["CreatorLock"] == True:
                if op.param3 in group.creator.mid:
                    if op.param2 in Admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1, [op.param2])
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1, [op.param3])
                    settings["blacklist"][op.param1][op.param2] = True
                    cl.sendMessage(op.param1, "成功新增黑名單\n" + "MID : " + op.param2)
                    cl.sendContact(op.param1, op.param2)
            if settings["protect"][op.param1] == True:
                if op.param2 in Admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][op.param2] = True
                    cl.sendMessage(op.param1, "成功新增黑名單\n" + "MID : " + op.param2)
                    cl.sendContact(op.param1, op.param2)
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
                bot = random.choice([cl])
                bot.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 24:
            print ("[ 24 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新配置文件")
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["ban"] == True:
                   if msg._from in Admin:
                       if msg.contentMetadata["mid"] in settings["blacklist"]:
                           cl.sendMessage(msg.to,"already")
                           wait["ban"] = False
                       else:
                           settings["blacklist"][msg.contentMetadata["mid"]] = True
                           wait["ban"] = False
                           cl.sendMessage(msg.to,"ok")
               elif wait["unban"] == True:
                   if msg._from in Admin:
                       if msg.contentMetadata["mid"] not in settings["blacklist"]:
                           cl.sendMessage(msg.to,"already")
                           wait["unban"] = False
                       else:
                           del settings["blacklist"][msg.contentMetadata["mid"]]
                           wait["unban"] = False
                           cl.sendMessage(msg.to,"ok")
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["op"] == True:
                   if msg._from in Admin:
                       if msg.contentMetadata["mid"] in settings["Owner"]:
                           cl.sendMessage(msg.to,"already")
                           wait["op"] = False
                       else:
                           settings["Owner"][msg.contentMetadata["mid"]] = True
                           wait["op"] = False
                           cl.sendMessage(msg.to,"ok")
               elif wait["unop"] == True:
                   if msg._from in Admin:
                       if msg.contentMetadata["mid"] not in settings["Owner"]:
                           cl.sendMessage(msg.to,"already")
                           wait["unop"] = False
                       else:
                           del settings["Owner"][msg.contentMetadata["mid"]]
                           wait["unop"] = False
                           cl.sendMessage(msg.to,"ok")

        if op.type == 15:
            if op.param2 in settings["blacklist"]:
                cl.sendMessage(op.param1, "[警告]\n此人位於黑名單中! ! !")
            else:
                if op.param2 not in settings['bot']:
                    if op.param1 not in settings['gel']:
                        try:
                            arrData = ""
                            text = "%s " %('掰掰~~')
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention + '!!此人退出群組!!!!'
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    else:
                        cl.sendMessage(op.param1, settings['gel'][op.param1])
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
                cl.sendMessage(op.param1, "[警告]\n此人位於黑名單中! ! !")
            else:
                if op.param2 not in settings['bot']:
                    if op.param1 not in settings['wel']:
                        try:
                            arrData = ""
                            text = "%s " %('你好~~')
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention + '!!歡迎加入群組!!!! 金合發娛樂城 kgj666.jf68.net 歡迎您'
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    else:
                        cl.sendMessage(op.param1, settings['wel'][op.param1])
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 13:
                if settings["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                            cl.sendMessage(msg.to,"[名稱]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s " %("[文章持有者]\n")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[文章預覽]\n(僅提供100字內容)\n " + msg.contentMetadata["text"] + "\n[文章網址]\n " + msg.contentMetadata["postEndUrl"]
                            cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "\n[文章預覽]\n(僅提供100字內容)\n " + msg.contentMetadata["text"]
                        ret_ += "\n[文章網址]\n " + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to, ret_)
            if msg.contentType == 0:
                if text is None:
                  return
            if sender in Admin or sender in settings["Admin"]:
                if "miya" in msg.text.lower():
                    while 1:
                        cl.sendMessage(to, text=None, contentMetadata={'mid': "ub2509af2bd4caa8b18973acf084fa2ea"}, contentType=13)
                elif msg.text in ["Help","help"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0h9lnRA_pbZkNTK0sSFYsZFG9uaC4kBWALKxp6dXMrOXt7GSMSbx0pciN5MXN5EyNCaB0hd34tPid3','AGENT_LINK':'https://line.me/ti/p/~212134a','AGENT_NAME':'Creator'})
                    cl.sendMessage(to, "我的作者")
                    cl.sendContact(to, "ub2509af2bd4caa8b18973acf084fa2ea")
                elif text.lower() == 'wind:help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to, "ub2509af2bd4caa8b18973acf084fa2ea")
                elif text.lower() == 'creator':
                	cl.sendContact(to, "ub2509af2bd4caa8b18973acf084fa2ea")
                elif text.lower() == '修改者':
                        cl.sendContact(to, "ub2509af2bd4caa8b18973acf084fa2ea")
                elif text.lower() == 'helptag':
                    helpMessageTag = helpmessagetag()
                    cl.sendMessage(to, str(helpMessageTag))
                elif text.lower() == 'helpkick':
                    helpMessageKick = helpmessagekick()
                    cl.sendMessage(to, str(helpMessageKick))
                elif msg.text.lower(). startswith("banadd "):
                    x = text.replace("banadd ",'')
                    y = x.split(' ')
                    for mid in y:
                        settings["blacklist"][mid] = True
                        cl.sendMessage(to, "已加入黑名單")
                elif ("Say " in msg.text):
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendMessage(to,x[1])
                elif "閃退炸彈" in msg.text.lower():
                    cl.sendMessage(msg.to, text=None, contentMetadata={'mid': "ub2509af2bd4caa8b18973acf084fa2ea',"}, contentType=13)
                    cl.sendMessage(msg.to, text=None, contentMetadata={'mid': "ub2509af2bd4caa8b18973acf084fa2ea',"}, contentType=13)
                    cl.sendMessage(to, Kickall)
                elif text.lower().startswith('admindel:'):
                    x = text.replace("admindel:",'')
                    y = x.split(' ')
                    for mid in y:
                        del settings["Admin"][mid]
                    cl.sendMessage(to, "已成功移除了第一權限")
                elif text.lower().startswith('adminadd:'):
                    x = text.replace("adminadd:",'')
                    y = x.split(' ' )
                    for mid in y:
                        settings["Admin"][mid] = True
                    cl.sendMessage(to, "成功加入第一權限")
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    else:
                        for target in targets:
                                try:
                                    cl.sendMessage(to,"出去反省一下")
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "Kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = cl.getGroup(to)
                            cl.sendMessage(to, "金合發云云")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                        try:
                                            klist=[cl]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif "Mk " in msg.text:
                    Mk0 = text.replace("Mk ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = cl.getGroup(to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "nk " in msg.text:
                    _name = text.replace("nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif msg.text.lower(). startswith("tag "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        sendMessageWithMention(to, inkey)
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = cl.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            mc = sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to,mc)
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = ""
                        for mi_d in targets:
                            mc += "->" + mi_d + "\n"
                        cl.sendMessage(to,mc)
                elif msg.text == "時間":
                    cl.sendMessage(msg.to, strftime("現在是 %H 時 %M 分 %S 秒"))
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    cl.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = cl.getGroup(ggid)
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "沒有"
                    else:
                        gQr = "開啟"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "<群組資料>"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(ret))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n<完>"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "取消人數:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower() == 'gcancel':
                    gid = cl.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "全部群組邀請已取消")
                    cl.sendMessage(to, "取消時間: %s秒" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"無法使用在群組外")
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n頭貼網址 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n封面網址 :\n" + str(cu))
                        except:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n封面網址:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif text.lower() == 'ban':
                    cl.sendMessage(to, "請傳送友資加入黑名單")
                    wait["ban"] = True
                elif text.lower() == 'unban':
                    cl.sendMessage(to, "請傳送友資移除黑名單")
                    wait["unban"] = True
                elif text.lower() == 'op':
                    cl.sendMessage(to, "請傳送友資加入權限")
                    wait["op"] = True
                elif text.lower() == 'unop':
                    cl.sendMessage(to, "請傳送友資移除權限")
                    wait["unop"] = True
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "已加入黑名單")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "已解除黑名單")
                                except:
                                    pass
                elif "adminadd" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["Admin"][target] = True
                                    cl.sendMessage(to, "已加入權限")
                                except:
                                    pass
                elif "admindel" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["Admin"][target]
                                    cl.sendMessage(to, "已解除權限")
                                except:
                                    pass
                elif text.lower() == 'clear ban':
                        settings["blacklist"] = {}
                        cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'clear admin':
                    settings["Admin"] = {}
                    cl.sendMessage(to, "已清空權限者")
                elif text.lower() == 'adminlist':
                    if settings["Admin"] == {}:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        cl.sendMessage(to, "以下是權限者")
                        mc = "╔══[ Admin List ]"
                        for mi_d in settings["Admin"]:
                            mc += "\n╠" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc+"╚══[總共"+str(len(settings["Admin"]))+ "個人有權限]")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        cl.sendMessage(to, "以下是黑名單")
                        mc = "╔══[ Black List ]"
                        for mi_d in settings["blacklist"]:
                            mc += "\n╠" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc+"╚══[總共"+str(len(settings["blacklist"]))+ "個人被黑單]")
                elif text.lower() == 'ownerlist':
                    if settings["Owner"] == {}:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        cl.sendMessage(to, "以下為權限者")
                        mc = "╔══[ Owner List ]"
                        for mi_d in settings["Owner"]:
                            mc += "\n╠ " +cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc+"╚══[總共"+str(len(settings["Owner"]))+ "個人有權限]")
                elif text.lower() == 'banmid':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        cl.sendMessage(to, "以下是黑名單")
                        mc = "以下是黑單的mid" + "\n"
                        for mi_d in settings["blacklist"]:
                            mc += "♡" + cl.getContact(mi_d).displayName + "\n" + mi_d + "\n"
                        cl.sendMessage(to, mc)
                        cl.sendMessage(to, "總共"+str(len(settings["blacklist"]))+ "個人被黑單")
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "沒有黑名單")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "黑名單已踢除")
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        cl.sendMessage(to, "請輸入群組ID")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendMessage(to, "我不在那個群組裡")
                elif msg.text in ["Friendlist"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"「 朋友列表 」\n"+ap+"人數 : "+str(len(anl)))
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "檢查中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")
                elif text.lower() == 'speed':
                    start = time.time()
                    cl.sendMessage(to, "檢查中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動中...請稍後...")
                    time.sleep(5)
                    cl.sendMessage(to, "重新啟動完成！")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運行時間 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ufba410943361a1fdc81693f6a9c977e8"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "《關於自己》"
                        ret_ += "\n名稱 : {}".format(contact.displayName)
                        ret_ += "\n群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n《關於機器》"
                        ret_ += "\n版本 : V1.0beta"
                        ret_ += "\n作者 : {}".format(creator.displayName)
                        ret_ += "\n(´・ω・｀)"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    group = cl.getGroup(to)
                    try:
                        ret_ = "[ 設定 ]"
                        ret_ += "\n顯示名稱 : {}".format(str(group.name))
                        if settings["autoAdd"] == True: ret_ += "\n自動加入好友 ✔"
                        else: ret_ += "\n自動加入好友 ✘"
                        if settings["autoJoin"] == True: ret_ += "\n自動加入群組 ✔"
                        else: ret_ += "\n自動加入群組 ✘"
                        if settings["autoJoinTicket"] == True: ret_ += "\n網址自動入群 ✔"
                        else: ret_ += "\n網址自動入群 ✘"
                        if settings["autoLeave"] == True: ret_ += "\n自動離開副本 ✔"
                        else: ret_ += "\n自動離開副本 ✘"
                        if settings["autoRead"] == True: ret_ += "\n自動已讀 ✔"
                        else: ret_ += "\n自動已讀 ✘"
                        if settings["kick"] == True: ret_ += "\n踢人顯示已開啟 ✔"
                        else: ret_ += "\n踢人顯示關閉 ✘"
                        if settings["autoJick"] == True: ret_ += "\n進群顯示已開啟 ✔"
                        else: ret_ += "\n進群顯示關閉 ✘"
                        if settings["inviteprotect"][to] == True: ret_ += "\n群組邀請保護 ✔"
                        else: ret_ += "\n群組邀請保護 ✘"
                        if settings["qrprotect"][to] == True: ret_ += "\n群組網址保護 ✔"
                        else: ret_ += "\n群組網址保護 ✘"
                        if settings["protect"][to] == True: ret_ += "\n群組保護 ✔"
                        else: ret_ += "\n群組保護 ✘"
                        if settings["CreatorLock"] == True: ret_ += "\n作者鎖定 ✔"
                        else: ret_ += "\n作者鎖定 ✘"
                        if settings["contact"] == True: ret_ += "\n詳細資料 ✔"
                        else: ret_ += "\n詳細資料 ✘"
                        if settings["reread"] == True: ret_ += "\n查詢收回開啟 ✔"
                        else: ret_ += "\n查詢收回關閉 ✘"
                        if settings["detectMention"] == True: ret_ += "\n標註回覆開啟 ✔"
                        else: ret_ += "\n標註回覆關閉 ✘"
                        ret_ += "\n"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友已開啟 ✔")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友已關閉 ✘")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動加入群組已開啟 ✔")
                elif text.lower() == 'kc on':
                    settings["kick"] = True
                    cl.sendMessage(to, "踢人顯示已開啟 ✔")
                elif text.lower() == 'kc off':
                    settings["kick"] = False
                    cl.sendMessage(to, "踢人顯示已關閉 ✘")
                elif text.lower() == 'jick on':
                    settings["autoJick"] = True
                    cl.sendMessage(to, "進群顯示已開啟 ✔")
                elif text.lower() == 'jick off':
                    settings["autoJick"] = False
                    cl.sendMessage(to, "進群顯示已關閉 ✘")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動加入群組已關閉 ✘")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開啟 ✔")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關閉 ✘")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    cl.sendMessage(to, "查看好友資料詳情開啟 ✔")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    cl.sendMessage(to, "查看好友資料詳情關閉 ✘")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"][to] = True
                    cl.sendMessage(to, "群組邀請保護已開啟 ✔")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"][to] = False
                    cl.sendMessage(to, "群組邀請保護已關閉 ✘")
                elif text.lower() == 'qr on':
                    settings["qrprotect"][to] = True
                    cl.sendMessage(to, "群組網址保護已開啟 ✔")
                elif text.lower() == 'qr off':
                    settings["qrprotect"][to] = False
                    cl.sendMessage(to, "群組網址保護已關閉 ✘")
                elif text.lower() == 'protect on':
                    settings["protect"][to] = True
                    cl.sendMessage(to, "群組保護已開啟 ✔")
                elif text.lower() == 'protect off':
                    settings["protect"][to] = False
                    cl.sendMessage(to, "群組保護已關閉 ✘")
                elif text.lower() == 'creatorlock on':
                    settings["CreatorLock"] = True
                    cl.sendMessage(to, "作者保護已開啟 ✔")
                elif text.lower() == 'creatorlock off':
                    settings["CreatorLock"] = False
                    cl.sendMessage(to, "作者保護已關閉 ✘")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟 ✔")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉 ✘")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟 ✔")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉 ✘")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    cl.sendMessage(to, "網址自動入群已開啟 ✔")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "網址自動入群已關閉 ✘")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "標註回覆已開啟 ✔")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "標註回覆已關閉 ✘")
                elif msg.text.lower().startswith("add_gc"):
                    list_ = msg.text.split(":")
                    if to not in settings['gel']:
                        try:
                           settings['gel'][to] = list_[1]
                           with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功設置群組退出訊息\n退出訊息: " + list_[1])
                        except:
                            cl.sendMessage(to, "[提示]\n設置群組退出訊息失敗!!!")
                    else:
                         l.sendMessage(to, "[提示]\n群組退出訊息已存在!!!")
                elif msg.text.lower().startswith("renew_gc"):
                    list_ = msg.text.split(":")
                    if to in settings['gel']:
                        try:
                            del settings['gel'][to]
                            settings['gel'][to] = list_[1]
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功更新群組退出訊息\n退出訊息: " + list_[1])
                        except:
                            cl.sendMessage(to, "[提示]\n更新群組退出訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[提示]\n你正在更新不存在的退出訊息!!!")
                elif msg.text.lower().startswith("gmadd "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                            for ls in lists:
                                if to not in settings['gm']:
                                    settings['gm'][to] = {}
                                if ls not in settings['gm'][to]:
                                    settings['gm'][to][ls] = ls
                                    with open('temp.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(to, "成功新增GM權限")
                                        cl.sendContact(to, ls)
                                else:
                                    cl.sendMessage(to, "此人已擁有GM權限")
                elif text.lower() == ("del_gc"):
                    list_ = msg.text.split(":")
                    if to in settings['gel']:
                        try:
                            del settings['gel'][to]
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功刪除群組退出訊息")
                        except:
                            cl.sendMessage(to, "[提示]\n刪除群組退出訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[提示]\n你正在刪除不存在的退出訊息!!!")
                elif text.lower() == 'gc':
                    if to in settings['gel']:
                        cl.sendMessage(to, settings['gel'][to])
                    else:
                        cl.sendMessage(to, "[提示]\n使用預設群組退出訊息中!!!")
                elif msg.text.lower().startswith("add_wc"):
                    list_ = msg.text.split(":")
                    if to not in settings['wel']:
                        try:
                            settings['wel'][to] = list_[1]
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功設置群組歡迎訊息\n歡迎訊息: " + list_[1])
                        except:
                            cl.sendMessage(to, "[提示]\n設置群組歡迎訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[提示]\n群組歡迎訊息已存在!!!")
                elif msg.text.lower().startswith("renew_wc"):
                    list_ = msg.text.split(":")
                    if to in settings['wel']:
                        try:
                            del settings['wel'][to]
                            settings['wel'][to] = list_[1]
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功更新群組歡迎訊息\n歡迎訊息: " + list_[1])
                        except:
                            cl.sendMessage(to, "[提示]\n更新群組歡迎訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[提示]\n你正在更新不存在的歡迎訊息!!!")
                elif text.lower() == ("del_wc"):
                    if to in settings['wel']:
                        try:
                            del settings['wel'][to]
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功刪除群組歡迎訊息")
                        except:
                            cl.sendMessage(to, "[提示]\n刪除群組歡迎訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[提示]\n你正在刪除不存在的歡迎訊息!!!")
                elif text.lower() == 'wc':
                    if to in settings['wel']:
                        cl.sendMessage(to, settings['wel'][to])
                    else:
                        cl.sendMessage(to, "[提示]\n使用預設群組歡迎訊息中!!!")
                elif text.lower() == 'me':
                    cl.sendContact(to, sender)
                elif text.lower() == 'mytag':
                    sendMessageWithMention(to, sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[顯示名稱]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[狀態消息]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "以上為標註者MID" + "\n"
                        for ls in lists:
                            ret_ += "[•]" + cl.getContact(ls).displayName + "\n" + ls + "\n"
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 名稱 ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 個簽 ]\n" + contact.statusMessage)
                elif text.lower() == 'wind:bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        cl.leaveGroup(to)
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif text.lower() == 'gowner':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組ID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://cl.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "群組網址未開啟，請用Ourl先開啟".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開啟")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功開啟群組網址")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關閉")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功關閉群組網址")
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        GM = group.creator.displayName
                    except:
                        GM = settings['gm'][to]
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "沒有"
                    else:
                        gQr = "開啟"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《群組資料》"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(GM))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[成員列表]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[總共： {} 人]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        group = cl.getGroup(to)
                        ret_ = "[群組列表]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//10
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*10 : (a+1)*10]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 個成員".format(str(len(nama))))
                elif text.lower() == 'sn':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to,"已讀點已開始")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "設定已讀點:\n" + readTime)
                elif text.lower() == 'sf':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%Y') + " - " + bln + " - " + timeNow.strftime('%d') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        cl.sendMessage(msg.to,"已讀點已經關閉")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        cl.sendMessage(msg.to, "刪除已讀點:\n" + readTime)
                elif text.lower() == 'sr':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "星期二", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%Y') + " - " + bln + " - " + timeNow.strftime('%d') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        cl.sendMessage(msg.to, "重置已讀點:\n" + readTime)
                    else:
                        cl.sendMessage(msg.to, "已讀點未設定")
                elif text.lower() == 'r':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "星期一", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%Y') + " - " + bln + " - " + timeNow.strftime('%d') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            cl.sendMessage(receiver,"[ 已讀者 ]:\n沒有")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ 已讀者 ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ 已讀時間 ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        cl.sendMessage(receiver,"已讀點未設定")
                elif msg.text.lower().startswith("gmdel "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            if ls in settings['gm'][to][ls]:
                                try:
                                    del settings['gm'][to][ls]
                                    with open('temp.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(to, "成功刪除Group Master權限")
                                except:
                                       cl.sendMessage(to, "[ERROR]\n刪除Group Master權限失敗")
                            else:
                                cl.sendMessage(to, "[ERROR]\n此人並未擁有Group Master權限")
                elif msg.text.lower().startswith("owneradd "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                       names = re.findall(r'@(\w+)', text)
                       mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                       mentionees = mention['MENTIONEES']
                       lists = []
                       for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                       for ls in lists:
                           if ls not in settings['Owner']:
                               settings['Owner'][ls] = True
                               with open('temp.json', 'w') as fp:
                                   json.dump(settings, fp, sort_keys=True, indent=4)
                                   cl.sendMessage(to, "成功新增Owner權限")
                                   cl.sendContact(to, ls)
                           else:
                               cl.sendMessage(to, "此人已擁有Owner權限")
                elif msg.text.lower().startswith("del "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                       names = re.findall(r'@(\w+)', text)
                       mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                       mentionees = mention['MENTIONEES']
                       lists = []
                       for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                       for ls in lists:
                           if ls in settings['Admin']:
                               del settings['Admin'][ls]
                               with open('temp.json', 'w') as fp:
                                   json.dump(settings, fp, sort_keys=True, indent=4)
                                   cl.sendMessage(to, "成功移除Admin權限")
                                   cl.sendContact(to, ls)
                           else:
                               cl.sendMessage(to, "此人並未擁有Admin權限")

                elif msg.text.lower().startswith("add "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                       names = re.findall(r'@(\w+)', text)
                       mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                       mentionees = mention['MENTIONEES']
                       lists = []
                       for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                       for ls in lists:
                           if ls not in settings['Admin']:
                               settings['Admin'][ls] = True
                               with open('temp.json', 'w') as fp:
                                   json.dump(settings, fp, sort_keys=True, indent=4)
                                   cl.sendMessage(to, "成功新增Admin權限")
                                   cl.sendContact(to, ls)
                           else:
                               cl.sendMessage(to, "此人已擁有Admin權限")
                elif msg.text.lower().startswith("ownerdel "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                       names = re.findall(r'@(\w+)', text)
                       mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                       mentionees = mention['MENTIONEES']
                       lists = []
                       for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                       for ls in lists:
                           if ls in settings['Owner']:
                               del settings['Owner'][ls]
                               with open('temp.json', 'w') as fp:
                                   json.dump(settings, fp, sort_keys=True, indent=4)
                                   cl.sendMessage(to, "成功移除Owner權限")
                                   cl.sendContact(to, ls)
                           else:
                               cl.sendMessage(to, "此人並未擁有Owner權限")
                elif text.lower() == 'status':
                        contact = cl.getContact(sender)
                        ret_ = "[使用者狀態]\n"
                        ret_ += '使用者名稱 => ' + contact.displayName + "\n"
                        ret_ += '使用者MID => ' + contact.mid + "\n"
                        if sender in Admin:
                            ret_ += '使用者權限 => ' + 'God mod\n'
                            ret_ += '使用者限制 => ' + '無限制\n'
                            ret_ += '指令權限 => ' + 'All usefull'
                        elif sender in settings['Owner']:
                            ret_ += '使用者權限 => ' + 'Admin\n'
                            ret_ += '使用者限制 => ' + '無限制\n'
                            ret_ += '指令權限 => ' + 'All without revoke'
                        elif sender in ban['blacklist']:
                            ret_ += '使用者權限 => ' + 'Blacklist\n'
                            ret_ += '使用者限制 => ' + '全功能制限\n'
                            ret_ += '指令權限 => ' + 'All useless\n'
                        else:
                            ret_ += '使用者權限 => ' + 'Normal\n'
                            ret_ += '使用者限制 => ' + '普通限制\n'
                            ret_ += '指令權限 => ' + 'Only normal\n'
                        cl.sendMessage(to, ret_)
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            if settings["reread"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                contact = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(contact.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                contact = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 收回訊息 」\n"
                                ret_ += "• 收回訊息者 : {}".format(str(contact.displayName))
                                ret_ += "\n• 群組名稱 : {}".format(str(ginfo.name))
                                ret_ += "\n• 收回時間 : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• 訊息內容 : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                image = "https://stickershop.line-scdn.net/stickershop/v1/sticker/" + contact.pictureStatus								
                                cl.sendImageWithURL(op.param1,image)	
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            sendMention(op.param1,"@! \n試圖收回了↓\n"+str(msg_dict[msg_id]["text"]),[msg_dict[msg_id]["from"]])
                            cl.sendMessage(at,"[收回訊息者]\n%s\n[訊息內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"])+ "\n[發送時間]\n"+strftime("%Y-%m-%d-%p-%w  %H:%M:%S "))
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "標我有事？(此為系統自動回覆)")
                                    sendMessageWithMention(to, contact.mid)
                                break
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
