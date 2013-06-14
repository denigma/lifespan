class Denigma.LabeledBar extends Denigma.ExperimentBar



  append: (row)->
    bars = super(row)
    bars.append("rect").attr("class","textmax")
    bars.append("rect").attr("class","textmean")
    bars.append("rect").attr("class","textmin")
    bars.append("text").attr("class","max").text("max")
    bars.append("text").attr("class","mean").text("mean")
    bars.append("text").attr("class","min").text("min")
    bars

  updateLabel: (sel,key)->


  updateBar: (sel,key,h)->
    super(sel,key,h)
    val = (d)=> Math.round(d[@group].get(key))
    fun = (d)=>@scale(val(d)) - @minW

    bh = @minH*2
    bw = @minW*2+@poser.rowMargin
    posBY = @poser.getMiddlePos(bh)

    back = @select(sel,"text#{key}", "rect")
    back.attr("height",bh)
      .attr("x",0)
      .attr("y",posBY)
      .attr("width",bw)


    posTY = @poser.getMiddlePos(-@minH)
    text = @select(sel,key, "text")
    text.attr("x",0)
      .attr("y",posTY)
    text.transition().duration(@poser.dur)
      .attr("x",fun)
      .text(val)

    back.transition().duration(@poser.dur)
      .attr("x",(d)=>fun(d)-@poser.rowMargin)
