package demoapp;

public class Editor {
    IGrammar grammarCheck;

    Editor(IGrammar grammar)
    {
        grammarCheck = grammar;
    }
    public void startEdit(String lang)
    {
        if(lang.equals("English")) {
            grammarCheck.checkGrammar();
        } else if(lang.equals("Hindi")) {
            System.out.println("Hindi coming soon");
        } else if(lang.equals("Sanskrit")) {
            System.out.println("Sanskrit is hard to support");
        } else if(lang.equals("German")) {
            System.out.println("German is the hardest");
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
