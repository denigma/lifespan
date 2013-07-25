class Denigma.MemberController extends Batman.Controller
  constructor: ->
    super
    @set 'search', null

  index: ->
    #alert "Hello!"
    #@render(view: new Batman.View(html: '[<div data-yield="foo"></div>]'))

  out: (node, event, context)->
    node  = $(context.get("node"))
    node.removeClass("selected")

  over: (node, event, context)->
    node  = $(context.get("node"))
    node.addClass("selected")

  click: (node, event, context)->
    node  = context.get("node")
    $node = $(node)
    #$node.children().css('background-color', 'red')
    model = context.get("member")
    #debugger

  create: ->
    new Denigma.Member.save()
    @set 'search', null

  save: (node, event, context) ->
    alert "saving"
    model = context.get("member")
    options =
      recordUrl: "http://localhost:8000/grids/"
      url: "http://localhost:8000/grids/"
      urlPrefix: "http://localhost:8000/grids/"
      collectionUrl: "http://localhost:8000/grids/"


    model.save(options)

  @accessor 'items',
    get: ->
      items = Denigma.get('Member.all')
      items

Denigma.root("member#index")
