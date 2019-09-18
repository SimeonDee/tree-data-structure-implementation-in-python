
# coding: utf-8

# # My Tree Implementation in Python

#     *************************************************************************************
#     Author:    Adeyemi Adedoyin Simeon
#     Date:      23rd April, 2019 8:48 pm
#     Course:    AI: Search Problems
#     Location:  Room A29, Abdulsalam Abubakar Hall, University of Ibadan, Nigeria
#     E-mail:    adeyemi.sa1@gmail.com
#     *************************************************************************************

# In[1]:


class DoyinTree:
    child = None
    parent = None
    def __init__(self, data,children=None):
        self.data = data
        self.children = []
    
    def add_child(self, data):
        assert isinstance(data,DoyinTree)
        self.child = data
        self.children.append(self.child)
        data.parent = self
    
    def add_children(self, L):
        if len(L) > 0:
            for t in L:
                assert isinstance(t,DoyinTree)
                self.child = t
                self.children.append(self.child)
                t.parent = self
        
    def get_neighbours(self):
        if self.children is not None:
            return [chl for chl in self.children]
        else:
            return None
    
    def get_neighbours_data(self):
        if self.children is not None:
            return [chl.data for chl in self.children]
        else:
            return None
        
    def get_data(self):
        return self.data
    
    def get_parent(self):
        if self.parent is not None:
            print(self.parent.data)
            return self.parent
        else:
            print(str(self.data), ' is the root node. \n It has no parent.')
            return None
        
    def get_parents(self):
        result = []
        a = self.parent
        while a is not None:
            result.append(a.data)
            a = a.parent
        else:
            return result
        
    def get_children(self):
        answer = []
        if self.children is not None:
            [answer.append(c.data) for c in self.children]
            #for c in self.children:
             #   answer.append(c.data)
                
            print(answer)    
            return self.children
        else:
            print(str(self.data), " has no child node.")
            return None

    def get_siblings(self):
        if self.parent is not None:
            c = self.parent.children
            if len(c) > 1:
                siblings = [sibling for sibling in c if sibling.data != self.data]
                print("Siblings: ", [str(sibling.get_data()) for sibling in siblings])
                return siblings
            else:
                print(str(self.data), " is the only child node.")
                return None
        else:
            print(str(self.data), ' is the root node. \n It has no parent.')
            return None
                        

