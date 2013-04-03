import pyodbc
import re

import logging
logger = logging.getLogger(__name__)

doi_to_em_db_name = {
    'pbio': 'PBIOLOGY',
    'pcbi': 'PCOMBIOL',
    'pgen': 'PGENETICS',
    'pmed': 'PMEDICINE',
    'pntd': 'PNTD',
    'pone': 'PONE',
    'ppat': 'PPATHOGENS',
    }

# This should rightly be added to a 'PLOS Utils' type package
def get_journal_from_doi(doi):
    match = re.match('.*(?=\.)', doi)
    
    if not match:
        raise ValueError('Could not find a journal short_name in doi, %s' % doi)
    short_name = re.match('.*(?=\.)', doi).group(0)

    try:
        return doi_to_em_db_name[short_name]
    except KeyError:
        raise ValueError("doi prefix, %s, does not match any known journal" % short_name)

class MSSQLConnection(object):
    def __init__(self, host, user, password, port=1433, database=''):
        cnx_settings = 'DRIVER={freeTDS};SERVER=%s;PORT=%d;DATABASE=%s;UID=%s;PWD=%s;TDS_VERSION=8.0' % (host, port, database, user, password)
        self.cnxn = pyodbc.connect(cnx_settings)
        self.cursor = self.cnxn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.cnxn.close()
        
class EMConnection(MSSQLConnection):
    def __init__(self, cred_dict):
        super(EMConnection, self).__init__(\
            host=cred_dict['HOST'],
            port=cred_dict['PORT'],
            user=cred_dict['USER'],
            password=cred_dict['PASSWORD'])
        self.cursor.execute('USE %s' % 'PONE')
        
class EMQueryConnection(EMConnection):
    def get_pubdate(self, doi):
        # will throw ValueError if can't figure out journal from DOI
        # will throw LookupError if EM doesn't return good data
        journal = get_journal_from_doi(doi)
        self.cursor.execute('USE %s' % journal)
        self.cursor.execute(
            """
            SELECT actual_online_pub_date
            FROM document d
            WHERE d.doi like '%%%s'
            """ % doi)
        
        r = self.cursor.fetchall()

        if len(r) == 0:
            raise LookupError("DOI: %s not found in EM" % doi)
        if len(r) > 1:
            raise LookupError("Multiple entries found for DOI: %s" % doi)
        
        return r[0][0]

def main():
    with EMQueryConnection() as emq:
        print emq.get_pubdate('pone.0053871')

if __name__ == '__main__':
    main()
