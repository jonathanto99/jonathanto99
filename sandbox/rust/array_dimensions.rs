use std::fs::File;
use std::io::Write;

const ARRAY_SIZE: usize = 5;

fn main() {
    let mut my_array = [0; ARRAY_SIZE];
    let mut my_vector: Vec<i32> = Vec::new();

    for i in 0..ARRAY_SIZE {
        my_array[i] = i as i32;
    }

    for i in 0..ARRAY_SIZE {
        my_vector.push(i as i32);
    }

    print!("myArray: ");
    for i in 0..ARRAY_SIZE {
        print!("{} ", my_array[i]);
    }
    println!();

    print!("myVector: ");
    for i in 0..my_vector.len() {
        print!("{} ", my_vector[i]);
    }
    println!("\n");

    println!("Before change:");
    println!("myArray[3] is {}", my_array[3]);
    println!("myVector.at(3) is {}\n", my_vector[3]);

    my_array[3] = 27;
    my_vector[3] = 27;

    println!("After change:");
    println!("myArray[3] is {}", my_array[3]);
    println!("myVector.at(3) is {}\n", my_vector[3]);

    for i in 0..ARRAY_SIZE {
        if my_array[i] % 2 == 1 {
            my_array[i] = 0;
        }
    }

    for i in 0..my_vector.len() {
        if my_vector[i] % 2 == 1 {
            my_vector[i] = 0;
        }
    }

    print!("myArray: ");
    for i in 0..ARRAY_SIZE {
        print!("{} ", my_array[i]);
    }
    println!();

    print!("myVector: ");
    for i in 0..my_vector.len() {
        print!("{} ", my_vector[i]);
    }
    println!("\n");

    let mut new_array = [0; ARRAY_SIZE];
    for i in 0..ARRAY_SIZE {
        new_array[i] = my_array[i];
    }
    print!("newArray: ");
    for i in 0..ARRAY_SIZE {
        print!("{} ", new_array[i]);
    }
    println!();

    let mut new_vector = my_vector.clone();
    print!("newVector: ");
    for i in 0..new_vector.len() {
        print!("{} ", new_vector[i]);
    }
    println!("\n");

    new_vector.resize(new_vector.len() + 2, 0);
    let new_len = new_vector.len();
    new_vector[new_len - 2] = (new_len - 2) as i32;
    new_vector[new_len - 1] = (new_len - 1) as i32;

    print!("newVector: ");
    for i in 0..new_vector.len() {
        print!("{} ", new_vector[i]);
    }
    println!("\n");

    let mut multi_dimensional_array = [[0; ARRAY_SIZE]; ARRAY_SIZE];
    for i in 0..ARRAY_SIZE {
        for j in 0..ARRAY_SIZE {
            multi_dimensional_array[i][j] = (i * ARRAY_SIZE + j) as i32;
        }
    }

    println!("multiDimensionalArray:");
    for i in 0..ARRAY_SIZE {
        for j in 0..ARRAY_SIZE {
            print!("{}\t ", multi_dimensional_array[i][j]);
        }
        println!();
    }
    println!("\n");

    one_dimensional_function(&my_array);
    multi_dimensional_function(&mut multi_dimensional_array);

    println!("multiDimensionalArray:");
    for i in 0..ARRAY_SIZE {
        for j in 0..ARRAY_SIZE {
            print!("{}\t ", multi_dimensional_array[i][j]);
        }
        println!();
    }
    println!("\n");

    vector_function(&new_vector);

    let mut outfile = File::create("out.csv").unwrap();
    for i in 0..ARRAY_SIZE {
        for j in 0..ARRAY_SIZE {
            write!(outfile, "{} ", multi_dimensional_array[i][j]).unwrap();
        }
        writeln!(outfile).unwrap();
    }
}

fn one_dimensional_function(the_array: &[i32; ARRAY_SIZE]) {
    println!("theArray in a function:");
    for i in 0..ARRAY_SIZE {
        print!("{} ", the_array[i]);
    }
    println!("\n");
}

fn multi_dimensional_function(the_array: &mut [[i32; ARRAY_SIZE]; ARRAY_SIZE]) {
    println!("Multi dimensional array in a function:");
    for i in 0..ARRAY_SIZE {
        for j in 0..ARRAY_SIZE {
            print!("{}\t ", the_array[i][j]);
        }
        println!();
    }
    println!();
    the_array[1][1] = 100;
}

fn vector_function(the_vector: &Vec<i32>) {
    println!("theVector in a function");
    for i in 0..the_vector.len() {
        print!("{} ", the_vector[i]);
    }
    println!("\n");
}