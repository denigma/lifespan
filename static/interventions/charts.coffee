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

  poser: undefined
  iconView: undefined
  decorView:undefined

  iconWidth: 180

  durNew: 400


  constructor: (@selector)->
    ###
      jquery-like selector string is passed,
      something like '#lifespan'
    ###
    @poser = new Denigma.RowPoser(rowMargin =20, rowHeight = 56,marginX = 10, dur = 2000)
    @decorView = new Denigma.DecorView(@poser,@width)
    @iconView = new Denigma.IconView(poser = @poser, resources ="static/interventions/resources")
    @barView = new Denigma.BarView(poser =@poser,minW = 15,minH = 10)
    @node = d3.select(@selector)
    @svg = @node.append("svg")



  select: (data)->
    @svg.selectAll("svg.row").data(data)

  enter:(data)->@select(data).enter()

  exit:(data)->@select(data).exit()

  setSize: (w,h)->
    ###
      sets size of the main svg
    ###
    @width = w
    @height = h

    @decorView.width = w

    @svg.attr("width",w).attr("height",h)



  append: (novel)->
      rows = novel.append('svg')
      rows.attr "class", "row"
      rows.attr "y", 0
      #@posRows(rows)
      @decorView.append(rows)

      icons = rows.append("svg")
      icons.attr "class", "icon"
      @iconView.append(icons)

      bars = rows.append("svg")
      bars.attr("class", "bar")
        .attr("x",@iconWidth)
      @barView.append(bars)

      #novel.append("rect").attr("class","icon").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",0)

      #novel.append("rect").attr("class","test").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",150)
      #novel.append("rect").attr("class","control").attr("y",(d,i)=>i*c).attr("width",100).attr("height",h).attr("x",300)
      novel


  draw: (data)->
    sel =  @select(data)
    @hide(sel.exit())
    novel = @append(sel.enter())
    @update(sel)

  hide: (sel)->
    tr = sel.transition()
    tr.duration(@durNew).attr("y", 0)
    tr.delay(@durNew).remove()


  update: (sel)->
    pos = @poser.getRowPos

    icons = sel.select("svg.icon")
    icons.attr("width", @iconWidth)
    @iconView.update(icons)

    bars = sel.select("svg.bar")
    bars.attr("x",@iconWidth)
    bars.attr("width",@width-@iconWidth)
    @barView.update(bars)

    sel.transition().duration(@durNew)
      .attr("y", pos)
      .attr("width",@width)
