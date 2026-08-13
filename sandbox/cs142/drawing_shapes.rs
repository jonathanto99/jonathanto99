use std::io::{self, Write};

fn main() {
    let mut arrow_base_height = 0;
    let mut arrow_base_width = 0;
    let mut arrow_head_width = 0;

    println!("Enter arrow base height: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    arrow_base_height = input.trim().parse().unwrap();

    println!("Enter arrow base width: ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    arrow_base_width = input.trim().parse().unwrap();

    println!("Enter arrow head width: ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    arrow_head_width = input.trim().parse().unwrap();

    // Loop kept exactly as in the original code, where it loops while arrowBaseHeight < arrowBaseHeight
    while arrow_base_height < arrow_base_height {
        println!("**");
    }

    println!("****");
    println!("***");
    println!("**");
    println!("*");
}

/*
fn main() {
    let mut triangle_char = ' ';
    let mut triangle_height = 0;

    println!("Enter a character: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    triangle_char = input.trim().chars().next().unwrap();

    println!("Enter triangle height: ");
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    triangle_height = input.trim().parse().unwrap();
    
    let mut triangle_width = 0;

    while triangle_width < triangle_height {
        let mut num_char_per_line = 0;
        while num_char_per_line <= triangle_width {
            num_char_per_line += 1;
            print!("{} ", triangle_char);
        }
        println!();
        triangle_width += 1;
    }
}
*/