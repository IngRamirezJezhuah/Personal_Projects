package src;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.List;

public class ShimejiPanel extends JPanel {
    private Animation animation;
    private Point mouseClickPoint;
    private ShimejiMenu shimejiMenu;

    public ShimejiPanel() {
        animation = new Animation(100); // 100ms por frame
        shimejiMenu = new ShimejiMenu();
        loadShimejiImages();
        setBounds(100, 100, 100, 100);
        Timer timer = new Timer(1000 / 60, e -> repaint());
        timer.start();

        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                mouseClickPoint = e.getPoint();
                if (SwingUtilities.isRightMouseButton(e)) {
                    shimejiMenu.show(e.getComponent(), e.getX(), e.getY());
                }
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                Point mouseLocation = e.getLocationOnScreen();
                setLocation(mouseLocation.x - mouseClickPoint.x, mouseLocation.y - mouseClickPoint.y);
            }
        });
    }

    private void loadShimejiImages() {
        for (int i = 1; i <= 46; i++) {
            try {
                String imagePath = String.format("/resources/shimeji_images/shimeji_%d.png", i);
                Image frame = new ImageIcon(getClass().getResource(imagePath)).getImage();
                animation.addFrame(frame);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(animation.getCurrentFrame(), 0, 0, this);
    }
}

class Animation {
    private List<Image> frames;
    private int currentFrame;
    private long lastFrameTime;
    private int frameDuration;

    public Animation(int frameDuration) {
        this.frames = new ArrayList<>();
        this.currentFrame = 0;
        this.frameDuration = frameDuration;
        this.lastFrameTime = System.nanoTime();
    }

    public void addFrame(Image frame) {
        frames.add(frame);
    }

    public Image getCurrentFrame() {
        long currentTime = System.nanoTime();
        if (currentTime - lastFrameTime >= frameDuration * 1_000_000) {
            currentFrame = (currentFrame + 1) % frames.size();
            lastFrameTime = currentTime;
        }
        return frames.get(currentFrame);
    }
}

class ShimejiMenu extends JPopupMenu {
    public ShimejiMenu() {
        JMenuItem danceItem = new JMenuItem("Dance");
        danceItem.addActionListener(e -> dance());

        JMenuItem stealItem = new JMenuItem("Steal Icon/Text");
        stealItem.addActionListener(e -> steal());

        add(danceItem);
        add(stealItem);
    }

    private void dance() {
        // Lógica para que el Shimeji baile
        System.out.println("Dancing!");
    }

    private void steal() {
        // Lógica para que el Shimeji robe iconos o texto
        System.out.println("Stealing!");
    }
}
