class Solution {
    public boolean verifyPostorder(int[] postorder) {
        if(postorder == null || postorder.length <= 0)
            return true;
        return verifyPostorderOfBST(postorder, 0, postorder.length-1);
    }
    public boolean verifyPostorderOfBST(int[] sequence, int left, int right){
        if(left >= right)
            return true;
        //在二叉搜索树种查找位于根节点的左子树上的节点
        int i = left;
        while(sequence[i] < sequence[right])
            i++;
        //在二叉搜索树种查找位于根节点的右子树上的节点
        int mid = i;
        while(sequence[i] > sequence[right])
            i++;
        //判断左右子树是不是二叉搜索树
        return i == right && verifyPostorderOfBST(sequence, left, mid-1) && verifyPostorderOfBST(sequence, mid, right-1);
    }
}
