class MinHeap {
    // definition:
    // a complete binary tree, all the levels are filled except the last level which if it is partially filled up, it has to be filled from left to right
    // heap property, minHeap states every node in the heap has a value, this value is going to smaller or equal to its children node values. maxheap, node >= children nodes
    // from the property, we know that the root node is the smallest values in the heap
    // MinHeap can be represent by arrays, from parent to leftchild i -> 2i+1, rightchild i -> 2i+2
    // from child to parentNode: floor((i-1)/2) 
    // MinHeap:
    //         8
    //     12      23
    //   17  31  30  44
    //102 18
    // array representation: [8, 12, 23, 17, 31, 30, 44, 102, 18] 


    constructor(array) {
        this.heap = this.buildHeap(array);
    }

    buildHeap(array){
    // unsorted or sorted array, this is the method need other methods
    // after add to the end of the heap and sift it around to the correct position
    // think about append a new value to the array and swap it to the correct position

    }

    siftDown(i, j, heap){

    }

    siftUp(){

    }

    peek(){
        return this.heap[0];
    }

    remove(){

    }

    insert(value){

    }

    swap(i, j){
        let tmp = this.heap[j];
        this.heap[j] = this.heap[i];
        this.heap[i] = tmp;
    }
}


