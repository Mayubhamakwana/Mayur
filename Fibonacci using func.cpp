#include<iostream>
using namespace std;
int fibonacci(int n)
{
    int n3=0,n4=1,n5,i;
    for(i=1;i<=n;i++){
    n3=n4+n5;
    n5=n4;
    n3=n5;
    cout<<n3;
    }
}
int main()
{
    int n;
    
    cout << "enter a value:" << endl;
    cin>>n;
    
    fibonacci(n);
    return 0;
}

