#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Binary Search Tree Implementation for Product Inventory System
# Description:
# This script demonstrates a Binary Search Tree (BST) to manage an inventory system.
# Nodes store Product IDs and associated details (name and stock quantity).
# It includes methods for in-order, pre-order, and post-order traversals, product search, and visualization using Graphviz.


# In[2]:


# Importing required libraries
import matplotlib.pyplot as plt


# In[3]:


# Binary Search Tree Node Class
class TreeNode:
    def __init__(self, value, content=None):
        self.left = None  # Left child
        self.right = None  # Right child
        self.value = value  # Node value (Product ID)
        self.content = content  # Node content (Product details)
    
    # Method to insert a new node
    def insert(self, value, content=None):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value, content)
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value, content)
            else:
                self.right.insert(value, content)
    
    # In-order Traversal: Left -> Root -> Right
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value, end=' ')
        if self.right:
            self.right.inorder_traversal()
    
    # Pre-order Traversal: Root -> Left -> Right
    def preorder_traversal(self):
        print(self.value, end=' ')
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    
    # Post-order Traversal: Left -> Right -> Root
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value, end=' ')
        
    # Method to find a node by value
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            return self.right.find(value)
        else:
            return (self.value, self.content)
    
    # Visualization Method for the Binary Search Tree
    def visualize(self, x=0, y=0, dx=2, level=0, pos=None, ax=None):
        if pos is None:
            pos = {}
        
        pos[self.value] = (x, y)
        
        # Drawing the current node
        ax.text(x, y, f"{self.value}\n{self.content['name']}\nStock: {self.content['stock']}", 
                ha='center', va='center', fontsize=10, fontweight='bold',
                bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='circle', pad=1.2))
        
        # Draw edges to children nodes
        if self.left:
            ax.plot([x, x - dx], [y, y - 2], color='black')
            self.left.visualize(x - dx, y - 2, dx / 1.5, level + 1, pos, ax)
        
        if self.right:
            ax.plot([x, x + dx], [y, y - 2], color='black')
            self.right.visualize(x + dx, y - 2, dx / 1.5, level + 1, pos, ax)
        
        return pos


# In[4]:


# Product Inventory Data
data = [
    (1001, {"name": "Laptop", "stock": 50}),
    (1002, {"name": "Smartphone", "stock": 200}),
    (1003, {"name": "Tablet", "stock": 150}),
    (1004, {"name": "Smartwatch", "stock": 80}),
    (1005, {"name": "Desktop", "stock": 30}),
    (1006, {"name": "Headphones", "stock": 300}),
    (1007, {"name": "Camera", "stock": 25}),
    (1008, {"name": "Printer", "stock": 60}),
    (1009, {"name": "Keyboard", "stock": 100}),
    (1010, {"name": "Mouse", "stock": 120}),
    (1011, {"name": "Monitor", "stock": 90}),
    (1012, {"name": "Webcam", "stock": 70}),
    (1013, {"name": "Microphone", "stock": 110}),
    (1014, {"name": "Speaker", "stock": 180}),
    (1015, {"name": "Router", "stock": 40}),
    (1016, {"name": "Switch", "stock": 20}),
    (1017, {"name": "External HDD", "stock": 42}),
    (1018, {"name": "Graphics Card", "stock": 32}),
    (1019, {"name": "Motherboard", "stock": 15})
]


# In[5]:


# Sorting data by Product ID for balanced tree
data.sort(key=lambda x: x[0])


# In[6]:


# Function to Build a Balanced Binary Search Tree
def build_balanced_bst(data_list):
    if not data_list:
        return None
    
    mid = len(data_list) // 2
    node = TreeNode(data_list[mid][0], data_list[mid][1])
    
    node.left = build_balanced_bst(data_list[:mid])
    node.right = build_balanced_bst(data_list[mid+1:])
    
    return node

# Building the Binary Search Tree
tree = build_balanced_bst(data)


# In[7]:


# In-Order Tree Traversals
print("In-order Traversal (Product IDs):")
tree.inorder_traversal()


# In[8]:


# Pre-Order Tree Traversals
print("\nPre-order Traversal (Product IDs):")
tree.preorder_traversal()


# In[9]:


# Post-Order Tree Traversals
print("\nPost-order Traversal (Product IDs):")
tree.postorder_traversal()


# In[10]:


# Testing the Find Method
print("\n\nFinding Products:")
print(tree.find(1002))  # Finding Smartphone
print(tree.find(1015))  # Finding Router


# In[11]:


# Visualizing the Binary Search Tree
fig, ax = plt.subplots(figsize=(40, 10))  # Larger figure size for better visibility
ax.set_title("Product Inventory Binary Search Tree", fontsize=11, fontweight='bold')
ax.set_xlim(-10, 14)
ax.set_ylim(-8, 1)
ax.axis('off')

tree.visualize(ax=ax)
plt.show()

