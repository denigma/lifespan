class Denigma.IconView extends Denigma.BasicView
  ###
    this icon view that draws icons
  ###
  resources: undefined  #path to pics folder

  constructor: (poser,@resources, @dur)->
    super(poser)


  addIcons: (row)->
    ###
      this function add all icons to the rowumn and groups them inside svg
    ###
    icon = row.append("svg")
    icon.attr "class", "icon"
    icon.append("rect").attr("class","billet") #TODO: move to another place
    icon.append("image").attr("class","animal")
      .attr("x",0)
    icon.append("image").attr("class","manipulation")
      .attr("x",0)


  getAnimalPic: (d)=>"#{@resources}/#{d.animal.icon}"

  getManipulationPic: (d)=>"#{@resources}/#{d.manipulation.icon}"

  updateIcons: (sel)->
    ###
      make all icons drawing and binding routine
    ###

    h = @poser.contentHeight()

    pos = @poser.getTopPos
    posM  = @poser.getMiddlePos(h/2)

    sel.select("rect.billet")
      .attr("x",0)
      .attr("y",pos)
      .attr("width",h*1.5+@poser.marginX*2)
      .attr("height",h)
      .attr("rx",10)
      .attr("ry",10)


    gpa = @getAnimalPic
    sel.select("image.animal").transition().duration(@dur)
      .attr("xlink:href",gpa)
      .attr("x",@poser.marginX)
      .attr("y",pos)
      .attr("width",h)
      .attr("height",h)

    gma = @getManipulationPic
    sel.select("image.manipulation").transition().duration(@dur)
      .attr("xlink:href",gma)
      .attr("x",@poser.marginX+h)
      .attr("y",posM)
      .attr("width",h/2)
      .attr("height",h/2)

  append: (novel)->
    @addIcons(novel)


  update: (sel)->
    @updateIcons(sel)
