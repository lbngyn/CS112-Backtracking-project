#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, S;
vector<int> t;
int Count = 0;
vector<vector<int>> ways;

void withdrawMoney(int id, int total, vector<int> path)
{
    if (total == S)
    {
        ways.push_back(path);
        Count++;
        return;
    }

    for (int i = id; i < n; i++)
    {
        if (t[i] + total <= S)
        {
            path.push_back(t[i]);
            withdrawMoney(i, total + t[i], path);
            path.pop_back();
        }
    }
}

int main()
{
    cin >> n >> S;
    t.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin >> t[i];
    }

    sort(t.begin(), t.end());

    withdrawMoney(0, 0, {});

    cout << Count << endl;
    for (auto way : ways)
    {
        for (auto num : way)
        {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}
