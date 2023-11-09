import json
import msgpack
import os

with open('./input/products_11.json') as f:
    json_data = json.load(f)

products_result = {}
for item in json_data:
    name = item["name"]
    price = item["price"]

    if name not in products_result:
        products_result[name] = {"average_price": price, "max_price": price, "min_price": price}
    else:
        data = products_result[name]
        data["average_price"] = (data["average_price"] + price) / 2
        data["max_price"] = max(data["max_price"], price)
        data["min_price"] = min(data["min_price"], price)

with open("./output/3_products_result.json", "w") as json_file:
    formatted_data = [{"name": name, **data} for name, data in products_result.items()]
    json.dump(formatted_data, json_file, indent=2)

with open("./output/3_products_result.msgpack", "wb") as msgpack_file:
    packed_data = msgpack.packb(products_result)
    msgpack_file.write(packed_data)

print(f"Размер json: {os.path.getsize('./output/3_products_result.json')}")
print(f"Размер msgpack: {os.path.getsize('./output/3_products_result.msgpack')}")
