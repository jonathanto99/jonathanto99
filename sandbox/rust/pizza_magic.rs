use std::io::{self, Write};
use std::f64::consts::PI;

fn main() {
    let diameter_per_large = 20.0;
    let diameter_per_medium = 16.0;
    let diameter_per_small = 12.0;
    let radius_per_large = diameter_per_large / 2.0;
    let radius_per_medium = diameter_per_medium / 2.0;
    let radius_per_small = diameter_per_small / 2.0;

    let price_per_large = 14.68;
    let price_per_medium = 11.48;
    let price_per_small = 7.28;

    let guest_per_large = 7;
    let guest_per_medium = 3;
    let guest_per_small = 1;

    let mut guest_count = 0;
    let mut tips = 0;

    println!("Please enter how many guests to order for: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    guest_count = input.trim().parse().unwrap();

    let large_count = guest_count / guest_per_large;
    let medium_count = (guest_count % guest_per_large) / guest_per_medium;
    let small_count = ((guest_count % guest_per_large) % guest_per_medium) / guest_per_small;

    print!("{} large pizzas, ", large_count);
    print!("{} medium pizzas, ", medium_count);
    println!("and {} small pizzas will be needed.", small_count);
    println!();

    let sqr_inch = (large_count as f64 * (PI * radius_per_large.powi(2))) 
                 + (medium_count as f64 * (PI * radius_per_medium.powi(2))) 
                 + (small_count as f64 * (PI * radius_per_small.powi(2)));
    let inch_per_guest = sqr_inch / guest_count as f64;

    print!("A total of {} square inches of pizza will be ordered", sqr_inch);
    println!(" ({} per guest).", inch_per_guest);
    println!();

    println!("Please enter the tip as a percentage (i.e. 10 means 10%): ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    tips = input.trim().parse().unwrap();

    let cost = (large_count as f64 * price_per_large) 
             + (medium_count as f64 * price_per_medium) 
             + (small_count as f64 * price_per_small);
    let total_cost = cost + (cost * (tips as f64 / 100.0));

    println!("The total cost of the event will be: ${}", total_cost.round());
    println!();
}