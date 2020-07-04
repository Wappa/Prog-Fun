#include <bits/stdc++.h>

using namespace std;

vector<int> Find (vector<int> list1,vector<int> list2)
{
    vector <int> vec1 = {1};
    vector <int> vec2 = {2};
    if(list1.size() < list2.size())
    {
        return vec1;
    }
    else
    {
        return vec2;
    }
}


int main()
{
    vector <int> l1 = {1,2,3};
    vector <int> l2 = {1,2,3,4,5};
    cout << Find(l1,l2);
}


