// DSU_DisjointSetUnion.cpp
// Author: Suraj Patil
// Description: Disjoint Set Union (Union-Find) implementation in C++
// Contribution for Hacktoberfest2025 repository

#include <iostream>
#include <vector>
using namespace std;

class DSU {
    vector<int> parent, size;
public:
    DSU(int n) {
        parent.resize(n);
        size.assign(n, 1);
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            if (size[a] < size[b]) swap(a, b);
            parent[b] = a;
            size[a] += size[b];
        }
    }

    bool same(int a, int b) {
        return find(a) == find(b);
    }
};

int main() {
    DSU dsu(6);
    dsu.unite(1, 2);
    dsu.unite(2, 3);
    cout << (dsu.same(1, 3) ? "Connected" : "Not Connected") << endl;
    cout << (dsu.same(1, 4) ? "Connected" : "Not Connected") << endl;
    return 0;
}
