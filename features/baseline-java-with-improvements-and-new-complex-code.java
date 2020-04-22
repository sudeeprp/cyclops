package demoapp;

public class Editor {
    IGrammar grammarCheck;

    Editor(IGrammar grammar)
    {
        grammarCheck = grammar;
    }
    Editor(String user, IGrammar grammar)
    {
        if(user.equals("Venkatesh")) {
            System.out.println("Your license expired");
        } else if(user.equals("Annie")) {
            System.out.println("Welcome");
        } else if(user.equals("Gunda")) {
            System.out.println("Come tomorrow");
        } else {
            System.out.println("Dont know you");
        }
        grammarCheck = grammar;
    }
    public void startEdit(String lang)
    {
        //lowered complexity
        if(lang.equals("English")) {
            grammarCheck.checkGrammar();
        } else {
            System.out.println("Better luck next time");
        }
        System.out.println(lang);
    }
    public void startEdit()
    {
        System.out.println("Editor here");
        grammarCheck.checkGrammar();
    }
}
