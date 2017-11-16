import sqlite3
import os
from jinja2 import Environment, PackageLoader, select_autoescape, Template
from helper import generate_table
import subprocess


# main functions
def generate_pg(tt,pg):
    tex = open('sec.tex','r')
    temp = Template(tex.read())
    tt = tt[0]
    pg = pg[0]
    result = temp.render(tt=tt,pg=pg)
    return result

def generate_sec(pid,table_name):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    sec_group = ''
    pg=c.execute('''select pg from %s where pid=%s;''' %(table_name,pid)).fetchall()
    tt=c.execute('''select tt from %s where pid=%s;''' %(table_name,pid)).fetchall()
    for i in range(len(pg)):
        sec_group += generate_pg(tt=tt[i],pg=pg[i])
        sec_group += '\r'
    conn.commit()
    conn.close()
    return sec_group

def generate_SWOT_sec(pid):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    sec_s = ''
    sec_w = ''
    sec_o = ''
    sec_t = ''
    strength = c.execute('''select pg from SWOT where pid=%s and tt='Strength';''' %(pid)).fetchall()
    weakness = c.execute('''select pg from swot where pid=%s and tt='Weakness';''' %(pid)).fetchall()
    opportunity = c.execute('''select pg from swot where pid=%s and tt='Opportunity';''' %(pid)).fetchall()
    threats = c.execute('''select pg from swot where pid=%s and tt='Threats';''' %(pid)).fetchall()
    for i in strength:
        sec_s += i[0]
        sec_s += '\\newline'+'\n'
    for i in weakness:
        sec_w += i[0]
        sec_w += '\\newline' +'\n'
    for i in opportunity:
        sec_o += i[0]
        sec_o += '\\newline'+'\n'
    for i in threats:
        sec_t += i[0]
        sec_t += '\\newline'+'\n'
    temp = open('swot_temp.tex','r')
    swot_temp = Template(temp.read())
    result = swot_temp.render(strength=sec_s,weakness=sec_w,opportunity=sec_o,threats=sec_t)
    conn.commit()
    conn.close()
    return result

def generate_risk_rows(pid):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    risks = c.execute('''select * from risk where pid = %s''' %(pid)).fetchall()
    risk_temp = open('risk_row.tex','r')
    temp = Template(risk_temp.read())
    result = ''
    for i in risks:
        result += temp.render(risk_d=i[2],risk_l=i[3],risk_i=i[4],risk_r=i[5],risk_m=i[6])
    conn.commit()
    conn.close()
    return result

def generate_risk_sec(rows):
    risk_temp = open('risk_temp.tex','r')
    temp = Template(risk_temp.read())
    result = temp.render(risk_rows=rows)
    return result

def generate_budget_rows(pid):
    result = ''
    budget_row = open('budget_row.tex','r')
    temp = Template(budget_row.read())
    budget = generate_table(pid)
    print budget
    if budget == []:
        print 'no budget'
        return '\\\\'
    result += temp.render(name='Total Sell',data=' & '.join(str(v) for v in budget['totalsell']),total=str(budget['sum_totalsell']))
    result += temp.render(name='Total COGS',data=' & '.join(str(v) for v in budget['totalcost']),total=str(budget['sum_totalcost']))
    result += temp.render(name='Gross Profit',data=' & '.join(str(v) for v in budget['totalgrossprofit']),total=str(budget['sum_totalgrossprofit']))
    result += temp.render(name='Labour',data=' & '.join(str(budget['labour']) for v in range(0,12)),total=str(budget['labour']*12))
    result += temp.render(name='Rent',data=' & '.join(str(budget['rent']) for v in range(0,12)),total=str(budget['rent']*12))
    result += temp.render(name='Utility',data=' & '.join(str(budget['utility']) for v in range(0,12)),total=str(budget['utility']*12))
    result += temp.render(name='Insurance',data=' & '.join(str(budget['insurance']) for v in range(0,12)),total=str(budget['insurance']*12))
    result += temp.render(name='Merchant Fee',data=' & '.join(str(v) for v in budget['merchant']),total=str(budget['sum_merchant']))
    result += temp.render(name='Financing Expense',data=' & '.join(str(budget['financing']) for v in range(0,12)),total=str(budget['financing']*12))
    result += temp.render(name='Subscription',data=' & '.join(str(budget['subscription']) for v in range(0,12)),total=str(budget['subscription']*12))
    result += temp.render(name='Marketing',data=' & '.join(str(budget['marketing']) for v in range(0,12)),total=str(budget['marketing']*12))
    result += temp.render(name='Professional Fee',data=' & '.join(str(budget['pro']) for v in range(0,12)),total=str(budget['pro']*12))
    result += temp.render(name='Others',data=' & '.join(str(v) for v in budget['other']),total=str(budget['sum_other']))
    result += temp.render(name='Total Expenses',data=' & '.join(str(v) for v in budget['totalexpenses']),total=str(budget['sum_totalexpenses']))
    result += temp.render(name='Net Profit',data=' & '.join(str(v) for v in budget['net_profit']),total=str(budget['sum_netprofit']))
    return result
def generate_budget_sec(rows):
    budget_temp = open('budget_temp.tex','r')
    temp = Template(budget_temp.read())
    return temp.render(budget_rows=rows)

### generate past chart 
def generate_past_chart(rows):
    if rows == False:
        return ''
    chart_temp = open('past.tex','r')
    temp = Template(chart_temp.read())
    return temp.render(rows=rows[0],legend=rows[1])
    
def generate_past_row(pid):
    result = ''
    legend = ''
    past_row = open('past_row.tex','r')
    temp = Template(past_row.read())
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    past1 = c.execute('''select * from 'firstyear' where pid = '%d';''' %(pid)).fetchall()
    past2 = c.execute('''select * from 'secondyear' where pid = '%d';''' %(pid)).fetchall()
    print 'here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',past1,past2
    conn.close()
    if past1 !=[]:
        result += temp.render(sales=past1[0][1],cogs=past1[0][2],revenue=past1[0][3],expense=past1[0][4])
        legend += 'Last Year'
    if past2 !=[]:
        result += temp.render(sales=past2[0][1],cogs=past2[0][2],revenue=past2[0][3],expense=past2[0][4])
        legend += ',Second last Year'
    print result
    if result == '':
        return False
    return [result,legend]
    
def generate_doc(pid):
    # generate parts
    disclaimer=generate_sec(pid,'disclaimer')
    exec_sum=generate_sec(pid,'exec_sum')
    competitor_analysis=generate_sec(pid,'competitoranalysis')
    customer_analysis=generate_sec(pid,'customeranalysis')
    industry_analysis=generate_sec(pid,'industry_analysis')
    product_service=generate_sec(pid, 'product_service')
    SWOT = generate_SWOT_sec(pid)
    risk = generate_risk_sec(generate_risk_rows(pid))
    budget = generate_budget_sec(generate_budget_rows(int(pid)))
    past = generate_past_chart(generate_past_row(int(pid)))
    print past
    tex = open('template.tex','r')
    temp = Template(tex.read())
    result = temp.render(budget_table=budget,past_chart=past,product_service_secs=product_service, SWOT_table=SWOT,risks_table=risk, customer_analysis_secs=customer_analysis, industry_analysis_secs=industry_analysis, competitor_analysis_secs=competitor_analysis,disclaimer_secs=disclaimer,exec_sum_secs=exec_sum)


    # write result in to files
    file_name = pid + '.tex'
    docdir = os.path.join('pdf',file_name)
    final_file = open(docdir,'w')
    final_file.write(result.encode('utf-8'))
    final_file.close()
    tex_file_name = pid +'.tex'
    tex_dir = os.path.join('pdf',tex_file_name)
    pdf_file_name = pid + '.pdf'
    pdf_dir = os.path.join('pdf',pdf_file_name)
    print 'before execution'
    subprocess.call(['pdflatex','-output-directory', 'pdf',tex_dir])