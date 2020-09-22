import decimal


def decimal2str(deci, style):
    return str(decimal.Decimal(deci).quantize(decimal.Decimal(style)))