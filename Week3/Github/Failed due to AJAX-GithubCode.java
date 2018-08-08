import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.*;
import java.util.Scanner;

public class GithubCode {

    public static String getData(String key) throws IOException {
        Document doc = Jsoup.connect("https://github.com/search?q="+key)
                .header("User-Agent","Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2")
                .timeout(50000).get();
        Elements ele = doc.getElementsByClass("menu border d-none d-md-block");
        return ele.text();
    }
    public static int i = 1;
    public static void main(String args[]) {
        File api = new File("api.txt");
        File output = new File("apiUsed.csv");
        FileWriter fw = null;
        try {
            fw = new FileWriter(output);
        } catch (IOException e) {
            e.printStackTrace();
        }

        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(api));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        Scanner in = new Scanner(br);
        String token,res="";
        while (in.hasNextLine()){
            token = in.nextLine().toLowerCase().trim();
            System.out.println(token);
            boolean err = true;
            while (err){
                try {


                    try {
                        Thread.sleep(i+500);
                    } catch (InterruptedException e1) {
                        e1.printStackTrace();
                    }

                    res = getData(token);
                    try {
                        Thread.sleep(i*500);
                    } catch (InterruptedException e1) {
                        e1.printStackTrace();
                    }
                    fw.write(token+","+res+"\r\n");
                    fw.flush();
                    err=false;
                } catch (IOException e) {
                    e.printStackTrace();
                    try {
                        Thread.sleep(i*1000);
                        i++;
                    } catch (InterruptedException e1) {
                        e1.printStackTrace();
                    }
                    System.out.println("ERROR:"+token+" Wait "+i+" Second.");
                }
            }


        }
        try {
            fw.flush();
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }





    }
}
