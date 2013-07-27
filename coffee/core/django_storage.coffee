class Batman.DjangoStorage extends Batman.RestStorage
  ###
    Storage with Django specific features
  ###

  request: (env, next) ->
    ###
      override to change put format
    ###
    options = Batman.extend env.options,
      autosend: false
      success: (data) -> env.data = data
      error: (error) -> env.error = error
      loaded: ->
        env.response = env.request.get('response')
        next()
    if options.data? and options.method == "PUT"
      #Dirty fix but, saving now works!
      for key,value of options.data
        options.data = value
        break
    env.request = new Batman.Request(options)

    console.log JSON.stringify(options)
    env.request.send()
