class Denigma.Charts
  ###
    class to generate chars with d3js

    WARNING: the code is very dirty with a lot of hardcoded stuff :(((((((((
  ###

  node: undefined
  svg: undefined

  resources: "static/interventions/resources" #path to pics folder

  marginX : 10 #left margin
  marginY : 10 #top margin

  colMargin : 5 #between cols


  minW: 10 #minimum width for shape
  width: 0

  minH: 5 #minimum height for shape
  height: 0

  iconW: 64
  iconH: 64

  colHeight : 56

  dur: 1700


  constructor: (@selector)->
    ###
      jquery-like selector string is passed,
      something like '#lifespan'
    ###
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

  #indian-like code warning: all these pos functions are inaccurate and mostly wrong
  getTopPos: (d,i)=> i* (@colHeight-@colMargin)
  getMiddlePos: (d,i)=> i* (@colHeight-@colMargin)+(@colHeight-@colMargin)/2
  getBottomPos: (d,i)=> (i+1)* (@colHeight-@colMargin)-@colMargin*2

  addDecor: (col)->
    ###
      adds column decorations
    ###
    pos =  @getTopPos
    h = @colHeight

    border = col.append("rect")
    border.attr("class","decor")
      .attr("width",@width)
      .attr("height",@colHeight)
      .attr("rx",15)
      .attr("ry",15)
      .attr("y",pos)

  addIcons: (col)->
    ###
      this function add all icons to the column and groups them inside svg
    ###
    h = @colHeight-@colMargin
    icon = col.append("svg")
    icon.attr "class", "icon"
    icon.append("image").attr("class","animal")
    icon.append("image").attr("class","control")
    icon.append("image").attr("class","manipulation")

  getAnimalPic: (d)=>"#{@resources}/#{d.animal.icon}"

  getManipulationPic: (d)=>"#{@resources}/#{d.manipulation.icon}"

  updateIcons: (sel)->
    ###
      make all icons drawing and binding routine
    ###

    h = @colHeight-@colMargin/2

    pos = @getTopPos
    posM = @getMiddlePos

    ###
      redraws icons in accordance with binding info
    ###
    gpa = @getAnimalPic
    sel.select("image.animal")
      .attr("xlink:href",gpa)
      .attr("x",@marginX)
      .attr("y",pos)
      .attr("width",h)
      .attr("height",h)

    sel.select("image.control")
      .attr("xlink:href",gpa)
      .attr("x",@marginX+h)
      .attr("y",pos)
      .attr("width",h/2)
      .attr("height",h/2)

    gma = @getManipulationPic
    sel.select("image.manipulation")
      .attr("xlink:href",gma)
      .attr("x",@marginX+h)
      .attr("y",posM)
      .attr("width",h/2)
      .attr("height",h/2)


  #sel.select(".icon text").text (d)->d.animal.name

  addTest: (col)->
    h = @colHeight-@colMargin/2
    test = col.append("svg")
    test.attr("class", "test").attr("x",h*2-@marginX)
    test.append("rect").attr("class","max")
    test.append("rect").attr("class","mean")
    test.append("rect").attr("class","min")



  addControl: (col)->
    h = @colHeight-@colMargin/2
    control = col.append("svg")
    control.attr("class", "control").attr("x",h*2-@marginX)
    control.append("rect").attr("class","max")
    control.append("rect").attr("class","mean")
    control.append("rect").attr("class","min")



  addBars: (col)->
    ###
      this function add all icons to the column and groups them inside svg
    ###
    @addTest(col)
    @addControl(col)



  scale: ->12 #in future use axises

  updateBar: (bar,pos,val)->
    ###
      updates any bar
    ###
    bar.attr("x",0)
      .attr("y",pos)
      .attr("width",@minW)
      .attr("height",@minH)

    bar.transition().duration(@dur)
      .attr("width",val)

  #indian-like code warning: all these pos functions are inaccurate and mostly wrong
  getTestMin: (d)=>@scale() * d.test.get "min"
  getTestMean: (d)=>@scale() * d.test.get "mean"
  getTestMedian: (d)=>@scale() * d.test.get "median"
  getTestMax: (d)=>@scale() * d.test.get "max"

  getTestPos: (d,i)=> i* (@colHeight-@colMargin)+@colHeight/2+@colMargin


  updateTests: (sel)->
    ###
     redraws bars in accordance with binding info
    ###
    gtMax = @getTestMax
    gtMean = @getTestMean
    gtMin = @getTestMin

    h = @colHeight-@colMargin/2
    posB = @getTestPos
    min = sel.select(".test .min")
    mean = sel.select(".test .mean")
    max = sel.select(".test .max")
    @updateBar(min,posB,gtMin)
    @updateBar(mean,posB,gtMean)
    @updateBar(max,posB,gtMax)

  getControlMin: (d)=>@scale() * d.control.get "min"
  getControlMean: (d)=>@scale() * d.control.get "mean"
  getControlMedian: (d)=>@scale() * d.control.get "median"
  getControlMax: (d)=>@scale() * d.control.get "max"

  #indian-like code warning: all these pos functions are inaccurate and mostly wrong

  getControlPos: (d,i)=> i* (@colHeight-@colMargin)+@colMargin*3


  updateControl: (sel)->
    ###
     redraws bars in accordance with binding info
    ###
    gcMax = @getControlMax
    gcMean = @getControlMean
    gcMin = @getControlMin

    h = @colHeight-@colMargin/2
    pos = @getControlPos
    min = sel.select(".control .min")
    mean = sel.select(".control .mean")
    max = sel.select(".control .max")
    @updateBar(min,pos,gcMin)
    @updateBar(mean,pos,gcMean)
    @updateBar(max,pos,gcMax)


  updateBars: (sel)->
    @updateTests(sel)
    @updateControl(sel)

  addShapes: (novel)->
      col = novel.append('svg')
      col.attr "class", "column"
      @addDecor(col)
      @addIcons(col)
      @addBars(col)
      #novel.append("rect").attr("class","icon").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",0)

      #novel.append("rect").attr("class","test").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",150)
      #novel.append("rect").attr("class","control").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",300)
      novel


  draw: (data)->
    sel =  @select(data)
    novel = @addShapes(sel.enter())
    #novel.select(".icon").attr("height",5)
    @updateIcons(sel)
    @updateBars(sel)



    y = d3.scale.ordinal().domain(30)#.rangeBands([@marginY, h-@marginY])

    x = @makeOX(data)
    #@drawBars(els,x,y)




  drawBars: (sel,ox,oy)->
    c = 20
    tests = sel.selectAll(".test")
    tests
      .attr("x",@iconW)
      .attr("width", 10)
    tests.transition().duration(800)
      .attr("y", (d,i)=>i*c)
      .attr("width", @dXmax(ox))
      .attr("height", c)


    ###
    #sel.enter()
    sel.append("rect").attr("class","mean").transition().duration(800)
      .attr("y", (d,i)=>i*c)
      .attr("width", @dXmean(ox))
      .attr("height", c)
      .style("fill","green")
      .style("opacity",0.2)

    ###



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

