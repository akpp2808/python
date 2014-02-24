# -*- coding: utf-8 -*-
"""
Created on Sep 23, 2013
filedesc:
@author: serg
"""
import unittest

transactions = [
{'id': 1, 'money': 1000, 'wagering_req': None, 'ttype': 'Deposit', 'req_sum': 0, 'ingame': 0, 'balance': 1000},
{'id': 2, 'money': 0, 'wagering_req': None, 'ttype': 'GameTransaction', 'stake': 1000, 'req_sum': 0, 'ingame': 0, 'balance': 1000},  # draw
#выдаем первый бонус
{'id': 3, 'money': 100, 'wagering_req': 2, 'ttype': 'BonusTransaction', 'req_sum': 200, 'ingame': 0, 'balance': 1100},
{'id': 4, 'money': 0, 'wagering_req': None, 'ttype': 'GameTransaction', 'stake': 300, 'req_sum': 0, 'ingame': 300, 'balance': 1100},
# #списываеи первый бонус
{'id': 5, 'money': -100, 'wagering_req': 2, 'ttype': 'BonusCancelled', 'bonus_dist_id': 3, 'req_sum': 0, 'ingame': 0, 'balance': 1000},
# # #выдаем второй бонус
{'id': 6, 'money': 1000, 'wagering_req': 1, 'ttype': 'BonusTransaction', 'req_sum': 1000, 'ingame': 0, 'balance': 2000},
# # #списываеи второй бонус
# {'id': 7, 'money': -100, 'wagering_req': 1, 'ttype': 'BonusCancelled', 'bonus_dist_id': 5, 'req_sum': 0, 'ingame': 0, 'balance': 1000},
{'id': 8, 'money': 0, 'wagering_req': None, 'ttype': 'GameTransaction', 'stake': 500, 'req_sum': 500, 'ingame': 500, 'balance': 2000},  # draw
    ]

bonus_types = ('BonusTransaction', 'BonusCancelled')


class TestWageringRequirements(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_wagering_req_sum(self):
        wagering_req_sum = 0
        balance = 0
        bonuses_idx = []
        calc_gaming_sum = False
        ingame_gainings_sum = 0

        for t in transactions:
#             print 'id', t['id']
            balance += t['money']

            #calc ingame_gainings
            print t['ttype'], calc_gaming_sum
            if calc_gaming_sum and t['ttype'] == 'GameTransaction':
                #считаем только в том случае если был выдан бонус
                ingame_gainings_sum += t['stake']

            #calc wagering req sum
            if t['ttype'] in bonus_types:
                ingame_gainings_sum = 0
                if t['ttype'] == 'BonusTransaction':
                    calc_gaming_sum = True
                    bonuses_idx.append(t['id'])
                if t['ttype'] == 'BonusCancelled':
                    calc_gaming_sum = False
                    bonuses_idx.pop(bonuses_idx.index(t['bonus_dist_id']))
                    pass
                wagering_req_sum += t['wagering_req'] * t['money']

            wagering_req_sum -= ingame_gainings_sum
            if wagering_req_sum < 0:
                wagering_req_sum = 0

            #TODO: нет бонусов - нет смысла считать игровые деньги
            #check wagering_req_sum
            self.assertEqual(wagering_req_sum, t['req_sum'])
            #check ingame_gainings
            self.assertEqual(ingame_gainings_sum, t['ingame'])
            #check balance
            self.assertEqual(balance, t['balance'])

            print '#', t['id'], 'ingame', ingame_gainings_sum, 'sum', wagering_req_sum, 'b', balance

if __name__ == '__main__':
    unittest.main()
