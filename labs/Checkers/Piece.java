package exercise1_1_checkers;

import javafx.scene.paint.Color;
import javafx.scene.shape.Ellipse;

/**
 * Represents a movable piece on the board.
 */
public class Piece {
    public enum Type {
        RED, BLACK
    }
    private final Type type;

    /**
     * The position of the bee on the board, where 0,0 is a corner position and 7,7 is the
     * opposite corner
     */
    private int x, y;
    private final Ellipse ellipse;

    public Piece(Type type, int x, int y) {
        this.type = type;
        this.x = x;                 // initial location of bee; for your solution,
        this.y = y;                 //     capture this in an object
        // draws bee
        ellipse = new Ellipse();
        ellipse.setRadiusX(25.0f);
        ellipse.setRadiusY(12.0f);
        if(this.type == Type.RED) {
            ellipse.setFill(Color.RED);
        } else if(this.type == Type.BLACK) {
            ellipse.setFill(Color.BLACK);
        } else {
            throw new IllegalArgumentException("Unknown type:"+type);
        }
        ellipse.setStroke(Color.WHITE);
        setActive(false);
        ellipse.setOnMouseClicked(event -> trySetActive());
        BoardController.addChild(ellipse);
        display();
    }

    public String toString() {
        return "Piece at "+x+", "+y;
    }

    public Type getType() {
        return type;
    }

    // display the bee at the (beeXLocation, beeYLocation), ensuring the bee does not leave the garden
    private void display() {
        ellipse.setLayoutX(x*BoardController.SQUARE_SIZE + BoardController.SQUARE_SIZE/2);
        ellipse.setLayoutY(y*BoardController.SQUARE_SIZE + BoardController.SQUARE_SIZE/2);
    }

    private void trySetActive() {
        BoardController.trySetActive(this);
    }

    public void setActive(boolean isActive) {
        if(isActive) {
            ellipse.setStrokeWidth(3);
        } else {
            ellipse.setStrokeWidth(1);
        }
    }

    /**
     * If possible, perform either an ordinary or capture move to the given square.
     *
     * (Report the problem to the user if not possible)
     * @param square the square to which the move will be made if possible.
     */
    public void tryMove(Square square) {
        if(isValidOrdinaryMove(square)) {
            move(square);
        } else if(isValidCapture(square)) {
            captureMoveTo(square);
        } else {
            BoardController.setMessage("The piece can neither move nor capture to that position" +
                    ".\nPlease try a " +
                    "different " +
                    "square.");
        }
    }

    /**
     * Perform an ordinary move.  Move this piece to the new position and switch turns.
     * @param square the position to which this piece will be moved.
     */
    private void move(Square square) {
        BoardController.getSquare(x,y).removePiece();
        this.x = square.getX();
        this.y = square.getY();
        BoardController.getSquare(x,y).placePiece(this);
        display();
        BoardController.switchTurns();
        setActive(false);

        if(type.equals(Type.BLACK) && y == 0) {
            BoardController.setMessage("Kings are not yet implemented. Sorry!");
        }
    }

    /**
     * Perform a capture move.  Identify the piece to be captured
     * and move to that square.
     * @param square A square to which this piece is able to move and capture at the same time.
     * @throws  IllegalArgumentException If no capture is made by moving to the square.
     */
    private void captureMoveTo(Square square) {
        Piece captured = getCapturedPiece(square);
        if(captured == null) {
            throw new IllegalArgumentException("Cannot capture by moving to "+square);
        }
        BoardController.capturePiece(captured);
        move(square);
    }

    public void beCaptured() {
        BoardController.getSquare(x,y).removePiece();
        BoardController.removeChild(ellipse);
    }

    /**
     * @param square The square to which this piece will move
     * @return true if this piece can move to that square and capture another
     *    piece at the same time.
     */
    private boolean isValidOrdinaryMove(Square square) {
        if(type.equals(Type.BLACK)) {
            return (square.getY() == y - 1 &&
                    Math.abs(square.getX()-x) == 1);
        } else if(type.equals(Type.RED)){
            return (square.getY() == y + 1 &&
                    Math.abs(square.getX()-x) == 1);
        } else {
            throw new IllegalStateException("This piece has an unknown type:"+type);
        }
    }

    /**
     * @param square The square to which this piece will move
     * @return true if this piece can move to that square and capture another
     *    piece at the same time.
     */
    private boolean isValidCapture(Square square) {
        return getCapturedPiece(square) != null;
    }

    /**
     * Find the piece that would be captured by moving this piece to a given square.
     *
     * The piece is not actually captured when calling this method.
     * It is simply identified by calling this method.
     *
     * @param square The square to which a move will be mode
     * @return null if the move cannot be made.
     *      Otherwise, return the piece that would be removed by moving to that square.
     */
    private Piece getCapturedPiece(Square square) {
        if(type.equals(Type.BLACK)) {
            if (!((square.getY() == y - 2 &&
                    Math.abs(square.getX()-x) == 2))) {
                return null;
            } else {
                return getMiddlePiece(square);
            }
        } else if(type.equals(Type.RED)){
            if (!((square.getY() == y + 2 &&
                    Math.abs(square.getX()-x) == 2))) {
                return null;
            } else {
                return getMiddlePiece(square);
            }
        } else {
            throw new IllegalStateException("This piece has an unknown type:"+type);
        }
    }

    private Piece getMiddlePiece(Square square) {
        int middleX = (square.getX() + x) / 2;
        int middleY = (square.getY() + y) / 2;
        return BoardController.getSquare(middleX, middleY).getPiece();
    }
}

