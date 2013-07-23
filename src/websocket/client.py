'''
Created on May 8, 2013

@author: serg
'''


import websocket
import thread
import time
import json
import uuid
import gevent

def on_message(ws, message):
    print 'message', message

def on_error(ws, error):
    print 'error', error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
#    def run(*args):
#        for i in range(1):
        action = 'open'
        pkg = {'pkg':
               {'action': action,
                'data':
                {'channel': 'support',
                 'token': 'bf420b533f814079b5da20369991b509'}}}
        req = json.dumps(pkg)
#        msg = {'action': 'msg', 'data': {'text': 'Hello %d' % 0}}
#            print 'msg', msg
        ws.send(req)
#        time.sleep(1)
#        time.sleep(3)
#        ws.close()
        print "thread terminating..."
#    thread.start_new_thread(run, ())

def _listener(self):
    def run():
        while self.keep_running:
#            raw_data = self.ws.recv()
            raw_data = self.sock.recv()
            print 'raw_data::', raw_data
        else:
            'EXIT'
    thread.start_new_thread(run, ())
#                self.RECV.append(parse_action(raw_data))
#    return gevent.spawn(_listener)


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp('ws://127.0.0.1:8080/game/api/ws/',
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
#    ws.on_message = lambda data: 1/0
    _listener(ws)
    ws.run_forever()
    time.sleep(0.5)
    ws.close()