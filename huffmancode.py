# import heapq
# class Tree:
#     def __init__(self,data,fr,l,r):
#         self.data=data
#         self.freq=fr
#         self.left=l
#         self.right=r
        
#     def __it__(self, other):
#         return(self.freq<other.freq) 
#     def __init__(self,arr,freq):
#        n=len(arr)
#        hp=[]
#        for i in range (n): 
#         heapq.heappush(hp,self.node(arr[i],freq[i],None,None))
#        while len(hp)>1:
#            lt=heapq.heappop(hp)
#            rt=heapq.heappop(hp)
#            heapq.heappush(hp,self.node('+',lt.freq+rt.freq,lt,rt))
#        self.root=hp[0] 
#     def printutil(self,root,s):
#         if (root.left == None and root.right== None and root.data !='+'):
#             print(root.data,"=",s)
#             return
#         self.printutil(root.left,s+ "0")
#         self.printutil(root.right,s+"1")
#     def print(self):
#         print("char=huffman code")
#         self.printutil(self.root,"")
        
# ar=['a','b','f','c']
# fr=[4,9,7,3]
# tt=Tree(ar,fr)
# tt.print()
string='bcadddccacacac'
class treenode:
    def __init__(self,left,right):
        self.left=None
        self.right=None
    def children(self):
        return(self.left,self.right)
    def nodes(self):
        return(self.left,self.right)
    def __str__(self):
        return '%s_%s'%(self.left,self.right)
    # main function implementing huffman code
    def huffman_code_tree(self,node,left=True,binString=''):
        if type(node)is str:
            (l,r)=node.children()
            d=dict()
            d.update (huffman_code_tree(l,True,binString +'0'))
            d.update(huffman_code_tree(r,False, binString + '1'))
            return d
        # calculate frequency
        freq={}
        for c in string:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
        freq=sorted(freq.item(), key=lambda x:x[1],reverse=True)
        nodes=freq
        while len(nodes)>1:
            (key1,c1)=nodes[-1]
            (key2,c2)=nodes[-2]
            nodes=nodes[:-2]
            node=treenode(key1,key2)
            nodes.append(node,c1+c2)
            nodes=sorted(nodes,key=lambda x:x[1],reverse=True)
        huffmancode=huffman_code_tree(nodes[0][0])
        print('char|huffman code')
        print("-----------")
        for (char,freqency)in freq:
            print('%-4r | %12s' %(char,huffmancode[char]))
