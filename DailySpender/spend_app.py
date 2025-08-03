from docopt import docopt
from tabulate import tabulate
from api import *

usage = '''
usage:
    spend_app.py --init
    spend_app.py --show [<category>]
    spend_app.py --add <category> [<message>]
    
'''

args = docopt(usage)

if args ['--init']:
    create_table()
    print('Your Table has been initialized')
if args ['--show']:
    category = args['<category>']
    amount, results = show(category)
    print(f'Total expenses: {amount}')
    print(tabulate(results, headers=['Date', 'Amount', 'Message'], tablefmt='orgtbl'))
    
if args ['--add']:
    try:
        amount = float(args['<category>'])
        add(amount, args['<category>'], args['<message>'])
        print('Expense added successfully')
    except :
        print(usage)
        
        