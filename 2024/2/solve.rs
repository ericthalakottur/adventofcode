use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let lines: Vec<String> = fs::read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect();

    let mut answer1 = 0;
    for line in lines {
        let values: Vec<i32> = line.split(" ").map(|s| s.parse().unwrap()).collect();
        let mut diff: Vec<i32> = Vec::new();
        let mut i = 0;
        while i + 1 < values.len() {
            diff.push(values[i + 1] - values[i]);
            i += 1
        }
        let result =
            diff.iter().all(|&x| 0 <= x && x < 2) || diff.iter().all(|&x| -2 <= x && x <= 0);
        answer1 += if result { 1 } else { 0 };
        dbg!(values);
    }
    println!("Answer 1: {answer1}");
}
