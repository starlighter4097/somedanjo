//let Telegraf = require('telegraf')
const { Telegraf } = require('telegraf')
let token="6291384049:AAHczC98ZrsIThc30yiUIyxrD-haVci037M";
const bot = new Telegraf(token)
const { exec } = require("child_process");
var moment = require('moment');

bot.launch()
bot.start((ctx) => {
    console.log(ctx);
    ctx.reply('👍')
});



exec("node sqlexcecutor.js",  (error, stdout, stderr) => {
  
       sendMessage(stdout);
    
	
	


})

sendMessage("sending to group")


function sendMessage(msg){
   
if(msg)
{

  console.log("sending mesage to group")
 bot.telegram.sendMessage(-1001967200557, msg.substring(0,4090)
).then((msg)=> { console.log("then",msg)} ).catch
(e=>console.log(e))
}
else
{
console.log("msg empty");
}
}








