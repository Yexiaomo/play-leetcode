class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    /** initialize your data structure here. */
    public MinStack() {
        this.stack = new Stack();
        this.minStack = new Stack();
    }
    
    public void push(int x) {
        stack.push(x);
        //判断是否比最小栈的top小, 小的话入栈
        if(minStack.empty() || x <= minStack.peek())
            minStack.push(x);
    }
    
    public void pop() {
        int x = stack.pop();
        //如果当前pop出去的值小于等于最小栈top值, 那么两个栈同时pop
        if(x == minStack.peek())
            minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int min() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.min();
 */
 