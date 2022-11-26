package exercise1_1_checkers;

import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Rectangle;

/**
 * Represents a place on the board where a piece can sit.
 */
public class Square {
    private int x;
    private int y;
    private static int SQUARE_SIZE = BoardController.SQUARE_SIZE;

    /**
     * The piece currently sitting on this square.
     *
     * null if this square is empty.
     */
    private Piece piece = null;
    private final Rectangle rectangle;

    public Square(int x, int y) {
        this.x = x;
        this.y = y;

        Paint paint;
        if((this.y + this.x)%2==0) {
            paint = Color.BLACK.brighter().brighter().brighter().brighter();
        } else {
            paint = Color.RED.darker().darker();
        }
        rectangle = new Rectangle(SQUARE_SIZE, SQUARE_SIZE, paint);
        rectangle.setX(this.x *SQUARE_SIZE);
        rectangle.setY(this.y *SQUARE_SIZE);
        rectangle.setOnMouseClicked(event -> tryMovePieceHere());
        BoardController.addChild(rectangle);
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String toString() {
        return "Square at "+x+", "+y;
    }

    private void tryMovePieceHere() {
        BoardController.tryMovePiece(this);
    }

    /**
     * @return The piece currently sitting on this square.
     * null if this square is empty.
     */
    public Piece getPiece() {
        return piece;
    }

    public void removePiece() {
        if(piece == null) {
            throw new UnsupportedOperationException("Cannot remove piece from an empty square.");
        }
        piece = null;
    }

    public void placePiece(Piece piece) {
        if(piece == null) {
            throw new IllegalArgumentException("No piece provided.");
        }
        this.piece = piece;
    }

}
