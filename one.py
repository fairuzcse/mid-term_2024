def flatten_dict(d, parent_key='', separator='.'):
    flat_dict = {}

    for key, value in d.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key

        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, new_key, separator))
        else:
            flat_dict[new_key] = value

    return flat_dict


nested_dict = {'a': {'b': 1}}
flattened = flatten_dict(nested_dict)
print(flattened)  # Output: {'a.b': 1}
