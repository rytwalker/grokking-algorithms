const factoral = num => (num === 1 ? 1 : num * factoral(num - 1));

console.log(factoral(4));
