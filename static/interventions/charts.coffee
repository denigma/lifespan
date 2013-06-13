class Denigma.Charts
  ###
    class to generate chars with d3js

    WARNING: the code is very dirty with a lot of hardcoded stuff :(((((((((
  ###

  node: undefined
  svg: undefined


  marginY : 10 #top margin

  width: 0
  height: 0

  iconW: 64
  iconH: 64


  poser: undefined
  iconView: undefined


  constructor: (@selector)->
    ###
      jquery-like selector string is passed,
      something like '#lifespan'
    ###
    @poser = new Denigma.RowPoser(rowMargin =10, rowHeight = 56,marginX = 10)
    @iconView = new Denigma.IconView(@poser,"static/interventions/resources", dur = 2000)
    @barView = new Denigma.BarView(poser =@poser,minW = 10,minH = 10, dur = 2000)

    @node = d3.select(@selector)
    @svg = @node.append("svg")


  select: (data)->
    @svg.selectAll("svg").data(data)

  enter:(data)->@select(data).enter()

  exit:(data)->@select(data).exit()

  setSize: (w,h)->
    ###
      sets size of the main svg
    ###
    @width = w
    @height = h
    @svg.attr("width",w).attr("height",h)


  addDecor: (row)->
    ###
      adds rowumn decorations
    ###
    h = @poser.contentHeight()
    pos =  @poser.getTopPos
    border = row.append("rect")
    border.attr("class","decor")
      .attr("width",@width)
      .attr("height",h)
      .attr("rx",10)
      .attr("ry",10)
      .attr("y",pos)



  addShapes: (novel)->
      row = novel.append('svg')
      row.attr "class", "rownum"
      @addDecor(row)
      @iconView.append(row)
      @barView.append(row)

      #novel.append("rect").attr("class","icon").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",0)

      #novel.append("rect").attr("class","test").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",150)
      #novel.append("rect").attr("class","control").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",300)
      novel


  draw: (data)->
    sel =  @select(data)
    novel = @addShapes(sel.enter())
    #novel.select(".icon").attr("height",5)
    @iconView.update(sel)
    @barView.update(sel)


class Denigma.LifeCharts extends Denigma.Charts



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

