class Denigma.Experiment extends Batman.Object
  ###
    class that describes experimental group (it can be either test or control one
    it has many accessors as the info is often incomplete
  ###
  _number: 0
  _min: -1
  _mean: 0
  _median: 0
  _max: 0


  constructor: (@line, animals = [])->
    if(animals?)
      @set "animals", animals
    else
      @set "animals", []

  rnd: (numberToRound) ->  Math.round(numberToRound * 100) / 100

  @accessor "median",
    get: ->
      get: ->
        animals =@get("animals")
        if(animals.length>0)
          d3.median(animals)
        else
          @_median
    set: (value)->
      if @get("animals")?.length>0
        throw new Error("has animals inside")
      else
        @_median = value


  @accessor "max",

    get: ->
      animals =@get("animals")
      if(animals.length>0)
        d3.max(animals)
      else
        @_max

    set: (key,value)->
      if @get("animals")?.length>0
        throw new Error("has animals inside")
      else
        @_max = value

  @accessor "mean",

    get: ->
      animals =@get("animals")
      if(animals.length>0)
        d3.mean(animals)
      else
        @_mean

    set: (key,value)->
      if @get("animals")?.length>0
        throw new Error("has animals inside")
      else
        @_mean = value


  @accessor "min",

    get: ->
      animals =@get("animals")
      if(animals.length>0)
        d3.min(animals)
      else
        @_min

    set: (key,value)->
      if @get("animals")?.length>0
        throw new Error("has animals inside")
      else
        @_min = value

  @accessor "number",

    get: ->
      animals = @get "animals"
      if animals.length>0 then animals.length else @_number

    set: (key,value)->
      if @get("animals")?.length>0
        throw new Error("has animals inside")
      else
        @_number = value




