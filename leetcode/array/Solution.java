package leetcode.array;

class Solution {
    public int scoreOfString(String s){
        int sum=0;
        for(int i =0;i<s.length();i++){
         sum =  sum + Math.abs((int)s.charAt(i) - (int)s.charAt(i+1));
        }
        return sum;
    }
}