var vis = d3.select("#graph").append("svg");

function addBase(vis,target,object,tag) {
	return vis.selectAll(target).data(object).enter().append(tag);
}

var w = 900, h = 400;
//add attributes such as width and height of the graph. 
vis.attr("width", w).attr("height", h);
//add text.
vis.text("The Graph").select("#graph");
//create a node.
var nodes = [{x: 30, y: 50},
			{x: 50, y: 80},
			{x: 90, y: 120}];z
//add node to DOM with tag name "circle" and other attr.
addBase(vis,"circle .nodes",nodes,"svg:circle")
     .attr("class", "nodes")
     .attr("cx", function(d) { return d.x; })
     .attr("cy", function(d) { return d.y; })
	 .attr("r", "10px")
     .attr("fill", "black")
//connecting edges
var links = [
  {source: nodes[0], target: nodes[1]},
  {source: nodes[2], target: nodes[1]}
]
//add edges to DOM
addBase(vis,".line",links,"line")
   .attr("x1", function(d) { return d.source.x })
   .attr("y1", function(d) { return d.source.y })
   .attr("x2", function(d) { return d.target.x })
   .attr("y2", function(d) { return d.target.y })
   .style("stroke", "rgb(6,120,155)");
