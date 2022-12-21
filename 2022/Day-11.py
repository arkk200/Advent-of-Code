from math import floor
from typing import TypedDict

num = 8
monkey_list = []

for i in range(num):
    monkey_info: dict = {}
    monkey_info["monkey_num"] = int(input()[7])
    monkey_info["items"] = list(map(int, input()[18:].split(', ')))
    monkey_info["operation"] = input()[13:]
    monkey_info["division_by"] = int(input()[21:])
    monkey_info["if_true"] = int(input()[29:])
    monkey_info["if_false"] = int(input()[30:])
    monkey_info["inspect_count"] = 0
    monkey_list.append(monkey_info)
    getchar: str = input()

class ItemsCount(TypedDict):
    items: list
    inspect_count: int

def test(monkey_obj: dict, order: int) -> None:
    global monkey_list
    for item in monkey_obj["items"]:
        ldict= {}
        exec(f"old = {item}; {monkey_obj['operation']}", globals(), ldict)
        new: int = ldict["new"] // 3
        if new % monkey_obj["division_by"] == 0:
            monkey_list[monkey_obj["if_true"]]["items"].append(new)
        else:
            monkey_list[monkey_obj["if_false"]]["items"].append(new)
        monkey_list[order]["inspect_count"] += 1
    monkey_obj["items"] = []



for i in range(20):
    for j in range(num):
        test(monkey_list[j], j)
    for k, v in enumerate(monkey_list):
        print(f"{k}: {v['items']} count : {v['inspect_count']}")

arr = [i["inspect_count"] for i in monkey_list]
arr.sort(reverse=True)
print(arr[0] * arr[1])