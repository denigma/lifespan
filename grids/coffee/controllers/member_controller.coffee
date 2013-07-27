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
    model = context.get("member")
    model.save()


  @accessor 'items',
    get: ->
      items = Denigma.get('Member.all')
      items

Denigma.root("member#index")
