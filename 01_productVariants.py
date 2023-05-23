from itertools import product

"""
Series: PyCodeTweets 01
Issue: generate product variants

GitHub: https://github.com/zamaniamin
Twitter: https://twitter.com/zamaniamiin
"""


def generate_product_variants2(attr):
    variants = list(product(*attr.values()))
    return variants


attributes = {
    'color': ['Red', 'Green', 'Blue'],
    'size': ['SM', 'M', 'L'],
    'material': ['Cotton', 'Polyester']
}

product_variants = generate_product_variants2(attributes)
print(product_variants)

"""
The `generate_product_variants()` function now takes an `attributes` parameter, which is expected to be a dictionary 
where the keys represent the attribute names, and the values are lists of possible values for each attribute.

In the line `variants = list(product(*attributes.values()))`, the `product()` function from the `itertools` module is used to calculate the Cartesian product of the attribute values. Let's break down this line to understand it better:

1. `attributes.values()` retrieves a view object that contains all the values from the `attributes` dictionary. The view object represents a dynamic view of the dictionary's values.

2. The `*` operator is used to unpack the values obtained from `attributes.values()`. It allows passing multiple arguments to a function. In this case, it expands the values as separate arguments.

3. The expanded values are passed as arguments to the `product()` function. The `product()` function takes multiple iterables and returns the Cartesian product of those iterables.

4. By using `*attributes.values()`, we ensure that each value from the dictionary is treated as a separate argument to the `product()` function. This is necessary because `product()` expects each iterable as a separate argument, rather than a single list or tuple.

5. The result of `product(*attributes.values())` is an iterable that contains tuples representing all possible combinations of the attribute values. Each tuple in the iterable represents a unique combination of values from different attributes.

6. Finally, `list()` is used to convert the iterable into a list, storing all the product combinations in the `variants` list.

In summary, `variants = list(product(*attributes.values()))` generates a list of tuples that represents all possible combinations of attribute values based on the given `attributes` dictionary.
"""
