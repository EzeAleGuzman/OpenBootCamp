package com.open_bootcamp;

public class Main {

    public static void main(String[] args) {
        int valor;
        valor = suma(10 , 30, 50);
        System.out.println("las suma es " + valor);
        Coche MiCoche = new Coche();
        MiCoche.AgregarPuerta();
        MiCoche.AgregarPuerta();
        System.out.println("la cantidad de puertas es " + MiCoche.Puertas);



    }
    public static int suma(int a, int b, int c) {
        return a + b + c;
    }
}

class Coche {
    public int Puertas = 0;

    public void AgregarPuerta() {
        this.Puertas++;
    }
}