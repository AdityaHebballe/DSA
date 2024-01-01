#include <iostream>
#include <stack>
#include <string>

struct Bracket {
    char type;
    int position;
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }
};

int main() {
    std::string text;
    getline(std::cin, text);

    std::stack <Bracket> opening_brackets_stack;
    for (int unsigned position = 0; position < text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            opening_brackets_stack.push(Bracket(next,position+1));
        }

        if (next == ')' || next == ']' || next == '}') {
            if(!opening_brackets_stack.empty() && opening_brackets_stack.top().Matchc(next)){
                opening_brackets_stack.pop();
            }
            else{
                std::cout<<position+1<<std::endl;
                return 0;
            };
        }        
    }
    if(!opening_brackets_stack.empty()){
        std::cout<<opening_brackets_stack.top().position<<std::endl;
    }
    else{
        std::cout<<"Success"<<std::endl;
    }
    return 0;
}