/**
 * @type { ( length?: number ) => Array<Date> }
 */
export const continuousDates = (length) => {
  const curDate = new Date().getDate();
  const dates = [];

  for (let day = length; day > 0; day--) {
    const date = new Date();
    date.setDate(curDate - day);
    date.setHours(12, 0, 0, 0);
    dates.push(date);
  }

  return dates;
};

/**
 * @type { ( length?: number ) => Array<string> }
 */
export const continuousLocaleDateStrings = (length) => {
  const curDate = new Date().getDate();
  const dates = [];

  for (let day = length; day > 0; day--) {
    const date = new Date();
    date.setDate(curDate - day);
    date.setHours(12, 0, 0, 0);
    dates.push(date.toLocaleDateString('ko-KR', { month: 'long', day: '2-digit' }));
  }

  return dates;
};
