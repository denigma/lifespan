jQuery =>
  data = ["one","two","three"]

  ###
  data =
    first:"first value"
    second: "second value"
    third: "third value"
  ###


  pl = d3.select("#lifespan").append("div")
  pl.select("p").data(data).enter().append("p").text (d)->d

  tr = d3.selectAll("tbody tr")


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

  ###
  xAxis = d3.svg.axis().scale(x).orient("bottom").ticks(5)

  td = d3.selectAll("tbody td")

  svg.append("g")
    .call(xAxis);
  ###

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