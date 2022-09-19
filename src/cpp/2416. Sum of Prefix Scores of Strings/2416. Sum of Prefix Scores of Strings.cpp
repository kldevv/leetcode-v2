class Trie {
public:
    vector<Trie*> children;
    int counts;
    Trie(): children(26, nullptr), counts{0} {}
};


class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        auto root {new Trie()};
            
        for (const auto& word : words) {
            auto iter {root};
            for (const auto& c : word) {
                auto idx {c - 'a'};
                if (iter->children[idx] == nullptr) {
                    iter->children[idx] = new Trie();
                }
                iter = iter->children[idx];
                iter->counts += 1;
            }
        }
        
        
        vector<int> out;
        for (auto word : words) {
            auto iter {root};
            auto score {0};
            for (const auto& c : word) {
                auto idx {c - 'a'};
                iter = iter->children[idx];
                score += iter->counts;
            }
            out.push_back(score);
        }
        return out;
    }
};
