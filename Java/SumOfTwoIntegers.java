public class Solution {
    public int getSum(int a, int b) {
        if(a == 0) return b;
        while (b != 0){
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
}
/*

// this won't work, why?

public class Solution {
    public int getSum(int a, int b) {
        if(a == 0) return b;
        int sum;
        while (b != 0){
            int carry;
            sum = a ^ b;
			carry = a & b;
            b = carry << 1;
        }
        return sum;
    }
}
*/