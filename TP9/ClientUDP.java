import java.io.*;
import java.net.*;

public class ClientUDP
{

	public static void main(String[] args)
	{
		try
		{
			String message = "Hello World";
			byte[] data = message.getBytes();
			InetAddress address = InetAddress.getLocalHost();
			System.out.println("Sending to address: " + address.getHostName());
			DatagramPacket packet = new DatagramPacket(data, data.length, address, 1234);
			DatagramSocket socket = new DatagramSocket();
			socket.send(packet);
			System.out.println("Message sent successfully!");

			socket.receive(packet);
			String str = new String(packet.getData());

			System.out.println("reception en retour: "+ str );


			socket.close();

			System.out.println("Message sent successfully!");
		}
		catch (Exception ex)
		{
			System.out.println("Erreur!");
		}
	}
}
