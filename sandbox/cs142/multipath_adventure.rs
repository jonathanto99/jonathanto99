use std::io::{self, Write};
// Random number logic
use std::time::{SystemTime, UNIX_EPOCH};

fn special_error_message() -> String {
    "Ummm that didn't quite work, you gotta choose either \"Yes\" or \"No\", otherwise the computer wouldn't know what to do. Try again! \n".to_string()
}

fn error_message() {
    println!("Ummm that didn't quite work, you gotta choose from one of the two prompts and type it in verbatim, otherwise the computer wouldn't know what to do. Try again! ");
}

fn second_branch(user_input_exam: &mut String, user_input_help: &mut String) {
    println!("You realize that there is an exam that you should probably study for, so you decline. ");
    println!("So You get home and are tempted to watch a studio Ghibli movie, do you study or watch movie? ");
    print!("You should type in \"Study\" or \"Movie\": ");
    io::stdout().flush().unwrap();
    user_input_exam.clear();
    io::stdin().read_line(user_input_exam).unwrap();
    *user_input_exam = user_input_exam.trim().to_string();

    if user_input_exam == "Study" {
        println!("You turn on your laptop and start doing exercises for your exam. ");
        print!("You run into a problem with your code, do you google the solution or ask TA for help? ");
        print!("You should type in \"Google\" or \"TA\": ");
        io::stdout().flush().unwrap();
        user_input_help.clear();
        io::stdin().read_line(user_input_help).unwrap();
        *user_input_help = user_input_help.trim().to_string();

        if user_input_help == "Google" {
            print!("OK so you try to google the solution, ");
            println!("but all you run into are confusing Stack Overflow examples that make you want to pull your hair out. ");
            print!("The end! You've reached one of the 7 possible endings of the program. ");
        } else if user_input_help == "TA" {
            println!("You email your TA and get on a Zoom call with them, they are very helpful and get off Zoom with a sign of relief");
            print!("The end! You've reached one of the 7 possible endings of the program. ");
        } else {
            error_message();
        }
    } else if user_input_exam == "Movie" {
        println!("You sit down in front of your TV and enjoy the master piece of a movie. ");
        print!("The end! You've reached one of the 7 possible endings of the program. ");
    } else {
        error_message();
    }
}

fn main() {
    let mut start_program_yes_no = String::new();
    let mut user_input_yes_no = String::new();
    let mut user_input_buddy = String::new();
    let mut user_input_invitation = String::new();
    let mut user_input_dinner = String::new();
    let mut user_input_exam = String::new();
    let mut user_input_help = String::new();
    let mut random_num_user: i32;

    for i in 0..3 {
        for _ in 0..(3 - i) {
            print!("* ");
        }
    }
    
    print!("First and foremost it is crucial that when you are asked to type in your input, ");
    print!("you type in word for word what the program asks you do type in, ");
    print!("Like \"Yes\", not \"yes\" or \"YES\" ");
    
    for i in 0..3 {
        for _ in 0..(3 - i) {
            print!("* ");
        }
    }
    print!("\nType in \"Let's Start\" to start: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut start_program_yes_no).unwrap();
    start_program_yes_no = start_program_yes_no.trim().to_string();

    if start_program_yes_no == "Let's Start" {
        println!("Thanks for willing to spend your time with my little program! ");
        print!("Your friend calls you out of the blue (You haven't talked in years) ");
        println!("and asks you if you could help her move her stuff to her new apartment with her husband.");
        print!("Would you like to help her or not? You should type in \"Yes\" or \"No\": ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut user_input_yes_no).unwrap();
        user_input_yes_no = user_input_yes_no.trim().to_string();
    }

    if user_input_yes_no == "Yes" {
        println!("She tells you to meet her in 3 days at 10 AM, and says that you could bring a buddy with. ");
        print!("Do you bring a buddy with you? You should type in \"Yes\" or \"No\": ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut user_input_buddy).unwrap();
        user_input_buddy = user_input_buddy.trim().to_string();
        
        if user_input_buddy == "Yes" {
            println!("You bring you friend to help. Turns out your buddy knows the husband of your friend as well");
            println!("he husband and your buddy invite you to a barbeque and a basketball game, ");
            print!("but you only have time for one, which one do you go to? You should type in \"Barbeque\" or \"Game\" ");
            io::stdout().flush().unwrap();
            io::stdin().read_line(&mut user_input_invitation).unwrap();
            user_input_invitation = user_input_invitation.trim().to_string();
            
            if user_input_invitation == "Barbeque" {
                println!("You go to the barbeque. You get to meet your friend's husband's family and make new friends. ");
                print!("The end! You've reached one of the 7 possible endings of the program. ");
            } else if user_input_invitation == "Game" {
                println!("You go to the basketball game. It was loud and boring, so you didn't enjoy your time at all. ");
                print!("The end! You've reached one of the 7 possible endings of the program. ");
            } else {
                error_message();
            }
        } else if user_input_buddy == "No" {
            println!("You go alone to help. Your friend asks you if you want to stay and have Panda Express for dinner");
            println!("You contemplate, even though you are hungry you know that Panda is an insult to Chinese cuisine. ");
            print!("Do you stay for dinner or go home to eat your own food? You should type in \"Panda\" or \"Respect4ChineseFood\" ");
            io::stdout().flush().unwrap();
            io::stdin().read_line(&mut user_input_dinner).unwrap();
            user_input_dinner = user_input_dinner.trim().to_string();
            
            if user_input_dinner == "Panda" {
                println!("You decide to stay. Even though the food ain't great but you have a good time with the people you are with. ");
                print!("The end! You've reached one of the 7 possible endings of the program. ");
            } else if user_input_dinner == "Respect4ChineseFood" {
                println!("You politely decline and go home to make some authentic chicken friend rice yourself. ");
                print!("The end! You've reached one of the 7 possible endings of the program. ");
            } else {
                error_message();
            }
        } else {
            error_message();
        }
    } else if user_input_yes_no == "No" {
        second_branch(&mut user_input_exam, &mut user_input_help);
    } else {
        print!("{}", special_error_message());
    }

    println!("\nThanks so much for using my program here. Now before we leave, here's a minigame that we could play: ");
    println!("Would you like to keep going? Say \"Yes\" or \"No\"");
    let mut keep_going = String::new();
    io::stdin().read_line(&mut keep_going).unwrap();
    keep_going = keep_going.trim().to_string();

    while keep_going == "Yes" {
        print!("Choose between 20 or 50 for a range of random numbers that the program can choose from: ");
        io::stdout().flush().unwrap();
        
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        random_num_user = input.trim().parse().unwrap_or(0);
        
        let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_nanos();
        
        if random_num_user == 20 {
            random_num_user = ((now % 20) + 1) as i32;
            print!("{}", random_num_user);
        } else if random_num_user == 50 {
            random_num_user = ((now % 50) + 1) as i32;
            print!("{}", random_num_user);
        } else {
            println!("Invalid response, sorry. ");
        }
        
        println!(" So that's your lucky number! ");
        print!("Would you like to do it again? ");
        io::stdout().flush().unwrap();
        keep_going.clear();
        io::stdin().read_line(&mut keep_going).unwrap();
        keep_going = keep_going.trim().to_string();
    }
}