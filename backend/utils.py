import re


def camelize(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])


def snakeize(camel_str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def transform_dict_keys(d, keyer):
    if isinstance(d, dict):
        nd = {}
        for key, value in d.items():
            transformed_key = keyer(key)
            nd[transformed_key] = transform_dict_keys(value, keyer)
    elif isinstance(d, list):
        nd = [transform_dict_keys(el, keyer) for el in d]
    else:
        nd = d
    return nd


def camelize_dict_keys(d):
    return transform_dict_keys(d, keyer=camelize)


def snakeize_dict_keys(d):
    return transform_dict_keys(d, keyer=snakeize)
