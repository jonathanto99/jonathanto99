fn calc_rectangle_perimeter(height: f64, width: f64) -> f64 {
    (height + width) * 2.0
}

fn double_rectangle_perimeter(height: &mut f64, width: &mut f64) {
    *height *= 2.0;
    *width *= 2.0;
}

fn print_rectangle_perimeter(height: f64, width: f64) {
    let print_perimeter = calc_rectangle_perimeter(height, width);
    println!("A rectangle with height {:.1} and width {:.1} has a perimeter of {:.1}.", height, width, print_perimeter);
}

fn main() {
    // Left empty as in the original C++ code
}