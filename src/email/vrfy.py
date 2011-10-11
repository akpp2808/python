import smtplib

#server = smtplib.SMTP('smtp.gmail.com', 587)
server = smtplib.SMTP('localhost')

server.set_debuglevel(False) # show communication with the server
try:
    dhellmann_result = server.verify('serg09822227@gmail.com')
    
    #notthere_result = server.verify('notthere')
finally:
    server.quit()

print 'dhellmann:', dhellmann_result
#print 'notthere :', notthere_result