# -*- coding: utf-8 -*-
"""
Created on Oct 18, 2014
filedesc:
@author: sergey.g
"""
import time

from noodles.utils.fixtures import Fixture
from noodles.utils.logger import log


class DBFixture(Fixture):
    def __init__(self, destination, session):
        self.destination = destination
        self.session = session
        self.raw_data = {}
        self.mapped_data = {}

    def prepare_data(self):
        self._prepare_mapped_data()

        values = self.mapped_data.values()
        if values and getattr(values[0], 'id', None):
            values.sort(key=lambda o: o.id)
        return values

    def load(self):
        log.info(
            'Load fixtures data for %s, %s', self.destination, time.time())
        map(self.session.add, self.prepare_data())
        self.session.commit()  # commit point
        if hasattr(self.session, 'remove'):
            self.session.remove()
        else:
            self.session.close()


class TestTransactionData(DBFixture):
    """Transaction test fixture"""

    #noinspection PyClassicStyleClass,PyClassHasNoInit
    class FirstTransactions:
        money = 10
        balance = 10
