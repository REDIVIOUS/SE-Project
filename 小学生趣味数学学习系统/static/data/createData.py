import json
import random
import time

# dumps：将python中的 字典 转换为 字符串
# test_dict = {'bigberg': [
#     7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
# print(test_dict)
# print(type(test_dict))
# #dumps 将数据转换成字符串
# json_str = json.dumps(test_dict)
# print(json_str)
# print(type(json_str))

# # loads: 将 字符串 转换为 字典
# new_dict = json.loads(json_str)
# print(new_dict)
# print(type(new_dict))

# # dump: 将数据写入json文件中
# with open("../config/record.json", "w") as f:
#     json.dump(new_dict, f)
#     print("加载入文件完成...")

# # load:把文件打开，并把字符串变换为数据类型
# with open("../config/record.json", 'r') as load_f:
#     load_dict = json.load(load_f)
#     print(load_dict)
# load_dict['smallberg'] = [8200, {1: [['Python', 81], ['shirt', 300]]}]
# print(load_dict)

# with open("../config/record.json", "w") as dump_f:
#     json.dump(load_dict, dump_f)

# random.seed()
add10 = [{"num1": i, "num2": j, "op": "add", "res": i+j}
         for i in range(10) for j in range(i, 10)]
add100 = [{"num1": i, "num2": j, "op": "add", "res": i+j}
          for i in range(100) for j in range(i, 100) if random.randint(1, 30) == 1]
sub10 = [{"num1": i, "num2": j, "op": "sub", "res": i-j} for i in range(10) for j in range(0, i+1)]
sub100 = [{"num1": i, "num2": j, "op": "sub", "res": i-j}
          for i in range(100) for j in range(0, i+1) if random.randint(1, 30) == 1]
mul10 = [{"num1": i, "num2": j, "op": "mul", "res": i*j}
         for i in range(10) for j in range(i, 10)]
mul100 = [{"num1": i, "num2": j, "op": "mul", "res": i*j}
          for i in range(100) for j in range(i, 100) if random.randint(1, 30) == 1]
div10 = [{"num1": i, "num2": j, "op": "div", "res": i//j, "rem": i%j}
         for i in range(0, 10) for j in range(1, 10)]
div100 = [{"num1": i, "num2": j, "op": "div", "res": i//j, "rem": i % j}
          for i in range(100) for j in range(1, 100) if random.randint(1, 30) == 1]
div100_no_rem = [{"num1": i, "num2": j, "op": "div", "res": round(i/j, 1), "rem": i % j}
          for i in range(100) for j in range(1, 100) if random.randint(1, 30) == 1]


data_dict = {
    'easy': {
        'add10': {
            "numbers": len(add10),
            "data": random.sample(add10, len(add10))
        },
        "add100": {
            "numbers": len(add100),
            "data": random.sample(add100, len(add100))
        },
        "sub10": {
            "numbers": len(sub10),
            "data": random.sample(sub10, len(sub10))
        },
        "sub100": {
            "numbers": len(sub100),
            "data": random.sample(sub100, len(sub100))
        },
        "mul10": {
            "numbers": len(mul10),
            "data": random.sample(mul10, len(mul10))
        },
        "mul100": {
            "numbers": len(mul100),
            "data": random.sample(mul100, len(sub100))
        },
        "div10": {
            "numbers": len(div10),
            "data": random.sample(div10, len(div10))
        },
        "div100": {
            "numbers": len(div100),
            "data": random.sample(div100, len(div100))
        }
    },
    "medium": {

    }
}

with open("./class.json", "w") as dump_f:
    json.dump(data_dict, dump_f)
