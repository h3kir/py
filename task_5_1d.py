#!/usr/bin/python3.7

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

source = input('Введите имя устройства (r1,r2 или sw1): ')
list_keys = list(london_co[source].keys())
a = ', '.join(list_keys)
param = input('Введите имя параметра (' + a +'): ')
param = param.lower()
print(london_co[source].get(param, 'Такого параметра нет'))

