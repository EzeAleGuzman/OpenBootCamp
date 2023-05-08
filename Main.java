public class Main {
    public static void main(String[] args) {
        int numero =-1;
        if (numero < 0)     {
            System.out.println("es negativo");
        } else if (numero > 0){
            System.out.println("es positivo");
        }else   {
            System.out.println("es Cero");
        }
        while (numero < 3)  {
            System.out.println(numero);
            numero++;
        }
        do              {
            numero+=5 ;
            System.out.println(numero);
        } while (numero < 5) ; {
            System.out.println();
            numero++;
        }
        for (int numeroFor = 0; numeroFor >= 3; numeroFor++)    {
            System.out.println(numeroFor);
        }
        var estacion ="otoño";
        switch (estacion)   {
            case "invierno":
                System.out.println("es invierno");
                break;
            case "verano":
                System.out.println("es verano");
                break;
            case "Primavera":
                System.out.println(" es Primavera");
                break;
            case "otoño":
                System.out.println("es otoño");
                break;
            default:
                System.out.println("No es una estacion");
        }

    }

}
