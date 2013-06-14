class Denigma.Intervention extends Batman.Object
  ###
    Intervention with animal
  ###
  @accessor "number",
    get: -> @test.get("number") + @control.get("number")

  @accessor "deltaNumber",
    get: -> @test.get("number") - @control.get("number")


  @accessor "deltaMax",
    get: -> @test.get("max") - @control.get("max")

  @accessor "deltaMean",
    get: -> @test.get("mean") - @control.get("mean")

  @accessor "deltaMin",
    get: -> @test.get("min") - @control.get("min")


  constructor: (@species, @manipulation, @test, @control)->
    ###
      constructor that stores test, control groups and manipulations
    ###

  ###
    static functions start
  ###

  #indian-like code warning: all these pos functions are inaccurate and mostly wrong
  @scale: ->12
  @getTestMin: (d)=>@scale() * d.test.get "min"
  @getTestMean: (d)=>@scale() * d.test.get "mean"
  @getTestMedian: (d)=>@scale() * d.test.get "median"
  @getTestMax: (d)=>@scale() * d.test.get "max"

  @getControlMin: (d)=>@scale() * d.control.get "min"
  @getControlMean: (d)=>@scale() * d.control.get "mean"
  @getControlMedian: (d)=>@scale() * d.control.get "median"
  @getControlMax: (d)=>@scale() * d.control.get "max"

  @getSpeciesName: (d)=>d.species.commonName



