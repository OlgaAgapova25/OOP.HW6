from Hot_drinks import *
from Hot_drinks_machine import *

drink1 = Hot_drinks('tea', 250, 85)
drink2 = Hot_drinks('coffee', 250, 80)

list_drinks = Hot_drinks_machine()
list_drinks.init_product(drink1)
list_drinks.get_product(drink1)

