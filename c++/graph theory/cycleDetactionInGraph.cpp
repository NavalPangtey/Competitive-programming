#include<bits/stdc++.h>
using namespace std;

vector<int> v[100000];
int vis[100000];

void read()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

bool dfs(int node, int par)
{
    vis[node] = 1;
    for (int child : v[node])
    {
        if (vis[child] == 0)
        {
            if (dfs(child, node) == true)
                return true;
        }
        else if (child != par)
        {
            return true;
        }
    }
    return false;

}


int main()
{

    read();
    int t;
    cin >> t;
    int i = 1;
    while (t--)
    {
        // v.empty();
        int a , b, n, m;
        cin >> n >> m;
        for (int i = 0 ; i <= n; i++)
        {
            vis[i] = 0;
            v[i].clear();
        }
        for (int i = 0 ; i < m; i++)
        {
            cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }
        bool flag = false;
        for (int i = 1; i <= n; i++)
        {
            if (vis[i] == 0)
            {
                bool res = dfs(i, 0);

                if (res == true)
                    flag = true;

            }

        }
        cout << "Scenario #" << i << ":" << "\n";
        if (flag == true)
            cout << "Cycle Found!!" << "\n";
        else
            cout << "No Cycle found!" << "\n";
        i++;
    }

}


