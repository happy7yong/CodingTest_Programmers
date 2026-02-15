const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

class MinHeap{
    constructor(){
        this.heap = [];
    }

    insert(value){
        let heap = this.heap;
        heap.push(value);
        this.heapifyUp();
    }

    extractMin(){
        let heap = this.heap;

        if(heap.length === 1) return heap.pop();

        let min = heap[0];
        heap[0] = heap.pop();
        this.heapifyDown();
        return min;
    }

    heapifyUp(){
        let heap = this.heap;
        let currentIndex = heap.length - 1;

        while(currentIndex > 0){
            let parentIndex = (currentIndex - 1) >> 1;

            if(heap[parentIndex] <= heap[currentIndex]) break;

            let temp = heap[parentIndex];
            heap[parentIndex] = heap[currentIndex];
            heap[currentIndex] = temp;

            currentIndex = parentIndex;
        }
    }

    heapifyDown(){
        let heap = this.heap;
        let currentIndex = 0;

        while(true){
            let left = currentIndex*2 + 1;
            let right = currentIndex*2 + 2;
            let minIndex = currentIndex;

            if(left < heap.length && heap[left] < heap[minIndex])
                minIndex = left;

            if(right < heap.length && heap[right] < heap[minIndex])
                minIndex = right;

            if(minIndex === currentIndex) break;

            let temp = heap[minIndex];
            heap[minIndex] = heap[currentIndex];
            heap[currentIndex] = temp;

            currentIndex = minIndex;
        }
    }
}

function solution(n, cards){
    if(n === 1) return 0;

    const minHeap = new MinHeap();
    let total = 0;

    for(let c of cards){
        minHeap.insert(c);
    }

    while(minHeap.heap.length > 1){
        let a = minHeap.extractMin();
        let b = minHeap.extractMin();

        let sum = a + b;
        total += sum;
        minHeap.insert(sum);
    }

    return total;
}

const n = Number(input[0]);
const cards = input.slice(1).map(Number);

console.log(solution(n, cards));
