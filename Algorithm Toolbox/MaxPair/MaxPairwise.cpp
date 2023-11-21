#include<iostream>
#include<vector>
using namespace std;

long long MaxPairwiseProductFast(vector<int> numbers)
{
    int n = numbers.size();

    int max_index1=-1;
    for(int i=0;i<n;++i)
     if((max_index1 == -1)|| (numbers[i]> numbers[max_index1]))
        max_index1 = i;
    
    int max_index2 = -1;
    for(int j=0;j<n;++j)
     if((numbers[j]!=numbers[max_index1])&&(max_index2 == -1)|| (numbers[j]> numbers[max_index2]))
        max_index2 = j;

    return ((long long)(numbers[max_index1])) *numbers[max_index2];

}

int main(){
    // int n;
    // cin>>n;
    // vector<int>number(n);
    // for(int i=0; i<n;i++)
    // {
    //     cin>>number[i];
    // }
    long long result= MaxPairwiseProductFast(vector<int>(100000,0));
    cout<<result<<"\n";
    return 0;
}