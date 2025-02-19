import java.util.Scanner;
public class teste {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int dia;
        System.out.println("Digite um número de 1 a 7: ");
        dia = scanner.nextInt();

        if (dia == 1) {
            System.out.println("Você escolheu domingo");
        } else if (dia == 2) {
            System.out.println("Você escolheu segunda");
        } else if (dia == 3) {
            System.out.println("Você escolheu terça");
        } else if (dia == 4) {
            System.out.println("Você escolheu quarta"); 
        } else if (dia == 5) {
            System.out.println("Você escolheu quinta");
        } else if (dia == 6) {
            System.out.println("Você escolheu sexta");
        } else if (dia == 7) {
            System.out.println("Você escolheu sábado");
        } else {
            System.out.println("Número Inválido");
        }

        scanner.close();

    }
}
