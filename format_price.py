import argparse


def parse_price():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', type=float, help='Enter a price you want to format')
    return parser.parse_args()


def prettify_int(int_price):
    return '{:,}'.format(int_price).replace(",", " ")


def format_price(price):
    try:
        int_price = int(price)
    except ValueError:
        return None
    else:
        return prettify_int(int_price)


if __name__ == '__main__':
    user_price = parse_price().price
    print(format_price(user_price))

    
