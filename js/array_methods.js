let arr = [1, 'key', 2, 3, 'info', 'key'];
console.log(arr);
// arr.unshift([23]);
// let op = arr.pop();

// delete arr[1]
// console.log(arr.length);
// console.log(arr.splice(2, 5));
let sp_op = arr.splice(1, 2);
console.log(arr);

let arr2 = [66, 55, 77]
let op =  arr.concat(arr2);
console.log(op);

arr.forEach(function(element){
    console.log(element);
});

arr.forEach((element, index, array)=>{
    console.log(element, 'INDEX', index, 'ARRAY', array);
})

console.log(arr.indexOf('key'));
console.log(arr.lastIndexOf('key'));
console.log(arr.includes('info'));

t_arr = [
    {id:1, item:'r1'},
    {id:2, item:'r2'},
    {id:3, item:'r3'}
]

let us = t_arr.find(item => item.id == 1);
console.log(us);
console.log('####################');

let ms = t_arr.filter(item => item.id < 3);
ms.forEach(function(element){
    console.log(element);
})

let num_arr = [1, 2, 3, 4]

let map_op = num_arr.map(function(element, index){
    let mt = {'val':element, 'sq':element*element}
    return mt
});
// console.log(map_op);

let uo_arr = [6, 4, 1, 23, 9]
let srt_arr = uo_arr.sort(function(a, b){
    return a-b
});
// console.log(srt_arr);

let rev_op = uo_arr.reverse()
// console.log(rev_op);

console.log('T');
let st = 'python, world';
ar_op = st.split(', ');
console.log(ar_op);
res_op = ar_op.join(' ');
console.log(res_op);

let sum_ar = uo_arr.reduce((sum, curr) => sum+curr);
console.log(sum_ar);

let r_o = {
    min_a:18,
    max_a:27,
    c_j : function(user){
        return user.a >= this.min_a && user.a <= this.max_a
    }
}

let users = [
    {a:10},
    {a:22},
    {a:33},
    {a:18}
]

let sd = users.filter(r_o.c_j, r_o)
console.log(sd);