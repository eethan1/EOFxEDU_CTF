package com.kaibro.rmi;

import java.util.*;
import java.rmi.Remote;
import java.rmi.RemoteException;

// Every remote object sholud implement this interface
public interface RMIInterface extends Remote {
        String sayHello() throws RemoteException;
        String getSecret() throws RemoteException;
        String FLAG() throws RemoteException;
}
