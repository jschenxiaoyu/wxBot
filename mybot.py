#!/usr/bin/env python
# coding: utf-8

from wxbot import *

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        ''' 群消息 '''
        if msg['msg_type_id'] == 3:
            msg_id = msg['msg_id']
            content = msg['content']
            src_name = content['user']['name']
            uid_test1 = self.get_user_id('test1')
            uid_test2 = self.get_user_id('test2')
            reply = 'from ' + src_name + ': '
            ''' 文本消息 '''
            if content['type'] == 0:
                data = content['data']
                reply = reply + data
                if uid_test1 == msg['user']['id']:
                    self.send_msg_by_uid(reply, uid_test2)
                if uid_test2 == msg['user']['id']:
                    self.send_msg_by_uid(reply, uid_test1)
            ''' 图片消息。动画表情(type=6)支持不好，后期考虑通过转发实现，系统自带动画表情通过图片方式不支持 '''
            if content['type'] == 3:
                self.get_msg_img(msg_id)
                path = 'temp/img_' + msg_id + '.jpg'
                if uid_test1 == msg['user']['id']:
                    self.send_msg_by_uid(reply, uid_test2)
                    self.send_img_msg_by_uid(path, uid_test2)
                if uid_test2 == msg['user']['id']:
                    self.send_msg_by_uid(reply, uid_test1)
                    self.send_img_msg_by_uid(path, uid_test1)
            ''' 语音消息 '''
            if content['type'] == 4:
                self.get_voice(msg_id)
                path = 'temp/voice_' + msg_id + '.mp3'
                if uid_test1 == msg['user']['id']:
                    self.send_msg_by_uid(reply, uid_test2)
                    self.send_file_msg_by_uid(path, uid_test2)
                if uid_test2 == msg['user']['id']:
                    self.send_msg_by_uid(reply, uid_test1)
                    self.send_file_msg_by_uid(path, uid_test1)
            ''' 视频消息 '''
            if content['type'] == 13:
                self.get_video(msg_id)
                path = 'temp/video_' + msg_id + '.mp4'
                if uid_test1 == msg['user']['id']:
                    self.send_msg_by_uid(reply, uid_test2)
                    self.send_file_msg_by_uid(path, uid_test2)
                if uid_test2 == msg['user']['id']:
                    self.send_msg_by_uid(reply, uid_test1)
                    self.send_file_msg_by_uid(path, uid_test1)

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.is_big_contact = False   #如果确定通讯录过大，无法获取，可以直接配置，跳过检查。假如不是过大的话，这个方法可能无法获取所有的联系人
    bot.run()

if __name__ == '__main__':
    main()
