def linear_search_product(product_list, target_product):
  indices = []

  for index, product in enumerate(product_list):
    if product == target_product:
      indices.append(index)

  if not indices:
    print(f"'{target_product}' not found in the list.")
  else:
    print(f"Indices of '{target_product}' found in the list: {indices}")


# Example usage:
products = ["Apple", "Banana", "Orange", "Grape"]
target = input(
    "Enter Target to find: ")  # Change the target to a product not in the list
linear_search_product(products, target)
