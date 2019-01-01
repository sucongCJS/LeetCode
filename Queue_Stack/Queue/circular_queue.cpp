#include <iostream>
#include <vector>
using namespace std;

class MyCircularQueue{
private:
    vector<int> data;
    int head;
    int tail;
    int size;
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k){
        data.resize(k);
        head = -1;
        tail = -1;
        size = k;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value){
        if (isFull()){
            return false;
        }
        // head and tail are the same
        if (isEmpty()){
            head = 0;
        }
        tail = (tail + 1) % size;
        data[tail] = value;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue(){
        if (isEmpty()){
            return false;
        }
        // only one element left
        if (head == tail){
            head = -1;
            tail = -1;
            return true;
        }
        head = (head + 1) % size;
        return true;
    }
    /** Get the front item from the queue. */
    int Front(){
        if (isEmpty()){
            return -1;
        }
        return data[head];
    }
    /** Get the last item from the queue. */
    int Rear(){
        if (isEmpty()){
            return -1;
        }
        return data[tail];
    }
    /** Checks whether the circular queue is full or not. */
    bool isFull(){
        return ((tail + 1) % size) == head;
    }
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty(){
        return head == -1;
    }
};

int main(){
    MyCircularQueue q(3);
    q.enQueue(1);
    q.enQueue(3);
    q.enQueue(13);
    if (q.isFull()){
        cout<<"full now"<<endl;
    }
    else{
        cout<<"not full"<<endl;
    }
    if (!q.isEmpty()) {
        cout<<q.Rear()<<endl;
        cout<<q.Front()<<endl;
    }
    q.deQueue();
    if (!q.isEmpty()) {
        cout<<q.Front()<<endl;
    }
    q.deQueue();
    if (!q.isEmpty()) {
        cout<<q.Front()<<endl;
    }
}