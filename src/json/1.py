import json
str = '{"Action": "init", "Result": {"gsid": "1515", "Balance": 10, "credit": 0}}}, "chid": 2}'
str = {'errorCode': 0, 'Data': {'Action': 'set_balance', 'Result': {'Balance': 1}}}
str = '{"Action": "set_balance", "Result": {"Balance": 1}}'
print type(str)
print json.loads('{"foo": "bar", "a":"b"}')
print json.loads(str)
#print json.loads('{"Action": "init","a" {"x":"y"} "chid": 2}')
