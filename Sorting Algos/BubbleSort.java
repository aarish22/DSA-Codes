public class BubbleSort {
    public static int[] bubbleSort(int[] arr) {
        int temp;
        for (int i = arr.length - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] my_list = {2, 7, 1, 4, 9};
        int[] output = bubbleSort(my_list);

        for (int num : output) {
            System.out.print(num + " ");
        }
    }
}
