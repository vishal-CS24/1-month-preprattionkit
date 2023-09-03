#include <iostream>
using namespace std;
void myswap(int &vref_1,int &vref_2)
{
	int temp_var;
	temp_var=vref_1;
	vref_1=vref_2;
	vref_2=temp_var;
}
int main()
{
int var_1=30;
int var_2=40;
cout<<"Brfore swapping myswap(),value of var_1 : "<<var_1<<endl;
cout<<"Brfore swapping myswap(),value of var_2 : "<<var_2<<endl<<endl;

cout<<"calling myswap() function- call by value"<<endl<<endl;
myswap(var_1,var_2);
cout<<"After swapping myswap(),value of var_1 : "<<var_1<<endl;
cout<<"After swapping myswap(),value of var_2 : "<<var_2<<endl;
return 0;
}
