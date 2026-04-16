from smartphone import Smartphone
catalog = []

phone1 = Smartphone("Samsung", "Galaxy S26", "+79102345678")
phone2 = Smartphone("Realme", "16 Pro+", "+79113456789")
phone3 = Smartphone("Huawey", "Pupa 90", "+79124567890")
phone4 = Smartphone("Xiaomi", "17 Pro Max", "+79135678901")
phone5 = Smartphone("Honor", "Magic8 Pro", "+79157890123")

catalog.extend ([phone1, phone2, phone3, phone4, phone5])
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")