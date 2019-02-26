import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
	print(msg)
	return '对方并不想鸟你，并竖起了中指。'

itchat.auto_login()
itchat.run()