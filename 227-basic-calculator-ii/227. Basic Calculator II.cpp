
#include<bits/stdc++.h>
class Solution {
public:
    

    int calculate(string s) {
        
        cleanExpression(s);// clean the expression from negative numbers ( i.e convert -1+2 into 0-1+2)
       
        int n = s.length();
        
        stack<int> value;
        stack<char> oprator;

        int i=0;
        while(i < n){
            char c = s[i];
            
            // if you found a digit 
            if(isdigit(c)){

                // go ahead and make the entire number 
                int num = 0;
                while(i < n && isdigit(s[i])){
                    num = num*10 + (s[i]-'0');
                    i++;
                }
                i--;

                
                // push the number in the value stack
                value.push(num);
            }

            else if(c == '(')
                oprator.push(c);
            
            else if(c==')'){
                while(oprator.top() != '('){
                    
                    char op = oprator.top();
                    oprator.pop();

                    int b = value.top(); value.pop();
                    int a = value.top(); value.pop();

                    int res = operate(a,b,op);
                    value.push(res);
                }
                oprator.pop();
            }

            else if(c == ' ')
                ;

            else{ // when c is an operator 
                
                while(oprator.size() && isGreaterPref(oprator.top(), c)){
                    
                    char op = oprator.top();
                    oprator.pop();

                    int b = value.top(); value.pop();
                    int a = value.top(); value.pop();

                    int res = operate(a,b,op);
                    value.push(res);
                }

                oprator.push(c);

            }

            i++;
        }


        while(oprator.size()){

            char op = oprator.top();
            oprator.pop();

            int b = value.top(); value.pop();
            int a = value.top(); value.pop();

            int res = operate(a,b,op);
            value.push(res);

        }

        if(value.size() != 1)   exit(100);

        return value.top();


    }

    int operate(int a, int b, char op){
        switch(op){
            case '+':
                return a+b;

            case '-':
                return a-b;
            
            case '*':
                return a*b;
            
            case '/':
                return a/b;
            
            default:
                exit(100);
        }
        return INT_MAX;
    }

    bool isGreaterPref(char a, char b){
        // returns true if 'a' has greater (or) equal preference as 'b'
        // here, a will be the top of operator stack
        // and, b will be the current operator 

        if(a == '*' || a == '/') 
            return true;
        
        if(b == '*' || b == '/') // a may be +, -, or ( 
            return false;


        // a may be +,-,( AND b may be +,-
        return (a =='+' || a == '-');  // when a and b both are one of '+' or '-'
    }
    
    void cleanExpression(string& s){
        //cleans the expression (i.e. converts -1+2 into 0-1+2)
        vector<char> ss;
        for(int i=0;i<s.length();i++){
            
            if(s[i] == '+' || s[i] == '-' ){
                
                if(i == 0 || s[i-1] == '(')    ss.push_back('0');
                
            }
            
            ss.push_back(s[i]);
        }
        s = string(ss.begin(), ss.end());
        return;
    }
    
};
/*
1. While there are still tokens to be read in,
   1.1 Get the next token.
   1.2 If the token is:
       1.2.1 A number: push it onto the value stack.
       1.2.2 A variable: get its value, and push onto the value stack.
       1.2.3 A left parenthesis: push it onto the operator stack.
       1.2.4 A right parenthesis:
         1 While the thing on top of the operator stack is not a 
           left parenthesis,
             1 Pop the operator from the operator stack.
             2 Pop the value stack twice, getting two operands.
             3 Apply the operator to the operands, in the correct order.
             4 Push the result onto the value stack.
         2 Pop the left parenthesis from the operator stack, and discard it.
       1.2.5 An operator (call it thisOp):
         1 While the operator stack is not empty, and the top thing on the
           operator stack has the same or greater precedence as thisOp,
           1 Pop the operator from the operator stack.
           2 Pop the value stack twice, getting two operands.
           3 Apply the operator to the operands, in the correct order.
           4 Push the result onto the value stack.
         2 Push thisOp onto the operator stack.
2. While the operator stack is not empty,
    1 Pop the operator from the operator stack.
    2 Pop the value stack twice, getting two operands.
    3 Apply the operator to the operands, in the correct order.
    4 Push the result onto the value stack.
3. At this point the operator stack should be empty, and the value
   stack should have only one value in it, which is the final result.

*/
