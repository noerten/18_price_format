import argparse


def parse_price():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', type=float, help='Enter a price you want to format')
    return parser.parse_args()


def prettify_price(price):
    if int(price) == float(price):
        decimals = 0
    else:
        decimals = 2
    return '{0:,.{1}f}'.format(price, decimals).replace(",", " ")


def format_price(price):
    try:
        int(price)
    except ValueError:
        return None
    else:
        return prettify_price(price)

if __name__ == '__main__':
    user_price = parse_price().price
    print(format_price(user_price))


