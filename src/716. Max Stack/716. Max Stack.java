class MaxStack {
    DoubleLinkedList ddl = new DoubleLinkedList();
    TreeMap<Integer, List<Node>> map = new TreeMap();

    public MaxStack() {
        
    }
    
    public void push(int x) {
        Node node = ddl.add(x);
        if(!map.containsKey(x)) {
            map.put(x, new ArrayList<Node>());
        }
        map.get(x).add(node);
    }
    
    public int pop() {
        int val = ddl.pop();
        
        List<Node> ls = map.get(val);
        ls.remove(ls.size() - 1);
        if (ls.isEmpty()) {
            map.remove(val);
        }
        
        return val;
    }
    
    public int top() {
        return ddl.peek();
    }
    
    public int peekMax() {
        return map.lastKey();
    }
    
    public int popMax() {
        int val = peekMax();
        
        List<Node> ls = map.get(val);
        Node node = ls.remove(ls.size() - 1); 
        ddl.remove(node);
        if (ls.isEmpty()) {
            map.remove(val);
        }
        
        return val;
    }
}

class DoubleLinkedList {
    private Node head;
    private Node tail;
    
    public DoubleLinkedList() {
        head = new Node(0);
        tail = new Node(0);
        head.next = tail;
        tail.prev = head;
    }
    
    public boolean isEmpty() {
        return head == tail;
    }
    
    public Node add(int val) {
        Node node = new Node(val);
        
        node.next = tail;
        node.prev = tail.prev;
        tail.prev.next = node;
        tail.prev = node;
        
        return node;
    }
    
    public int pop() {
        return this.remove(tail.prev).val;
    }
    
    public int peek() {
        return tail.prev.val;
    }
    
    public Node remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        return node;
    }
    
    
}

class Node {
    int val;
    Node prev = null;
    Node next = null;
    public Node(int val) {
        this.val = val;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */