import sqlite3
from jinja2 import Environment, PackageLoader, select_autoescape, Template

conn = sqlite3.connect('test.db')
c = conn.cursor()

abc="\r\n HaHaHa!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

# main functions
def generate_pg(tt,pg):
    tex = open('sec.tex','r')
    temp = Template(tex.read())
    tt = tt[0].encode('utf-8')
    pg = pg[0].encode('utf-8')
    result = temp.render(tt=tt,pg=pg)
    return result

def generate_sec(pid,table_name):
    sec_group = ''
    pg=c.execute('''select pg from %s where pid=%s;''' %(table_name,pid)).fetchall()
    tt=c.execute('''select tt from %s where pid=%s;''' %(table_name,pid)).fetchall()
    for i in range(len(pg)):
        sec_group += generate_pg(tt=tt[i],pg=pg[i])
        sec_group += '\r'
    return sec_group

def generate_SWOT_sec(pid):
    sec_s = ''
    sec_w = ''
    sec_o = ''
    sec_t = ''
    strength = c.execute('''select pg from SWOT where pid=%s and tt='Strength';''' %(pid)).fetchall()
    weakness = c.execute('''select pg from swot where pid=%s and tt='Weakness';''' %(pid)).fetchall()
    opportunity = c.execute('''select pg from swot where pid=%s and tt='Opportunity';''' %(pid)).fetchall()
    threats = c.execute('''select pg from swot where pid=%s and tt='Threats';''' %(pid)).fetchall()
    for i in strength[0]:
        sec_s += i
        #sec_s += '\r'
    for i in weakness[0]:
        sec_w += i
        #sec_w += '\r'
    for i in opportunity[0]:
        sec_o += i
        #sec_o += '\r'
    for i in threats[0]:
        sec_t += i
        #sec_t += '\r'
    temp = open('swot_temp.tex','r')
    swot_temp = Template(temp.read())
    print sec_o
    result = swot_temp.render(strength=sec_s,weakness=sec_w,opportunity=sec_o,threats=sec_t)
    print result
    return result


    

# generate parts
disclaimer=generate_sec('1','disclaimer')
exec_sum=generate_sec('1','exec_sum')
competitor_analysis=generate_sec('1','competitoranalysis')
customer_analysis=generate_sec('1','customeranalysis')
industry_analysis=generate_sec('1','industry_analysis')
product_service=generate_sec('1', 'product_service')
SWOT = generate_SWOT_sec('1')
tex = open('template.tex','r')
temp = Template(tex.read())
result = temp.render(product_service_secs=product_service, SWOT_table=SWOT, customer_analysis_secs=customer_analysis, industry_analysis_secs=industry_analysis, competitor_analysis_secs=competitor_analysis,disclaimer_secs=disclaimer,exec_sum_secs=exec_sum)

# write result in to files
final_file = open('final_file.tex','w')
final_file.write(result)
final_file.close()

conn.close()
