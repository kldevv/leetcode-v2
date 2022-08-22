#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> split(const std::string& word, const std::string& delim);

template <typename T>
void print(std::vector<T> v);


int main() {
    using std::string;
    using std::vector;

     auto delim1 = ", ";
    // empty string
    auto str1 = "";
    auto result1 = split(str1, delim1);
    print<string>(result1);

    // one split
    auto str2 = "apple, orange";
    auto result2 = split(str2, delim1);
    print<string>(result2);

    // two split
    auto str3 = "apple, orange, lemon";
    auto result3 = split(str3, delim1);
    print<string>(result3);

    // trialing delim
    auto str4 = "apple, orange, ";
    auto result4 = split(str4, delim1);
    print<string>(result4);

    // pre delim
    auto str5 = ", apple, orange";
    auto result5 = split(str5, delim1);
    print<string>(result5);

    return 0;
}

std::vector<std::string> split(const std::string& word, const std::string& delim) {
    using std::vector;
    using std::string;

    if (word.empty()) {
        return {};
    }

    vector<string> results;

    auto start = 0ul;
    auto end = word.find(delim);
    while (end != string::npos) {
        auto token= word.substr(start, end - start);
        results.push_back(token);

        start = end + delim.size();
        end = word.find(delim, start);
    }
    results.push_back(word.substr(start, end - start));

    return results;
}

template <typename T>
void print(std::vector<T> v) {
    std::cout << "* Start..." << std::endl;
    for (auto t : v) {
        if (t.empty()) {
            std::cout << "<#space#>,";
        } else {
            std::cout << t << ",";
        }
    }
    std::cout << std::endl << "* End..." << std::endl;
    std::cout << "***********************" << std::endl;
}


