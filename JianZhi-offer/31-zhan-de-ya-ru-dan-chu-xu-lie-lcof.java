class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        if(pushed == null && popped == null)
            return true;
        if(pushed == null || popped == null)
            return false;
        Stack<Integer> stack = new Stack();
        for(int idxPush = 0, idxPop = 0; idxPush < pushed.length; idxPush++){
            stack.push(pushed[idxPush]);
            while(!stack.isEmpty() && idxPop < popped.length && stack.peek() == popped[idxPop]){
                stack.pop();
                idxPop++;
            }
        }
        return stack.isEmpty();
    }
}
