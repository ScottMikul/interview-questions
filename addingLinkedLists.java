

public class addingLinkedLists {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        ListNode cur = res;
        int c= 0;

        //first node
        if(l1!=null && l2!=null){
            res.val = (l1.val + l2.val) % 10 ;
            c = (l1.val+ l2.val)/10;
            if(l1.next==null && l2.next==null){
                if(c==1){
                    res.next = new ListNode(1);
                }
            }
        }
        else 
            return res;

        while(l1.next != null || l2.next != null ){


            if(l1.next==null){
                l1.next= new ListNode(0);
            }
            if(l2.next==null){
                l2.next= new ListNode(0);
            }
            cur.next = new ListNode((l1.next.val + l2.next.val + c ) %10);
            c = (l1.next.val + l2.next.val + c)/10;

            cur = cur.next;
            l1= l1.next;
            l2 = l2.next;

        }
        if(c ==1){
            cur.next = new ListNode(1);
        }
        return res;
    }

    public static void main(String[]args) {

        //(2 -> 4 -> 3)
        ListNode l1 = new ListNode(1);
       // l1.next= new ListNode(4);
       // l1.next.next = new ListNode(3);

        //(5 -> 6 -> 4)
        ListNode l2 = new ListNode(9);
       l2.next= new ListNode(5);
       // l2.next.next = new ListNode(4);

        System.out.println(l1);
        System.out.println(l2);

        System.out.println(addTwoNumbers(l1,l2));
    }
    
}
class ListNode {
         int val;
         ListNode next;
         ListNode(int x) 
         { 
             val = x; 
        }

        @Override
        public String toString() {
            if(next!=null){
                return val+ " -> " + next;
            }
             return val+ "";
        }
}