#include <bits/stdc++.h>
using namespace std;
#define ll long long 

//https://algoleague.com/problem/where-am-i/detail

int main() {
// write your code here
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll N, x, y;
    cin >> N >> x >> y;

    ll min_pos = min(N - x, y+1);
    cout << min_pos << endl;

    return 0;
    
}