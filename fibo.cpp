#include <iostream>
using namespace std;
int main(int argc, char *argv[])
{
    cout<<"value of argc : "<<argc<<endl;
    cout<<"value of argv "<<endl;
    for(int i = 0; i < argc; i++)
    {
        cout<< argv[i]<<" "<< typeof(argv[i])<<endl;

    }
    
    return 0;
}

// #include <iostream>
// using namespace std;
// int main(int argc, int *argv[])
// {
//     int f=0,s=1,temp;
//    in n=argv[1];
//    cout<< n;
//     for(int i = 0; i < n; i++)
//     {
//         // cout<<f<<" ";
//         temp=f;
//         f=s;
//         s=s+i;

//     }
    
    
//     return 0;
// }