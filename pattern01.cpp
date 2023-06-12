// 1 
// 0 1 
// 1 0 1
// 0 1 0 1 
// 1 0 1 0 1
#include <iostream>
using namespace std;
void printTriangle(int n) {
        int status=1;
        for(int i=0;i<n;i++){
               if(i%2==0){
                    status=1;
                }
                else{
                    status=0;
                }
            for(int j=0;j<=i;j++){
                cout<<status<<" ";
                status=1-status;
            }
            cout<<"\n";
        }
    }

int  main()
{   int n;
    cin>>n;
    printTriangle(n);
    return 0;
}
