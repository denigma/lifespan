class Denigma.Charts
  ###
    class to generate chars with d3js
  ###

  node: undefined
  svg: undefined
  rects: undefined
  labels: undefined


  width: 0
  height: 0


  constructor: (@selector)->
    @node = d3.select(@selector)
    @svg = @node.append("svg")


  select: (data)->
    @svg.selectAll("svg").data(data)

  enter:(data)->@select(data).enter().append("svg")

  exit:(data)->@select(data).exit()

  setSize: (w,h)->
    @width = w
    @height = h
    @svg.attr("width",w).attr("height",h)

class Denigma.LifeCharts extends Denigma.Charts

  marginX : 10
  marginY : 10

  constructor: (selector)->super(selector)

  dMin: (d)->d.test.get("min")
  dMean: (d)->d.test.get("mean")
  dMax:  (d)->d.test.get("max")

  makeOX:(data)->
    fun = @dMax
    d3.scale.linear().domain([0, d3.max(data,fun)]).range([@marginX, @width-@marginX])


  dXmin: (ox)=> (d)=>ox @dMin(d)

  dXmean: (ox)=> (d)=>ox @dMean(d)

  dXmax: (ox)=> (d)=>ox @dMax(d)

  makeOY: (data)=>
    @oy = d3.scale.ordinal().domain().rangeBands([@marginY, @height-@marginY])

