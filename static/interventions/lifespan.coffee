###
  Here is where the main code of the demo is
###

class Denigma.LifeSpan extends Batman.Object

  fixture: undefined
  charts: undefined



  constructor: ()->

  main: =>
    @fixture = new Denigma.Fixture()
    @charts = new Denigma.LifeCharts("#lifespan")
    @draw()

  draw: =>
    data = @fixture.generate(10)
    w = 500
    c = 30
    h = c * data.length
    svg = @charts.svg
    @charts.setSize(w,h)
    svg.attr("class", "chart")
      .style("background-color","ivory")
    y = d3.scale.ordinal().domain(c)#.rangeBands([@marginY, h-@marginY])
    x = @charts.makeOX(data)

    sel = @charts.select(data)

    els = @charts.enter(data)
    els.append("rect").attr("class","max").transition().duration(800)
      .attr("y", (d,i)=>i*c)
      .attr("width", @charts.dXmax(x))
      .attr("height", c)
      .style("fill","lightgreen")

    #sel.enter()
    els.append("rect").attr("class","mean").transition().duration(800)
      .attr("y", (d,i)=>i*c)
      .attr("width", @charts.dXmean(x))
      .attr("height", c)
      .style("fill","green")
      .style("opacity",0.2)

  experiment: =>
    ###
      just for fun
    ###

    table = d3.select("table")
    tr = table.selectAll("tbody tr")


    td = tr.selectAll("td")

    tr.transition().duration(1000).style "font-size", (d, i) ->  switch i
      when 0 then "10pt"
      when 1 then "20pt"
      when 2 then "3opt"
      else "40pt"

    td.style("background-color","white").transition().duration(1000).style "background-color", (d, i) ->  switch i
      when 0 then "red"
      when 1 then "navy"
      when 3 then "yellow"
      else "white"

Denigma.on "start", ->
  ###
    Event to initiate the main app
  ###
  ls = new Denigma.LifeSpan()
  ls.main()
  ls.experiment()

###
  Lifespan
========
* progress bar lifespan
  - normal lifespan of mice, icon for mice
* errors bars
* lifespan curves

ICONS: species
ICONS: manipulations (svgs)

:Measurement a owl:Class ;
:min_lifespan
:mean_lifespan
:median_lifespan
:max_lifespan
:number for each individual (low-average-hight)
:variant +/- something
:pvalue < or > 0.05 (colors or artrisks) *   ** ***
###