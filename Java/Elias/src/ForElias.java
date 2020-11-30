

public class ForElias {

    public static void main( final String[] args ) {

        // Example Array With Some Values
        final int[] array = new int[] { 2, 3, 3, 3, 3, 4, 3, 3, 3, 5 };

        // The Position Of The Value We Want To Change
        final int iMasterPosition = 1;

        // The Current Value At The MasterPosition
        final int iValueAtMasterPos = array[iMasterPosition];

        // Nun das Array ab der MasterPosition durchlaufen und wenn der Wert dem Wert
        // von iValueAtMasterPos entspricht (als Beispiel) mit zwei Multiplizieren,
        // ansonsten bei der ersten unterschiedlichen Zahl beenden.
        for (int iCounter = iMasterPosition; iCounter < array.length; iCounter++ ) {

            int iValueAtCounter = array[iCounter];

            if (iValueAtCounter == iValueAtMasterPos) {

                iValueAtCounter *= 2;
                System.out.println(iValueAtCounter);
            } else {

                System.out.println("Finished");
                break;
            }
        }
    }
}
