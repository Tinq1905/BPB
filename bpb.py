from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from flask import send_file
import generate_doc
import sqlite3
import db_func
import helper
import os
import sys


app = Flask(__name__)
app.secret_key = 'Trconsulting'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#entry of the website
@app.route('/')
def main():
	return render_template('main.html')

#backend sys for BPB
@app.route('/admin',methods=['GET'])
def admin():
	if login_status(session,0):
		result = db_func.select_all('user')
		return render_template('admin.html',data=result)
	else:
		return redirect('/login')

#Add a user to the system
@app.route('/add',methods=['POST'])
def add():
	if login_status(session,0):
		name = request.form['name']
		password = request.form['psw']
		db_func.add_account(name,password)
		flash('Successfully added a new account')
		return redirect('/admin')
	else:
		return redirect('/login')

#Change psw
@app.route('/psw',methods=['POST'])
def changepsw():
	if login_status(session,0):
		pid = request.form['pid']
		password = request.form['psw']
		db_func.change_psw(pid,password)
		flash('Successfully changed the password')
		return redirect('/admin')
	else:
		return redirect('/login')

#Login window
@app.route('/login',methods=('GET','POST'))
def login():
	if request.method == 'GET':
		return render_template('login.html')
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		print email,password
		id = suc_login(email, password)
		if (id == []):
			session['logged_in'] = False
			flash('Failed to login')
			return redirect(url_for('login'))
		else:
			session['logged_in'] = True
			session['project_number'] = id[0]
			pid = id[0]
			if pid[0]==0:
				return redirect('/admin')
			else:
				flash('You were successfully logged in')
				return redirect('/%d/info' % pid )

#Logout window
@app.route('/logout', methods=['GET'])
def logout():
	session.clear()
	return redirect(url_for('main'))

#download the pdf
@app.route('/<int:pid>/sendpdf',methods=['GET'])
def sendpdf(pid):
	print 'aaa'
	pid = str(session['project_number'][0])
	print 'aaa'
	generate_doc.generate_doc(pid)
	file_name = pid + '.pdf'
	docdir = os.path.join('pdf',file_name)
	return send_file(docdir)

@app.route('/<int:pid>/info',methods=['GET','POST'])
def info(pid):
	if login_status(session,pid):
		if request.method == 'GET':
			data=db_func.select_record('info',pid)
			return render_template('info.html',data=data)
		elif request.method == 'POST':
			c_name = request.form['theName']
			p_name = request.form['projectName']
			e_addr = request.form['theEmail']
			p_addr = request.form['postAddr']
			num = request.form['phoneNum']
			industry = request.form['theIndustry']
			if db_func.validate_content(db_func.select_record('info',pid)):
				db_func.update_info(pid,c_name,p_name,e_addr,p_addr,num,industry)
				flash('successfully update !')
				return redirect('/%d/info' % pid)
			else:
				db_func.insert_info(pid, c_name,p_name,e_addr,p_addr,num,industry)
				flash('successfully insert !')
				return redirect('/%d/info' % pid)
		else:
			return redirect(url_for('login'))
	return redirect(url_for('login'))

@app.route('/<int:pid>/customeranalysis',methods=['GET','POST'])
def customeranalysis(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_record('customeranalysis',pid)
				return render_template('customeranalysis.html', data=data)
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				db_func.insert_record('customeranalysis',pid,tt,pg)
				flash('successfully insert !')
				return redirect('/%d/customeranalysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/customeranalysis/update',methods=['GET','POST'])
def customeranalysis_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				did = request.form['did']
				db_func.update_record('customeranalysis',did,tt,pg)
				flash('successfully update !')
				return redirect('/%d/customeranalysis' % pid)
			else:
				return redirect('/%d/customeranalysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/customeranalysis/delete',methods=['GET','POST'])
def customeranalysis_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				did = request.form['did']
				db_func.delete_record('customeranalysis',did)
				flash('successfully deleted !')
				return redirect('/%d/customeranalysis' % pid)
			else:
				return redirect('/%d/customeranalysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/competitoranalysis',methods=['GET','POST'])
def competitoranalysis(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_record('competitoranalysis',pid)
				return render_template('competitoranalysis.html', data=data)
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				db_func.insert_record('competitoranalysis',pid,tt,pg)
				flash('successfully insert !')
				return redirect('/%d/competitoranalysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/competitoranalysis/update',methods=['GET','POST'])
def competitoranalysis_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				did = request.form['did']
				db_func.update_record('competitoranalysis',did,tt,pg)
				flash('successfully update !')
				return redirect('/%d/competitoranalysis' % pid)
			else:
				return redirect('/%d/competitoranalysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/competitoranalysis/delete',methods=['GET','POST'])
def competitoranalysis_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				did = request.form['did']
				db_func.delete_record('competitoranalysis',did)
				flash('successfully deleted !')
				return redirect('/%d/competitoranalysis' % pid)
			else:
				return redirect('/%d/competitoranalysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/SWOT',methods=['GET','POST'])
def SWOT(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_record('SWOT',pid)
				return render_template('swot.html', data=data)
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				db_func.insert_record('SWOT',pid,tt,pg)
				flash('successfully insert !')
				return redirect('/%d/SWOT' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/SWOT/update',methods=['GET','POST'])
def SWOT_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				did = request.form['did']
				db_func.update_record('SWOT',did,tt,pg)
				flash('successfully update !')
				return redirect('/%d/SWOT' % pid)
			else:
				return redirect('/%d/SWOT' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/SWOT/delete',methods=['GET','POST'])
def SWOT_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				print request.form
				did = request.form['did']
				db_func.delete_record('SWOT',did)
				flash('successfully deleted !')
				return redirect('/%d/SWOT' % pid)
			else:
				return redirect('/%d/SWOT' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))


@app.route('/<int:pid>/product_service',methods=['GET','POST'])
def product_service(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_record('product_service',pid)
				return render_template('product_service.html', data=data)
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				db_func.insert_record('product_service',pid,tt,pg)
				flash('successfully insert !')
				return redirect('/%d/product_service' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/product_service/update',methods=['GET','POST'])
def product_service_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				did = request.form['did']
				db_func.update_record('product_service',did,tt,pg)
				flash('successfully update !')
				return redirect('/%d/product_service' % pid)
			else:
				return redirect('/%d/product_service' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/product_service/delete',methods=['GET','POST'])
def product_service_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				did = request.form['did']
				db_func.delete_record('product_service',did)
				flash('successfully deleted !')
				return redirect('/%d/product_service' % pid)
			else:
				return redirect('/%d/product_service' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/law_reg',methods=['GET','POST'])
def law_reg(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_record('law_reg',pid)
				return render_template('law_reg.html', data=data)
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				db_func.insert_record('law_reg',pid,tt,pg)
				flash('successfully insert !')
				return redirect('/%d/law_reg' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/law_reg/update',methods=['GET','POST'])
def law_reg_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				did = request.form['did']
				db_func.update_record('law_reg',did,tt,pg)
				flash('successfully update !')
				return redirect('/%d/law_reg' % pid)
			else:
				return redirect('/%d/law_reg' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/law_reg/delete',methods=['GET','POST'])
def law_reg_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				print request.form
				did = request.form['did']
				db_func.delete_record('law_reg',did)
				flash('successfully deleted !')
				return redirect('/%d/law_reg' % pid)
			else:
				return redirect('/%d/law_reg' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/industry_analysis',methods=['GET','POST'])
def industry_analysis(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_record('industry_analysis',pid)
				return render_template('industry_analysis.html', data=data)
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				db_func.insert_record('industry_analysis',pid,tt,pg)
				flash('successfully insert !')
				return redirect('/%d/industry_analysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/industry_analysis/update',methods=['GET','POST'])
def industry_analysis_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				did = request.form['did']
				db_func.update_record('industry_analysis',did,tt,pg)
				flash('successfully update !')
				return redirect('/%d/industry_analysis' % pid)
			else:
				return redirect('/%d/industry_analysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/industry_analysis/delete',methods=['GET','POST'])
def industry_analysis_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				print request.form
				did = request.form['did']
				db_func.delete_record('industry_analysis',did)
				flash('successfully deleted !')
				return redirect('/%d/industry_analysis' % pid)
			else:
				return redirect('/%d/industry_analysis' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/disclaimer',methods=['GET','POST'])
def disclaimer(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_record('disclaimer',pid)
				return render_template('disclaimer.html', data=data)
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				db_func.insert_record('disclaimer',pid,tt,pg)
				flash('successfully insert !')
				return redirect('/%d/disclaimer' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/disclaimer/update',methods=['GET','POST'])
def disclaimer_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				did = request.form['did']
				db_func.update_record('disclaimer',did,tt,pg)
				flash('successfully update !')
				return redirect('/%d/disclaimer' % pid)
			else:
				return redirect('/%d/disclaimer' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/disclaimer/delete',methods=['GET','POST'])
def disclaimer_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				print request.form
				did = request.form['did']
				db_func.delete_record('disclaimer',did)
				flash('successfully deleted !')
				return redirect('/%d/disclaimer' % pid)
			else:
				return redirect('/%d/disclaimer' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/exec_sum',methods=['GET','POST'])
def exec_sum(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_record('exec_sum',pid)
				return render_template('exec_sum.html', data=data)
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				db_func.insert_record('exec_sum',pid,tt,pg)
				flash('successfully insert !')
				return redirect('/%d/exec_sum' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/exec_sum/update',methods=['GET','POST'])
def exec_sum_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				tt = request.form['tt']
				pg = request.form['pg']
				did = request.form['did']
				db_func.update_record('exec_sum',did,tt,pg)
				flash('successfully update !')
				return redirect('/%d/exec_sum' % pid)
			else:
				return redirect('/%d/exec_sum' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/exec_sum/delete',methods=['GET','POST'])
def exec_sum_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				print request.form
				did = request.form['did']
				db_func.delete_record('exec_sum',did)
				flash('successfully deleted !')
				return redirect('/%d/exec_sum' % pid)
			else:
				return redirect('/%d/exec_sum' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/risk',methods=['GET','POST'])
def risk(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				data = db_func.select_risk('risk',pid)
				return render_template('risk.html', data=data)
			if request.method == 'POST':
				des = request.form['des']
				likelihood = request.form['likelihood']
				impact = request.form['impact']
				rating = request.form['rating']
				strat = request.form['strat']
				db_func.insert_risk('risk',pid,des,likelihood,impact,rating,strat)
				flash('successfully insert !')
				return redirect('/%d/risk' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/risk/update',methods=['GET','POST'])
def risk_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				did = request.form['did']
				des = request.form['des']
				likelihood = request.form['likelihood']
				impact = request.form['impact']
				rating = request.form['rating']
				strat = request.form['strat']
				db_func.update_risk('risk',did,des,likelihood,impact,rating,strat)
				flash('successfully update !')
				return redirect('/%d/risk' % pid)
			else:
				return redirect('/%d/risk' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/risk/delete',methods=['GET','POST'])
def risk_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'POST':
				did = request.form['did']
				db_func.delete_record('risk',did)
				flash('successfully deleted !')
				return redirect('/%d/risk' % pid)
			else:
				return redirect('/%d/risk' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/budget',methods=['GET','POST'])
def budget(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				itemData = db_func.select_item(pid)
				expenseData = db_func.select_record('expense',pid)
				table = helper.generate_table(pid)
				past1 = db_func.select_record('firstyear',pid)
				past2 = db_func.select_record('secondyear',pid)
				past = [past1,past2]
				print past
				data = [itemData,expenseData,table,past]
				return render_template('budget.html', data=data)
			if request.method == 'POST':
				pass
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/item',methods=['POST'])
def item(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				return render_template('budget.html')
			if request.method == 'POST':
				name = request.form['name']
				price = request.form['price']
				num = request.form['num']
				cost = request.form['cost']
				inc = request.form['inc']
				db_func.insert_item(pid,name,price,cost,num,inc)
				flash('successfully insert !')
				return redirect('/%d/budget' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

@app.route('/<int:pid>/item/delete',methods=['GET','POST'])
def item_delete(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				return render_template('budget.html')
			if request.method == 'POST':
				did = request.form['did']
				db_func.delete_record('ITEM',did)
				flash('successfully delete !')
				return redirect('/%d/budget' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

#past data insert and update
@app.route('/<int:pid>/past',methods=['POST'])
def past(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			action = request.form['action']
			if action =='update':
				print request.form['sales']
				sales = request.form['sales']
				cogs = request.form['cogs']
				revenue = request.form['revenue']
				expense = request.form['expense']
				table = request.form['table']
				if db_func.validate_content(db_func.select_record(table,pid)):
					db_func.update_past(table,pid,sales,cogs,revenue,expense)
					flash('successfully update !')
					return redirect('/%d/budget' % pid)
				else:
					db_func.insert_past(table,pid,sales,cogs,revenue,expense)
					flash('successfully insert !')
					return redirect('/%d/budget' % pid)
			if action == 'delete':
				table = request.form['table']
				db_func.delete_past(table,pid)
				flash('successfully delete !')
				return redirect('/%d/budget' % pid)
			else:
				pass
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))



@app.route('/<int:pid>/budget/update',methods=['GET','POST'])
def budget_update(pid):
	if 'logged_in' in session:
		if (session['logged_in'] == True):
			if request.method == 'GET':
				return redirect('/%d/budget' % pid)
			if request.method == 'POST':
				monHours = request.form['monHours']
				monRate = request.form['monRate']
				tueHours = request.form['tueHours']
				tueRate = request.form['tueRate']
				wedHours = request.form['wedHours']
				wedRate = request.form['wedRate']
				thuHours = request.form['thuHours']
				thuRate = request.form['thuRate']
				friHours = request.form['friHours']
				friRate = request.form['friRate']
				satHours = request.form['satHours']
				satRate = request.form['satRate']
				sunHours = request.form['sunHours']
				sunRate = request.form['sunRate']
				rent = request.form['rent']
				elec = request.form['elec']
				gas = request.form['gas']
				water = request.form['water']
				wifi = request.form['wifi']
				tele = request.form['tele']
				cont = request.form['cont']
				pub = request.form['pub']
				other = request.form['other']
				fitout = request.form['fitout']
				dep = request.form['dep']
				mer = request.form['mer']
				equip = request.form['equip']
				acqui = request.form['acqui']
				bankrate = request.form['bankrate']
				monnew = request.form['monnew']
				mondig = request.form['mondig']
				socmedia = request.form['socmedia']
				seo = request.form['seo']
				account = request.form['account']
				bkeeper = request.form['bkeeper']
				legal = request.form['legal']
				cons = request.form['cons']
				exps = request.form['exps']
				if db_func.validate_content(db_func.select_record('expense',pid)):
					db_func.update_expense(pid,monHours,monRate,tueHours,tueRate,wedHours,wedRate,thuHours,thuRate,friHours,friRate,satHours,satRate,sunHours,sunRate,rent,elec,gas,water,wifi,tele,cont,pub,other,fitout,dep,mer,equip,acqui,bankrate,monnew,mondig,socmedia,seo,account,bkeeper,legal,cons,exps)
					flash('successfully update !')
					return redirect('/%d/budget' % pid)
				else:
					db_func.insert_expense(pid,monHours,monRate,tueHours,tueRate,wedHours,wedRate,thuHours,thuRate,friHours,friRate,satHours,satRate,sunHours,sunRate,rent,elec,gas,water,wifi,tele,cont,pub,other,fitout,dep,mer,equip,acqui,bankrate,monnew,mondig,socmedia,seo,account,bkeeper,legal,cons,exps)
					flash('successfully insert !')
					return redirect('/%d/budget' % pid)
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))

# login and get id
def suc_login(email,password):
	info = [email,password]
	def getone(info):
		conn = sqlite3.connect('test.db')
		c = conn.cursor()
		id = c.execute('''SELECT id FROM user WHERE email = ? AND password = ? ''',info).fetchall()
		conn.close()
		return id
	return getone(info)

# login status validation
def login_status(session,pid):
	if 'logged_in' in session:
		if session['logged_in'] == True and session['project_number'][0] == pid:
			return True
		else:
			return False
	return False

# Service start
if __name__=='__main__':
	app.run(debug=True,port=8000)
