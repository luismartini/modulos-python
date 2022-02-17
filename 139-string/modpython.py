from string import Template
from datetime import datetime

with open(r"D:\udemy-python\est\modulos-python\string\modelo.html", 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Luís', data=data_atual)

print(corpo_msg)