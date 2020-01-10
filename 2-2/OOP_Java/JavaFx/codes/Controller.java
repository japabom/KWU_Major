package sample;

import javafx.event.*;
import java.lang.*;

import java.net.URL;
import java.util.*;
import javafx.collections.FXCollections;
import javafx.fxml.*;
import javafx.stage.Modality;
import javafx.stage.StageStyle;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.collections.*;
import javafx.scene.control.TableView;
import javafx.scene.control.Button;
import javafx.scene.Parent;
import javafx.scene.control.TableColumn;
import javafx.scene.chart.BarChart;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.chart.XYChart;
import javafx.scene.control.TextField;

public class Controller implements Initializable{
    @FXML private TableView<Score> tableview;
    @FXML private Button button1;
    @FXML private Button button2;
    private Stage primaryStage;
    ObservableList<Score> scoreList= FXCollections.observableArrayList();

    @Override
    public void initialize(URL location, ResourceBundle resources){
        button1.setOnAction(event->{
            try{
                handleBtnlAction(event);
            }catch(Exception e){
                e.printStackTrace();
            }
        });
        button2.setOnAction(event->{
            try{
                handleBtn2Action(event);
            }catch(Exception e){
                e.printStackTrace();
            }
        });
    }
    public void setPrimaryStage(Stage primaryStage){
        this.primaryStage=primaryStage;
    }
    public void handleBtnlAction(ActionEvent event) throws Exception{
        Stage dialog=new Stage(StageStyle.UTILITY);
        dialog.initModality(Modality.WINDOW_MODAL);
        dialog.initOwner(primaryStage);
        dialog.setTitle("추가");

        Parent parent = FXMLLoader.load(getClass().getResource("chart.fxml"));
        Button btn1=(Button)parent.lookup("#btn1");
        btn1.setOnAction(e->{
            TextField textfield1 = (TextField)parent.lookup("#textfield1");
            TextField textfield2 = (TextField)parent.lookup("#textfield2");
            TextField textfield3 = (TextField)parent.lookup("#textfield3");
            TextField textfield4 = (TextField)parent.lookup("#textfield4");

            scoreList.add(new Score(textfield1.getText(),
                    Integer.parseInt(textfield2.getText()),
                    Integer.parseInt(textfield3.getText()),
                    Integer.parseInt(textfield4.getText())));

            TableColumn<Score, ?> tcName=tableview.getColumns().get(0);
            tcName.setCellValueFactory(new PropertyValueFactory<>("name"));
            tcName.setStyle("-fx-alignment: CENTER;");

            TableColumn<Score, ?> tcKorean=tableview.getColumns().get(1);
            tcKorean.setCellValueFactory(new PropertyValueFactory<>("korean"));
            tcKorean.setStyle("-fx-alignment: CENTER;");

            TableColumn<Score, ?> tcMath=tableview.getColumns().get(2);
            tcMath.setCellValueFactory(new PropertyValueFactory<>("math"));
            tcMath.setStyle("-fx-alignment: CENTER;");

            TableColumn<Score, ?> tcEnglish=tableview.getColumns().get(3);
            tcEnglish.setCellValueFactory(new PropertyValueFactory<>("english"));
            tcEnglish.setStyle("-fx-alignment: CENTER;");

            tableview.setItems(scoreList);
            dialog.close();
        });

        Button btn2=(Button)parent.lookup("#btn2");
        btn2.setOnAction(e->dialog.close());
        Scene scene=new Scene(parent);

        dialog.setScene(scene);
        dialog.setResizable(false);
        dialog.show();
    }
    public void handleBtn2Action(ActionEvent event) throws Exception{
        Stage dialog = new Stage(StageStyle.UTILITY);
        dialog.initModality(Modality.WINDOW_MODAL);
        dialog.initOwner(primaryStage);
        dialog.setTitle("막대 그래프");

        Parent parent = FXMLLoader.load(getClass().getResource("graph.fxml"));
        BarChart<String,Number> barChart = (BarChart<String,Number>)parent.lookup("#barchart");

        XYChart.Series<String,Number> dataSeries1=new XYChart.Series<>();
        dataSeries1.setName("국어");

        XYChart.Series<String,Number> dataSeries2=new XYChart.Series<>();
        dataSeries2.setName("수학");

        XYChart.Series<String,Number> dataSeries3=new XYChart.Series<>();
        dataSeries3.setName("영어");

        for(int i=0;i<scoreList.size();i++){
            dataSeries1.getData().add(new XYChart.Data<>(scoreList.get(i).getName(), scoreList.get(i).getKorean()));
            dataSeries2.getData().add(new XYChart.Data<>(scoreList.get(i).getName(), scoreList.get(i).getMath()));
            dataSeries3.getData().add(new XYChart.Data<>(scoreList.get(i).getName(), scoreList.get(i).getEnglish()));
        }
        barChart.getData().add(dataSeries1);
        barChart.getData().add(dataSeries2);
        barChart.getData().add(dataSeries3);

        Button btn3=(Button)parent.lookup("#btn3");
        btn3.setOnAction(e->dialog.close());
        Scene scene=new Scene(parent);

        dialog.setScene(scene);
        dialog.setResizable(false);
        dialog.show();
    }
}
