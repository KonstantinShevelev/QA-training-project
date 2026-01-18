def get_as_float(data_dict, key):
    try:
        value = float(data_dict[key])
        print(f"Success {value}")
        return value
    except KeyError:
        print(f"Error. Key '{key}' not found")
    except ValueError:
        print(f"Error. Cannot turn the value on the key '{key}' to a number")

data = {"price": "10.5", "id": "abc"}

new_value = get_as_float(data, "price")
get_as_float(data, "id")
get_as_float(data, "amount")
print(new_value)

