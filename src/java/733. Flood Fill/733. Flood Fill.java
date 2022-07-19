class Solution {
    private int n;
    private int m;
    private int[][] image;
    private int[] delta = {1, -1};
    
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        this.n = image.length;
        this.m = image[0].length;
        this.image = image;
        
        int source = image[sr][sc];
        if (source != color) {
            floodFill(sr, sc, source, color);   
        }
        return image;
    }
    
    public void floodFill(int i, int j, int source, int color) {
        if (i < 0 || i >= n || j < 0 || j >= m || image[i][j] != source) {
            return;
        }
        
        image[i][j] = color;
        
        for (var deltaI : delta) {
            floodFill(i + deltaI, j, source, color);
        }
        
        for (var deltaJ : delta) {
            floodFill(i, j + deltaJ, source, color);
        }
    }
}