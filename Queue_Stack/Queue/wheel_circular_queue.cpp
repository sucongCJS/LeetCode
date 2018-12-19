#include <iostream>
#include <queue>
using namespace std;

int main(){
    queue<int> q;

    q.push(5);
    q.push(8);
    q.push(10);

    cout<<q.size()<<endl;
    cout<<q.front()<<endl;
    cout<<q.back()<<endl;

    q.pop();

    cout<<q.front()<<endl;
    cout<<q.back()<<endl;

    q.pop();

    cout<<q.empty()<<endl;

    q.pop();

    cout<<q.empty()<<endl;
}