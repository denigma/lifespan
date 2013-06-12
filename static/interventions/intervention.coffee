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


  constructor: (@animal, @manipulation, @test, @control)->
    ###
      constructor that stores test, control groups and manipulations
    ###



