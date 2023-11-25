bucket = {
    "leather wallet": {"quantity": 1, "unit_price": 1100},
         "umbrella": {"quantity": 4, "unit_price": 900},
         "cigarette": {"quantity": 3, "unit_price": 200},
         "honey": {"quantity": 2, " unit_price": 100}, }
max_gst_product = None
max_gst_amount = 0
for product, details in bucket.items():
    quantity = details["quantity"]
    unit_price = details["unit_price"]
    gst_amount = 0.18*(quantity*unit_price)
    if gst_amount > max_gst_amount:
            max_gst_amount = gst_amount
            max_gst_product = product
tot_amnt = sum(details["quantity"]*details["unit_price"] for details in bucket.values())

print(max_gst_product,max_gst_product,tot_amnt)

