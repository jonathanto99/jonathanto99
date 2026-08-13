use std::io::{self, Write};

const POSITIONS_PER_PLAYER: usize = 6;
const ROW_MAX: usize = 5;
const COLUMN_MAX: usize = 5;

fn main() {
    let mut guess_player1 = String::new();
    let mut guess_player2 = String::new();

    let mut all_ships_coordinate_player1: Vec<String> = Vec::with_capacity(POSITIONS_PER_PLAYER);
    
    println!("Enter Player 1's chosen coordinates: ");
    for _ in 0..POSITIONS_PER_PLAYER {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        all_ships_coordinate_player1.push(input.trim().to_string());
    }

    let mut all_ships_coordinate_player2: Vec<String> = Vec::with_capacity(POSITIONS_PER_PLAYER);

    println!("Enter Player 2's chosen coordinates: ");
    for _ in 0..POSITIONS_PER_PLAYER {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        all_ships_coordinate_player2.push(input.trim().to_string());
    }

    while !all_ships_coordinate_player1.is_empty() && !all_ships_coordinate_player2.is_empty() {
        let mut ship_hit = false;
        print!("It is player 1's turn. Enter a guess: ");
        io::stdout().flush().unwrap();
        
        guess_player1.clear();
        io::stdin().read_line(&mut guess_player1).unwrap();
        guess_player1 = guess_player1.trim().to_string();

        let mut i = 0;
        while i < all_ships_coordinate_player2.len() {
            if guess_player1 == all_ships_coordinate_player2[i] {
                ship_hit = true;
                println!("{} was a hit!", all_ships_coordinate_player2[i]);
                all_ships_coordinate_player2.remove(i);
            } else {
                i += 1;
            }
        }
        if !ship_hit {
            println!("{} was a miss.", guess_player1);
        }

        if !all_ships_coordinate_player2.is_empty() {
            ship_hit = false;
            print!("It is player 2's turn. Enter a guess: ");
            io::stdout().flush().unwrap();
            
            guess_player2.clear();
            io::stdin().read_line(&mut guess_player2).unwrap();
            guess_player2 = guess_player2.trim().to_string();

            let mut j = 0;
            while j < all_ships_coordinate_player1.len() {
                if guess_player2 == all_ships_coordinate_player1[j] {
                    ship_hit = true;
                    println!("{} was a hit!", all_ships_coordinate_player1[j]);
                    all_ships_coordinate_player1.remove(j);
                } else {
                    j += 1;
                }
            }
            if !ship_hit {
                println!("{} was a miss.", guess_player2);
            }
        }
    }

    if all_ships_coordinate_player1.is_empty() {
        print!("Player 2 is the winner. Their unsunk ships were at: ");
        for ship in &all_ships_coordinate_player2 {
            print!("{} ", ship);
        }
        println!();
    }

    if all_ships_coordinate_player2.is_empty() {
        print!("Player 1 is the winner. Their unsunk ships were at: ");
        for ship in &all_ships_coordinate_player1 {
            print!("{} ", ship);
        }
        println!();
    }
}

fn init_2d_array(array: &mut [[char; COLUMN_MAX]; ROW_MAX]) {
    for row in 0..ROW_MAX {
        for col in 0..COLUMN_MAX {
            array[row][col] = '-';
        }
    }
}

#[allow(dead_code)]
fn show_remaining_positions(player: &[String]) {
    let mut grid = [['-'; COLUMN_MAX]; ROW_MAX];
    init_2d_array(&mut grid);

    for current_ship in player {
        let row = (current_ship.chars().nth(0).unwrap() as u8 - b'A') as usize;
        let col = (current_ship.chars().nth(1).unwrap() as u8 - b'1') as usize;
        grid[row][col] = 'X';
    }

    print!(" ");
    for i in 1..=COLUMN_MAX {
        print!(" {}", i);
    }
    println!();
    
    for c in b'A'..b'A' + ROW_MAX as u8 {
        print!("{} ", c as char);
        for i in 0..COLUMN_MAX {
            print!("{} ", grid[(c - b'A') as usize][i]);
        }
        println!();
    }
    println!();
}