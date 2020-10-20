#include <bits/stdc++.h>
using namespace std;
int main() {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    vector <int> v;
    for (int i=1 ; i<=10; i++)
    {
        v.push_back(i);
    }
    v.push_back(11);

    v.push_back(12);
    //v.erase(v.begin()+2,v.begin()+5+1);
    v.insert(v.begin()+3,5);
    //v.clear();
    if (v.empty())
    {
       cout<<"yes empty \n";
    }
    else
        {
        cout<<"no not empt \n";
        }
    v[0]=100;
    int l=v.size();
    for (int i=0; i<l; i++)
    {
        cout<<v[i]<<" ";
    }


    pair <int,string> p;
    p=make_pair(1,"naval");
    int x=p.first;
    string y=p.second;
    cout<<"\n"<<x<<"-"<<y;

}
