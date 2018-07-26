import java.io.*;
import java.util.Scanner;
import java.util.TreeSet;

public class ReactAPI {
    public static TreeSet<String> functions = new TreeSet<>();
    public static boolean isWord(char c){
        if(c>='a' && c<='z' || c>='A' && c<='Z'){
            return true;
        }
        return false;
    }

    public static void handleFile(String filename) throws FileNotFoundException {
        File js1 = new File(filename);
        BufferedReader reader = null;
        reader = new BufferedReader(new FileReader(js1));
        Scanner in = new Scanner(reader);
        while (in.hasNextLine()){
            String str = in.nextLine();
//            System.out.println("Line:"+str);
            if(str.contains("function")){
                int posi = str.indexOf("function");
//                int last = str.lastIndexOf("function");
//                if(posi!=last)System.out.println("ERROR");//YES!!! It appears.
                Scanner sin = new Scanner(str);
                while (sin.hasNext()){
                    String token = sin.next();
                    if(token.equals("function")){
                        if(!sin.hasNext())break;
                        token=sin.next();
                        if(token.contains("(")){
                            String name = token.substring(0,token.indexOf('('));
                            if(name.length()!=0){
                                functions.add(name);
                                System.out.println("ADD:"+name);
                            }
                        }
                    }
                }
//                int nxtToken = posi+9;
//                String name = "";
//                int sl = str.length();
//
//                while (isWord(str.charAt(nxtToken))){
//                    name = name+str.charAt(nxtToken);
//                    nxtToken++;
//                    if(nxtToken>=sl){
//                        name="";
//                        break;
//                    }
//                }
//                if(!name.equals("") && str.charAt(nxtToken)=='('){
//                    functions.add(name);
//                    System.out.println("ADD:"+name);
//                }


            }
        }


    }

    public static void main(String args[]) throws IOException {
        functions.clear();
        try {
//            handleFile("test.txt");
            handleFile("react.development.js");
            handleFile("react-dom.development.js");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        File output = new File("ReactAPIFunctions.txt");
        FileWriter fw = null;
        fw = new FileWriter(output);
        for(String str:functions){
            System.out.println(str);
            fw.write(str+"\r\n");
        }
        fw.flush();
        fw.close();

    }

}
