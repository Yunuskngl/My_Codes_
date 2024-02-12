#include <iostream>
using namespace std;

class TreeNode{
    public:
    int value;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int value=0 ,TreeNode* left = NULL,TreeNode* right = NULL) : value(value), right(right) , left(left) {     }
};

class BinarySearchtree{
    TreeNode* root;                           
    public:
    BinarySearchtree() : root(NULL) {};

    TreeNode* insert(TreeNode *start , int data){
        if(start){
            if(data < start->value) 
                start->left = insert(start->left,data);
            else 
                start->right = insert(start->right,data);
        }
    }

    int depth(TreeNode* start ,TreeNode* finish){        
        if(start){
            if(start == finish){
                return 0;
            }
            int left = depth(start->left,finish);         
            int right = depth(start->right,finish);        
            return 1 + max(left,right);
        }
        else
            return INT_MIN;                                  
    }


};

int main(){
    TreeNode* root;
    root = new TreeNode(30);
    root->left = new TreeNode(25);
    root->left->right = new TreeNode(27);
    root->left->left = new TreeNode(23);
    root->right  = new TreeNode(34);
    root->right->right = new TreeNode(35);
    root->right->right->right = new TreeNode(36);
    BinarySearchtree tree;
    cout<< tree.depth(root,root->right->right->right)<< endl;
}