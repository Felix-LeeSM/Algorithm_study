use std::collections::BinaryHeap;

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let (n, first_person) = (n as usize, first_person as usize);

        let mut links = vec![vec![]; n];

        // links[node1] = vec![(node2, threshold)]
        links[0].push((first_person, 0));
        links[first_person].push((0, 0));

        meetings
            .into_iter()
            .map(|v| (v[0] as usize, v[1] as usize, v[2] as usize))
            .for_each(|(x, y, t)| {
                links[x].push((y, t));
                links[y].push((x, t));
            });

        let mut thresholds = vec![usize::MAX; n];
        thresholds[0] = 0;
        thresholds[first_person] = 0;

        let mut queue: BinaryHeap<(i32, usize)> = BinaryHeap::new();
        queue.push((0, 0));
        queue.push((0, first_person));

        while let Some((time, node)) = queue.pop() {
            let time = (-time) as usize;

            for &(another, link_time) in links[node].iter() {
                if link_time < time {
                    continue;
                }

                if thresholds[another] <= link_time {
                    continue;
                }

                thresholds[another] = link_time;
                queue.push((-(link_time as i32), another))
            }
        }

        thresholds
            .into_iter()
            .enumerate()
            .filter(|&(_node, threshold)| threshold != usize::MAX)
            .map(|(node, _threshold)| node as i32)
            .collect()
    }
}
