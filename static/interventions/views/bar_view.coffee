class Denigma.BarView extends Denigma.BasicView

  width: undefined
  test: undefined
  control: undefined

  constructor: (poser,@minW,@minH)->
    super(poser)
    @test = new Denigma.LabeledBar(@poser,"test",@minW,@minH)
    @control = new Denigma.ExperimentBar(@poser,"control",@minW,@minH*3)

  append: (novel)->
    @control.append(novel)
    @test.append(novel)
    #@addTest(novel)

  update: (sel)->
    @makeScale(sel)
    @control.scale = @scale
    @control.update(sel)
    @test.scale = @scale
    @test.update(sel)

  makeScale: (sel)->
    @width = sel.attr("width")
    data = sel.data()
    max = d3.max(data, (d)->d.get "max")
    @scale = d3.scale.linear().domain([0,max]).range([0, @width-@poser.rowMargin])
