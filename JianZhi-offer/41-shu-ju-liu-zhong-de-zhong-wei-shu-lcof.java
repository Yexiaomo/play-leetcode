class MedianFinder {
    private PriorityQueue<Integer> left;
    private PriorityQueue<Integer> right;
    private int size;

    /** initialize your data structure here. */
    public MedianFinder() {
        //较小的一部分也就是左半部分, 用大根堆
        this.left = new PriorityQueue<>((x, y) -> y - x);
        //较大的一部分也就是右半部分, 用小根堆
        this.right = new PriorityQueue<>();
        this.size = 0;
    }
    
    public void addNum(int num) {
        size++;
        //输入流过来的数首先进入左边
        left.offer(num);
        //再将左边最大的值移入右边, (注意: 此时小根堆会进行调整堆, 左边最大进入右边后, 不一定是右边最小的)
        right.offer(left.poll());
        //如果size为偶数, 则两边的数量相等, 不用调整
        //如果size为奇数, 则需要保证较左边的数量要比右边多一个
        if((size & 1) == 1){
            left.offer(right.poll());
        }
    }
    
    public double findMedian() {
        if( (size & 1) == 0){
            //size 为偶数
            return (double) (left.peek() + right.peek()) / 2;
        }else{
            //size 为奇数
            return (double) left.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
 