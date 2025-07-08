using System;
using System.Collections.Generic;

/*
 The stdin mcp configuration was
 {
    "servers": {
        "demo-server": {
            "type": "stdio",
            "command": "uv",
            "args": [
                "run",
                "mcp",
                "run",
                "C:\\Gonen\\Teaching\\ai\\mcp\\mcpserver.py"
            ],
        }
    }
}
*/
namespace HelloWorld
{    public class Program
    {
        public static void Main(string[] args)
        {
            Impl8331();
            DemonstrateQuickSort();
        }

        public static void Impl8331()
        {
            Console.WriteLine("Hello, World!");
            Console.WriteLine("This is the traditional C# program format.");
        }

        public static void DemonstrateQuickSort()
        {
            Console.WriteLine("\n--- Quicksort Algorithm Demonstration ---");
            
            // Test with different arrays
            int[] array1 = { 64, 34, 25, 12, 22, 11, 90 };
            int[] array2 = { 5, 2, 8, 1, 9, 3, 7, 4, 6 };
            int[] array3 = { 1 };
            int[] array4 = { };
            
            Console.WriteLine("Original array 1: " + string.Join(", ", array1));
            QuickSort(array1, 0, array1.Length - 1);
            Console.WriteLine("Sorted array 1: " + string.Join(", ", array1));
            
            Console.WriteLine("\nOriginal array 2: " + string.Join(", ", array2));
            QuickSort(array2, 0, array2.Length - 1);
            Console.WriteLine("Sorted array 2: " + string.Join(", ", array2));
            
            Console.WriteLine("\nOriginal array 3: " + string.Join(", ", array3));
            QuickSort(array3, 0, array3.Length - 1);
            Console.WriteLine("Sorted array 3: " + string.Join(", ", array3));
            
            Console.WriteLine("\nOriginal array 4: " + string.Join(", ", array4));
            QuickSort(array4, 0, array4.Length - 1);
            Console.WriteLine("Sorted array 4: " + string.Join(", ", array4));
        }

        /// <summary>
        /// Quicksort algorithm implementation
        /// </summary>
        /// <param name="arr">Array to be sorted</param>
        /// <param name="low">Starting index</param>
        /// <param name="high">Ending index</param>
        public static void QuickSort(int[] arr, int low, int high)
        {
            if (low < high)
            {
                // Partition the array and get the pivot index
                int pivotIndex = Partition(arr, low, high);
                
                // Recursively sort elements before and after partition
                QuickSort(arr, low, pivotIndex - 1);
                QuickSort(arr, pivotIndex + 1, high);
            }
        }

        /// <summary>
        /// Partition function for quicksort
        /// </summary>
        /// <param name="arr">Array to partition</param>
        /// <param name="low">Starting index</param>
        /// <param name="high">Ending index</param>
        /// <returns>Index of the pivot element</returns>
        private static int Partition(int[] arr, int low, int high)
        {
            // Choose the rightmost element as pivot
            int pivot = arr[high];
            
            // Index of smaller element (indicates right position of pivot)
            int i = low - 1;
            
            for (int j = low; j < high; j++)
            {
                // If current element is smaller than or equal to pivot
                if (arr[j] <= pivot)
                {
                    i++; // increment index of smaller element
                    Swap(arr, i, j);
                }
            }
            
            // Place pivot in its correct position
            Swap(arr, i + 1, high);
            return i + 1;
        }

        /// <summary>
        /// Swap two elements in an array
        /// </summary>
        /// <param name="arr">Array containing elements to swap</param>
        /// <param name="i">Index of first element</param>
        /// <param name="j">Index of second element</param>
        private static void Swap(int[] arr, int i, int j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
}
