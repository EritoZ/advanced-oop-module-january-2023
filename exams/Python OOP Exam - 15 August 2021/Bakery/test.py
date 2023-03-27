from project.baked_food.bread import Bread
from project.bakery import Bakery
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

bakery = Bakery('naem')

print(bakery.add_table('InsideTable', 12, 10))
print(bakery.add_table('InsideTable', 32, 40))
print(bakery.add_food('Cake', 'Cak', 12.1))
print(bakery.add_food('Bread', 'DAd', 12.1))
print(bakery.reserve_table(30))
print(bakery.order_food(32, 'Cak', 'DAd'))
print(bakery.get_free_tables_info())