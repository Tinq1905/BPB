import sqlite3
from jinja2 import Environment, PackageLoader, select_autoescape, Template

conn = sqlite3.connect('test.db')
c = conn.cursor()

abc="\r\n HaHaHa!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

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

disclaimer=generate_sec('1','disclaimer')
exec_sum=generate_sec('1','exec_sum')
competitor_analysis=generate_sec('1','competitoranalysis')
tex = open('template.tex','r')
temp = Template(tex.read())
result = temp.render(competitor_analysis_secs=competitor_analysis,disclaimer_secs=disclaimer,exec_sum_secs=exec_sum)
final_file = open('final_file.tex','w')
final_file.write(result)
final_file.close()
