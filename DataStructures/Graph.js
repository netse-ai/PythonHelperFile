"use strict"

class Node {
    constructor(data, rank) {
        this.name = data;
        this.rank = rank;
    }
    returnName(){
        return this.name;
    }
}

class Graph {
    constructor() {
        this.edges = [];
    }

    returnNeighbors(index){
        return this.edges[index];
    }

    addNeighbor(node1, node2, node3, node4){
        if (node1 == null){
            console.log("something went terribly wrong!");
        }
        else if (node1 != null && node2 == null && node3 == null && node4 == null) {
            this.edges.push({[node1]: []});
        }
        else if (node4 == null){
            this.edges.push({[node1]:[node2, node3]})
        }
        else{
            this.edges.push({[node1]: [node2, node3, node4]})
        }
    }
    returnEdges(){
        return JSON.stringify(this.edges, null, 2);
    }
}

var g = new Graph();
var resolveNode0 = new Node("Mastery1", 5);
var resolveNode1 = new Node("Mastery2", 0);
var resolveNode2 = new Node("Mastery3", 1);
var resolveNode3 = new Node("Mastery4", 0);
var resolveNode4 = new Node("Mastery5", 5);
var resolveNode5 = new Node("Mastery6", 0);
var resolveNode6 = new Node("Mastery7", 1);
var resolveNode7 = new Node("Mastery8", 0);
var resolveNode8 = new Node("Mastery9", 5);
var resolveNode9 = new Node("Mastery10", 0);
var resolveNode10 = new Node("Mastery11", 1);
var resolveNode11 = new Node("Mastery12", 0);
var resolveNode12 = new Node("Mastery13", 0);


// ------- Beginning OF RESOLVE TREE OPTIONS -------- //
if (resolveNode0.rank == 5 && resolveNode1.rank != 5){
    g.addNeighbor(resolveNode0.name, resolveNode2.name, resolveNode3.name);
}
else if (resolveNode1.rank == 5 && resolveNode0.rank != 5){
    g.addNeighbor(resolveNode1.name, resolveNode2.name, resolveNode3.name);
}


if (resolveNode2.rank == 1 && resolveNode3.rank != 1){
    g.addNeighbor(resolveNode2.name, resolveNode4.name, resolveNode5.name);
}
else if (resolveNode3.rank == 1 && resolveNode2 !=1){
    g.addNeighbor(resolveNode3.name, resolveNode4.name, resolveNode5.name);
}


if (resolveNode4.rank == 5 && resolveNode5.rank != 5){
    g.addNeighbor(resolveNode4.name, resolveNode6.name, resolveNode7.name)
}
else if (resolveNode5.rank == 5 && resolveNode4.rank != 5){
    g.addNeighbor(resolveNode5.name, resolveNode6.name, resolveNode7.name);
}


if (resolveNode6.rank == 1 && resolveNode7.rank != 1){
    g.addNeighbor(resolveNode6.name, resolveNode8.name, resolveNode9.name);
}
else if (resolveNode7.rank == 1 && resolveNode6.rank != 1){
    g.addNeighbor(resolveNode7.name, resolveNode8.name, resolveNode9.name);
}


if (resolveNode8.rank == 5 && resolveNode9.rank != 5){
    g.addNeighbor(resolveNode8.name, resolveNode10.name, resolveNode11.name, resolveNode12.name);
}
else if (resolveNode9.rank == 5 && resolveNode8.rank != 5){
    g.addNeighbor(resolveNode9.name, resolveNode10.name, resolveNode11.name, resolveNode12.name);
}


if (resolveNode10.rank == 1 && resolveNode11.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode10.name);
}
else if (resolveNode11.rank == 1 && resolveNode10.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode11.name);
}
else if (resolveNode12.rank == 1 && resolveNode10.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode12.name);
}
// ------- END OF RESOLVE TREE OPTIONS -------- //

// ------- Beginning OF FEROCITY TREE OPTIONS --------
if (resolveNode0.rank == 5 && resolveNode1.rank != 5){
    g.addNeighbor(resolveNode0.name, resolveNode2.name, resolveNode3.name);
}
else if (resolveNode1.rank == 5 && resolveNode0.rank != 5){
    g.addNeighbor(resolveNode1.name, resolveNode2.name, resolveNode3.name);
}


if (resolveNode2.rank == 1 && resolveNode3.rank != 1){
    g.addNeighbor(resolveNode2.name, resolveNode4.name, resolveNode5.name);
}
else if (resolveNode3.rank == 1 && resolveNode2 !=1){
    g.addNeighbor(resolveNode3.name, resolveNode4.name, resolveNode5.name);
}


if (resolveNode4.rank == 5 && resolveNode5.rank != 5){
    g.addNeighbor(resolveNode4.name, resolveNode6.name, resolveNode7.name)
}
else if (resolveNode5.rank == 5 && resolveNode4.rank != 5){
    g.addNeighbor(resolveNode5.name, resolveNode6.name, resolveNode7.name);
}


if (resolveNode6.rank == 1 && resolveNode7.rank != 1){
    g.addNeighbor(resolveNode6.name, resolveNode8.name, resolveNode9.name);
}
else if (resolveNode7.rank == 1 && resolveNode6.rank != 1){
    g.addNeighbor(resolveNode7.name, resolveNode8.name, resolveNode9.name);
}


if (resolveNode8.rank == 5 && resolveNode9.rank != 5){
    g.addNeighbor(resolveNode8.name, resolveNode10.name, resolveNode11.name, resolveNode12.name);
}
else if (resolveNode9.rank == 5 && resolveNode8.rank != 5){
    g.addNeighbor(resolveNode9.name, resolveNode10.name, resolveNode11.name, resolveNode12.name);
}


if (resolveNode10.rank == 1 && resolveNode11.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode10.name);
}
else if (resolveNode11.rank == 1 && resolveNode10.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode11.name);
}
else if (resolveNode12.rank == 1 && resolveNode10.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode12.name);
}
// ------- END OF FEROCITY TREE OPTIONS --------

// ------- Beginning OF CUNNING TREE OPTIONS --------
if (resolveNode0.rank == 5 && resolveNode1.rank != 5){
    g.addNeighbor(resolveNode0.name, resolveNode2.name, resolveNode3.name);
}
else if (resolveNode1.rank == 5 && resolveNode0.rank != 5){
    g.addNeighbor(resolveNode1.name, resolveNode2.name, resolveNode3.name);
}


if (resolveNode2.rank == 1 && resolveNode3.rank != 1){
    g.addNeighbor(resolveNode2.name, resolveNode4.name, resolveNode5.name);
}
else if (resolveNode3.rank == 1 && resolveNode2 !=1){
    g.addNeighbor(resolveNode3.name, resolveNode4.name, resolveNode5.name);
}


if (resolveNode4.rank == 5 && resolveNode5.rank != 5){
    g.addNeighbor(resolveNode4.name, resolveNode6.name, resolveNode7.name)
}
else if (resolveNode5.rank == 5 && resolveNode4.rank != 5){
    g.addNeighbor(resolveNode5.name, resolveNode6.name, resolveNode7.name);
}


if (resolveNode6.rank == 1 && resolveNode7.rank != 1){
    g.addNeighbor(resolveNode6.name, resolveNode8.name, resolveNode9.name);
}
else if (resolveNode7.rank == 1 && resolveNode6.rank != 1){
    g.addNeighbor(resolveNode7.name, resolveNode8.name, resolveNode9.name);
}


if (resolveNode8.rank == 5 && resolveNode9.rank != 5){
    g.addNeighbor(resolveNode8.name, resolveNode10.name, resolveNode11.name, resolveNode12.name);
}
else if (resolveNode9.rank == 5 && resolveNode8.rank != 5){
    g.addNeighbor(resolveNode9.name, resolveNode10.name, resolveNode11.name, resolveNode12.name);
}


if (resolveNode10.rank == 1 && resolveNode11.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode10.name);
}
else if (resolveNode11.rank == 1 && resolveNode10.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode11.name);
}
else if (resolveNode12.rank == 1 && resolveNode10.rank != 1 && resolveNode12.rank != 1){
    g.addNeighbor(resolveNode12.name);
}
// ------- END OF CUNING TREE OPTIONS --------



console.log(g.returnEdges())
console.log(g.returnNeighbors(0))



//
