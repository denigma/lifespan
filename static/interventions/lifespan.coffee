###
  Here is where the main code of the demo is
###

class Denigma.LifeSpan extends Batman.Object

  fixture: undefined
  charts: undefined



  @main: =>
    @fixture = new Denigma.Fixture()
    @charts = new Denigma.Charts("#lifespan")
    @position()
    @generate()

  @position: =>
    svg = @charts.svg
    svg.style("background-color","ivory")
    w = 800
    h = 800
    @charts.setSize(w,h)

  @generate: =>
    num = @fixture.rand(2,5)
    data = @fixture.generate(num)
    @charts.draw(data)

  @experiment: =>
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
  Denigma.LifeSpan.main()
  #ls.experiment()

