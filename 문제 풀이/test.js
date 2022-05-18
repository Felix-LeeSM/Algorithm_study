// // class Node {
// //   constructor(value = undefined, next = undefined) {
// //     this.next = next
// //     this.value = value
// //   }
// // }

// // class Queue {
// //   constructor() {
// //     this.head = undefined
// //     this.tail = undefined
// //     this.size = 0
// //   }

// //   length() {
// //     return this.size
// //   }

// //   push(value) {
// //     const node = new Node(value)
// //     const tail = this.tail
// //     if (!tail) {
// //       this.head = node
// //       this.tail = node
// //       this.size = 1
// //       return
// //     }
// //     tail.next = node
// //     this.tail = node
// //     this.size++
// //   }

// //   popLeft() {
// //     const head = this.head
// //     if (!head) {
// //       throw new Error('No Element to pop')
// //     }
// //     this.head = head.next
// //     if (!head) {
// //       this.tail = undefined
// //     }
// //     this.size--
// //     return head.value
// //   }
// // }

// // class Stack {
// //   constructor() {
// //     this.head = undefined
// //     this.tail = undefined
// //     this.size = 0
// //   }

// //   length() {
// //     return this.size
// //   }

// //   push(value) {
// //     const node = new Node(value)
// //     const tail = this.tail
// //     if (!tail) {
// //       this.head = node
// //       this.tail = node
// //       this.size = 1
// //       return
// //     }
// //     tail.next = node
// //     this.tail = node
// //     this.size++
// //   }

// //   pop() {
// //     const tail = this.tail
// //     if (!this.size) {
// //       throw new Error('No Element to pop')
// //     }
// //     if (this.size === 1) {
// //       this.tail = this.head = undefined
// //       this.size = 0
// //       return tail.value
// //     }

// //     let head = this.head
// //     while (head.next.next) {
// //       head = head.next
// //     }

// //     head.next = undefined
// //     this.tail = head
// //     this.size--

// //     return tail.value
// //   }
// // }

// // class DequeNode {
// //   constructor(value = undefined, left = undefined, right = undefined) {
// //     this.value = value
// //     this.left = left
// //     this.right = right
// //   }
// // }

// // class Deque {
// //   constructor() {
// //     this.head = undefined
// //     this.tail = undefined
// //     this.size = 0
// //   }

// //   length() {
// //     return this.size
// //   }

// //   pushLeft(value) {
// //     const node = new DequeNode(value)
// //     if (!this.head) {
// //       this.head = this.tail = node
// //       this.size = 1
// //       return
// //     }
// //     this.tail.left = this.tail.left || node
// //     this.head.left = node
// //     node.right = this.head
// //     this.head = node

// //     this.size++
// //   }

// //   push(value) {
// //     const node = new DequeNode(value)
// //     if (!this.head) {
// //       this.head = this.tail = node
// //       this.size = 1
// //       return
// //     }
// //     this.head.right = this.head.right || node
// //     this.tail.right = node
// //     node.left = this.tail
// //     this.tail = node

// //     this.size++
// //   }

// //   popLeft() {
// //     if (!this.size) {
// //       throw new Error('No Element to pop')
// //     }
// //     const ret = this.head.value

// //     this.head = this.head.right || undefined
// //     if (!this.head) {
// //       this.tail = undefined
// //       this.size = 0
// //       return ret
// //     }
// //     this.head.left = undefined
// //     this.size--
// //     return ret
// //   }

// //   pop() {
// //     if (!this.size) {
// //       throw new Error('No Element to pop')
// //     }
// //     const ret = this.tail.value

// //     this.tail = this.tail.left || undefined
// //     if (!this.tail) {
// //       this.head = undefined
// //       this.size = 0
// //       return ret
// //     }
// //     this.tail.right = undefined
// //     this.size--
// //     return ret
// //   }
// // }

// // class Heap {
// //   constructor() {
// //     this.items = [];
// //   }

// //   //값을 서로 바꾸는 메소드
// //   swap(index1, index2) {
// //     let temp = this.items[index1]; // items의 index1의 값을 temp(임시공간)에 담음
// //     this.items[index1] = this.items[index2]; // index1에 index2의 값을 저장
// //     this.items[index2] = temp; // index2에 아까 index1의 값을 temp에 넣어놓은 값을 저장
// //   }

// //   //부모 인덱스 구하는 메소드
// //   parentIndex(index) {
// //     return Math.floor((index - 1) / 2);
// //   }

// //   //왼쪽 자식 인덱스 구하는 메소드
// //   leftChildIndex(index) {
// //     return index * 2 + 1;
// //   }

// //   //오른쪽 자식 인덱스 구하는 메소드
// //   rightChildIndex(index) {
// //     return index * 2 + 2;
// //   }

// //   //부모 노드 구하는 메소드
// //   parent(index) {
// //     return this.items[this.parentIndex(index)];
// //   }

// //   //왼쪽 자식 노드 구하는 메소드
// //   leftChild(index) {
// //     return this.items[this.leftChildIndex(index)];
// //   }

// //   //오른쪽 자식 노드 구하는 메소드
// //   rightChild(index) {
// //     return this.items[this.rightChildIndex(index)];
// //   }

// //   //최대 힙의 경우 최댓값을 반환하고 최소 힙의 경우 최솟값을 반환하는 메소드
// //   peek() {
// //     return this.items[0];
// //   }

// //   //힙의 크기(항목 개수)를 반환하는 메소드
// //   size() {
// //     return this.items.length;
// //   }
// // }

// // class MinHeap extends Heap {
// //   // MinHeap 클래스는 Heap 클래스를 상속받았으므로 Heap 클래스의 메소드를 모두 사용할 수 있다.
// //   bubbleUp() {
// //     let index = this.items.length - 1;
// //     while (this.parent(index) !== undefined && this.parent(index) > this.items[index]) {
// //       this.swap(index, this.parentIndex(index));
// //       index = this.parentIndex(index);
// //     }
// //   }

// //   bubbleDown() {
// //     let index = 0;
// //     while (this.leftChild(index) !== undefined
// //       && (this.leftChild(index) < this.items[index] || this.rightChild(index) < this.items[index])) {
// //       let smallerIndex = this.leftChildIndex(index);

// //       if (this.rightChild(index) !== undefined && this.rightChild(index) < this.items[smallerIndex]) {
// //         smallerIndex = this.rightChildIndex(index);
// //       }
// //       this.swap(index, smallerIndex);
// //       index = smallerIndex;
// //     }
// //   }

// //   // 힙에 원소를 추가하는 함수

// //   add(item) {
// //     this.items[this.items.length] = item;
// //     this.bubbleUp();
// //   }

// //   // 최소 힙이라면 최솟값이 빠져나올 것이고 최대힙이라면 최댓값이 빠져나온다.
// //   poll() {
// //     let item = this.items[0]; // 첫번째 원소 keep
// //     this.items[0] = this.items[this.items.length - 1]; // 맨 마지막 원소를 첫번째 원소로 복사
// //     this.items.pop(); // 맨 마지막 원소 삭제
// //     this.bubbleDown();
// //     return item; // keep해둔 값 반환
// //   }
// // }

// // class MaxHeap extends MinHeap {
// //   //MaxHeap의 경우 MinHeap을 상속받았으므로 MinHeap의 모든 함수를 사용할 수 있지만 bubbleUp과 bubbleDown은 Overriding(재정의)하였다.
// //   bubbleUp() {
// //     let index = this.items.length - 1;
// //     while (this.parent(index) !== undefined && this.parent(index) < this.items[index]) {
// //       this.swap(index, this.parentIndex(index));
// //       index = this.parentIndex(index);
// //     }
// //   }

// //   bubbleDown() {
// //     let index = 0;

// //     while (this.leftChild(index) !== undefined
// //       && (this.leftChild(index) > this.items[index] || this.rightChild(index) > this.items[index])) {
// //       let largerIndex = this.leftChildIndex(index);
// //       if (this.rightChild(index) !== undefined && this.rightChild(index) > this.items[largerIndex]) {
// //         largerIndex = this.rightChildIndex(index);
// //       }
// //       this.swap(largerIndex, index);
// //       index = largerIndex;
// //     }
// //   }
// // }

// function oldSolution(board) {
//   function makeVisited(edge) {
//     const visited = [];
//     for (let i = 0; i < edge; i++) {
//       visited.push([]);
//       for (let j = 0; j < edge; j++) {
//         visited[i].push(0);
//       }
//     }
//     return visited;
//   }

//   function check(edge, i, j, board) {
//     const [dx, dy] = [
//       [0, 1, 0, -1],
//       [1, 0, -1, 0],
//     ];
//     const visited = makeVisited(edge);

//     let ret = edge;
//     const stack = [];
//     if (i === -1) {
//       for (let r = 0; r < edge; r++) {
//         stack.push([r, j, board[r][j]]);
//         visited[r][j]++;
//       }
//     } else {
//       for (let r = 0; r < edge; r++) {
//         stack.push([i, r, board[i][r]]);
//         visited[i][r]++;
//       }
//     }

//     while (stack.length) {
//       const [x, y, b] = stack.pop();
//       for (let d = 0; d < 4; d++) {
//         const [nx, ny] = [x + dx[d], y + dy[d]];
//         if (0 <= nx && nx < edge && 0 <= ny && ny < edge) {
//           if (visited[nx][ny]) continue;
//           if (board[nx][ny] === b) {
//             visited[nx][ny]++;
//             ret++;
//             stack.push([nx, ny, b]);
//           }
//         }
//       }
//     }

//     return ret;
//   }

//   function solution(board) {
//     const L = board.length;
//     let answer = 0;

//     for (let i = 0; i < L; i++) {
//       answer = Math.max(answer, check(L, -1, i, board), check(L, i, -1, board));
//     }

//     return answer;
//   }

//   return solution(board);
// }

// function solution(board) {
//   const L = board.length;
//   const horizontal = [0];
//   const vertical = [0];
//   const visited = [];

//   for (let i = 0; i < L; i++) {
//     horizontal.push(0);
//     vertical.push(0);
//     visited.push([]);
//     for (let j = 0; j < L; j++) {
//       visited[i].push(0);
//     }
//   }

//   // visited, vertical, horizontal 만들었음
//   const [dx, dy] = [
//     [0, 1, 0, -1],
//     [1, 0, -1, 0],
//   ];
//   for (let i = 0; i < L; i++) {
//     for (let j = 0; j < L; j++) {
//       if (visited[i][j]) continue;

//       visited[i][j]++;
//       let [foreLeft, foreRight, ceil, floor] = [j, j, i, i];
//       let area = 1;
//       const stack = [[i, j, board[i][j]]];

//       while (stack.length) {
//         const [x, y, b] = stack.pop();
//         for (let d = 0; d < 4; d++) {
//           const [nx, ny] = [x + dx[d], y + dy[d]];
//           if (0 <= nx && nx < L && 0 <= ny && ny < L) {
//             if (visited[nx][ny] || board[nx][ny] !== b) continue;

//             area++;
//             visited[nx][ny]++;
//             foreLeft = ny < foreLeft ? ny : foreLeft;
//             foreRight = foreRight < ny ? ny : foreRight;
//             ceil = nx < ceil ? nx : ceil;
//             floor = floor < nx ? nx : floor;
//             stack.push([nx, ny, b]);
//           }
//         }
//       }

//       horizontal[foreLeft] += area;
//       horizontal[foreRight + 1] -= area;
//       vertical[ceil] += area;
//       vertical[floor + 1] -= area;
//     }
//   }

//   for (let i = 0; i < L; i++) {
//     horizontal[i + 1] += horizontal[i];
//     vertical[i + 1] += vertical[i];
//   }

//   const answer = Math.max(Math.max(horizontal), Math.max(vertical));
//   return answer;
// }

console.log(typeof {} === 'object');
