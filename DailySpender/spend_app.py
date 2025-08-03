from docopt import docopt
from tabulate import tabulate
from api import *

usage = '''
Usage:
    spend_app.py --init
    spend_app.py --show [<category>]
    spend_app.py --add <amount> <category> [<message>]
    spend_app.py --remove <amount> <category> [<message>]
    spend_app.py --update <amount_old> <category_old> [--new-amount=<amount_new>] [--new-category=<category_new>] [--new-message=<message_new>]
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

elif args['--remove']:
    try:
        amount = float(args['<amount>'])
        category = args['<category>']
        message = args['<message>'] if args['<message>'] else None
        remove(amount, category, message)
        print("Expense removed successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

elif args['--update']:
    try:
        amount_old = float(args['<amount_old>'])
        category_old = args['<category_old>']
        amount_new = float(args['--new-amount']) if args['--new-amount'] else None
        category_new = args['--new-category']
        message_new = args['--new-message']
        
        updated = update(amount_old, category_old, amount_new, category_new, message_new)
        if updated:
            print("Expense updated successfully.")
        else:
            print("Nothing to update.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

else:
    print(usage)
