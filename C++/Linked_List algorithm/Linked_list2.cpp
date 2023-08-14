#include <iostream>
using namespace std;

class Node{
    public:
    Node(const int& data = 0,Node* next = NULL) : data(data),next(next){ }
    int data;
    Node* next;
};
 
class list{
    Node* root;
    public : 
        list() : root(NULL){   }
        Node* begin()const{ return root;   }
        Node* end()const{ return NULL;     }
        //bool isEmpty()const{ return root==NULL; }
        bool isEmpty()const{return begin() == end(); }
        void push_back(const int& value){
            if(isEmpty()){
                root = new Node(value);
            }
            else{
                Node* temp = begin();
                while(temp->next != end()){
                    temp = temp ->next;
                }
                temp ->next = new Node(value);
            }
        }
        void push_front(const int &value){
            Node* temp = new Node(value);
            temp ->next = root;
            root = temp;

        }
        void print(){
            Node* temp = begin();
            while(temp !=  end()){
            cout << temp->data << " ";
            temp = temp->next;
            }
        }
};

int main(){
    list L;
    cout << L.isEmpty() << endl ; // boş ise 1 değerini döndürür.
    L.push_back(5);
    cout << L.isEmpty() << endl ;// dolu ise 0 değerini döndürür
    L.push_back(10);
    L.push_back(3);
    L.push_front(25);
    L.print();
    

return 0;}