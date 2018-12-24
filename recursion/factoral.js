const factoral = num => (num === 1 ? 1 : num * factoral(num - 1));

console.log(factoral(3));

// 1
// 2 * factoral(1)
// 3 * factoral(2)
