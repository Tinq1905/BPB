import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
#c.execute('''DROP TABLE exec_sum;''')

#c.execute('''CREATE TABLE exec_sum(pid INTEGER, did INTEGER PRIMARY KEY ASC, tt TEXT NOT NULL,pg TEXT NOT NULL, FOREIGN KEY (pid) REFERENCES user(pid));''')

#cont = c.execute('''SELECT * FROM exec_sum;''').fetchall()
#print cont

def delete_record(table,did):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()	
	c.execute('''DELETE FROM '%s' WHERE did='%s' ''' % (table,did))	
	conn.commit()
	conn.close()
	return 'success'

def select_record(table,pid):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''SELECT * FROM '%s' WHERE pid='%d' ''' % (table,pid))
	content = c.fetchall()
	conn.commit()
	conn.close()
	return content

delete_record('EXEC_SUM','3')

print select_record('EXEC_SUM', 1)


#print select_record('EXEC_SUM',1)

c.execute('''CREATE TABLE testtable(pid INTEGER, did INTEGER ASC, tt TEXT NOT NULL,pg TEXT NOT NULL, FOREIGN KEY (pid) REFERENCES user(pid), PRIMARY KEY (pid,did));''')
