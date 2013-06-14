class Denigma.BarView extends Denigma.BasicView

  width: undefined

  constructor: (poser,@minW,@minH,@dur)->
    super(poser)

  addTest: (row)->
    test = row.append("svg")
    test.attr("class", "test")

    test.append("rect").attr("class","max")
    test.append("rect").attr("class","mean")
    test.append("rect").attr("class","min")
    ###
      test.append("text").attr("class","max").text("max")
      test.append("text").attr("class","mean").text("mean")
      test.append("text").attr("class","min").text("min")
    ###

  addControl: (row)->
    control = row.append("svg")
    control.attr("class", "control")

    posY = @poser.getMiddlePos()

    control.append("rect").attr("class","max")
    control.append("rect").attr("class","mean")
    control.append("rect").attr("class","min")


  updateBars: (sel,group,key,posY,h)->
    h = @minH unless h?
    fun = (d)=>@scale(d[group].get(key))
    bar =  sel.select(".#{group} rect.#{key}")
    bar.attr("x",0)
    .attr("y",posY)
    .attr("width",@minW)
    .attr("height",h)

    bar.transition().duration(@dur)
      .attr("width",fun)
      .attr("rx",3)
      .attr("ry",3)




  updateTests: (sel)->
    h = @minH
    posY = @poser.getMiddlePos(h)
    @updateBars(sel,"test","min",posY)
    @updateBars(sel,"test","mean",posY)
    @updateBars(sel,"test","max",posY)


  updateControl: (sel)->
    h = @minH *3
    posY = @poser.getMiddlePos(h)
    @updateBars(sel,"control","min",posY,h)
    @updateBars(sel,"control","mean",posY,h)
    @updateBars(sel,"control","max",posY,h)


  append: (novel)->
    @addControl(novel)
    @addTest(novel)

  update: (sel)->
    @makeScale(sel)
    @updateTests(sel)
    @updateControl(sel)

  makeScale: (sel)->
    @width = sel.attr("width")
    data = sel.data()
    max = d3.max(data, (d)->d.get "max")
    @scale = d3.scale.linear().domain([0,max]).range([0, @width-@poser.rowMargin])
