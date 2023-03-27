class Heap extends Array {
  constructor(value, rank) {
    super();
    if (value) this.hPush(value, rank);
  }
  hPush(value, rank) {
    const node = new Node(value, rank);
    this.push(node);
    this.heapifyUp(this.length - 1);
  }
  hPop() {
    const node = this[0];
    this[0] = this.pop();
    this.heapifyDown(0);
    return node.value;
  }
  heapifyUp(idx) {
    if (idx === 0) return;
    const parentIdx = Math.floor((idx - 1) / 2);
    if (this[parentIdx].rank > this[idx].rank) {
      [this[parentIdx], this[idx]] = [this[idx], this[parentIdx]];
      this.heapifyUp(parentIdx);
    }
  }
  heapifyDown(idx) {
    const leftIdx = idx * 2 + 1;
    const rightIdx = idx * 2 + 2;

    const leftRank = this[leftIdx] ? this[leftIdx].rank : Infinity;
    const rightRank = this[rightIdx] ? this[rightIdx].rank : Infinity;

    if (this[idx].rank > leftRank || this[idx].rank > rightRank) {
      const nextIdx = leftRank < rightRank ? leftIdx : rightIdx;
      [this[idx], this[nextIdx]] = [this[nextIdx], this[idx]];
      this.heapifyDown(nextIdx);
    }
  }
}
class Node {
  constructor(value, rank) {
    this.value = value;
    this.rank = rank;
  }
}
const input = (() => {
  const { readFileSync } = require('fs');
  const line = readFileSync('/dev/stdin', 'utf8').toString().split('\n').reverse();
  return () => {
    return line.pop();
  };
})();

function solution(N, foods) {
  const getDif = (from, to) => (from > to ? getDif(to, from) : Math.min(to - from, 10 + from - to));
  const getRank = (cnt, idx) => cnt * 10000 + idx;
  const getNext = (a, b, c, food) => [
    [...[b, c, food].sort((a_, b_) => a_ - b_), getDif(a, food)],
    [...[a, c, food].sort((a_, b_) => a_ - b_), getDif(b, food)],
    [...[a, b, food].sort((a_, b_) => a_ - b_), getDif(c, food)],
  ];

  const dp = Array(N)
    .fill(null)
    .map(() =>
      Array(10)
        .fill(null)
        .map(() =>
          Array(10)
            .fill(null)
            .map(() => Array(10).fill(Infinity))
        )
    );

  const queue = new Heap([0, 0, 0, 0, 0], 0);
  while (queue.length) {
    const [cnt, idx, a, b, c] = queue.hPop();
    if (idx === N) return cnt;

    for (const [na, nb, nc, dif] of getNext(a, b, c, foods[idx])) {
      if (dp[idx][na][nb][nc] > cnt + dif) {
        dp[idx][na][nb][nc] = cnt + dif;
        queue.hPush([cnt + dif, idx + 1, na, nb, nc], getRank(cnt + dif, idx + 1));
      }
    }
  }
}

(function main() {
  try {
    const N = Number(input());
    const foods = input().split(' ').map(Number);

    const answer = solution(N, foods);
    console.log(answer);
    return 1;
  } catch (err) {
    return 0;
  }
})();
