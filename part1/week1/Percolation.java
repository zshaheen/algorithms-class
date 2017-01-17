import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.In;

// javac-algs4 Percolation.java
// java-algs4 Percolation
public class Percolation {
  private int nValue;
  private int numberOfOpenSitesVariable;
  private int[][] id;
  private WeightedQuickUnionUF uf;
  private int[] virtual_top; // [0] is row, [1] is col
  private int[] virtual_bottom; // [0] is row, [1] is col

  public Percolation(int n) {
    // create n-by-n grid, with all sites blocked
    if (n <= 0)
      throw new java.lang.IllegalArgumentException();

    nValue = n;
    numberOfOpenSitesVariable = 0;
    virtual_top = new int[] {nValue, nValue+1}; // second to last element, cause we used +2 in uf initialization
    virtual_bottom = new int[] {nValue, nValue+2}; // last element, cause we used +2 in uf initialization

    // the +2 account for the virtual top and bottom
    uf = new WeightedQuickUnionUF(n*n + 2);
    id = new int [n][n];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        id[i][j] = 0;
      }
    }

    // connect the virtual top to the top row
    for (int i = 1; i <= nValue; i++) {
      union(virtual_top[0]-1, virtual_top[1]-1, 1-1, i-1);
    }

    // connect the virtual bottom to the bottom row
    for (int i = 1; i <= nValue; i++) {
      union(virtual_bottom[0]-1, virtual_bottom[1]-1, nValue-1, i-1);
    }
  }

  private boolean connected(int row1, int col1, int row2, int col2) {
    return uf.connected(row1*nValue+col1, row2*nValue+col2);
  }

  private void union(int row1, int col1, int row2, int col2) {
      uf.union(row1*nValue+col1, row2*nValue+col2);
  }

  private void checkValues(int row, int col) {
    if (row <= 0 || row > nValue)
      throw new java.lang.IndexOutOfBoundsException();
    if (col <= 0 || col > nValue)
      throw new java.lang.IndexOutOfBoundsException();
  }

  private boolean checkValuesBoolean(int row, int col) {
    int r = row-1;
    int c = col-1;
    if (r < 0 || r >= nValue)
      return false;
    if (c < 0 || c >= nValue)
      return false;
    return true;
  }

  public void open(int row, int col) {
    int[] values = {row-1, col, row+1, col, row, col-1, row, col+1};

    checkValues(row, col);
    id[row-1][col-1] = 1;
    numberOfOpenSitesVariable++;

    int r, c;
    for (int i = 0; i < values.length; i = i + 2) {
      r = values[i];
      c = values[i+1];

      if (checkValuesBoolean(r, c) && isOpen(r, c) && !connected(row-1, col-1, r-1, c-1))
        union(row-1, col-1, r-1, c-1);
    }
  }

  public boolean isOpen(int row, int col) {
    // is site (row, col) open?
    checkValues(row, col);

    if (id[row-1][col-1] == 0)
      return false;
    else
      return true;
  }

  public boolean isFull(int row, int col) {
    // is site (row, col) full?
    // a site is full iff it's open and can be connected to an open site in the top row
    //  via a chaining of neighbors (l,r,u,d) open sites.

    // First check if this is an open site
    if (!isOpen(row, col))
      return false;

    // just check if current site connects to the virtual_top
    if(connected(row-1, col-1, virtual_top[0]-1, virtual_top[1]-1))
      return true;
    else
      return false;
  }

  public int numberOfOpenSites() {
    // number of open sites
    return numberOfOpenSitesVariable;
  }

  public boolean percolates() {
    // does the system percolate?
    // percolates if there is a full site on the bottom row
    // -- just check if virtual top is connected to virtual bottom
    if(connected(virtual_top[0]-1, virtual_top[1]-1, virtual_bottom[0]-1, virtual_bottom[1]-1))
      return true;
    else
      return false;
  }

  public static void main(String[] args) {
    // test client (optional)
    try {
      In in = new In(args[0]);
      Percolation p = new Percolation(in.readInt());
      int row, col;

      while (!in.isEmpty()) {
        row = in.readInt();
        col = in.readInt();
        p.open(row, col);
      }

      // System.out.println(args[0]);
      // System.out.println(p.percolates());

    } catch (IllegalArgumentException e) {
      System.out.println(e);
    }
  }
}
