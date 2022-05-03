// class Node {
//   constructor(value = undefined, next = undefined) {
//     this.next = next
//     this.value = value
//   }
// }
//
// class Queue {
//   constructor() {
//     this.head = undefined
//     this.tail = undefined
//     this.size = 0
//   }
//
//   length() {
//     return this.size
//   }
//
//   push(value) {
//     const node = new Node(value)
//     const tail = this.tail
//     if (!tail) {
//       this.head = node
//       this.tail = node
//       this.size = 1
//       return
//     }
//     tail.next = node
//     this.tail = node
//     this.size++
//   }
//
//   popLeft() {
//     const head = this.head
//     if (!head) {
//       throw new Error('No Element to pop')
//     }
//     this.head = head.next
//     if (!head) {
//       this.tail = undefined
//     }
//     this.size--
//     return head.value
//   }
// }
//
//
// class Stack {
//   constructor() {
//     this.head = undefined
//     this.tail = undefined
//     this.size = 0
//   }
//
//   length() {
//     return this.size
//   }
//
//   push(value) {
//     const node = new Node(value)
//     const tail = this.tail
//     if (!tail) {
//       this.head = node
//       this.tail = node
//       this.size = 1
//       return
//     }
//     tail.next = node
//     this.tail = node
//     this.size++
//   }
//
//   pop() {
//     const tail = this.tail
//     if (!this.size) {
//       throw new Error('No Element to pop')
//     }
//     if (this.size === 1) {
//       this.tail = this.head = undefined
//       this.size = 0
//       return tail.value
//     }
//
//     let head = this.head
//     while (head.next.next) {
//       head = head.next
//     }
//
//     head.next = undefined
//     this.tail = head
//     this.size--
//
//     return tail.value
//   }
// }
//
// class DequeNode {
//   constructor(value = undefined, left = undefined, right = undefined) {
//     this.value = value
//     this.left = left
//     this.right = right
//   }
// }
//
// class Deque {
//   constructor() {
//     this.head = undefined
//     this.tail = undefined
//     this.size = 0
//   }
//
//   length() {
//     return this.size
//   }
//
//   pushLeft(value) {
//     const node = new DequeNode(value)
//     if (!this.head) {
//       this.head = this.tail = node
//       this.size = 1
//       return
//     }
//     this.tail.left = this.tail.left || node
//     this.head.left = node
//     node.right = this.head
//     this.head = node
//
//     this.size++
//   }
//
//   push(value) {
//     const node = new DequeNode(value)
//     if (!this.head) {
//       this.head = this.tail = node
//       this.size = 1
//       return
//     }
//     this.head.right = this.head.right || node
//     this.tail.right = node
//     node.left = this.tail
//     this.tail = node
//
//     this.size++
//   }
//
//   popLeft() {
//     if (!this.size) {
//       throw new Error('No Element to pop')
//     }
//     const ret = this.head.value
//
//     this.head = this.head.right || undefined
//     if (!this.head) {
//       this.tail = undefined
//       this.size = 0
//       return ret
//     }
//     this.head.left = undefined
//     this.size--
//     return ret
//   }
//
//   pop() {
//     if (!this.size) {
//       throw new Error('No Element to pop')
//     }
//     const ret = this.tail.value
//
//     this.tail = this.tail.left || undefined
//     if (!this.tail) {
//       this.head = undefined
//       this.size = 0
//       return ret
//     }
//     this.tail.right = undefined
//     this.size--
//     return ret
//   }
// }
//
// class MinHeap {
//   constructor() {
//     this.list = []
//   }
//
//   push(value) {
//     this.list.push(value)
//     this.siftDown(this.list, 0, heap.length - 1)
//   }
//
//   pop() {
//     ret = this.list.pop()
//     if (!this.list.length) {
//       return ret
//     }
//     returnItem = this.list[0]
//     this.list[0] = ret
//     this.siftUp(this.list, 0)
//     return ret
//   }
//
//   siftDown(heap = this.list)
// }
//
// // def heappush(heap, item):
// //     """Push item onto heap, maintaining the heap invariant."""
// //     heap.append(item)
// //     _siftdown(heap, 0, len(heap)-1)
//
// // def heappop(heap):
// //     """Pop the smallest item off the heap, maintaining the heap invariant."""
// //     lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
// //     if heap:
// //         returnitem = heap[0]
// //         heap[0] = lastelt
// //         _siftup(heap, 0)
// //         return returnitem
// //     return lastelt
//
// // def _siftdown(heap, startpos, pos):
// //     newitem = heap[pos]
// //     # Follow the path to the root, moving parents down until finding a place
// //     # newitem fits.
// //     while pos > startpos:
// //         parentpos = (pos - 1) >> 1
// //         parent = heap[parentpos]
// //         if newitem < parent:
// //             heap[pos] = parent
// //             pos = parentpos
// //             continue
// //         break
// //     heap[pos] = newitem
//
// // def _siftup(heap, pos):
// //     endpos = len(heap)
// //     startpos = pos
// //     newitem = heap[pos]
// //     # Bubble up the smaller child until hitting a leaf.
// //     childpos = 2*pos + 1    # leftmost child position
// //     while childpos < endpos:
// //         # Set childpos to index of smaller child.
// //         rightpos = childpos + 1
// //         if rightpos < endpos and not heap[childpos] < heap[rightpos]:
// //             childpos = rightpos
// //         # Move the smaller child up.
// //         heap[pos] = heap[childpos]
// //         pos = childpos
// //         childpos = 2*pos + 1
// //     # The leaf at pos is empty now.  Put newitem there, and bubble it up
// //     # to its final resting place (by sifting its parents down).
// //     heap[pos] = newitem
// //     _siftdown(heap, startpos, pos)
