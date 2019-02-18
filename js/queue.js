/*
 
队列的特点是「先进先出」，一般有这几个操作

# enqueue 将一个元素存入队列中
# dequeue 将一个元素从队列中取出，并在队列中删除它

# empty 查看栈是否是空的

可以把队列看做排队，银行叫号机就是队列，先取号的先入队，叫号的时候也就先出队

*/
var log = function(){
    console.log.apply(console, arguments)
}

// 队列结构
// 主要有 2 个操作
// enqueue dequeue
//
var Queue = function() {
    // data 是存储元素的数组
    this.data = []
}

// 入队
Queue.prototype.enqueue = function (element) {
    this.data.push(element)
}

// 出队
Queue.prototype.dequeue = function () {
    return this.data.splice(0, 1)[0]
}

// 队列长度
Queue.prototype.length = function () {
    return this.data.length
}

// 清空队列
Queue.prototype.empty = function() {
    this.data = []
}

var q = new Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
log('length', q.length())
log(q.dequeue())
q.enqueue(4)
log(q.dequeue())
log(q.dequeue())
log(q.dequeue())