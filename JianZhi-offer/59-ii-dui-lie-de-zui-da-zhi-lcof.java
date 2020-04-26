class MaxQueue {
    private Deque<Integer> queue;
    private Deque<Integer> help;

    public MaxQueue() {
        queue = new ArrayDeque<>();
        help = new ArrayDeque<>();
    }
    
    public int max_value() {
        return queue.isEmpty() ? -1 : help.peekFirst();
    }
    
    public void push_back(int value) {
        queue.offerLast(value);
        while(!help.isEmpty() && value > help.peekLast())
            help.pollLast();
        help.offerLast(value);
    }
    
    public int pop_front() {
        if(queue.isEmpty())
            return -1;
        int val = queue.pollFirst();
        if(val == help.peekFirst())
            help.removeFirst();
        return val;
    }
}

/**
 * Your MaxQueue object will be instantiated and called as such:
 * MaxQueue obj = new MaxQueue();
 * int param_1 = obj.max_value();
 * obj.push_back(value);
 * int param_3 = obj.pop_front();
 */
 