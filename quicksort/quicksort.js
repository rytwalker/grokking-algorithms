const quicksort = arr => {
  if (arr.length < 2) {
    return arr;
  } else {
    let pivot = arr[0];
    let less = [];
    let greater = [];
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] <= pivot) {
        less = [...less, arr[i]];
      } else if (arr[i] > pivot) {
        greater = [...greater, arr[i]];
      }
    }
    return [...quicksort(less), pivot, ...quicksort(greater)];
  }
};

console.log(quicksort([10, 5, 2, 3]));
