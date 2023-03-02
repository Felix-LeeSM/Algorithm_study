{
  class Heap {
    constructor(key = null) {
      if (key === null) {
        this.key = (x) => x;
      } else {
        this.key = key;
      }

      this.arr = [null];
    }

    push(x) {
      let idx = this.arr.length;
      this.arr.push(x);

      while (idx > 1) {
        const parent = idx >> 1;

        if (this.key(this.arr[parent]) > this.key(this.arr[idx])) {
          [this.arr[parent], this.arr[idx]] = [this.arr[idx], this.arr[parent]];
        } else {
          break;
        }
        idx >>= 1;
      }
    }

    pop() {
      if (this.arr.length == 1) throw new Error('Heap is empty');

      [this.arr[this.arr.length], this.arr[1]] = [this.arr[1], this.arr.at(-1)];
      const ret = this.arr.pop();

      let idx = 1;
      while (idx < this.arr.length) {
        const left = idx << 1;
        const right = left + 1;

        if (left >= this.arr.length) break;

        let next = left;
        if (right < this.arr.length && this.key(this.arr[left]) > this.key(this.arr[right])) {
          next = right;
        }

        if (this.key(this.arr[idx]) > this.key(this.arr[next])) {
          [this.arr[idx], this.arr[next]] = [this.arr[next], this.arr[idx]];
        }
        idx = next;
      }
      return ret;
    }
  }
}
