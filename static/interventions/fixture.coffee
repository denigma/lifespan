class Denigma.Fixture extends Batman.Object
  ###
    this class is just for ease of use
    it has no other meaning
  ###
  controls: []
  tests:  []
  ints:  []
  animal: undefined
  manipulation: undefined

  constructor: ->
    @species = new Denigma.Species("mouse","mus",18,"mouse.svg") #in months
    @manipulation = new Denigma.Manipulation("radiaction", "test grouped lived and mutated inside the reactor", "radiation.svg")

  rand: (min, max) -> Math.round(Math.random() * (max - min) + min)

  rnd_snd: ->   (Math.random() * 2 - 1) + (Math.random() * 2 - 1) + (Math.random() * 2 - 1)

  rnd: (mean, stdev) ->
    ###
      closer to normal distribution
      where stdev = standard deviation
    ###
    Math.round @rnd_snd() * stdev + mean

  @accessor "max",
    get: ->
      max = 0
      for exp in @controls
        m = exp.get "max"
        max = m if m>max
      max

  clean: ->
    @controls =[]
    @tests =  []
    @ints =  []

  generate: (num)->
    @clean()
    num = 10 unless num?
    mean = @rand(10,14)
    stdev = @rand(5,12)
    for i in [0..num]
      animals = []
      for a in [0..@rand(5,15)]
        an = @rnd(mean,stdev)
        an = an*-1 if an<=0
        animals.push(an)

      test = new Denigma.Experiment("Chernobyl mouse",animals)
      @tests.push(test)

      control = new Denigma.Experiment("House mouse")
      control.set "number", @rand(5,10)
      control.set "min", 10
      control.set "mean", @rand(10,20)
      control.set "max", @rand(25,30)

      @controls.push(control)
      int = new Denigma.Intervention(@species, @manipulation, test, control)
      @ints.push(int)
    @ints

