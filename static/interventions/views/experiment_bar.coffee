class Denigma.ExperimentBar extends Denigma.BasicView
  ###
    creates a bar for interventions
  ###

  scale:undefined

  constructor: (poser,@group,@minW,@minH)->
    super(poser)

  append: (row)->
    control = row.append("svg")
    control.attr("class", @group)

    control.append("rect").attr("class","max")
    control.append("rect").attr("class","mean")
    control.append("rect").attr("class","min")


  updateBar: (sel,key,posY,h)->
    h = @minH unless h?
    fun = (d)=>@scale(d[@group].get(key))
    bar =  sel.select(".#{@group} rect.#{key}")
    bar.attr("x",0)
      .attr("y",posY)
      .attr("width",@minW)
      .attr("height",h)

    bar.transition().duration(@poser.dur)
      .attr("width",fun)
      .attr("rx",3)
      .attr("ry",3)


  update: (sel)->
    h = @minH
    posY = @poser.getMiddlePos(h)
    @updateBar(sel,"min",posY,h)
    @updateBar(sel, "mean",posY,h)
    @updateBar(sel, "max",posY,h)
