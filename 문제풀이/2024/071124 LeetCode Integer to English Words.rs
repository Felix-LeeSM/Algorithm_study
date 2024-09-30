struct Solution;

impl Solution {
    pub fn number_to_words(num: i32) -> String {
        if num == 0 {
            return "Zero".to_string();
        }
        let mut num = num as usize;
        let mut string = String::new();

        let digits = ["", " Thousand", " Million", " Billion"];

        let mut nums = vec![];

        while num > 0 {
            nums.push(num % 1000);
            num /= 1000;
        }

        for (digit, num) in digits.into_iter().zip(nums).rev() {
            if num > 0 {
                string
                    .push_str(format!(" {} {}", Self::three_digits(num).as_str(), digit).as_str());
            }
        }

        string
            .split_ascii_whitespace()
            .collect::<Vec<_>>()
            .join(" ")
    }

    fn three_digits(num: usize) -> String {
        let mut string = String::new();

        if num / 100 > 0 {
            string.push_str(format!("{} Hundred", Self::single_digit(num / 100)).as_str());
        }

        if num % 100 > 0 {
            string.push_str(format!(" {}", Self::two_digits(num % 100)).as_str());
        }

        string
    }

    fn single_digit(num: usize) -> String {
        [
            "", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine",
        ][num]
            .to_string()
    }

    fn two_digits(num: usize) -> String {
        if num < 10 {
            Self::single_digit(num)
        } else if num < 20 {
            [
                " Ten",
                " Eleven",
                " Twelve",
                " Thirteen",
                " Fourteen",
                " Fifteen",
                " Sixteen",
                " Seventeen",
                " Eighteen",
                " Nineteen",
            ][num % 10]
                .to_string()
        } else {
            let first = [
                "", "", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty",
                " Ninety",
            ][num / 10];
            format!(" {} {}", first, Self::single_digit(num % 10))
        }
    }
}
fn main() {
    assert_eq!(
        "Twelve Thousand Three Hundred Forty Five",
        Solution::number_to_words(12_345)
    );
    assert_eq!(
        "One Billion Two Hundred Thirty Four Million Two Hundred Thirteen Thousand Four Hundred Fifty Five", 
        Solution::number_to_words(1_234_213_455)
    );

    assert_eq!(
        "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        Solution::number_to_words(1_234_567)
    )
}
