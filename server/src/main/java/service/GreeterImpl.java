package service;

import io.grpc.stub.StreamObserver;
import hello.GreeterGrpc;
import hello.Hello;

public class GreeterImpl extends GreeterGrpc.GreeterImplBase {

    @Override
    public void sayHello(Hello.HelloRequest request, StreamObserver<Hello.HelloReply> responseObserver) {
        /* Build a response composed with the constant Hello and the name variable from the request.
         * For example, if the request is: gRPC the reply will be: "Hello gRPC".
         */
        Hello.HelloReply reply = Hello.HelloReply.newBuilder().setText("Hello " + request.getName()).build();
        responseObserver.onNext(reply);
        /* We use the response observer's onCompleted method to specify that we've finished dealing with the RPC */
        responseObserver.onCompleted();
    }

}
