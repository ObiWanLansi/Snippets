
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;



/**
 * The Class HelloWorld Is For ...
 *
 */
public final class HelloWorld extends Application {

    @Override
    public void start( final Stage primaryStage ) {

        final Label label = new Label("Hello JavaFX World!");

        final StackPane root = new StackPane();
        root.getChildren().add(label);

        final Scene scene = new Scene(root, 400, 300);

        primaryStage.setTitle("Hello JavaFX World!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }


    public static void main( final String[] args ) {

        launch(args);
    }

} // end public final class HelloWorld

