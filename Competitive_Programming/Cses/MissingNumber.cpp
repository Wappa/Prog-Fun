#include <iostream>
using namespace std;

int main()
{
    long long int n, s = 0, ele;
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        cin >> ele;
        s += ele;
    }
    cout << n * (n + 1) / 2 - s;
    return 0;
}


//FirstTry

/*#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main ()
{
    long long n, x;
    cin >> n;
    vector<long long > vec;
    for (long long i = 0 ; i < n-1 ; i++)
    {
        cin >> x;
        vec.push_back(x);
    }

    if(n == 2)
    {
        if (vec[0] == 1)
        {
            cout << 2 << "\n";
        }
        else
        {
            cout << 1 << "\n";
        }
    }
    sort(vec.begin(),vec.end());
    for(long long j = 0 ; j < vec.size()-1;j++)
    {
        if(vec[j]+1 != vec[j+1])
        {
            cout << vec[j]+1 << "\n" ;
        }
    }

    return 0;
}
