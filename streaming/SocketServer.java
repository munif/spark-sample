package org.munif.server;


import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

public class SocketServer {

	public static void main(String[] args) {
		
		ServerSocket socServer = null;
		DataInputStream is;
		PrintStream os;
		Socket clientSocket = null;
		
		Path path = FileSystems.getDefault().getPath("D:/SparkCourse", "streamingtweets.txt");
		System.out.println(path.toString());
		
		List<String> lines = null;
		try {
			lines = Files.readAllLines(path, StandardCharsets.UTF_8);
		} catch (IOException e) {
			 e.printStackTrace();
		}
		
		try {
			socServer = new ServerSocket(9000);
			System.out.println("Socked opened.");
			
			System.out.println("Total records read: " + lines.size());
			
		} catch (IOException e) {
			System.out.println(e);
		}
		
		try {
			clientSocket = socServer.accept();
			System.out.println("Accepted client request from: " + clientSocket.getInetAddress());
			
			is = new DataInputStream(clientSocket.getInputStream());
			os = new PrintStream(clientSocket.getOutputStream());
			
			while (true) {
				// Pick a random line
				int randomLine = (int) (Math.random() * lines.size());
				
				Date date = new Date();
				DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
				
				System.out.println(dateFormat.format(date) + ": Publishing " + lines.get(randomLine));
				os.println(lines.get(randomLine));
				os.flush();
				
				// Random sleep 1-3 seconds
				Thread.sleep((long) (Math.random()*3000));
			}
		} catch (Exception e) {
			System.out.println(e);
		}
		
	}

}
