stockDict = { 
    'GE': 'General Electric',
    'GM': 'General Motors',
    'CAT':'Caterpillar', 
    'EK':"Eastman Kodak" }

purchases = [ 
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 ) ]


def create_purchase_report(x):
    '''Create Purchase Report
    Returns a string formatted in the following fashion :
    General Electric : 100 Shares at 48 Dollars : Total = 4800

    Arguments :
    x -- a tuple formatted in the following fashion :
    ( 'GE', 100, '10-sep-2001', 48 )

    Joins in data from stockDict
    '''
    return f"{stockDict[x[0]]} : {x[1]} Shares at {x[3]} Dollars : Total = {x[1] * x[3]}"

purchase_report = [create_purchase_report(x) for x in purchases]

for line in purchase_report:
    print(line)

purchase_report_2 = {}

# Define a function to print the purchase report
def print_1(self):
    for symbol, value in self["data"].items():
        print(f"{symbol} : {value}")

# Add the print function as a key on the purchase report dict
purchase_report_2['print'] = print_1

# Use dictionary comprehension to create a list of unique stock symbols as a data property on the dict
purchase_report_2['data'] = { x: 0 for x in set(stockDict.keys())}

# Iterate over the purchases tuples and add stock quantites to the corresponding entry in the purchase_report_2 dict
for purchase in purchases:
    purchase_report_2['data'][purchase[0]] += purchase[1]

# Call the print function -- and pass itself in??
purchase_report_2['print'](purchase_report_2)

