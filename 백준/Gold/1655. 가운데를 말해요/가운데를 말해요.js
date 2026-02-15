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
    let answer = [];
    const minHeap = new MinHeap();
    const maxHeap = new MaxHeap();
    let med = 0;


    for(let i=0;i<arr.length;i++){

        //첫값 처리
        if(minHeap.heap.length == 0 && maxHeap.heap.length == 0) {
            maxHeap.insert(arr[i]);
            med = maxHeap.heap[0];
            answer.push(med);
            continue;
        }

        if(arr[i] <= maxHeap.heap[0]){
            maxHeap.insert(arr[i]);
        }else{
            minHeap.insert(arr[i]);
        }

        //크기 균형 맞추기 
        if(maxHeap.heap.length > minHeap.heap.length + 1){
            minHeap.insert(maxHeap.extractMax());
        }else if(minHeap.heap.length > maxHeap.heap.length){
            maxHeap.insert(minHeap.extractMin());
        }

        //순서 깨짐 방지
        if(minHeap.heap.length && maxHeap.heap[0] > minHeap.heap[0]){
            let a = maxHeap.extractMax();
            let b = minHeap.extractMin();
            maxHeap.insert(b);
            minHeap.insert(a);
        }

        med = maxHeap.heap[0];
        answer.push(med);


    }


    return answer;
}

let n = Number(input[0]);
let arr = input.slice(1).map(Number);


console.log(solution(n,arr).join("\n"));
