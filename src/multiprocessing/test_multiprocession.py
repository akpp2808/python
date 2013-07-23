
# -*- coding: utf-8 -*-
"""
filedesc: test for the chat
@author: Yura A
"""
import uuid
import json
import time
import random
import logging
import traceback
from ctypes import c_int
from itertools import ifilter as flt
from websocket import create_connection
from multiprocessing import Pool, Value, Queue, Process

# HACK
import threading
from gevent.queue import JoinableQueue
threading._DummyThread._Thread__stop = lambda x: 42

#from benchmark_utils import get_bm_config
#from minimal.chat.chat import USER_HANDLER, OPERATOR_HANDLER, USER, ANY

#QUIT = get_bm_config('QUIT')
term_flag = None
msg_queue = None


def init(term, queue):
    global term_flag
    global msg_queue
    term_flag = term
    msg_queue = queue


class AProto(object):
    """
    Ð‘Ð°Ð·Ð¾Ð²Ñ‹Ð¹ ÐºÐ»Ð°ÑÑ Ð´Ð»Ñ Ð¿Ñ€Ð¾Ñ‚Ð¾ÐºÐ¾Ð»Ð¾Ð².
    Ð£Ð¼ÐµÐµÑ‚ Ð²Ð»Ð°Ð´ÐµÑ‚ÑŒ Ð²ÐµÐ±ÑÐ¾ÐºÐµÑ‚Ð¾Ð¼
    """
    def __init__(self, uri_args):
        self.ws = create_connection(
            'ws://%(host)s:%(port)s%(ws)s'
            % uri_args)

    def open_channel(self):
        pkg = {'pkg':
               {'action': 'open',
                'data':
                {'channel': self.channel_name,
                 'token': '@'}}}
        req = json.dumps(pkg)
        logging.debug('>> %s', req)
        self.ws.send(req)
        response = self.ws.recv()
        logging.debug('<< %s', response)
        #assert response == '{"pkg": {"action": "open", "data": ' \
        #    '{"closable": true, "result": 200, "channel": "%s"}}}' \
        #    % self.channel_name

    def say(self, action, data='#'):
        pkg = {'pkg':
               {'action': action,
                'data': data},
               'chid': self.channel_name}
        req = json.dumps(pkg)
        if action != 'msg':  # reduce output
            logging.debug('%s>> %s', action, req)
        self.ws.send(req)
        response = json.loads(self.ws.recv())
        if not 'pkg' in response:
            logging.error('bad response: %s', response)
            return 
        if not 'data' in response['pkg']:
            logging.error('bad response: %s', response)
            return 
        if not response['pkg']['data']:  # reduce output
            logging.debug('<< %s', response)
        return self.parse(response)

    def parse(self, response):
        pass


class UserProto(AProto):
    """
    ÑƒÐ¼ÐµÐµÑ‚:
      * ÑÐ¾Ð·Ð´Ð°Ð²Ð°Ñ‚ÑŒ room;
      * Ð¾Ñ‚Ð¿Ñ€Ð°Ð²Ð»ÑÑ‚ÑŒ ÑÐ¾Ð¾Ð±Ñ‰ÐµÐ½Ð¸Ñ;
      * Ð¿Ñ€Ð¸Ð½Ð¸Ð¼Ð°Ñ‚ÑŒ ÑÐ¾Ð¾Ð±Ñ‰ÐµÐ½Ð¸Ñ;
      * Ð·Ð°ÐºÑ€Ñ‹Ð²Ð°Ñ‚ÑŒ room;
    """
    def __init__(self, *args, **kw):
        self.channel_name = USER_HANDLER
        super(UserProto, self).__init__(*args, **kw)

    def parse(self, response):
        ack = response['pkg']['data']
        assert ack

    def start(self):
        self.open_channel()

    def call(self):
        self.say('call')

    def msg(self, text):
        self.say('msg', text)

    def bye(self):
        self.say('bye')


class AdminProto(AProto):
    """
    ÑƒÐ¼ÐµÐµÑ‚:
      * Ð—Ð°Ð¿Ñ€Ð¾Ñ world:
         * user_rooms: cÐ¿Ð¸ÑÐ¾Ðº user rooms
         * admin_rooms: cÐ¿Ð¸ÑÐ¾Ðº admin rooms
         * talk: cÐ¿Ð¸ÑÐ¾Ðº Msg Ð² Room
         * users: cÐ¿Ð¸ÑÐ¾Ðº User
         * admins: cÐ¿Ð¸ÑÐ¾Ðº Admin
         * info: Ð´ÐµÑ‚Ð°Ð»Ð¸ userÐ° Ð¸Ð· Ñ‚ÐµÐºÑƒÑ‰ÐµÐ³Ð¾ talk
      * delta - Ð¸Ð·Ð¼ÐµÐ½ÐµÐ½Ð¸Ñ Ð¿Ð¾ ÑÐ¿Ð¸ÑÐºÐ°Ð¼ Ð²Ñ‹ÑˆÐµ (ÐºÑ€Ð¾Ð¼Ðµ talk)
        *** talk Ð¿Ñ€Ð¸Ñ…Ð¾Ð´Ð¸Ñ‚ Ð² realtime
      * call - ÑƒÐ¼ÐµÐµÑ‚ Ð¾Ñ‚ÐºÑ€Ñ‹Ð²Ð°Ñ‚ÑŒ Room
      * attach - ÐŸÐ¾Ð´Ð¿Ð¸ÑÑ‹Ð²Ð°Ñ‚ÑŒÑÑ Ð½Ð° Room == ÐŸÐ¾Ð´Ð¿Ð¸ÑÑ‹Ð²Ð°Ñ‚ÑŒÑÑ Ð½Ð° UserDetail
      * bye - ÐžÑ‚Ð¿Ð¸ÑÐ°Ñ‚ÑŒÑÑ Ð¾Ñ‚ Room, Room Ð·Ð°ÐºÑ€Ð¾ÐµÑ‚ÑÑ
              Ð¸ ÑÐ¾Ñ…Ñ€Ð°Ð½Ð¸Ñ‚ Ñ‡Ð°Ñ‚-Ð»Ð¾Ð³ ÐµÑÐ»Ð¸ Ð²ÑÐµ ÑƒÑˆÐ»Ð¸
      * msg - Ð¾Ñ‚Ð¿Ñ€Ð°Ð²Ð»ÑÐµÑ‚ Msg
    """
    def __init__(self, *args, **kw):
        self.channel_name = OPERATOR_HANDLER
        self.fields = ['users',
                       'admins',
                       'talk',
                       'admin_rooms',
                       'user_rooms',
                       'userinfo']
        for x in self.fields:
            setattr(self, x, [])
        super(AdminProto, self).__init__(*args, **kw)

    def parse(self, response):
        response_action = response['pkg']['action']
        data = response['pkg']['data']
        
        if response_action == 'world':
            for x in self.fields:
                if x in data:
                    setattr(self, x, data[x])
        elif response_action == 'delta':
            for x in self.fields:
                if x in data:
                    slot = data[x]
                    print '>>>', id(self), dir(self)
                    col = getattr(self, str(x), None)
                    if col is None:
                        logging.error('%s:%s field does not exist',
                                      id(self), x)
                    repl = lambda line: col.__setitem__(
                        col.index(flt(
                            lambda el: el['id'] == line['id'],
                            col).next()), line)
                    for sign, op in [('+', col.append),
                                     ('-', col.remove),
                                     ('*', repl)]:
                        if sign in slot:
                            op(slot[sign])
        elif response_action == 'msg':
            pass

    def start(self):
        self.open_channel()

    def world(self):
        self.say('world')

    def call(self, user):
        # create room
        self.say('call', user)

    def msg(self, text):
        self.say('msg', text)

    def attach(self, room):
        self.say('attach', room)

    def bye(self):
        self.say('bye')


import redis
queue = JoinableQueue()
rc = redis.Redis()
channel_name = 'bla-bla'


def visit(_args):
    global term_flag
    global msg_queue
    try:
        logging.debug('visit')
        print 'args', _args, _args % 2
        pubsub = rc.pubsub()
        pubsub.subscribe(channel_name)
        print 'listen ch:', channel_name
        for msg in pubsub.listen():
            data = msg['data']
            if msg['type'] == 'message':
                print 'data:', data, _args

    except KeyboardInterrupt:
        logging.info('terminating...')
        term.value = 1
    except Exception as e:
        traceback.print_exc()
        logging.error(e)
    return True


def run_test(*args):
#    logins = get_bm_config('ADMINS') 
#    logins.extend([get_bm_config('API_USER_PREFIX') % i
#                   for i in xrange(args['proc'])])
#    msg_count = get_bm_config('MSG_COUNT')
#    host = args['host']
#    port = args['port']
#    visit_args = [(login, host, port, msg_count) for login in logins]
    visit_args = [[i] for i in [1, 2]]
    term = Value(c_int, 0)
    queue = Queue()
    logging.debug('users pool')
    pool = Pool(initializer=init,
                initargs=(term, queue),
                processes=10,
                maxtasksperchild=1)
    try:
        swarm = pool.map(visit, [i for i in range(10)])
        logging.debug('finishing...')
    except KeyboardInterrupt:
        logging.info('terminating...')
        term.value = 1
        pool.terminate()


if __name__ == '__main__':
    run_test()