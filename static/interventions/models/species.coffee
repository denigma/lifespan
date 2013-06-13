#TODO: Animal to Species, latin -> latinName
class Denigma.Animal extends Batman.Object
  ###
    class of the species
  ###


  constructor: (@commonName, @latinName, @lifespan, @icon)->

###
class Denigma.Line extends Denigma.Species
  constructor: (@commonName, @latinName, @lifespan, @line)->
    super(name,latin)
###