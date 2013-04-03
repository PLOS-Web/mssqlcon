from __future__ import absolute_import

import unittest

from ..api import *
from .settings import EM_REPORTING_DATABASE

class TestEMQueryConnection(unittest.TestCase):
    def test_get_journal_from_doi(self):
        f = get_journal_from_doi
        with self.assertRaises(ValueError):
            f('fake.000000')
        with self.assertRaises(ValueError):
            f('00000')
        self.assertEqual(f('pbio.'), 'PBIOLOGY')
        self.assertEqual(f('pone.000000000000'), 'PONE')

    def test_em_query_connection(self):
        # naive exception test
        with EMQueryConnection(EM_REPORTING_DATABASE) as eqc:
            eqc.get_pubdate('pone.0050000')

