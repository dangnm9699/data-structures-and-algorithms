import java.io.FileNotFoundException;

import TSP.TSPSolver;

public class Main {
    public static void main(String[] args) {
        TSPSolver solver = new TSPSolver();
        try {
            solver.readInput(
                    "/mnt/ExUbuntu/Workspace/my_projects/Data_Structures_and_Algorithms/Exercise/TSP/data.txt");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        solver.solve();
    }
}