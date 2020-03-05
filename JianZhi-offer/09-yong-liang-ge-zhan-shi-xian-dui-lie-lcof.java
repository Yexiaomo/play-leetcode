/*注意,使用Java自带的Stack()类, 速度比较慢
可以使用LinkedList()代替Stack();
*/
class CQueue {
    private int length;
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    public CQueue() {
        stack1 = new Stack<Integer>();
        stack2 = new Stack<Integer>();
        length = 0;
    }
    
    public void appendTail(int value) {
        stack1.push(value);
        length++;
    }
    
    public int deleteHead() {
        if(length == 0) return -1;
        if(!stack2.empty()){
            length--;
            return stack2.pop();
        }
        while(!stack1.empty()){
            stack2.push(stack1.pop());
        }
        length--;
        return stack2.pop();
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = new CQueue();
 * obj.appendTail(value);
 * int param_2 = obj.deleteHead();
 */
