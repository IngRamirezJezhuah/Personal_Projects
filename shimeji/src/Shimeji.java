package src;
import javax.swing.*;

public class Shimeji {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Shimeji");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(800, 600);
            frame.setLayout(null);
            
            ShimejiPanel shimejiPanel = new ShimejiPanel();
            frame.add(shimejiPanel);
            
            frame.setVisible(true);
        });
    }
}
