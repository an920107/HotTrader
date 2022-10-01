package ncu_project.crypto_analysis_gui;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

import java.io.IOException;

public class MainController extends Application {

    @Override
    public void start(Stage stage) throws Exception {
        //stage.initStyle(StageStyle.TRANSPARENT);

        SceneController.stage = stage;
        SceneController.show(SceneController.Scenes.LOADING,true);
        stage.getIcons().add(new Image(MainController.class.getResource("hot-face.png").toExternalForm()));
        stage.setTitle("HotTrader");

        stage.show();

        //MySQL.setConnection("jdbc:mysql://finalproject.ddns.net:3306/tradersdb", "tradersuser", "TRADERSuser");
    }

    public static void main(String[] args) {
        launch();
    }
}
