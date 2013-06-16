class Denigma.Curves extends Denigma.Charts
  ###
    class to display lifespan curves
  ###



  constructor: (selector)->
    super(selector)
    @xAxis = d3.svg.axis().orient("bottom")
    funY = (t)->if(t==0) then "" else (t+"%")
    @yAxis = d3.svg.axis().orient("right").ticks(20).tickFormat(funY)
    @svg.append("svg").attr("class","xAxis")
    @svg.append("svg").attr("class","yAxis")


  draw: (data)->
    max = @max(data)
    yrMax = @height-@marginY
    @xScale = d3.scale.linear().domain([0,max]).range([@marginX, @width-@marginX])
    @yScale = d3.scale.linear().domain([0,100]).range([yrMax, @marginY])
    @updateAxises(data)
    sel =  @select(data)
    @hide(sel.exit())
    console.log("not yet working!")
    #novel = @append(sel.enter())
    #@update(sel)

  max: (data)->d3.max(data,(d)->d.get("max"))

  append: (novel)->
    sv = novel.append("svg")
    sv.attr("class","point")
    sv.append("path")
    novel

  update: (sel)->
    data = sel.data
    xFun = (d)=>@xScale(d)
    yFun = (d)=>@yScale(d)

    poly = d3.svg.line()
      .x((d)->d  )
      .y((d)->d )
      .interpolate("monotone");

    #  .interpolate("monotone")
    curves = sel.select("path")
    curves.attr("stroke", "blue").attr("stroke-width", 4)
    curves.attr("d",(d,i)->
      alert i
      poly([i*30,100])
    )


  updateAxises: (data)->
    @xAxis.scale(@xScale)
    gx = @svg.select("svg.xAxis")
    gx.attr("y",@height-@marginY).call(@xAxis)

    @yAxis.scale(@yScale)
    gy = @svg.select("svg.yAxis")
    gy.attr("x",@marginX)
      .call(@yAxis)


