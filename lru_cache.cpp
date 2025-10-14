#include <iostream>
#include <list>
#include <unordered_map>
#include <string>
#include <stdexcept>
#include <bits/stdc++.h>
using namespace std;

class LRUCache {
    using Node = pair<int,int>;
    int cap;
    list<Node> dq;
    unordered_map<int, list<Node>::iterator> pos;

    void touch(list<Node>::iterator it) {
        dq.splice(dq.begin(), dq, it);
    }
    void evict_if_needed() {
        if ((int)dq.size() > cap) {
            auto [k,_] = dq.back();
            pos.erase(k);
            dq.pop_back();
        }
    }
public:
    explicit LRUCache(int capacity) : cap(capacity) {
        if (cap <= 0) throw invalid_argument("capacity must be positive");
    }

    int get(int key) {
        auto it = pos.find(key);
        if (it == pos.end()) return -1;
        touch(it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = pos.find(key);
        if (it != pos.end()) {
            it->second->second = value;
            touch(it->second);
        } else {
            dq.emplace_front(key, value);
            pos[key] = dq.begin();
            evict_if_needed();
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q; 
    if (!(cin >> Q)) return 0;
    int capacity; 
    if (!(cin >> capacity)) return 0;
    LRUCache cache(capacity);

    string op;
    for (int i = 0; i < Q; ++i) {
        if (!(cin >> op)) break;
        if (op == "GET") {
            int k; cin >> k;
            cout << cache.get(k) << '\n';
        } else if (op == "PUT") {
            int k, v; cin >> k >> v;
            cache.put(k, v);
        } else {
            string line; getline(cin, line);
        }
    }
    return 0;
}