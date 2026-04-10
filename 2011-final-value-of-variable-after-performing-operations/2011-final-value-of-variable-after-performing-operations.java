class Solution {
    public int finalValueAfterOperations(String[] op) {
        int x=0;
        for(int i=0;i<op.length;i++)
        {
            String t=op[i];
            if (t.equals("++X") || t.equals("X++"))
            {
                x=x+1;
            }
            else
            {
                x=x-1;
            }
        }
        return x;
    }
}

