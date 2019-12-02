import java.util.List;

public class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }

    @Override
    public String toString() {
         String r = this.val+" ";
         ListNode n = this.next;
         while(n != null){
             r += n.val+" ";
             n= n.next;

         }
        return r;
    }

    public static void main(String[] args) {
         ListNode l1 = new ListNode(2);
         ListNode l1n = new ListNode(4);
         l1.next = l1n;
        /*l1n.next = new ListNode(3);*/

        ListNode l2 = new ListNode(5);
        ListNode l2n = new ListNode(6);
        l2.next = l2n;
        l2n.next = new ListNode(4);
        Solution s = new Solution();

        System.out.println(s.addTwoNumbers(l1, l2));



    }


    static class Solution{


        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
           ListNode sum=new ListNode(0), next = sum;
           int carry = 0;


           while(l1 != null || l2 != null){
               int intermediate = 0;
               if(l1==null){
                   intermediate = l2.val + carry;
                   carry = 0;
               }
               else if(l2==null){
                   intermediate = l1.val + carry;
                   carry = 0;
               }

               else{
                   intermediate = l1.val + l2.val + carry;
                   carry = 0;
               }
               if(intermediate > 9){
                   carry = intermediate / 10;
                   intermediate = intermediate % 10;
               }
               next.next = new ListNode(intermediate);
               next = next.next;

               if(l1!= null)  l1 = l1.next;
               if(l2!=null)    l2 = l2.next;


               if(l1== null && l2==null & carry > 0){
                   next.next = new ListNode(carry);
               }

           }
           return sum.next;
        }


    }


}

