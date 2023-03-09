# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.setdefault('e')
# print(x)

# # update(키=값)은 키가 문자열일 때만 사용할 수 있습니다. 만약 키가 숫자일 경우에는 update(딕셔너리)처럼 딕셔너리를 넣어서 값을 수정할 수 있습니다.
# x.update(e=90)
# print(x)

keys = ['a', 'b', 'c', 'd']
# x = dict.fromkeys(keys, 900)
# print(x)
# print(x.get("a"))

# make dictionary out of list
a = {key: value for key, value in dict.fromkeys(keys).items() if value != 20}

print(a)
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
print(terrestrial_planet["Venus"]["mean_radius"])


x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()
y["a"] = 90
print(y)

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

average = sum(maria.values())/len(maria)

print(average)


keys = input().split()
values = map(int, input().split())
x = dict(zip(keys, values))
# del x["delta"]
a = {key: value for key, value in x.items() if value != 30 and key != "delta"}
print(a)
