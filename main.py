from sshdropbear.sshdropbear import sshdropbear
from sshdropbear.scraping import ScrapingSSHDropbear
from createssh.createssh import createssh
from bestssh.bestssh import bestssh
from skyssh.skyssh import skyssh
from skyssh.scraping import ScrapingSKYSSH
from fullssh.fullssh import fullssh
from sshudp.sshudp import sshudp
import telepot, time
from telepot.loop import MessageLoop
from telepot.delegate import per_message, create_open, pave_event_space


welcome = """
=============== SSH Generator =======================
Welcome in SSH Generator for Gretongers Maniak
Donation Bitcoin Address : 1CzPAYiF8PRuYGHBTw5MkAoTTLEXjvnamW
Tanks for join here.
=======================================================
"""

help = """
========= How to using =============
First you must run command /start on @username_bot
Server List : sshdropbear, createssh, skyssh
Command : /ssh
Help Command : /ssh sshdropbear help
Example : /ssh sshdropbear sg-do2
Many requests : /ssh sshdropbear sg-do2 10 (Request count is 10, auto break if server full)
Note : bestssh blm dapat ditambahkan masih proses pembuatan.
Donation Bitcoin Address : 1CzPAYiF8PRuYGHBTw5MkAoTTLEXjvnamW
Tanks for join here.
====================================
"""
class SSHGenerator(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(SSHGenerator, self).__init__(*args, **kwargs)
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        frm = msg['from']
        count = 1
        print msg
        user_id = frm['id']
        first_name = frm['first_name'].encode('utf-8')
        group_id = -1001104749192
        admin_id = 286281499

        ScrapingSSHDropbear().run()
        ScrapingSKYSSH().run()

        if content_type == "text":
            if chat_type == "supergroup":
                if msg['chat']['username'] == "SSHGenerator":
                    if "/ssh" in msg['text']:
                        try:
                            self.bot.sendMessage(user_id, "Please wait...")
                        except:
                            self.bot.sendMessage(group_id, help)
                            return False
                        tmp_msg = msg['text'].split()
                        if len(tmp_msg) == 4:
                            count = int(tmp_msg[3])
                            #print count
                        if len(tmp_msg) < 3:
                            self.bot.sendMessage(user_id, "Command incomplete")
                            self.bot.sendMessage(user_id, help)
                        else:
                            if "sshdropbear" in msg['text']:
                                for i in range(0, count):
                                    self.bot.sendMessage(admin_id, "Generating ssh requests from "+first_name)
                                    self.bot.sendMessage(user_id, "Generating you ssh request.....")
                                    result = sshdropbear(self.bot, tmp_msg[2], group_id, user_id, admin_id).generate(first_name)
                                    self.bot.sendMessage(admin_id, result.encode('utf-8'))
                                    self.bot.sendMessage(user_id, result.encode('utf-8'))
                                    if "Server Full" in result or "Cannot connect to server" in result:
                                        break
                            elif "createssh" in msg['text']:
                                for i in range (0, count):
                                    self.bot.sendMessage(admin_id, "Generating ssh requests from "+first_name)
                                    self.bot.sendMessage(user_id, "Generating you ssh request.....")
                                    result = createssh(self.bot, tmp_msg[2], group_id, user_id, admin_id).generate(first_name)
                                    self.bot.sendMessage(admin_id, result)
                                    self.bot.sendMessage(user_id, result)
                                    if "Server Full" in result or "Cannot connect to server" in result:
                                        break
                            elif "skyssh" in msg['text']:
                                for i in range(0, count):
                                    self.bot.sendMessage(admin_id, "Generating ssh requests from "+first_name)
                                    self.bot.sendMessage(user_id, "Generating you ssh request.....")
                                    result = skyssh(self.bot, tmp_msg[2], group_id, user_id, admin_id).generate(first_name)
                                    self.bot.sendMessage(admin_id, result)
                                    self.bot.sendMessage(user_id, result)
                                    if "Server Full" in result or "Cannot connect to server" in result:
                                        break
                            else:
                                self.bot.sendMessage(user_id, "Command incomplete")
                                self.bot.sendMessage(user_id, help)
                            self.bot.sendMessage(user_id, "Tanks for using SSHGenerator")
                    elif "/help" in msg['text']:
                        self.bot.sendMessage(group_id, help)
                else:
                    self.bot.sendMessage(frm['id'], "Please join to @SSHGenerator first")
            elif chat_type == "private":
                if "/start" in msg['text']:
                    self.bot.sendMessage(admin_id, first_name+" join to group")
                    self.bot.sendMessage(user_id, welcome)


def main():
    bot = telepot.DelegatorBot("API_BOT",[
            pave_event_space()(
                per_message(), create_open, SSHGenerator, timeout=10
            ),
        ])
    MessageLoop(bot).run_as_thread()

    # Keep the program running.
    while 1:
        time.sleep(1)
        pass


if __name__ == '__main__':
    main()
