package com.open_bootcamp;

public class Main {

    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setNombre("ezequiel");
        System.out.println(persona.getNombre());
        persona.setEdad(23);
        System.out.println(persona.getEdad());
        persona.setTelefono("+5491155845764");
        System.out.println(persona.getTelefono());
        }

    }
class Persona   {
        private int edad;
        private String nombre;
        private String telefono;

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getEdad() {
        return edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getTelefono() {
        return telefono;
    }
}
