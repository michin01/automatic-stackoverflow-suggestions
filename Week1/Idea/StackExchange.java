import com.csvreader.CsvReader;
import com.csvreader.CsvWriter;

import java.io.*;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;

public class StackExchange {

    public static String fileName = "data.csv";
//    public static void findReactTag() throws IOException {
//        File file = new File(fileName);
//        BufferedReader reader = null;
//        reader = new BufferedReader(new FileReader(file));
//        Scanner in = new Scanner(reader);
//        in.useDelimiter("\r\n");
//        String firstline = in.next();
//        System.out.println(firstline+"\r\n");
//        firstline = in.next();firstline = in.next();
//        System.out.println(firstline+"\r\n");
////        firstline = in.next();
////        System.out.println(firstline);
//        File res = new File("res.txt");
//        FileWriter resW = new FileWriter(res);
//        File notFound = new File("NotFound.txt");
//        FileWriter nfW = new FileWriter(notFound);
//
//
//    }

    public static TreeSet<String> tag = new TreeSet<>();
    public static String csvFilePath = "Output.csv";
    public static CsvWriter csvWriter;
    public static boolean first = true;
    public static void writeCSV(String[] content) throws IOException {
        // 定义一个CSV路径

        if(first){
            first=false;
            try {
                // 创建CSV写对象 例如:CsvWriter(文件路径，分隔符，编码格式);
                csvWriter = new CsvWriter(csvFilePath, ',', Charset.forName("UTF-8"));
                // 写表头
                String[] csvHeaders = {"Id","PostTypeId","AcceptedAnswerId","ParentId","CreationDate","DeletionDate","Score","ViewCount","Body","OwnerUserId","OwnerDisplayName","LastEditorUserId","LastEditorDisplayName","LastEditDate","LastActivityDate","Title","Tags","AnswerCount","CommentCount","FavoriteCount","ClosedDate","CommunityOwnedDate"};
                csvWriter.writeRecord(csvHeaders);
                // 写内容
    //            System.out.println("--------CSV文件已经写入--------");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        csvWriter.writeRecord(content);
    }
    public static void CloseWriter(){
        csvWriter.close();
    }


    public static ArrayList<String[]> readCSV(String fileName) throws IOException {
        ArrayList<String[]> csvFileList = new ArrayList<String[]>();
        CsvReader reader = new CsvReader(fileName, ',', Charset.forName("UTF-8"));
        reader.readHeaders();

        // 逐行读入除表头的数据
        while (reader.readRecord()) {
//                System.out.println(reader.getRawRecord());
            csvFileList.add(reader.getValues());
        }
        reader.close();
        return csvFileList;

    }
    public static void findTag() throws IOException {
        File res = new File("label.txt");
        FileWriter resW = new FileWriter(res);
        try {
            // 用来保存数据
            ArrayList<String[]> csvFileList = readCSV("data.csv");
            Scanner sin;
            tag.clear();
            // 遍历读取的CSV文件
            boolean cont = false;
            for (int row = 0; row < csvFileList.size(); row++) {
                // 取得第row行第0列的数据
                String cell = csvFileList.get(row)[16];
                String[] block = cell.split("<");
                cont = false;
                for(int i=0;i<block.length;i++){
                    if(block[i].contains("react")){
                        tag.add(block[i]);
                        cont = true;
                    }
//                    System.out.println("------------>" + block[i]);
                }

                if(!cont){
                    writeCSV(csvFileList.get(row));
//                    System.out.println("--------");
                }
//                break;
            }
            for(String t:tag){
                resW.write("<"+t+"\r\n");
            }
            CloseWriter();
            resW.flush();
            resW.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static TreeSet<Integer> idset = new TreeSet<>();
    public static void merge() throws IOException {
        String[] files = {"QueryResults 5-1.csv","QueryResults 5-2.csv"};
        ArrayList<String[]> csvFileList = null;
        idset.clear();
        for(String f:files){
            csvFileList = readCSV(f);
            for (int row = 0; row < csvFileList.size(); row++) {
                // 取得第row行第0列的数据
                String cell = csvFileList.get(row)[0];
                int id = Integer.parseInt(cell);
                if(!idset.contains(id)){
                    idset.add(id);
                    writeCSV(csvFileList.get(row));
                }

//                break;
            }

        }
        CloseWriter();

    }




    public static void main(String args[]){
        try {
            merge();
        } catch (IOException e) {
            e.printStackTrace();
        }

//        try {
//            readCSV();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//
//        try {
//            findReactTag();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
    }

}
