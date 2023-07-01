// Import Module
// const tutorial = require('./tut1')
// console.log("Hello World from node js");
// console.log(tutorial)
// console.log(tutorial(1,3))

// const eventemmitter = require('events');
// const ee = new eventemmitter ();

// ee.on('tut', ()=>{
//     console.log("sdfsad")
// })

// ee.emit('tut');

// Events
// const event  = require('events');
// const Eventemit = new event();

// class Family extends event {
//     constructor(n){
//         super();
//         this.name = n;
//     }
// }

// const hammad = new Family("zzz")
// hammad.on("name",()=>{
// console.log(`my name is ${hammad.name}`)
// })
// hammad.emit("name")

const readline  = require ('readline');
const rl = readline.createInterface({input: process.stdin , output: process.stdout});
let ans = 6;
rl.question("what is 2 + 4?", (ui)=>{
if(ui.trim() == ans){
    console.log(ui)
    rl.close();
}
});

