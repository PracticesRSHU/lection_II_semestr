import sqlite3

class Database1:
    def __init__(self,**args):
        self.filename = args.get('filename')
        self.table = args.get('table','test')

    def sql_do(self,sql,*params):
        self._db.execute(sql,params)

    def insert(self,row):
        self._db.execute('insert into {}(t1,i1)values(?,?)'.format(self._table),(row['t1'],row['i1']))

    def retrieve(self,key):
        cursor = self._db.execute('select * from {} where i1 = ?'.format(self._table),(key,))
        return dict(cursor.fetchone())

    def update(self,row):
        self._db.execute('update {} set t1 = ? where i1 = ?'.format(self._table),(row['t1'],row['i1']))

    def delete(self,key):
        self._db.execute('delete from {} where i1 = ?'.format(self._table),(key,)) #<<<<< Amended

    def __iter__(self):
        cs = self._db.execute('select * from {} order by i1'.format(self._table))
        for i in cs:
            yield dict(i)       #no dict

    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self,fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): return self._table

    @table.setter
    def table(self,T): self._table = T

    @table.deleter
    def table(self): self._table = "test"

    def close(self):
        self._db.close()
        del self._filename

def main():
    table = "test"
    db = Database1(filename = "dbfile.db",table = table) #<<<<< Optional use the single value previously defined

    db.sql_do('drop table if exists ' + table) #<<<<< Amended
    db.sql_do('create table ' + table + '(t1 text,i1 int)') #<<<<< Amended

    print('Insert data')
    db.insert(dict(t1 = 'one',i1 = 1))
    db.insert(dict(t1 = 'two',i1 = 2))
    db.insert(dict(t1 = 'three',i1 = 3))
    for disp in db: print(disp)

    print('Retrieve data')
    print(db.retrieve(1),db.retrieve(2),db.retrieve(3))

    print('Updateed data')
    db.update(dict(t1 = 'amir',i1 = 1))
    db.update(dict(t1 = 'reza',i1 = 2))
    for disp in db: print(disp)

    print('deleteed data')
    db.delete(3)
    db.delete(1)
    for disp in db: print(disp)

main()