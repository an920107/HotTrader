package ncu_project.crypto_analysis_gui;

import javafx.event.ActionEvent;
import javafx.scene.control.Button;

public class CloseButton extends Button {
    private void closewindow(ActionEvent e){
        SceneController.stage.close();
    }
}
