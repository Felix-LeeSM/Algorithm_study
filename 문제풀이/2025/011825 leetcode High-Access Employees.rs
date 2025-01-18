use std::collections::VecDeque;

impl Solution {
    pub fn find_high_access_employees(access_times: Vec<Vec<String>>) -> Vec<String> {
        let mut access_times = access_times
            .into_iter()
            .map(|access_time| {
                let time = access_time[1].parse::<isize>().unwrap();
                let hours = time / 100;
                let minutes = time % 100 + hours * 60;
                (access_time[0].clone(), minutes)
            })
            .fold(
                std::collections::HashMap::new(),
                |mut map, (employee, time)| {
                    map.entry(employee).or_insert(vec![]).push(time);
                    map
                },
            );

        for (_, times) in access_times.iter_mut() {
            times.sort_unstable();
        }

        let mut curr_employes = vec![];

        for (employee, times) in access_times.into_iter() {
            let mut current_times = VecDeque::new();

            for time in times.into_iter() {
                while let Some(&prev_time) = current_times.front() {
                    if prev_time + 59 < time {
                        current_times.pop_front();
                    } else {
                        break;
                    }
                }

                current_times.push_back(time);

                if current_times.len() >= 3 {
                    curr_employes.push(employee.clone());
                    break;
                }
            }
        }

        curr_employes
    }
}
