/*
数据结构的核心是，一个结构只有特定的操作，可以实现特定的功能

栈的特点是「先进后出」，一般有这几个操作
# push 将一个元素存入栈中
# pop  将一个元素从栈中取出，并在栈中删除它
# top  将一个元素从栈中取出

*/

var log = function(){
    console.log.apply(console, arguments)
}

var Stack = function() {
    this.data = []
}

// push 添加一个元素
Stack.prototype.push = function(e) {
    this.data.push(e)
}

// pop 删除并返回最新添加的元素
Stack.prototype.pop = function() {
    var index = this.data.length - 1
    return this.data.splice(index, 1)[0]
}

// top 仅返回最新添加的元素
Stack.prototype.top = function() {
    var index = this.data.length - 1
    return this.data[index]
}

var s = new Stack()
s.push('hello')
s.push('world')
log(s.pop())
log(s.pop())

var str = 'hello'
for (var i = 0; i < str.length; i++) {
    s.push(str[i])
}

var str1 = ''
for (var i = 0; i < str.length; i++) {
    str1 += s.pop()
}
log(str1)
