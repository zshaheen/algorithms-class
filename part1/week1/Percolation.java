import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.In;

// javac-algs4 Percolation.java
// java-algs4 Percolation
public class Percolation {
  private int nValue;
  private int[][] id;
  private WeightedQuickUnionUF uf;

  public Percolation(int n) {
    // create n-by-n grid, with all sites blocked
    nValue = n;
    uf = new WeightedQuickUnionUF(n*n);
    id = new int [n][n];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        id[i][j] = 0;
      }
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
    try {
      r = id[r][c];
      return true;
    } catch (ArrayIndexOutOfBoundsException e) {
      return false;
    }
  }

  public void open(int row, int col) {
    int[] values = {row-1, col, row+1, col, row, col-1, row, col+1};

    checkValues(row, col);
    id[row-1][col-1] = 1;

    for (int i = 0; i < values.length; i = i + 2) {
      int r = values[i];
      int c = values[i+1];

      if (checkValuesBoolean(r, c) && isOpen(r, c) && !connected(row-1, col-1, r-1, c-1))
            union(row-1, col-1, r-1, c-1);
    }
  }

  public boolean isOpen(int row, int col) {
    // is site (row, col) open?
    checkValues(row, col);

    try {
      if (id[row-1][col-1] == 0)
        return false;
      else
        return true;
    }
    catch (ArrayIndexOutOfBoundsException exception) {
      return false;
    }
  }

  public boolean isFull(int row, int col) {
    // is site (row, col) full?
    // a site is full iff it's open and can be connected to an open site in the top row
    //  via a chaining of neighbors (l,r,u,d) open sites.

    // First check if this is an open site
    if (!isOpen(row, col))
      return false;

    // Check all open sites on the top row and see if it's connected to row, col.
    for (int i = 1; i <= nValue; i++) {
      if (isOpen(1, i) && connected(row-1, col-1, 1-1, i-1))
        return true;
    }
    return false;
  }

  public int numberOfOpenSites() {
    // number of open sites
    return uf.count();
  }

  public boolean percolates() {
    // does the system percolate?
    // percolates if there is a full site on the bottom row
    for (int i = 1; i <= nValue; i++) {
      if (isFull(nValue, i))
        return true;
    }
    return false;
  }

  public static void main(String[] args) {
    // test client (optional)
    try {
      In in = new In(args[0]);
      Percolation p = new Percolation(in.readInt());
      int row, col;

      while(!in.isEmpty()) {
        row = in.readInt();
        col = in.readInt();
        p.open(row, col);
      }

      // System.out.println(args[0]);
      // System.out.println(p.percolates());

    } catch(IllegalArgumentException e) {
      System.out.println(e);
    }
  }
}
