#alert "Hello django-coffeescript!"
fun = (d)=>
  d+"px"

jQuery =>
  w = 420
  h = 30
  data = [10,34,76,89,40,23,80,400]

  chart = d3.select("#bars").append("svg")
    .attr("class", "chart")
    .attr("width", 800)
    .attr("height", h * data.length)

  y = d3.scale.ordinal().domain(data).rangeBands([0, 220])

  x = d3.scale.linear().domain([0, d3.max(data)]).range(["0px", w/2+"px"])

  recs = chart.selectAll("rect").data(data).enter().append("rect").attr("y", y).attr("width", x).attr "height", y.rangeBand()


  text = chart.selectAll("text").data(data).enter().append("text")
    .attr("y", (d) ->y(d) + y.rangeBand() / 2)
    .attr("dx", -3).attr("dy", ".35em")
    .attr("text-anchor", "end")
    .attr("fill","white")
    .text(String)
    .attr("x", x)


  nx = d3.scale.linear().domain([0, d3.max(data)]).range(["0px", w+"px"])

  recs.transition().duration(4400).attr("width", nx)

  text.transition().duration(4400).attr("width", nx).attr("x", nx)
  ticks = x.ticks(10)
  lines = chart.selectAll("line").data(ticks)
  lines
    .enter().append("line")
    .attr("x1", x)
    .attr("x2", x)
    .attr("y1", 0)
    .attr("y2", h * data.length)
    .style("stroke", "#ccc")

  lines.data(x.ticks(10)).transition().duration(4400)
    .attr("x1", nx)
    .attr("x2", nx)
