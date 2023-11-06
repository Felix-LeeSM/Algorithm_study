// https://www.acmicpc.net/problem/6597
use std::io::{self};

fn input() -> Vec<String> {
    io::read_to_string(io::stdin())
        .unwrap()
        .trim()
        .split('\n')
        .map(|s| s.to_string())
        .collect()
}

#[derive(Debug)]
struct Tree {
    root: char,
    left: Option<Box<Tree>>,
    right: Option<Box<Tree>>,
}

impl Tree {
    fn new() -> Self {
        Tree {
            root: '\0',
            left: None,
            right: None,
        }
    }

    fn put_root(&mut self, root: char) {
        self.root = root;
    }

    fn init_left(&mut self) {
        self.left = Some(Box::new(Tree::new()));
    }

    fn init_right(&mut self) {
        self.right = Some(Box::new(Tree::new()));
    }
}

impl std::fmt::Display for Tree {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        if let Some(left) = &self.left {
            write!(f, "{}", left)?;
        }
        if let Some(right) = &self.right {
            write!(f, "{}", right)?;
        }
        write!(f, "{}", self.root)?;
        Ok(())
    }
}

fn main() {
    let input = input();
    for line in input {
        let line = line.split(' ').collect::<Vec<_>>();
        let (pre_order, in_order) = (line[0].to_string(), line[1].to_string());

        fn build_tree(pre_order: &String, in_order: &String, tree: &mut Tree) -> () {
            if let Some(cur_root) = pre_order.chars().nth(0) {
                tree.put_root(cur_root);

                let last_in = in_order
                    .chars()
                    .position(|node| node.eq(&cur_root))
                    .unwrap();

                let length = in_order.len();

                if last_in != 0 {
                    let left_pre_order = pre_order[1..last_in + 1].chars().collect::<String>();
                    let left_in_order = in_order[0..last_in].chars().collect::<String>();

                    tree.init_left();

                    build_tree(
                        &left_pre_order,
                        &left_in_order,
                        &mut tree.left.as_mut().unwrap(),
                    );
                }

                if last_in + 1 != length {
                    let right_pre_order = pre_order[last_in + 1..].to_string();
                    let right_in_order = in_order[last_in + 1..].to_string();

                    tree.init_right();

                    build_tree(
                        &right_pre_order,
                        &right_in_order,
                        &mut tree.right.as_mut().unwrap(),
                    );
                }

                ()
            }
        }

        let mut tree = Tree::new();
        build_tree(&pre_order, &in_order, &mut tree);

        println!("{}", tree);
    }
}
