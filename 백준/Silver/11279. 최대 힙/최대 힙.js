const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

class MaxHeap{
    constructor(){
        this.heap = [];
    }

    insert(value){
        let heap = this.heap;
        heap.push(value);
        this.heapifyUp();
    }
    extractMax(){
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

            if(heap[parentIndex] >= heap[currentIndex]) break;

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

            if(leftChildIndex < heap.length && heap[leftChildIndex] > heap[minIndex]) minIndex = leftChildIndex;
            if(rightChildIndex < heap.length && heap[rightChildIndex] > heap[minIndex]) minIndex = rightChildIndex;

            if(minIndex === currentIndex) break;

            let swap = heap[minIndex];
            heap[minIndex] = heap[currentIndex];
            heap[currentIndex] = swap;

            currentIndex = minIndex;
        }


    }

}

function solution(n, arr){
    let max = 0;
    const maxHeap = new MaxHeap();
    let answer = [];

    //배열이 비어있는데 0일 경우
    for(let i of arr){
        if(i === 0){
            if(maxHeap.heap.length === 0) {
                answer.push(0);
                continue;
            }
            max = maxHeap.extractMax();
            answer.push(max);
            continue;
        }
        maxHeap.insert(i)
    }

    return answer;
}

const n = Number(input[0]);
const arr = input.slice(1).map(Number);

console.log(solution(n, arr).join("\n"));

