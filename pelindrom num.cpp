#include<iostream>
using namespace std;

 int main()
 {
   int rem,rev=0,n,i;
   
   cout << "enter a value:" << endl;
   cin>>n;
   int j=n;
   while(n!=0)
   {
     rem=n%10;
     rev=rev*10+rem;
     n=n/10;
   }
   cout <<rev;
   if(rev==j)
   {
     cout << "enter number is pelindrom" << endl;
     
   }
   else
   {
    cout << "enter number is not pelindrom" << endl;
   }
   
   return 0;
 }
