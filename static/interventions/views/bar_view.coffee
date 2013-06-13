class Denigma.BarView extends Denigma.BasicView

  constructor: (poser,@minW,@minH,@dur)->
    super(poser)

    #sel.select(".icon text").text (d)->d.animal.name

  addTest: (row)->
    x = 2*(@poser.rowHeight+@poser.rowMargin/2) - @poser.marginX
    test = row.append("svg")
    test.attr("class", "test").attr("x",x)
    test.append("rect").attr("class","max")
    test.append("rect").attr("class","mean")
    test.append("rect").attr("class","min")



  addControl: (row)->
    x = 2*(@poser.rowHeight-@poser.rowMargin/2) - @poser.marginX
    control = row.append("svg")
    control.attr("class", "control").attr("x",x)
    control.append("rect").attr("class","max")
    control.append("rect").attr("class","mean")
    control.append("rect").attr("class","min")



  updateBar: (bar,pos,val, h)->
    ###
      updates any bar
    ###
    h = @minH unless h?
    bar.attr("x",0)
      .attr("y",pos)
      .attr("width",@minW)
      .attr("height",h)

    bar.transition().duration(@dur)
      .attr("width",val)
      .attr("rx",3)
      .attr("ry",3)


  updateTests: (sel)->
    ###
     redraws bars in accordance with binding info
    ###
    gtMax = Denigma.Intervention.getTestMax
    gtMean = Denigma.Intervention.getTestMean
    gtMin = Denigma.Intervention.getTestMin

    h = @minH
    pos = @poser.getMiddlePos(h)
    min = sel.select(".test .min")
    mean = sel.select(".test .mean")
    max = sel.select(".test .max")
    @updateBar(min,pos,gtMin,h)
    @updateBar(mean,pos,gtMean,h)
    @updateBar(max,pos,gtMax, h)


  updateControl: (sel)->
    ###
     redraws bars in accordance with binding info
    ###
    gcMax = Denigma.Intervention.getControlMax
    gcMean = Denigma.Intervention.getControlMean
    gcMin = Denigma.Intervention.getControlMin

    h = @minH *3
    pos = @poser.getMiddlePos(h)

    min = sel.select(".control .min")
    mean = sel.select(".control .mean")
    max = sel.select(".control .max")
    @updateBar(min,pos,gcMin,h)
    @updateBar(mean,pos,gcMean,h)
    @updateBar(max,pos,gcMax,h)

  append: (novel)->
    @addControl(novel)
    @addTest(novel)

  update: (sel)->
    @updateTests(sel)
    @updateControl(sel)

