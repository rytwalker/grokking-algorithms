// Selection Sort
const selection_sort = arr => {
  let unsortedArr = [...arr];
  let sortedArr = [];
  for (let i = 0; i < arr.length; i++) {
    let smallest = findSmallest(unsortedArr);
    sortedArr = [...sortedArr, smallest];
    unsortedArr = unsortedArr.filter(item => smallest !== item);
  }
  return sortedArr;
};

const findSmallest = arr => {
  let smallest = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < smallest) {
      smallest = arr[i];
    }
  }
  return smallest;
};

console.log(selection_sort([5, 3, 6, 2, 10]));
