import pickle
import json

with open("./input/products_11.pkl", "rb") as pkl_file:
    products_data = pickle.load(pkl_file)

with open("./input/price_info_11.json", "r") as json_file:
    new_prices_data = json.load(json_file)

price_info_dict = {}

for item in new_prices_data:
    price_info_dict[item["name"]] = item

for product in products_data:
    current_price_info = price_info_dict[product["name"]]
    method = current_price_info["method"]

    if method == "sum":
        product["price"] += current_price_info["param"]
    elif method == "sub":
        product["price"] -= current_price_info["param"]
    elif method == "percent+":
        product["price"] *= (1 + current_price_info["param"])
    elif method == "percent-":
        product["price"] *= (1 - current_price_info["param"])
    product["price"] = round(product["price"], 2)

with open("./output/4_result.pkl", "wb") as modified_pkl_file:
    pickle.dump(products_data, modified_pkl_file)
