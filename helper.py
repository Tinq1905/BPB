import db_func

## generate table for budget module
def generate_table(pid):
	item = db_func.select_record('ITEM',pid)
	## number of items
	num = len(item)
	expense = db_func.select_record('expense',pid)
	if num==0 or expense==[]:
		return []
	sell=[]
	cost=[]
	totalsell=[]
	totalcost=[]
	totalgrossprofit=[]
	totalexpenses=[]
	labour=[]
	weeklabour=0
	merchant=[]
	other=[]
	gross_profit=[]
	net_profit=[]
	sum_sell=[]
	sum_cost=[]
	sum_gross_profit=[]
	sum_totalgrossprofit=[]
	sum_totalsell=[]
	sum_totalcost=[]
	sum_merchant=0
	sum_other=0
	sum_totalexpenses=[]
	sum_netprofit=[]

	rent = (expense[0][15])/12
	utility = (expense[0][16]+expense[0][17]+expense[0][18]+expense[0][19]+expense[0][20])
	insurance = round((expense[0][21]+expense[0][22]+expense[0][23])/12,2)
	fitout = (expense[0][24]/expense[0][25])
	financing = round(((expense[0][27]+expense[0][28])*expense[0][29]/100)/12,2)
	subscription = expense[0][30]+expense[0][31]
	marketing = (expense[0][32]+expense[0][33])
	pro = (expense[0][34]+expense[0][35]+expense[0][36]+expense[0][37])

	for i in [0,2,4,6,8,10,12]:
		weeklabour += (expense[0][1:15][i]*expense[0][1:15][i+1])
	labour = (weeklabour*4)
	for i in item:
		a=[]
		for j in range(0,12):
			b=i[3]*i[5]*28*((1+(i[6])*0.01)**j)
			a.append(round(b,2))
		sell.append(a)
	for j in range(0,12):
		a = 0
		for i in sell:
			a += i[j]
		totalsell.append(a)
	for i in totalsell:
		merchant.append(round(i*expense[0][26]*0.01,2))
	for i in item:
		a=[]
		for j in range(0,12):
			b=i[3]*i[5]*28*((1+(i[6])*0.01)**j)*0.01*i[4]
			a.append(round(b,2))
		cost.append(a)
	for j in range(0,12):
		a = 0
		for i in cost:
			a += i[j]
		totalcost.append(a)
	for i in item:
		a=[]
		for j in range(0,12):
			b=i[3]*i[5]*28*((1+(i[6])*0.01)**j)*0.01*(100-i[4])
			a.append(round(b,2))
		gross_profit.append(a)
	for j in range(0,12):
		a = 0
		for i in gross_profit:
			a += i[j]
		totalgrossprofit.append(a)
	for i in totalsell:
		other.append(round((i*expense[0][38]*0.01),2))
	for i in sell:
		sum_sell.append(sum(i))
	for i in cost:
		sum_cost.append(sum(i))
	for i in gross_profit:
		sum_gross_profit.append(sum(i))
	for j in range(0,12):
		totalexpenses.append(labour+rent+utility+insurance+financing+subscription+marketing+pro+merchant[j]+other[j])
	for j in range(0,12):
		net_profit.append(totalgrossprofit[j]-totalexpenses[j])
	sum_totalsell=sum(totalsell)
	sum_totalcost=sum(totalcost)
	sum_totalgrossprofit=sum(totalgrossprofit)
	sum_other=sum(other)
	sum_merchant=sum(merchant)
	sum_totalexpenses=sum(totalexpenses)
	sum_netprofit=sum_totalgrossprofit-sum_totalexpenses


	return {'num':num,'sell':sell,'cost':cost,'gross_profit':gross_profit, 'totalsell':totalsell,'totalcost':totalcost,'labour':labour,'rent':rent, 'utility':utility,'insurance':insurance,'fitout':fitout,'financing':financing,'subscription':subscription,'marketing':marketing,'pro':pro,'merchant':merchant,'other':other,'sum_sell':sum_sell,'sum_cost':sum_cost,'sum_other':sum_other,'sum_merchant':sum_merchant,'sum_totalsell':sum_totalsell,'sum_totalcost':sum_totalcost,'sum_gross_profit':sum_gross_profit,'totalgrossprofit':totalgrossprofit,'sum_totalgrossprofit':sum_totalgrossprofit,'totalexpenses':totalexpenses,'sum_totalexpenses':sum_totalexpenses,'net_profit':net_profit,'sum_netprofit':sum_netprofit}
