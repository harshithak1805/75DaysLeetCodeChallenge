class Solution {
    public int mostWordsFound(String[] s) {
        int res=0;
        for (int i=0;i<s.length;i++)
        {
            int count=0;
           for(int j=0;j<s[i].length();j++)
           {
               if (s[i].charAt(j)==' ')
               {
                   count+=1;
               }
           }
           res= Math.max(res,count+1);
        }
        return res;
    }
}
