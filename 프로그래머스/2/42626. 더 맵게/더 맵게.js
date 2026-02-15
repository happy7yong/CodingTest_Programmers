//40분에 시작
//50분에 heap 구현 시작 / 10분에 끝. : 첫 힙 - 20분정도 걸림 

class MinHeap {
    constructor(){
        this.heap = [];
    }
    insert(value){
        const heap = this.heap;
        heap.push(value);
        this.heapifyUp();
    }
    extractMin(){
        const heap = this.heap;
        
        if(heap.length === 0) return null;
        if(heap.length === 1) return heap.pop();
        
        let min = this.heap[0];
        
        heap[0] = heap.pop();
        this.heapifyDown();
        
        return min;
    }
    
    heapifyUp(){
        const heap = this.heap;
        let currentIndex = heap.length-1;
        
        while(currentIndex > 0){
            let parentIndex = Math.floor((currentIndex - 1)/2);
            
            if(heap[parentIndex] <= heap[currentIndex]) break;
            
            let temp = heap[parentIndex];
            heap[parentIndex] = heap[currentIndex];
            heap[currentIndex] = temp;
            
            currentIndex = parentIndex; 
        }
    }
    
    heapifyDown(){
        const heap = this.heap;
        let currentIndex = 0;
        
        
        while(true){
            let leftChildIndex = 2*currentIndex + 1;
            let rightChildIndex = 2*currentIndex + 2;
            let minIndex = currentIndex;
            
            if(leftChildIndex < heap.length && heap[leftChildIndex] < heap[minIndex] ){
               minIndex = leftChildIndex;
            }
            
            if(rightChildIndex < heap.length && heap[rightChildIndex] < heap[minIndex] ){
               minIndex = rightChildIndex;
            }
            
            if(minIndex === currentIndex) break;
            
            let temp = heap[minIndex];
            heap[minIndex] = heap[currentIndex];
            heap[currentIndex] = temp;

            currentIndex = minIndex;
            
        }
        
    }
    
    
}

function solution(scoville, K) {
    var answer = 0;
    
    //레오는 모든 음식의 스코빌 지수를 K 이상으로 만들거임.
    //모든 음식의 스코빌 지수를 K 이상으로 만듬.
    //스코빌 지수가 가장 낮은 두개의 음식을 섞어서 -> 새 음식 창출
    //섞은 음식의 스코빌 지수 : 가장 맵지 않은 음식의 스코빌 지수 + 두번째로 맵지 않은 스코빌 지수
    //ExtractMin 두번해서 섞기?
    //두번째 * 2 + 첫번째 
    
    //반복 횟수 : 모든 음식의 스코빌 지수가 K 이상이 될때까지 반복해서 섞기 
    const minHeap = new MinHeap();
    for(let i of scoville){
        minHeap.insert(i);
    }
    let first = 0;
    let second = 0;
    let count = 0;
    
    //scoville에서 첫번째 뽑아서 큐에 넣기 
    //1 | 2 3 9 10 12
    //길이가 2보다 작기 때문에 continue;
    
    //scoville에서 첫번째 뽑아서 큐에 넣기 
    //1 2| 3 9 10 12
    //첫번째 뽑아서 확인 < K일 경우 1 2 연산해서 5
    //5 | 3 9 10 12
    
    //scoville에서 첫번째 뽑아서 큐에 넣기 
    //3 5 | 9 10 12
    //첫번째 뽑아서 확인 < K일 경우 3 5 연산해서 13
    //13 | 9 10 12
    
    
    //만약 이렇게 끝났음.
    //6 | 0
    //루트 돌려고 할때 끝
    //6꺼내고 보니 7보다 작음
    
    let min = 0;
    
    

    

    while(minHeap.heap.length > 1 && minHeap.heap[0] < K){
        first = minHeap.extractMin();
        second = minHeap.extractMin();
        
        minHeap.insert(first + second*2);
        count++;
        
    }
    
    
    
    
    
    return minHeap.heap[0] >= K ? count : -1;
}