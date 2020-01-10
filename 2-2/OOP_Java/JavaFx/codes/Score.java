package sample;

import javafx.beans.property.*;

public class Score {
    private SimpleStringProperty name;
    private SimpleIntegerProperty korean;
    private SimpleIntegerProperty math;
    private SimpleIntegerProperty english;

    public Score(){
        this.name=new SimpleStringProperty();
        this.korean=new SimpleIntegerProperty();
        this.math=new SimpleIntegerProperty();
        this.english=new SimpleIntegerProperty();
    }
    public Score(String name, int korean, int math, int english){
        this.name=new SimpleStringProperty(name);
        this.korean=new SimpleIntegerProperty(korean);
        this.math=new SimpleIntegerProperty(math);
        this.english=new SimpleIntegerProperty(english);
    }
    public String getName(){
        return name.get();
    }
    public void setName(String name){
        this.name.set(name);
    }
    public int getKorean(){
        return korean.get();
    }
    public void setKorean(int korean){
        this.korean.set(korean);
    }
    public int getMath(){
        return math.get();
    }
    public void setMath(int korean){
        this.math.set(korean);
    }
    public int getEnglish(){
        return english.get();
    }
    public void setEnglish(int korean){
        this.english.set(korean);
    }
}
