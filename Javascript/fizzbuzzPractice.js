let fizzBuzz = function (str1 = 'fizzbuzz', str2 = 'fizz', str3 = 'buzz', num1 = 15, num2 = 3, num3 = 5) {

let arr = []

for(let i = 1; arr.length < 100; i++){
    if(i % num1 === 0){
        arr.push(str1)
    } else if(i % num2 === 0){
        arr.push(str2)
    } else if(i % num3 === 0){
        arr.push(str3)
    } else {
        arr.push(i)
    }
    
}

return arr

}

console.log(fizzBuzz())