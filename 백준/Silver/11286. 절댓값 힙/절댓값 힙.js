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

            if(this.compare(heap[parentIndex], heap[currentIndex]) <= 0) break;

            let swap = heap[parentIndex];
            heap[parentIndex] = heap[currentIndex];
            heap[currentIndex] = swap;

            currentIndex = parentIndex;
        }
    }

    compare(a,b){
        if(Math.abs(a) === Math.abs(b)){
            return a-b;
        }
        
        return Math.abs(a) - Math.abs(b)

    }

    heapifyDown(){
        let heap = this.heap;
        let currentIndex = 0;

        while(true) {
            let leftChildIndex = currentIndex*2 + 1;
            let rightChildIndex = currentIndex*2 + 2;
            let minIndex = currentIndex;

            if(leftChildIndex < heap.length && this.compare(heap[leftChildIndex], heap[minIndex]) < 0) minIndex = leftChildIndex;
            if(rightChildIndex < heap.length && this.compare(heap[rightChildIndex], heap[minIndex]) < 0) minIndex = rightChildIndex;

            if(minIndex === currentIndex) break;

            let swap = heap[minIndex];
            heap[minIndex] = heap[currentIndex];
            heap[currentIndex] = swap;

            currentIndex = minIndex;
        }


    }

}

function solution(n, arr){
    const minHeap = new MinHeap();
    let min = 0;
    let answer = [];

    for(let i of arr){
        if(i === 0){
            //절댓값이 가장 작은 값을 출력
            if(minHeap.heap.length === 0) {
                answer.push(0);
                continue;
            }
            min = minHeap.extractMin();
            answer.push(min);
            continue;

        }
        minHeap.insert(i);
    }

    return answer;
}

const n = Number(input[0]);
const arr = input.slice(1).map(Number);

console.log(solution(n, arr).join("\n"));

