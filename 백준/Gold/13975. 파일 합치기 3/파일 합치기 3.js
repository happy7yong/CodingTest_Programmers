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
        if(heap.length === 0) return null;
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
            let parentIndex = Math.floor((currentIndex - 1)/2);

            if(heap[parentIndex] <= heap[currentIndex]) break;

            let swap = heap[parentIndex];
            heap[parentIndex] = heap[currentIndex];
            heap[currentIndex] = swap;

            currentIndex = parentIndex;
        }
    }

    heapifyDown(){
        let heap = this.heap;
        let currentIndex = 0;

        while(true) {
            let leftChildIndex = currentIndex*2 + 1;
            let rightChildIndex = currentIndex*2 + 2;
            let minIndex = currentIndex;

            if(leftChildIndex < heap.length && heap[leftChildIndex] < heap[minIndex]) minIndex = leftChildIndex;
            if(rightChildIndex < heap.length && heap[rightChildIndex] < heap[minIndex]) minIndex = rightChildIndex;

            if(minIndex === currentIndex) break;

            let swap = heap[minIndex];
            heap[minIndex] = heap[currentIndex];
            heap[currentIndex] = swap;

            currentIndex = minIndex;
        }


    }

}

function solution(n, arr){
    let total = 0;
    const minHeap = new MinHeap();
    let min = 0 ;
    let sum = 0;

    for(let i of arr){
        minHeap.insert(i);
    }

    while(minHeap.heap.length > 1){
        first = minHeap.extractMin();
        second = minHeap.extractMin();
        sum = first + second
        total += sum;
        minHeap.insert(sum);
    }

    return total;
}

let n = Number(input[0]);

let answer = [];
for(let i=1;i<=n;i++){
    const n = Number(input[2*i-1]);
    const arr = input[2*i].split(" ").map(Number);

    answer.push(solution(n, arr));
}

console.log(answer.join("\n"));