use std::io::{self, Write};

/*
fn main() {
    let mut user_input = String::new();
    let bff = "best friend forever";
    let idk = "I don't know";
    let jk = "just kidding";
    let tmi = "too much information";
    let ttyl = "talk to you later";

    print!("Enter text: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut user_input).unwrap();
    let mut user_input = user_input.trim_end().to_string();

    println!("\nYou entered: {}", user_input);

    if let Some(pos) = user_input.find("BFF") {
        user_input.replace_range(pos..pos+3, bff);
    }
    if let Some(pos) = user_input.find("IDK") {
        user_input.replace_range(pos..pos+3, idk);
    }
    if let Some(pos) = user_input.find("JK") {
        user_input.replace_range(pos..pos+2, jk);
    }
    if let Some(pos) = user_input.find("TMI") {
        user_input.replace_range(pos..pos+3, tmi);
    }
    if let Some(pos) = user_input.find("TTYL") {
        user_input.replace_range(pos..pos+4, ttyl);
    }

    println!("Expanded: {}", user_input);
}

fn main() {
    let mut user_input = String::new();

    print!("Enter text: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut user_input).unwrap();
    let user_input = user_input.trim_end();

    println!("\nYou entered: {}", user_input);

    if user_input.contains("BFF") {
        println!("BFF: best friend forever");
    }
    if user_input.contains("IDK") {
        println!("IDK: I don't know");
    }
    if user_input.contains("JK") {
        println!("JK: just kidding");
    }
    if user_input.contains("TMI") {
        println!("TMI: too much information");
    }
    if user_input.contains("TTYL") {
        println!("TTYL: talk to you later");
    }
}
*/

fn main() {
    let mut user_text = String::new();

    println!("Input an abbreviation: ");
    io::stdin().read_line(&mut user_text).unwrap();
    let user_text = user_text.trim();

    if user_text == "LOL" {
        println!("laughing out loud");
    } else if user_text == "IDK" {
        println!("I don't know");
    } else if user_text == "BFF" {
        println!("best friends forever");
    } else if user_text == "IMHO" {
        println!("in my humble opinion");
    } else if user_text == "TMI" {
        println!("Too much information");
    } else {
        println!("Unknown");
    }
}