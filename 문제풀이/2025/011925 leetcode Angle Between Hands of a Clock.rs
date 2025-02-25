impl Solution {
    pub fn angle_clock(hour: i32, minutes: i32) -> f64 {
        let minutes_angle = minutes as f64 * 6.0;
        let mut hour_angle = (hour as f64 * 30.0 + minutes as f64 / 2.0);

        if hour_angle >= 360.0 {
            hour_angle -= 360.0;
        }

        let angle = (hour_angle - minutes_angle).abs();

        if angle > 180.0 {
            360.0 - angle
        } else {
            angle
        }
    }
}
