use std::fs::File;
use std::io::{Read, Write};

const ROW_MAX: usize = 10;
const COLUMN_MAX: usize = 10;

fn output_to_file(hot_plate: &[[f64; COLUMN_MAX]; ROW_MAX]) {
    let mut out_fs = File::create("Hotplate.csv").unwrap();
    for i in 0..COLUMN_MAX {
        if i > 0 {
            writeln!(out_fs).unwrap();
        }
        for j in 0..ROW_MAX {
            write!(out_fs, "{:9.3}", hot_plate[i][j]).unwrap();
            if j < COLUMN_MAX - 1 {
                write!(out_fs, ",").unwrap();
            }
        }
    }
}

fn print_array(hot_plate: &[[f64; COLUMN_MAX]; ROW_MAX]) {
    for i in 0..COLUMN_MAX {
        if i > 0 {
            println!();
        }
        for j in 0..ROW_MAX {
            print!("{:9.3}", hot_plate[i][j]);
            if j < COLUMN_MAX - 1 {
                print!(",");
            }
        }
    }
    println!();
}

fn input_file(hot_plate: &mut [[f64; COLUMN_MAX]; ROW_MAX]) {
    let mut file = File::open("Inputplate.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    
    let mut tokens = contents.split_whitespace();
    
    for i in 0..COLUMN_MAX {
        for j in 0..ROW_MAX {
            if let Some(token) = tokens.next() {
                hot_plate[i][j] = token.parse().unwrap();
            }
        }
    }

    for _ in 0..3 {
        let mut hot_plate2 = [[0.0; COLUMN_MAX]; ROW_MAX];
        for i in 0..COLUMN_MAX {
            for j in 0..ROW_MAX {
                hot_plate2[i][j] = hot_plate[i][j];
            }
        }
        for i in 1..COLUMN_MAX - 1 {
            for j in 1..ROW_MAX - 1 {
                hot_plate[i][j] = (hot_plate2[i-1][j] + hot_plate2[i][j-1] + hot_plate2[i+1][j] + hot_plate2[i][j+1]) / 4.0;
            }
        }
    }
    print_array(hot_plate);
}

fn main() {
    println!("Hotplate simulator\n");
    println!("Printing the initial plate values...");
    
    let mut hot_plate = [[0.0; COLUMN_MAX]; ROW_MAX];

    for i in 0..COLUMN_MAX {
        for j in 0..ROW_MAX {
            if (i == 0 || i == 9) && (j != 0 && j != 9) {
                hot_plate[i][j] = 100.0;
            } else {
                hot_plate[i][j] = 0.0;
            }
        }
    }
    print_array(&hot_plate);
    println!();

    let mut hot_plate2 = [[0.0; COLUMN_MAX]; ROW_MAX];
    for i in 0..COLUMN_MAX {
        for j in 0..ROW_MAX {
            hot_plate2[i][j] = hot_plate[i][j];
        }
    }
    for i in 1..COLUMN_MAX - 1 {
        for j in 1..ROW_MAX - 1 {
            hot_plate[i][j] = (hot_plate2[i-1][j] + hot_plate2[i][j-1] + hot_plate2[i+1][j] + hot_plate2[i][j+1]) / 4.0;
        }
    }
    
    println!("\nPrinting plate after one iteration...");
    print_array(&hot_plate);
    println!();

    let mut threshold: f64;
    let mut max_threshold: f64;
    
    loop {
        max_threshold = 0.0;
        for i in 0..COLUMN_MAX {
            for j in 0..ROW_MAX {
                hot_plate2[i][j] = hot_plate[i][j];
            }
        }
        for i in 1..COLUMN_MAX - 1 {
            for j in 1..ROW_MAX - 1 {
                hot_plate[i][j] = (hot_plate2[i-1][j] + hot_plate2[i][j-1] + hot_plate2[i+1][j] + hot_plate2[i][j+1]) / 4.0;
            }
        }
        for i in 0..COLUMN_MAX {
            for j in 0..ROW_MAX {
                threshold = hot_plate[i][j] - hot_plate2[i][j];
                if threshold.abs() > max_threshold {
                    max_threshold = threshold.abs();
                }
            }
        }
        
        if max_threshold <= 0.1 {
            break;
        }
    }
    
    println!("\nPrinting final plate...");
    print_array(&hot_plate);

    output_to_file(&hot_plate);
    // Note: To uncomment input_file, make sure Inputplate.txt exists!
    // input_file(&mut hot_plate);
}