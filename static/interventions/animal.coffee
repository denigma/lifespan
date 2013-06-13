#TODO: Animal to Species, latin -> latinName
class Denigma.Animal extends Batman.Object
  ###
    class of the animal
  ###

  constructor: (@name, @latin, @lifespan, @icon)->

###
class Denigma.Line extends Denigma.Animal
  constructor: (@name, @latin, @lifespan, @line)->
    super(name,latin)
###