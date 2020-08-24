let st = "a string is primitive";
console.log(st)
// console.log(st.length);

console.log('##########################');

console.log('##########################');

let op = st.slice(5, 15);
console.log(op);
console.log(st.length);
console.log(st.link);
console.log('indexOf', st.indexOf('p'));
console.log('lastIndexOf', st.lastIndexOf('st'));
console.log('Search', st.search('is'));
console.log('match', st.match('st'));
let it = 123
console.log(it.toString())

op = st.toUpperCase();
console.log(op);

l_op = op.toLowerCase();
console.log(l_op);

console.log('charAt', st.charAt(5))
console.log('charAt', st.charCodeAt(5))

let sti = 'this';
res = sti.concat(' ', 'is', ' ', 'js');
console.log(res);

let op = st.trim();
console.log(op);
console.log(op.length);

let op = st.split('/\s/');
console.log(op);

let op = st.replace('primitive', 'info');
console.log(op);

