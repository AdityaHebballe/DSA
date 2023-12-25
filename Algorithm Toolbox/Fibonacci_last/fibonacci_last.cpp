#include <iostream>
using namespace std;
int fibonacci_last(int n) {
    long long fibo[n];
    fibo[0] = 0;
    fibo[1] = 1;
    for(int i=2; i<=n; i++)
    {
        fibo[i] = ((long long)fibo[i-1] + (long long)fibo[i-2])%10;
    }
    return fibo[n];
}

int main(){
    int n;
    cin>>n;
    cout<<fibonacci_last(n)%10<<endl;

}