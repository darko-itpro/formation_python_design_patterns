def third_free(price:float, quantity:int=1):
    """
    Le troisième gratuit
    """
    return price * (quantity - quantity // 3)


def second_half_price(price:float, quantity:int=1):
    """
    Le second à 50%
    """
    return (price * (quantity // 2) * 1.5) + (price * (quantity % 2))

products_list = [['Kit Kat', 3.5, 2],
                 ['Choucroute', 7, 6],
                 ['Madeleines', 6.5, 3],
                 ['Sardines', 4, 5],
                 ['Pates', 5, 4]]


active_promotions = {'Kit Kat': second_half_price,
                     'Choucroute': third_free,
                     'Madeleines': second_half_price,
                     'Sardines': third_free,
                     'Pates': third_free}

for product, price, quantity in products_list:
    print(product, active_promotions[product](price, quantity))

def display_ckeck(products_list, active_promotions):
    PRODUCT = "{:15} (x{:2}) : {:8.2f} €"
    SUM = "Total {:26.2f} €"

    print('-' * 33)
    print("{:^33}\n".format('PyCa$h Store'))

    for product_entry in products_list:
        product, price, quantity = product_entry
        total_price = active_promotions.get(product,
                                            lambda price, quantity: price * quantity)(price, quantity)
        product_entry.append(total_price)  # (2)

        print(PRODUCT.format(product,
                             quantity,
                             total_price))

    print("-" * 33)
    print(SUM.format(sum([p[-1] for p in products_list])))


active_promotions = {'Kit Kat': second_half_price,
                     'Madeleines': second_half_price,
                     'Pates': third_free}

display_ckeck(products_list, active_promotions)