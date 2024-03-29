import sqlite3

def insert_record(table,pid,tt,pg):
	tt = tt.replace("'","''")
	pg = pg.replace("'","''")
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''INSERT INTO '%s' (pid,tt,pg) VALUES ('%d','%s','%s')''' % (table,pid,tt,pg))
	conn.commit()
	conn.close()
	return 'success'

def update_record(table,did,tt,pg):
	tt = tt.replace("'","''")
	pg = pg.replace("'","''")
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''UPDATE'%s' SET tt='%s',pg='%s' WHERE did='%s' ''' % (table,tt,pg,did))
	conn.commit()
	conn.close()
	return 'success'

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

###

def insert_risk(table,pid,des,likelihood,impact,rating,strat):
	des = des.replace("'","''")
	strat = strat.replace("'","''")
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''INSERT INTO '%s' (pid,des,likelihood,impact,rating,strat) VALUES ('%d','%s','%s','%s','%s','%s')''' % (table,pid,des,likelihood,impact,rating,strat))
	conn.commit()
	conn.close()
	return 'success'

def update_risk(table,did,des,likelihood,impact,rating,strat):
	des = des.replace("'","''")
	strat = strat.replace("'","''")
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''UPDATE'%s' SET des='%s',likelihood='%s',impact='%s',rating='%s',strat='%s' WHERE did='%s' ''' % (table,des,likelihood,impact,rating,strat,did))
	conn.commit()
	conn.close()
	return 'success'

def delete_risk(table,did):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''DELETE FROM '%s' WHERE did='%s' ''' % (table,did))
	conn.commit()
	conn.close()
	return 'success'

def select_risk(table,pid):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''SELECT * FROM '%s' WHERE pid='%d' ''' % (table,pid))
	content = c.fetchall()
	conn.commit()
	conn.close()
	return content

###

def update_info(pid,c_name,p_name,e_addr,p_addr,num,industry):
	c_name = c_name.replace("'","''")
	p_name = p_name.replace("'","''")
	e_addr = e_addr.replace("'","''")
	p_addr = p_addr.replace("'","''")
	industry = industry.replace("'","''")
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''UPDATE INFO SET c_name='%s',p_name='%s',e_addr='%s',p_addr='%s',num='%s', industry='%s' WHERE pid='%s' ''' % (c_name,p_name,e_addr,p_addr,num,industry,pid))
	conn.commit()
	conn.close()
	return 'success'

def insert_info(pid,c_name,p_name,e_addr,p_addr,num,industry):
	c_name = c_name.replace("'","''")
	p_name = p_name.replace("'","''")
	e_addr = e_addr.replace("'","''")
	p_addr = p_addr.replace("'","''")
	industry = industry.replace("'","''")
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''INSERT INTO INFO (pid, c_name,p_name,e_addr,p_addr,num,industry) VALUES ('%s','%s','%s','%s','%s','%s','%s')''' %(pid, c_name,p_name,e_addr,p_addr,num,industry))
	conn.commit()
	conn.close()
	return 'success'
###

def insert_item(pid,name,price,cost,num,inc):
	name = name.replace("'","''")
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''INSERT INTO ITEM (pid,name,price,cost,num,inc) VALUES ('%s','%s','%s','%s','%s','%s')''' % (pid,name,price,cost,num,inc))
	conn.commit()
	conn.close()
	return 'success'

def select_item(pid):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''SELECT * FROM ITEM WHERE pid='%d' ''' % (pid))
	content = c.fetchall()
	conn.commit()
	conn.close()
	return content

###

def insert_expense(pid,monHours,monRate,tueHours,tueRate,wedHours,wedRate,thuHours,thuRate,friHours,friRate,satHours,satRate,sunHours,sunRate,rent,elec,gas,water,wifi,tele,cont,pub,other,fitout,dep,mer,equip,acqui,bankrate,monnew,mondig,socmedia,seo,account,bkeeper,legal,cons,exps):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''INSERT INTO 'expense' VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (pid,monHours,monRate,tueHours,tueRate,wedHours,wedRate,thuHours,thuRate,friHours,friRate,satHours,satRate,sunHours,sunRate,rent,elec,gas,water,wifi,tele,cont,pub,other,fitout,dep,mer,equip,acqui,bankrate,monnew,mondig,socmedia,seo,account,bkeeper,legal,cons,exps))
	conn.commit()
	conn.close()
	return 'success'

def update_expense(pid,monHours,monRate,tueHours,tueRate,wedHours,wedRate,thuHours,thuRate,friHours,friRate,satHours,satRate,sunHours,sunRate,rent,elec,gas,water,wifi,tele,cont,pub,other,fitout,dep,mer,equip,acqui,bankrate,monnew,mondig,socmedia,seo,account,bkeeper,legal,cons,exps):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''UPDATE 'expense' SET monHours='%s',monRate='%s',tueHours='%s',tueRate='%s',wedHours='%s',wedRate='%s',thuHours='%s',thuRate='%s',friHours='%s',friRate='%s',satHours='%s',satRate='%s',sunHours='%s',sunRate='%s',rent='%s',elec='%s',gas='%s',water='%s',wifi='%s',tele='%s',cont='%s',pub='%s',other='%s',fitout='%s',dep='%s',mer='%s',equip='%s',acqui='%s',bankrate='%s',monnew='%s',mondig='%s',socmedia='%s',seo='%s',account='%s',bkeeper='%s',legal='%s',cons='%s',exps='%s' WHERE pid='%s' ''' % (monHours,monRate,tueHours,tueRate,wedHours,wedRate,thuHours,thuRate,friHours,friRate,satHours,satRate,sunHours,sunRate,rent,elec,gas,water,wifi,tele,cont,pub,other,fitout,dep,mer,equip,acqui,bankrate,monnew,mondig,socmedia,seo,account,bkeeper,legal,cons,exps,pid))
	conn.commit()
	conn.close()
	return 'success'

###

def insert_past(table,pid,sales,cogs,revenue,expense):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''INSERT INTO '%s' VALUES ('%s','%s','%s','%s','%s')''' % (table,pid,sales,cogs,revenue,expense))
	conn.commit()
	conn.close()
	return 'success'

def update_past(table,pid,sales,cogs,revenue,expense):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''UPDATE '%s' SET sales='%s',cogs='%s',revenue='%s',expense='%s' where pid='%s' ''' % (table,sales,cogs,revenue,expense,pid))
	conn.commit()
	conn.close()
	return 'success'

def delete_past(table,pid):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''DELETE FROM '%s' WHERE pid='%s' ''' % (table,pid))
	conn.commit()
	conn.close()
	return 'success'

###

def select_all(table):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	result = c.execute('''select * from '%s' ''' % (table)).fetchall()
	conn.commit()
	conn.close()
	return result

def add_account(name,password):
	name = name.replace("'","''")
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''insert into user(email,password) values ('%s','%s') ''' % (name,password))
	conn.commit()
	conn.close()
	return 'success'

def change_psw(pid,password):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('''update user set password = '%s' where id = '%s' ''' % (password,pid))
	conn.commit()
	conn.close()
	return 'success'

def validate_content(*arg):
	for i in arg:
		if len(i)== 0:
			return False
	return True
