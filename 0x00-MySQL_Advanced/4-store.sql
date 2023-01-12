-- QL script that creates a trigger that decreases the quantity of an item after adding a new order.

-- Quantity in the table items can be negative.

UPDATE items
SET quantity = quantity - orders.number
FROM orders
WHERE items.name = orders.item_name;
