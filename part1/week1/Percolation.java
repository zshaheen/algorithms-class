import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import java.util.*;

//javac-algs4 Percolation.java
//java-algs4 Percolation
public class Percolation {
  private int N;
  public int[][] id;
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

  private boolean connected(int row1, int col1, int row2, int col2) {
    return uf.connected(row1*N+col1, row2*N+col2);
  }

  private void union(int row1, int col1, int row2, int col2) {
      uf.union(row1*N+col1, row2*N+col2);
  }

  private void check_values(int row, int col) {
    if(row<=0 || row > N)
      throw new java.lang.IndexOutOfBoundsException();
    if(col<=0 || col > N)
      throw new java.lang.IndexOutOfBoundsException();

  }

  private boolean check_values_boolean(int row, int col) {
    int r = row-1;
    int c = col-1;
    try {
      int i = id[r][c];
      return true;
    } catch(ArrayIndexOutOfBoundsException e) {
      return false;
    }
  }

  //DELETE THIS
  /*
  private ArrayList listOfValuesToCheck(int row, int col) {
    //int[] values = new int[8];
    int[] values = {row-1, col, row+1, col, row, col-1, row, col+1};
    ArrayList good_values = new ArrayList();
    try {
      int i = id[values[0]][values[1]];
      good_values.add(values[0]+1);
      good_values.add(values[1]+1);
    } catch(ArrayIndexOutOfBoundsException e) {
      ;
    }
    try {
      int i = id[values[2]][values[3]];
      good_values.add(values[2]+1);
      good_values.add(values[3]+1);
    } catch(ArrayIndexOutOfBoundsException e) {
      ;
    }
    try {
      int i = id[values[4]][values[5]];
      good_values.add(values[4]+1);
      good_values.add(values[5]+1);
    } catch(ArrayIndexOutOfBoundsException e) {
      ;
    }
    try {
      int i = id[values[6]][values[7]];
      good_values.add(values[6]+1);
      good_values.add(values[7]+1);
    } catch(ArrayIndexOutOfBoundsException e) {
      ;
    }
    return good_values;
  }

  */
  public void open(int row, int col) {
    int[] values = {row-1, col, row+1, col, row, col-1, row, col+1};

    check_values(row, col);
    id[row-1][col-1] = 1;

    for(int i=0; i<values.length; i=i+2) {
      int r = values[i];
      int c = values[i+1];

      if(check_values_boolean(r, c)) {
        //if(isOpen(row, col)) {
        if(isOpen(r, c)) {
          /*System.out.println(row);
          System.out.println(col);
          System.out.println(r-1);
          System.out.println(c-1);
          System.out.println("-------");*/
          if (connected(row-1, col-1, r-1, c-1)==false) {
            //System.out.println("union called");
            union(row-1, col-1, r-1, c-1);
          }
        }
      }
    }


  }

  /*
  private void less_old_open(int row, int col) {
    ArrayList values = listOfValuesToCheck(row-1, col-1);

    for(int i=0; i<values.size(); i=i+2) {
      int r = values.get(i);
      int c = values.get(i+1);

      if(isOpen(row, col)) {
        if (connected(row, col, r-1, c-1)==false) {
          //System.out.println("union called");
          union(row, col, r-1, c-1);
        }
      }
    }

  }*/

  private void old_open(int row, int col) {

    //Check the sites around row, col and if they are open, connect them
    //right
    //try {
      if(isOpen(row, col+1)) {
        if (connected(row-1, col-1, row-1, col-1+1)==false) {
          System.out.println("union called");
          union(row-1, col-1, row-1, col-1+1);
        }
      }
    /*} catch(IndexOutOfBoundsException e) {
      ;
    }*/

    //left
    //try {
      if(isOpen(row, col-1)) {
        if(connected(row-1, col-1, row-1, col-1-1)==false) {
          System.out.println("union called");
          union(row-1, col-1, row-1, col-1-1);
        }
      }
    /*} catch(IndexOutOfBoundsException e) {
      ;
    }*/

    //down
    //try {
      if(isOpen(row+1, col)) {
        if(connected(row-1, col-1, row-1+1, col-1)==false) {
          System.out.println("union called");
          union(row-1, col-1, row-1+1, col-1);
        }
      }
    /*} catch(IndexOutOfBoundsException e) {
      ;
    }*/


    //up
    //try {
      if(isOpen(row-1, col)) {
        if(connected(row-1, col-1, row-1-1, col-1)==false) {
          System.out.println("union called");
          union(row-1, col-1, row-1-1, col-1);
        }
      }
    /*} catch(IndexOutOfBoundsException e) {
      ;
    }*/

      // open site (row, col) if it is not open already
      id[row-1][col-1] = 1;
  }

  //IMPORTANT NOTE: ANYTHING THAT DOES *NOT* INTERFACE WITH THE PUBLIC NEEDS TO BE DECREASED BY 1
  // OTHERW

  //TODO
  //have isOpen work with values from 1-n [x]
  //make open() give valid commands to isOpen so that there are no exceptions[x]
  //check that percolate() works with new schime (1-n)[x]
  //check isFull() for the third time [x]

  public boolean isOpen(int row, int col) {
    // is site (row, col) open?
    check_values(row, col);

    //System.out.println("passed check_values()");
    try {
      if (id[row-1][col-1] == 0)
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
    for(int i=1; i<=N; i++) {
      if(isOpen(1, i) && connected(row-1, col-1, 1-1, i-1))
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
    for(int i=1; i<=N; i++) {
      if(isFull(N, i))
        return true;
    }
    return false;
  }

  public static void main(String[] args) {
    // test client (optional)
    Percolation p = new Percolation(3);
    //Throw a java.lang.IndexOutOfBoundsException
    //p.open(0,0); //java.lang.ArrayIndexOutOfBoundsException
    //p.isOpen(0,0);
    //p.isFull(0,0);

    //System.out.println(Arrays.deepToString(p.id));
    //System.out.println(p.isOpen(1,1));
    p.open(1,1);

    //System.out.println(Arrays.deepToString(p.id));
    //System.out.println(p.isFull(3,1));

    //p.open(3,1);
    p.open(2,1);

    //System.out.println(p.isFull(3,1));
    p.open(3,1);
    //System.out.println(p.isFull(3, 2));
    //Why does open(1,1), open(2,1), open(3,2) work?
    System.out.println(p.percolates());
  }
}
