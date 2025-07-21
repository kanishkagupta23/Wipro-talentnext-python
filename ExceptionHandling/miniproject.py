''' Problem Statement:
# Read a purchase file ("<filename>.txt") with lines containing "<item> <price>".
# Possibly, a "Discount <amount>" line is present.
# Print: total items, free items, total before discount, discount, and net payable.
# Handle blank lines and invalid entries.'''

def main():
    
    filename = input("Enter the file name: ").strip() + ".txt"
    items = []
    discount = 0

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # Skip blank lines
                if line.lower().startswith("discount"):
                    parts = line.split()
                    if len(parts) == 2:
                        try:
                            discount = float(parts[1])
                        except ValueError:
                            discount = 0
                    continue
                parts = line.rsplit(' ', 1)
                if len(parts) == 2:
                    name, price_str = parts
                    try:
                        price = float(price_str)
                        items.append((name, price))
                    except ValueError:
                        continue  

        print("No of items purchased:", len(items))
     
        free_items = sum(1 for name, price in items if price == 0)
        print("No of free items:", free_items)
      
        total_amount = sum(price for name, price in items)
        print("Amount to pay:", int(total_amount) if total_amount.is_integer() else f"{total_amount:.2f}")
       
        print("Discount given:", int(discount) if discount.is_integer() else f"{discount:.2f}")

        final_amount = total_amount - discount
        print("Final amount paid:", int(final_amount) if final_amount.is_integer() else f"{final_amount:.2f}")

    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print("An error occurred:", e)

