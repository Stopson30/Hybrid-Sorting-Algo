using System;

public class HybridSort
{
    // The threshold determines when the algorithm switches from Bubble sort to Merge sort.
    private static int BubbleSortThreshold = 10;

    // The main sorting method to be called on the array.
    public static void Sort(int[] arr)
    {
        HybridSortAlgorithm(arr, 0, arr.Length - 1);
    }

    // The hybrid sorting algorithm that decides which method to use based on the threshold.
    private static void HybridSortAlgorithm(int[] arr, int left, int right)
    {
        // If the array portion is smaller or equal to the threshold, use Bubble sort.
        if (right - left <= BubbleSortThreshold)
        {
            BubbleSort(arr, left, right);
        }
        // If the array portion is larger than the threshold, use Merge sort.
        else
        {
            int mid = (left + right) / 2;
            HybridSortAlgorithm(arr, left, mid);
            HybridSortAlgorithm(arr, mid + 1, right);
            Merge(arr, left, mid, right);
        }
    }

    // The Bubble sort algorithm, sorting a portion of the array.
    private static void BubbleSort(int[] arr, int left, int right)
    {
        for (int i = left; i < right; i++)
        {
            for (int j = left; j < right - i + left; j++)
            {
                if (arr[j] > arr[j + 1])
                {
                    Swap(arr, j, j + 1);
                }
            }
        }
    }

    // The Merge sort algorithm, merging two sorted portions of the array.
    private static void Merge(int[] arr, int left, int mid, int right)
    {
        int[] temp = new int[right - left + 1];
        int i = left, j = mid + 1, k = 0;

        // Merging two sorted sub-arrays
        while (i <= mid && j <= right)
        {
            if (arr[i] <= arr[j])
            {
                temp[k++] = arr[i++];
            }
            else
            {
                temp[k++] = arr[j++];
            }
        }

        // Copying the remaining elements from the left sub-array
        while (i <= mid)
        {
            temp[k++] = arr[i++];
        }

        // Copying the remaining elements from the right sub-array
        while (j <= right)
        {
            temp[k++] = arr[j++];
        }

        // Copying the merged elements back to the original array
        Array.Copy(temp, 0, arr, left, temp.Length);
    }

    // A helper method to swap two elements in the array.
    private static void Swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

class Program
{
    static void Main(string[] args)
    {
        int[] arr = new int[] { 3, 5, 1, 7, 9, 2, 8, 4, 6, 0, 11, 15, 13, 12, 14, 10 };
        HybridSort.Sort(arr);

        Console.WriteLine("Sorted array:");
        foreach (int item in arr)
        {
            Console.Write(item + " ");
        }
    }
}
