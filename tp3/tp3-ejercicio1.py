# Ejercicio 1 - Caja del kiosco
DISCOUNT = 0.1

while True:  # Si no se permite while True, habria que usar una variable intermedia
    name = input("Ingrese el nombre del cliente: ").strip()
    if name and name.isalpha():
        break

    print("Error: ingrese unicamente letras.")


products_quantity = 0
while True:
    products_quantity_input = input("Cantidad de productos a comprar: ")

    if products_quantity_input.isdigit() and int(products_quantity_input) > 0:
        products_quantity = int(products_quantity_input)
        break

    print("Error: ingrese un número entero mayor a 0.")


subtotal = 0
total_discount = 0
products = (
    []
)  # Si no se permite listas, se podria imprimir el producto dentro del bucle
for i in range(products_quantity):
    price = 0
    discount = 0

    while True:
        price_input = input(f"Precio del producto {i + 1}: ").strip()
        if price_input and price_input.isdigit() and int(price_input) > 0:
            price = int(price_input)
            break

        print("Error: el precio debe ser un número entero positivo")

    while True:
        has_discount = input("¿Tiene descuento? (S/N): ")

        if has_discount.isalpha() and has_discount.lower() == "s":
            discount = price * DISCOUNT
            break
        elif has_discount.isalpha() and has_discount.lower() == "n":
            break

        print("Error: ingrese unicamente S o N")

    products.append({"price": price, "discount": discount})
    subtotal += price
    total_discount += discount


total = subtotal - total_discount
price_average = total / products_quantity

print(f"\nCliente: {name}")
print(f"Cantidad de productos: {products_quantity}")

for i in range(len(products)):
    product = products[i]
    print(
        f"Producto {i + 1} - Precio {product['price']} - Descuento: {product['discount']}"
    )

print(f"Total sin descuentos: {subtotal:.2f}")
print(f"Total: {total:.2f}")
print(f"Descuentos aplicados: {total_discount:.2f}")
print(f"Precio promedio por producto: {price_average:.2f}")
