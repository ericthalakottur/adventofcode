use std::env;
use std::fs;
use std::str::FromStr;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let lines: Vec<String> = fs::read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect();

    let mut v1: Vec<i32> = Vec::new();
    let mut v2: Vec<i32> = Vec::new();
    for line in lines {
        let values: Vec<&str> = line.split("   ").collect();
        v1.push(FromStr::from_str(values[0]).unwrap());
        v2.push(FromStr::from_str(values[1]).unwrap());
    }
    v1.sort();
    v2.sort();

    let mut answer1 = 0;
    for (i, _) in v1.iter().enumerate() {
        answer1 += (v1[i] - v2[i]).abs();
    }
    println!("Answer 1: {answer1}");
}
