package at.czlabinger;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import service.GreeterImpl;

import java.io.IOException;


public class App {
    public static void main( String[] args ) {
        try {
            Server server = ServerBuilder.forPort(8999).addService(new GreeterImpl()).build();

            server.start();
            System.out.println("Server started at " + server.getPort());
            server.awaitTermination();
        } catch (IOException | InterruptedException e) {
            System.out.println("Error: " + e);
        }
    }
}
