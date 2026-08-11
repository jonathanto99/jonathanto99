use std::io::{self, Write};

struct ItemToPurchase {
    item_name: String,
    item_price: f64,
    item_quantity: i32,
}

impl ItemToPurchase {
    fn new() -> Self {
        ItemToPurchase {
            item_name: "none".to_string(),
            item_price: 0.0,
            item_quantity: 0,
        }
    }

    fn set_name(&mut self, name: String) {
        self.item_name = name;
    }

    fn get_name(&self) -> &str {
        &self.item_name
    }

    fn set_price(&mut self, price: f64) {
        self.item_price = price;
    }

    fn get_price(&self) -> f64 {
        self.item_price
    }

    fn set_quantity(&mut self, quantity: i32) {
        self.item_quantity = quantity;
    }

    fn get_quantity(&self) -> i32 {
        self.item_quantity
    }

    fn get_total_price(&self) -> f64 {
        (self.item_quantity as f64) * self.item_price
    }
}

fn main() {
    let mut item1 = ItemToPurchase::new();
    let mut item2 = ItemToPurchase::new();

    println!("Item 1");
    println!("Enter the item name: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    item1.set_name(input.trim_end().to_string());

    println!("Enter the item price: ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    item1.set_price(input.trim().parse().unwrap());

    println!("Enter the item quantity: ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    item1.set_quantity(input.trim().parse().unwrap());

    println!("Item 2");
    println!("Enter the item name: ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    item2.set_name(input.trim_end().to_string());

    println!("Enter the item price: ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    item2.set_price(input.trim().parse().unwrap());

    println!("Enter the item quantity: ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    item2.set_quantity(input.trim().parse().unwrap());

    println!("TOTAL COST");
    println!("{} {} @ ${:.2} = ${:.2}", item1.get_name(), item1.get_quantity(), item1.get_price(), item1.get_total_price());
    println!("{} {} @ ${:.2} = ${:.2}", item2.get_name(), item2.get_quantity(), item2.get_price(), item2.get_total_price());

    println!("Total: ${:.2}", item1.get_total_price() + item2.get_total_price());
}