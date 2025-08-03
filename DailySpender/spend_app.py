from docopt import docopt
from tabulate import tabulate
from api import *

usage = '''
Usage:
    spend_app.py --init
    spend_app.py --show [<category>]
    spend_app.py --add <amount> <category> [<message>]
'''

args = docopt(usage)

if args['--init']:
    create_table()
    print('Your table has been initialized.')

elif args['--show']:
    category = args['<category>']
    total, records = show(category)
    print(f'Total expenses: {total}')
    print(tabulate(records, headers=['Date', 'Amount', 'Message'], tablefmt='orgtbl'))

elif args['--add']:
    try:
        amount = float(args['<amount>'])
        category = args['<category>']
        message = args['<message>'] if args['<message>'] else ''
        add(amount, category, message)
        print('Expense added successfully.')
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
else:
    print(usage)
