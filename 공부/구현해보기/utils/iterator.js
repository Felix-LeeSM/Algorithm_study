/**
 * @generator
 * @type { <T>(...iterables: Array<Iterable<T>>) => Iterable<Array<T>> }
 */
export function* zip(...Iterables) {
  const iterators = Iterables.map((iter) => iter[Symbol.iterator]());
  let finish = false;
  while (true) {
    const ret = iterators.map((iter) => {
      const { done, value } = iter.next();
      finish = finish || done;
      return value;
    });
    if (!finish) {
      yield ret;
      continue;
    }
    return;
  }
}

/**
 * @generator
 * @type { <T>(element: T, times: number) => Iterable<T> }
 * @description yields element for times
 */
export function* repeat(element, times) {
  if (typeof element === 'function') for (let i = 0; i < times; i++) yield element();
  else for (let i = 0; i < times; i++) yield element;
}

/**
 * @generator
 * @type { (from: number, to: number, times: number) => Iterable<number> }
 * @description yields random numbers in range [from, to)
 */
export function* randomRepeat(from, to, times) {
  for (let i = 0; i < times; i++) yield Math.random() * (to - from) + from;
}

/** @type { (from: number, to: number) => number } */
export function random(from, to) {
  return Math.random() * (to - from) + from;
}

/**
 *
 * @generator
 * @type { (from: number, to: number, step?: number) => Iterable<number> }
 * @description yields number in range [from, to) with step.
 * @description swaps variable 'from' and variable 'to' when (to - from) * step < 0
 */
export function* range(from, to, step = 1) {
  [from, to] = (to - from) * step > 0 ? [from, to] : [to, from];

  const comparator = step > 0 ? (i, to) => i < to : (i, to) => i > to;
  for (let i = from; comparator(i, to); i += step) {
    yield i;
  }
}

/**
 * @function
 * @type { <T>(iterable: Iterable<T>) => Iterable<T> }
 * @description yields elements of iterable recursively
 */
export function* flat(iterable) {
  if (arguments.length !== 1) yield* flat(arguments);
  else {
    const hasIterator = (element) =>
      element !== null && typeof element === 'object' && element[Symbol.iterator] !== undefined;

    for (const element of iterable) {
      if (hasIterator(element)) yield* flat(element);
      else yield element;
    }
  }
}
