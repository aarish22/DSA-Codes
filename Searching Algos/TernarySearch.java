class TernarySearch {
    int search(int arr[], int key, int lower_limit, int upper_limit) {
        if (upper_limit >= lower_limit) {
            int mid_1 = lower_limit + (upper_limit - lower_limit) / 3;
            int mid_2 = upper_limit - (upper_limit - lower_limit) / 3;

            if (arr[mid_1] == key) {
                return mid_1;
            }
            if (arr[mid_2] == key) {
                return mid_2;
            }
            if (key < arr[mid_1]) {
                return search(arr, key, lower_limit, mid_1 - 1);
            } else if (key > arr[mid_2]) {
                return search(arr, key, mid_2 + 1, upper_limit);
            } else {
                return search(arr, key, mid_1 + 1, mid_2 - 1);
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int lower_limit = 0;
        int target = 82;
        int upper_limit = 8;
        int my_list[] = { 15, 20, 47, 56, 59, 63, 65, 79, 82 };
        TernarySearch t1 = new TernarySearch();
        int result = t1.search(my_list, target, lower_limit, upper_limit);
        System.out.println(result);
    }
}
