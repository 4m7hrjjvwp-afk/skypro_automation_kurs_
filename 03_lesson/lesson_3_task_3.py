from address import Address
from mailing import Mailing

to_address = Address(603000, "Nizhniy Novgorod", "Maksima Gorkogo", 115, 123)
from_address = Address(101000, "Moskow", "Myasnickaya", 20, 11)
cost = 3000
track = 49450051450097
mailing = Mailing(to_address, from_address, cost, track)
print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. Стоимость {mailing.cost} рублей.")