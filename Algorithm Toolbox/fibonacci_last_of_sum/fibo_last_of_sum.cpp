#include<iostream>
#include<vector>
using namespace std;
int fibonacci_last(int n) {
    if(n==0) return 0;
    int fib,sum=0,curr=1,prev=0;
    for(int i=0; i<=n; i++)
    {
        fib = prev + curr;
        prev = curr;
        curr++;
        sum+=fib;
    }
    if(n==0) return 0;
    return sum;
}


int main(){
    int n;
    cin>>n;
    cout<<fibonacci_last(n)<<endl;
}