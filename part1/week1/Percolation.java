import edu.princeton.cs.algs4.WeightedQuickUnionUF;

//javac-algs4 Percolation.java
//java-algs4 Percolation
public class Percolation {
  private int N;
  private int[][] id;
  private WeightedQuickUnionUF uf;

  public Percolation(int n) {
    // create n-by-n grid, with all sites blocked
    N = n;
    uf = new WeightedQuickUnionUF(n*n);
    id = new int [n][n];

    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        id[i][j] = 0;
      }
    }

  }

  public boolean connected(int row1, int col1, int row2, int col2) {
    return uf.connected(row1*N+col1, row2*N+col2);
  }

  public void union(int row1, int col1, int row2, int col2) {
      uf.union(row1*N+col1, row2*N+col2);
  }

  public void open(int row, int col) {
    // open site (row, col) if it is not open already
    id[row][col] = 1;

    //Check the sites around row, col and if they are open, connect them
    //right
    if(isOpen(row, col+1)) {
      if (connected(row, col, row, col+1)==false) {
        System.out.println("union called");
        union(row, col, row, col+1);
      }
    }

    //left
    if(isOpen(row, col-1))
      if(connected(row, col, row, col-1)==false) {
        System.out.println("union called");
        union(row, col, row, col-1);
      }

    //down
    if(isOpen(row+1, col))
      if(connected(row, col, row+1, col)==false) {
        System.out.println("union called");
        union(row, col, row+1, col);
      }

    //up
    if(isOpen(row-1, col))
      if(connected(row, col, row-1, col)==false) {
        System.out.println("union called");
        union(row, col, row-1, col);
      }
  }

  public boolean isOpen(int row, int col) {
    // is site (row, col) open?
    try {
      if (id[row][col] == 0)
        return false;
      else
        return true;
    }
    catch(ArrayIndexOutOfBoundsException exception) {
      return false;
    }
  }

  public boolean isFull(int row, int col) {
    // is site (row, col) full?
    // a site is full iff it's open and can be connected to an open site in the top row
    //  via a chaining of neighbors (l,r,u,d) open sites.

    // First check if this is an open site
    if (isOpen(row, col) == false)
      return false;

    // Check all open sites on the top row and see if it's connected to row, col.
    for(int i=0; i<N; i++) {
      if(isOpen(0, i) && connected(row, col, 0, i))
        return true;
    }
    return false;
  }

  public int numberOfOpenSites() {
    // number of open sites
    int num = 0;
    for(int i = 0; i < id.length; i++) {
      for(int j = 0; j < id.length; j++) {
        if (id[i][j] == 1)
          num++;
      }
    }
    return num;
  }

  public boolean percolates() {
    // does the system percolate?
    // percolates if there is a full site on the bottom row
    for(int i=0; i<N; i++) {
      if(isFull(N-1, i))
        return true;
    }
    return false;
  }

  public static void main(String[] args) {
    // test client (optional)
    Percolation p = new Percolation(3);
    p.open(0,0);
    p.open(1,0);
    p.open(2,0);
    System.out.println(p.percolates());
  }
}
