import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

#c.execute('''CREATE TABLE user(pid INTEGER PRIMARY KEY ASC, email varchar(250) NOT NULL, password varchar(250) NOT NULL)''')
#c.execute('''CREATE TABLE EXEC_SUM (FOREIGN KEY(pid) REFERENCES user(pid),did INTEGER ASC, tt TEXT NOT NULL, pg TEXT NOT NULL, PRIMARY KEY (pid,did))''')
c.execute('''CREATE TABLE DISCLAIMER(pid INTEGER, did INTEGER PRIMARY KEY, tt TEXT NOT NULL, pg TEXT NOT NULL, FOREIGN KEY (pid) REFERENCES user(id))''')
c.execute('''CREATE TABLE PRODUCT_SERVICE(pid INTEGER, did INTEGER PRIMARY KEY, tt TEXT NOT NULL, pg TEXT NOT NULL,FOREIGN KEY (pid) REFERENCES user(id))''')
c.execute('''CREATE TABLE INDUSTRY_ANALYSIS(pid INTEGER, did INTEGER PRIMARY KEY, tt TEXT NOT NULL, pg TEXT NOT NULL, FOREIGN KEY (pid) REFERENCES user(id))''')
c.execute('''CREATE TABLE LAW_REG(pid INTEGER, did INTEGER PRIMARY KEY, tt TEXT NOT NULL, pg TEXT NOT NULL,FOREIGN KEY (pid) REFERENCES user(id))''')
c.execute('''CREATE TABLE SWOT(pid INTEGER, did INTEGER PRIMARY KEY, tt TEXT NOT NULL, pg TEXT NOT NULL, FOREIGN KEY (pid) REFERENCES user(id))''')
c.execute('''CREATE TABLE CUSTOMERANALYSIS(pid INTEGER, did INTEGER PRIMARY KEY, tt TEXT NOT NULL, pg TEXT NOT NULL, FOREIGN KEY (pid) REFERENCES user(id))''')
c.execute('''CREATE TABLE COMPETITORANALYSIS(pid INTEGER, did INTEGER PRIMARY KEY, tt TEXT NOT NULL, pg TEXT NOT NULL, FOREIGN KEY (pid) REFERENCES user(id))''')
c.execute('''CREATE TABLE RISK(pid INTEGER, did INTEGER PRIMARY KEY, des TEXT NOT NULL, likelihood VARCHAR NOT NULL, impact VARCHAR NOT NULL, rating VARCHAR NOT NULL, strat TEXT NOT NULL)''')
c.execute('''CREATE TABLE ITEM(pid INTEGER, did INTEGER PRIMARY KEY, name VARCHAR NOT NULL, price INTEGER, cost INTEGER, num INTEGER, inc INTEGER)''')
c.execute('''CREATE TABLE EXPENSE(pid INTEGER PRIMARY KEY, monHours INTEGER, monRate INTEGER, tueHours INTEGER, tueRate INTEGER,wedHours INTEGER, wedRate INTEGER, thuHours INTEGER, thuRate INTEGER,friHours INTEGER, friRate INTEGER, satHours INTEGER, satRate INTEGER,sunHours INTEGER, sunRate INTEGER, rent INTEGER, elec INTEGER, gas INTEGER, water INTEGER, wifi INTEGER, tele INTEGER, cont INTEGER, pub INTEGER, other INTEGER, fitout INTEGER, dep INTEGER, mer INTEGER,equip INTEGER,acqui INTEGER,bankrate INTEGER, monnew INTEGER, mondig INTEGER, socmedia INTEGER, seo INTEGER, account INTEGER, bkeeper INTEGER, legal INTEGER, cons INTEGER, exps INTEGER )''')


c.execute('''drop table disclaimer''')
c.execute('''drop table PRODUCT_SERVICE''')
c.execute('''drop table INDUSTRY_ANALYSIS''')
c.execute('''drop table LAW_REG''')
c.execute('''drop table SWOT''')
c.execute('''drop table customeranalysis''')
c.execute('''drop table competitoranalysis''')
