class MaxHeap {
  constructor() {
    this.heap = [];
  }
  hPush(value) {
    this.heap.push(value);
    this.heapifyUp(this.heap.length - 1);
  }
  hPop() {
    if (this.heap.length === 0) throw new Error('Cannot Pop Empty Heap');
    if (this.heap.length === 1) return this.heap.pop();

    const maxVal = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown(0);
    return maxVal;
  }
  heapifyUp(idx) {
    if (idx === 0) return;

    const parentIdx = Math.floor((idx - 1) / 2);
    if (this.heap[idx] > this.heap[parentIdx]) {
      [this.heap[parentIdx], this.heap[idx]] = [this.heap[idx], this.heap[parentIdx]];
      this.heapifyUp(parentIdx);
    }
  }
  heapifyDown(idx) {
    const leftIdx = idx * 2 + 1;
    const rightIdx = idx * 2 + 2;

    const left = this.heap[leftIdx] ? this.heap[leftIdx] : -Infinity;
    const right = this.heap[rightIdx] ? this.heap[rightIdx] : -Infinity;
    const nextIdx = left > right ? leftIdx : rightIdx;

    if (this.heap[idx] < this.heap[nextIdx]) {
      [this.heap[idx], this.heap[nextIdx]] = [this.heap[nextIdx], this.heap[idx]];
      this.heapifyDown(nextIdx);
    }
  }
}

const input = (() => {
  const { readFileSync } = require('fs');
  const line = readFileSync('/dev/stdin', 'utf8').toString().split('\n').reverse();
  return () => {
    return line.pop();
  };
})();
(function main() {
  try {
    const [N, M] = input().split(' ').map(Number);
    const sadIndexes = input().split(' ').map(Number);

    const answer = solution(N, M, sadIndexes);
    console.log(answer);
    return 1;
  } catch (err) {
    return 0;
  }
})();
function solution(N, M, sads) {
  const eaten = new MaxHeap();
  let cnt = 0,
    curSad = 0;

  for (const sad of sads) {
    curSad += sad;
    eaten.hPush(sad);

    if (curSad >= M) {
      cnt++;
      curSad -= 2 * eaten.hPop();
    }
  }

  return cnt;
}
