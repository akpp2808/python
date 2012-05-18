
import re
txt = 'http://192.168.154.113:8080/static/operator/games/framework/img/loss.png'
txt = 'http://192.168.154.113:8080/static/operator/games/magician/../framework/img/win.png'


print re.compile('loss.png').search(txt)


