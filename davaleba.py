import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }


# creating Product objects
product1 = Product("PC", 5000, 10)
product2 = Product("Playstation_5", 2000, 15)
product3 = Product("Xbox", 1800, 12)
product4 = Product("Sega", 200, 10)

products_list = [product1, product2, product3, product4]

# serializing products list


def serialize_products(products):
    if isinstance (products, Product):
        return {"name" : products.name, "price" : products.price, "quantity" : products.quantity}
    raise TypeError("Not a Product class!")
    

with open("products.json", 'w') as json_file:
    json.dump(products_list, json_file, default=serialize_products, indent=4)



# deserializing products.json file

def deserialize_json(json_obj):
    if isinstance(json_obj, list):
        return [Product(item["name"], item["price"], item["quantity"]) for item in json_obj]
    elif isinstance(json_obj, dict):
        return Product(json_obj["name"], json_obj["price"], json_obj["quantity"])
    else:
        raise ValueError("Invalid JSON format")


with open("products.json") as file:
    deserialized_data = json.load(file, object_hook=deserialize_json)

# printing the products  
for product in deserialized_data:
    print(product.get_dict())