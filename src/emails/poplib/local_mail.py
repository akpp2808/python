from email import parser
import getpass, poplib
'''
sudo aptitude isntall courier-authdaemon courier-authlib-mysql courier-pop courier-pop-ssl courier-imap courier-imap-ssl
maildirmake Maildir
postconf -e 'mailbox_command ='
sudo postconf -e 'home_mailbox = Maildir/'
'''




pop_conn = poplib.POP3('localhost')
pop_conn.set_debuglevel(2)
pop_conn.user(getpass.getuser())
pop_conn.pass_(getpass.getpass())

#pop_conn.user('serg@localhost')
#pop_conn.pass_('')
#pop_conn.stat()

#print dir(pop_conn)
#print pop_conn.list()[1]







print pop_conn.list()


##Get messages from server:
#messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
### Concat message pieces:
#messages = ["\n".join(mssg[1]) for mssg in messages]
###Parse message intom an email object:
#messages = [parser.Parser().parsestr(mssg) for mssg in messages]
#
#print messages
#print messages[-1]['subject']
#for message in messages:
#    print message['From']
##    print message['subject']
##pop_conn.quit()














