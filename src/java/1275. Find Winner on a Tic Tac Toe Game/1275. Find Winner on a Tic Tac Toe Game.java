class Solution {
    public String tictactoe(int[][] moves) {
        int[] situations = new int[8];
        
        for (int i = 0; i < moves.length; ++i) {
            int r = moves[i][0];
            int c = moves[i][1];
            int mark = (i % 2 == 1) ? 1 : -1;
                
            situations[r] += mark;
            situations[c + 3] += mark;
            
            if (r == c) {
                situations[6] += mark;
            } 
            if (r + c == 2) {
                situations[7] += mark;
            }
            
            for (var s : situations) {
                if (s == 3 || s == -3) {
                    return (i % 2 == 1) ? "B" : "A";
                }
            }
        }
    
        return (moves.length == 9) ? "Draw" : "Pending";
    }
}