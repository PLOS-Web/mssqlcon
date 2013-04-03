# MSSQLcon

An easy to set up connection for a MSSQL database in python. Doesn't do much besides give a connection, maybe we'll expand it later.

## Setup as project
1.  clone
2.  make and activate virtualenv
3.  `pip install -r requirements.txt`

## Install as package
`pip install git+ssh://git@github.com:PLOS-Web/mssqlcon.git`

## Usage
```python
from mssqlcon import EMQueryConnection

EM_REPORTING_DATABASE = {
    'USER': 'username',
    'PASSWORD': 'password',
    'HOST': '0.0.0.0',
    'PORT': 1433,
}

with EMQueryConnection(EM_REPORTING_DATABASE) as eqc:
    print eqc.get_pubdate('pone.0050000')
    eqc.cursor.execute('USE PONE')
    eqc.cursor.execute("SELECT * FROM document d WHERE d.doi like '%pone.0050000')
    docs = self.cursor.fetchall()
    for doc in docs:
        print doc 
'''
