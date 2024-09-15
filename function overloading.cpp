#include<iostream>
using namespace std;

  int sum(int a,int b)
  {
     return a+b;
  }
  float sum(float a,float b,float c)
  {
      return a+b+c;
  }
  int main()
  {
    int result1=sum(10,20);
    cout << "sum is :" <<result1<<endl;
    int result2=sum(10.26,20.95,30.37);
    cout << "sum is :" <<result2<<endl;
    
    return 0;
   }
