import poplib
from email import parser

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('sergey.g@ezscratch.com')
pop_conn.pass_('123')









#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
## Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
##Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
print messages[-1]['subject']
#for message in messages:
#    print message['subject']
#pop_conn.quit()














