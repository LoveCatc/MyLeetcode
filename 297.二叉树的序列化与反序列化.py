#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def __init__(self):
        self.SEPLBL = ","
        self.NULLBL = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        rsltList = list()
        def trav(node):
            nonlocal rsltList
            if node is None:
                rsltList.append(self.NULLBL)
                rsltList.append(self.SEPLBL)
                return 
            rsltList.append(str(node.val))
            rsltList.append(self.SEPLBL)
            trav(node.left)
            trav(node.right)
        trav(root)
        print("".join(rsltList))
        return "".join(rsltList)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        decodeList = data.split(self.SEPLBL)[:-1]
        if not decodeList:
            return None
        if decodeList[0] == self.NULLBL:
            return None
            
        def grow(ser):
            # print(ser)
            if len(ser) == 0:
                return None
            elif ser[0] == self.NULLBL:
                return None
            elif ser[0] != self.NULLBL and ser[1] == self.NULLBL and ser[2] != self.NULLBL:
                root = TreeNode(val=int(ser[0]))
                root.left = None
                root.right = grow(ser[2:])
                return root
            elif ser[0] != self.NULLBL and ser[1] == self.NULLBL and ser[2] == self.NULLBL:
                root = TreeNode(val=int(ser[0]))
                root.left = None
                root.right = None
                return root
            else:   # N node need N+1 null
                root = TreeNode(val=int(ser[0]))
                for i in range(len(ser)):
                    if "".join(ser[i:i+2]) == self.NULLBL+self.NULLBL:
                        nodeNum = len([_ for _ in ser[:i] if _ != self.NULLBL]) - 1
                        nullNum = i + 1 - nodeNum
                        if nullNum-nodeNum == 1:
                            leftidx = i
                            break
                left = ser[1:leftidx+2]
                right = ser[leftidx+2:]
                root.left = grow(left)
                root.right = grow(right)
                return root
        return grow(decodeList)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

