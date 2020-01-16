package com.kaibro.rmi;

import java.util.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    public static void main(String[] args) {

        String host = "140.113.203.209";
        int port = 11099;
        try {
            Registry registry = LocateRegistry.getRegistry(host, port);
            RMIInterface stub = (RMIInterface) registry.lookup("FLAG");
            String[] ports = registry.list();
            for (String qort: ports) {
                System.out.println(qort);
            }
            List<Integer> list = new ArrayList<Integer>();
            list.add(1);
            list.add(2);
            String response = stub.getSecret();
            System.out.println("response: " + response);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
