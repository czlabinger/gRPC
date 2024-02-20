package service;

import io.grpc.stub.StreamObserver;
import hello.GreeterGrpc;
import hello.Hello;

public class GreeterImpl extends GreeterGrpc.GreeterImplBase {

    @Override
    public void sayHello(Hello.HelloRequest request, StreamObserver<Hello.HelloReply> responseObserver) {
        Hello.HelloReply reply = Hello.HelloReply.newBuilder().setText("Hello " + request.getName()).build();
        System.out.println("Got message: " + request.getName());
        responseObserver.onNext(reply);
        responseObserver.onCompleted();
    }

}
