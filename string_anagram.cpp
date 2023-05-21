#include<iostream>
#include <string>
#include <vector>
using namespace std;

bool is_anagram(string s1,string s2){
    vector<int> v1(26,0);

    if(s1.size() != s2.size())
    {
        return false;
    }

    for(int i = 0; i < s1.size(); i++)
    {
        v1[s1[i]-'a']++;
        v1[s2[i]-'a']--;
    }
    for(int i = 0; i < 26; i++)
    {
        if(v1[i]!=0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    string s1,s2;
    cin>>s1>>s2;
    if (is_anagram(s1,s2)){
        cout << "strings are anagram";
    }
    else 
    {
        cout<<"strings are not anagram";
    }
    return 0;
}
