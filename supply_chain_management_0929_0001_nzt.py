# 代码生成时间: 2025-09-29 00:01:29
import pandas as pd

"""
Supply Chain Management System

This system manages the supply chain operations including
inventory, orders, and suppliers.
"""

class SupplyChainManagementSystem:
    """
    A class to manage the supply chain operations.
    """
    def __init__(self):
        # Initialize the data structures for inventory, orders, and suppliers
        self.inventory = pd.DataFrame(columns=['Product_ID', 'Product_Name', 'Quantity', 'Price'])
        self.orders = pd.DataFrame(columns=['Order_ID', 'Product_ID', 'Quantity', 'Status'])
        self.suppliers = pd.DataFrame(columns=['Supplier_ID', 'Supplier_Name', 'Contact_Info'])

    def add_product_to_inventory(self, product_id, product_name, quantity, price):
        """
        Add a product to the inventory.
        """
        try:
            # Check if the product already exists in the inventory
            if self.inventory.loc[self.inventory['Product_ID'] == product_id, 'Product_ID'].empty:
                self.inventory = self.inventory.append({
                    'Product_ID': product_id,
                    'Product_Name': product_name,
                    'Quantity': quantity,
                    'Price': price
                }, ignore_index=True)
            else:
                print(f"Product with ID {product_id} already exists in the inventory.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def place_order(self, order_id, product_id, quantity):
        """
        Place an order for a product.
        """
        try:
            # Check if the product exists in the inventory
            if not self.inventory.loc[self.inventory['Product_ID'] == product_id, 'Product_ID'].empty:
                self.orders = self.orders.append({
                    'Order_ID': order_id,
                    'Product_ID': product_id,
                    'Quantity': quantity,
                    'Status': 'Pending'
                }, ignore_index=True)
            else:
                print(f"Product with ID {product_id} does not exist in the inventory.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_inventory(self, product_id, quantity):
        """
        Update the inventory quantity after an order is fulfilled.
        """
        try:
            # Check if the product exists in the inventory
            if not self.inventory.loc[self.inventory['Product_ID'] == product_id, 'Product_ID'].empty:
                self.inventory.loc[self.inventory['Product_ID'] == product_id, 'Quantity'] += quantity
            else:
                print(f"Product with ID {product_id} does not exist in the inventory.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_supplier(self, supplier_id, supplier_name, contact_info):
        """
        Add a supplier to the system.
        """
        try:
            # Check if the supplier already exists
            if self.suppliers.loc[self.suppliers['Supplier_ID'] == supplier_id, 'Supplier_ID'].empty:
                self.suppliers = self.suppliers.append({
                    'Supplier_ID': supplier_id,
                    'Supplier_Name': supplier_name,
                    'Contact_Info': contact_info
                }, ignore_index=True)
            else:
                print(f"Supplier with ID {supplier_id} already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_inventory(self):
        """
        Display the current inventory.
        """
        print(self.inventory)

    def display_orders(self):
        """
        Display the current orders.
        """
        print(self.orders)

    def display_suppliers(self):
        """
        Display the current suppliers.
        """
        print(self.suppliers)

# Example usage
if __name__ == '__main__':
    sc_system = SupplyChainManagementSystem()
    sc_system.add_product_to_inventory('001', 'Product A', 100, 10.99)
    sc_system.add_supplier('S001', 'Supplier A', 'Contact A')
    sc_system.place_order('O001', '001', 20)
    sc_system.update_inventory('001', -20)
    sc_system.display_inventory()
    sc_system.display_orders()
    sc_system.display_suppliers()