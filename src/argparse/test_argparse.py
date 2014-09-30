# -*- coding: utf-8 -*-
"""
Created on Sep 8, 2013
filedesc:
@author: serg
"""

import argparse

parser = argparse.ArgumentParser(description='apply transaction for user.')
parser.add_argument('--user_id', dest='uid', required=True)
parser.add_argument('--amount', type=int, dest='amount', required=True)
parser.add_argument('--currency_id', type=int, dest='currency_id', default=1,
                    help='default currency_id=1')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print dir(args),
print type(args)
print args.uid, type(args.uid)
print args.amount, type(args.amount)
print args.currency_id, type(args.currency_id)
# print args.accumulate(args.integers)
