def show_product_details():
    """
    Calculates and displays the details of purchased products, discounts, and fees.
    """
    # Available product details
    product_catalog = [
        {"name":"Product A","price":20},
        {"name":"Product B","price":40},
        {"name":"Product C","price":50},
    ]
    # Available discount coupons
    discount_catalog =[
        {"flat_10_discount" : "Flat 10%","discount_percentage" :10,},
        {"bulk_5_discount" : "Bulk 5%","discount_percentage" :5,},
        {"bulk_10_discount" : "Bulk 10%","discount_percentage" :10,},
        {"tiered_50_discount" : "Tiered 50%","discount_percentage" :50,}
    ]
    # Initializing variables
    available_discounts = []
    product_details = []
    purchase_details = []
    ask_yes_or_no = "(Yes/No)"
    check_yes_or_no = ["yes", "no"]
    invalid_input_msg = "Please enter valid inputs !"
    price_a = price_b = price_c = 0
    discount_amount_a = discount_amount_b = discount_amount_c =0
    flat_10_discount_amount = bulk_5_discount_amount = 0
    bulk_10_discount_amount = tiered_50_discount_amount = 0
    applied_coupon = "No coupons available"
    discount_amount = 0

    # Get quantity of products from the user
    # And ask if each product is wrapped as a gift
    quantity_a = int(input(f"Enter the number of {product_catalog[0]['name']} to be added to the cart: "))
    if quantity_a > 0:
        ask_gift_wrap_a = input(f"Is {product_catalog[0]['name']} wrapped as a gift ? {ask_yes_or_no} ")
        while ask_gift_wrap_a.lower() not in check_yes_or_no:
            print(f"{invalid_input_msg} Either {ask_yes_or_no}")
            ask_gift_wrap_a = input(f"Is {product_catalog[0]['name']} wrapped as a gift ? {ask_yes_or_no} ")

    quantity_b = int(input(f"Enter the no.of {product_catalog[1]['name']}  to be added to the cart : "))
    if quantity_b > 0:
        ask_gift_wrap_b = input(f"Is {product_catalog[1]['name']} wrapped as a gift ? {ask_yes_or_no} ")
        while ask_gift_wrap_b.lower() not in check_yes_or_no:
            print(f"{invalid_input_msg} Either {ask_yes_or_no}")
            ask_gift_wrap_b = input(f"Is {product_catalog[1]['name']} wrapped as a gift ? {ask_yes_or_no} ")

    quantity_c = int(input(f"Enter the no.of {product_catalog[2]['name']}  to be added to the cart : "))
    if quantity_c > 0:
        ask_gift_wrap_c = input(f"Is {product_catalog[2]['name']} wrapped as a gift ? {ask_yes_or_no} ")
        while ask_gift_wrap_c.lower() not in check_yes_or_no:
            print(f"{invalid_input_msg} Either {ask_yes_or_no}")
            ask_gift_wrap_c = input(f"Is {product_catalog[2]['name']} wrapped as a gift ? {ask_yes_or_no} ")
        
    # Set gift wrapping values based on user inputs
    gift_wrap_a = gift_wrap_b = gift_wrap_c = 0
    if ask_gift_wrap_a.lower() == "yes":
        gift_wrap_a = 1 * quantity_a
    if ask_gift_wrap_b.lower() == "yes":
        gift_wrap_b = 1 * quantity_b
    if ask_gift_wrap_c.lower() == "yes":
        gift_wrap_c = 1 * gift_wrap_c

    # Calculate price and create product details for each product
    if quantity_a > 0:
        price_a = product_catalog[0]["price"] * quantity_a
        product_details.append(
            {
                "Product": product_catalog[0]["name"],
                "Quantity":quantity_a,
                "Price": price_a
            }
        )
    if quantity_b > 0:
        price_b = product_catalog[1]["price"] * quantity_b
        product_details.append(
            {
                "Product": product_catalog[1]["name"],
                "Quantity":quantity_b,
                "Price": price_b
            }
        )
    if quantity_c > 0:
        price_c = product_catalog[2]["price"] * quantity_c
        product_details.append(
            {
                "Product": product_catalog[2]["name"],
                "Quantity":quantity_c,
                "Price": price_c
            }
        )

    # Calculate total quantity of products purchased
    total_quantity = quantity_a + quantity_b + quantity_c

    # Calculate total purchased amount
    total_price = price_a + price_b + price_c

    # Determine applicable discount based on purchased products price
    if total_price > 200 :
        discount_coupon1 = discount_catalog[0]["flat_10_discount"]
        discount_percentage = discount_catalog[0]["discount_percentage"]
        flat_10_discount_amount = total_price * (discount_percentage / 100)
        available_discounts.append(flat_10_discount_amount)
    # Determine applicable discount based on quantity of each product
    if quantity_a > 10 or  quantity_b > 10 or  quantity_c > 10:
        discount_coupon2 = discount_catalog[1]["bulk_5_discount"]
        discount_percentage = discount_catalog[1]["discount_percentage"]
        if quantity_a > 10:
            discount_amount_a = price_a * (discount_percentage / 100)
        if quantity_b > 10:
            discount_amount_b = price_b * (discount_percentage / 100)
        if quantity_c > 10:
            discount_amount_c = price_c * (discount_percentage / 100)
        bulk_5_discount_amount = discount_amount_a + discount_amount_b + discount_amount_c
        available_discounts.append(bulk_5_discount_amount)
    # Determine applicable discount based on total quantity of products
    if total_quantity > 20:
        discount_coupon3 = discount_catalog[2]["bulk_10_discount"]
        discount_percentage = discount_catalog[2]["discount_percentage"]
        bulk_10_discount_amount = total_price * (discount_percentage / 100)
        available_discounts.append(bulk_10_discount_amount)
    # Determine applicable discount based on total quantity and individual quantity of products
    if total_quantity > 30 and (quantity_a > 15 or  quantity_b > 15 or  quantity_c > 15):
        discount_coupon4 = discount_catalog[3]["tiered_50_discount"]
        discount_percentage = discount_catalog[1]["discount_percentage"]
        if quantity_a > 15:
            discount_applicable_quantity = quantity_a -15
            discount_applicable_quantity_price = discount_applicable_quantity * product_catalog[0]["price"]
            discount_amount_a = discount_applicable_quantity_price * (discount_percentage / 100)
        if quantity_b > 15:
            discount_applicable_quantity = quantity_b -15
            discount_applicable_quantity_price = discount_applicable_quantity * product_catalog[1]["price"]
            discount_amount_b = discount_applicable_quantity_price * (discount_percentage / 100)
        if quantity_c > 15:
            discount_applicable_quantity = quantity_c -15
            discount_applicable_quantity_price = discount_applicable_quantity * product_catalog[2]["price"]
            discount_amount_c = discount_applicable_quantity_price * (discount_percentage / 100)
        tiered_50_discount_amount = discount_amount_a + discount_amount_b + discount_amount_c
        available_discounts.append(tiered_50_discount_amount)

    # Find the best discount amount
    if available_discounts:
        beneficial_discount_amount = max(available_discounts)

        # Determine the final applied coupon and discount amount
        if beneficial_discount_amount == flat_10_discount_amount:
            applied_coupon = discount_coupon1
            discount_amount = flat_10_discount_amount 
        if beneficial_discount_amount == bulk_5_discount_amount:
            applied_coupon = discount_coupon2
            discount_amount = bulk_5_discount_amount 
        if beneficial_discount_amount == bulk_10_discount_amount:
            applied_coupon = discount_coupon3
            discount_amount = bulk_10_discount_amount 
        if beneficial_discount_amount == tiered_50_discount_amount:
            applied_coupon = discount_coupon4
            discount_amount = tiered_50_discount_amount 


    # Calculate Shipping fee
    shipping_fee = (total_quantity / 10) * 5
    # Calculate total gift wrap fee
    total_gift_wrap = gift_wrap_a + gift_wrap_b + gift_wrap_c
    # Calculate total amount after applying discount 
    total = (total_price + shipping_fee + total_gift_wrap) - discount_amount
    # Add Purchase details to the list
    purchase_details.append(
        {
            "Sub total":total_price,
            "Shipping fee":shipping_fee,
            "Gift wrap fee":total_gift_wrap,
            "Applied coupon":applied_coupon,
            "Discount amount":discount_amount,
            "Total" :total
        }
    )
    print(available_discounts)
    print("\n=======================PURCHASED PRODUCTS==============================")
    print("\n", product_details)
    print("\n===============================BILL=====================================")
    print("\n", purchase_details)
    print("\n**************************")


# Function call to display purchased product details
show_product_details()