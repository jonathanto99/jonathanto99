use std::io;

const PI: f64 = 3.14;

fn main() {
    println!("Getting this line to print earns you points!");

    let mut height = 0.0;
    let mut width = 0.0;
    let mut radius = 0.0;

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    height = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    width = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    radius = input.trim().parse().unwrap();

    println!("A rectangle with height {:.1} and width {:.1} has a perimeter of {:.1}.", height, width, calc_rectangle_perimeter(height, width));
    println!("{:.1}", calc_rectangle_perimeter(height, width));

    double_rectangle_perimeter(&mut height, &mut width);
    println!("... about to double height and width...");
    print_rectangle_perimeter(height, width);
}

fn double_rectangle_perimeter(height: &mut f64, width: &mut f64) {
    *height *= 2.0;
    *width *= 2.0;
}

fn print_rectangle_perimeter(height: f64, width: f64) {
    let print_perimeter = calc_rectangle_perimeter(height, width);
    println!("A rectangle with height {:.1} and width {:.1} has a perimeter of {:.1}.", height, width, print_perimeter);
}

fn calc_rectangle_perimeter(height: f64, width: f64) -> f64 {
    (height + width) * 2.0
}

#[allow(dead_code)]
fn calc_circumference_of_circle(radius: f64) -> f64 {
    radius * PI * 2.0
}

#[allow(dead_code)]
fn calc_area_of_circle(radius: f64) -> f64 {
    PI * radius * radius
}

#[allow(dead_code)]
fn calc_volume_of_sphere(radius: f64) -> f64 {
    (4.0 / 3.0) * PI * radius.powi(3)
}

#[allow(dead_code)]
fn swap_int(a: &mut i32, b: &mut i32) {
    let temp_var = *a;
    *a = *b;
    *b = temp_var;
}

#[allow(dead_code)]
fn swap_double(x: &mut f64, y: &mut f64) {
    let temp_var = *x;
    *x = *y;
    *y = temp_var;
}