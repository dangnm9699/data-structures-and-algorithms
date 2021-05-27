package TSP;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class TSPSolver {
    TSPModel model;

    public TSPSolver() {
        model = new TSPModel();
    }

    public void readInput(String name) throws FileNotFoundException {
        double[][] c = null;
        Integer n = null;
        File myObj = new File(name);
        Scanner myReader = new Scanner(myObj);
        if (myReader.hasNextLine()) {
            n = Integer.parseInt(myReader.nextLine());
            c = new double[n + 1][n + 1];
        }
        int k = 0;
        double min_c = Double.MAX_VALUE;
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            String[] temp = data.split(" ");
            for (int i = 0; i <= n; i++) {
                c[k][i] = Double.valueOf(temp[i]);
                if (i != k) {
                    min_c = Double.min(min_c, c[k][i]);
                }
            }
            k += 1;
        }
        model.min_c = min_c;
        myReader.close();
        model.setInput(c);
    }

    public void solve() {
        model.marked[0] = true;
        model.X[0] = 0;
        model.tryValue(1);
        model.printSolution();
    }
}
